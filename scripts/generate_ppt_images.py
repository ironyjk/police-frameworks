"""
PPT용 이미지 생성기 — ComfyUI (Flux Schnell) API 호출

사용법:
    python scripts/generate_ppt_images.py

사전:
    ComfyUI 실행 중 (127.0.0.1:8188), Flux Schnell 모델 설치됨

결과:
    docs/images/*.png (7장, gitignored)
"""

import json
import time
import uuid
import urllib.request
import urllib.parse
from pathlib import Path

COMFY = "http://127.0.0.1:8188"
HERE = Path(__file__).resolve().parent
OUT_DIR = HERE.parent / "docs" / "images"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── 프롬프트 정의 ───────────────────────────────────────────
IMAGES = [
    {
        "key": "cover",
        "prompt": (
            "soft watercolor illustration, Korean police officer in dark navy uniform "
            "standing at a desk at sunset, looking at a laptop with warm screen glow, "
            "Korean neighborhood skyline outside the window, calm and dignified atmosphere, "
            "painterly brushstrokes, muted warm palette, no text, detailed but soft, "
            "cinematic wide composition"
        ),
        "width": 1280,
        "height": 720,
        "seed": 11,
    },
    {
        "key": "toolbox",
        "prompt": (
            "soft watercolor illustration, an open wooden toolbox with organized compartments "
            "containing symbolic tools, warm overhead light, police notebook next to it, "
            "painterly brushstrokes, muted warm palette, approachable and calm, no text, "
            "symbolic of frameworks as tools"
        ),
        "width": 1280,
        "height": 720,
        "seed": 22,
    },
    {
        "key": "case1_park",
        "prompt": (
            "soft watercolor illustration, Korean urban neighborhood park at night, "
            "dim street lamp glow, empty playground bench, silhouette of distant apartment "
            "buildings, atmosphere of quiet concern, warm lamp light contrasts cool night, "
            "painterly brushstrokes, muted palette, no people visible, no text"
        ),
        "width": 1280,
        "height": 720,
        "seed": 33,
    },
    {
        "key": "case2_hwangnidan",
        "prompt": (
            "soft watercolor illustration, Korean traditional alley at night with hanok rooftops, "
            "warm paper lantern light, cobblestone path, a few silhouettes walking, "
            "bustling but calm atmosphere, Gyeongju Hwangnidan-gil inspired, "
            "painterly brushstrokes, muted warm palette, no text"
        ),
        "width": 1280,
        "height": 720,
        "seed": 44,
    },
    {
        "key": "case3_industrial",
        "prompt": (
            "soft watercolor illustration, industrial complex parking lot at dawn, "
            "rows of trucks and parked cars, long shadows, dim overhead sodium lights, "
            "silent empty atmosphere, Korean industrial outskirts, muted blue and amber palette, "
            "painterly brushstrokes, no people, no text"
        ),
        "width": 1280,
        "height": 720,
        "seed": 55,
    },
    {
        "key": "case4_station",
        "prompt": (
            "soft watercolor illustration, Korean police station interior counter, "
            "one seated officer and a civilian in respectful conversation, warm interior "
            "light, dignified calm atmosphere, painterly brushstrokes, muted warm palette, "
            "faces blurred or turned away, no visible text"
        ),
        "width": 1280,
        "height": 720,
        "seed": 66,
    },
    {
        "key": "install_desk",
        "prompt": (
            "soft watercolor illustration, cozy home desk scene, a laptop showing warm glowing "
            "screen with abstract light, coffee cup steam rising, simple notebook, warm window "
            "light from the side, inviting and approachable atmosphere, painterly brushstrokes, "
            "muted warm palette, no text, no visible people"
        ),
        "width": 1280,
        "height": 720,
        "seed": 77,
    },
    {
        "key": "case5_fraud",
        "prompt": (
            "soft watercolor illustration, Korean mid-sized company office in afternoon, "
            "a procurement manager at desk with laptop and mobile phone, warm window light, "
            "cluttered paperwork, thoughtful concerned expression, calm but uncertain atmosphere, "
            "painterly brushstrokes, muted warm palette, face turned away or blurred, "
            "symbolic of fraud threat without being alarming, no visible text"
        ),
        "width": 1280,
        "height": 720,
        "seed": 88,
    },
]


# ── ComfyUI 워크플로우 (Flux Schnell) ────────────────────────
def build_workflow(prompt_text: str, width: int, height: int, seed: int, prefix: str):
    return {
        "5": {
            "class_type": "DualCLIPLoader",
            "inputs": {
                "clip_name1": "t5xxl_fp8_e4m3fn.safetensors",
                "clip_name2": "clip_l.safetensors",
                "type": "flux",
            },
        },
        "6": {
            "class_type": "CLIPTextEncode",
            "inputs": {"clip": ["5", 0], "text": prompt_text},
        },
        "8": {
            "class_type": "VAELoader",
            "inputs": {"vae_name": "ae.safetensors"},
        },
        "11": {
            "class_type": "EmptySD3LatentImage",
            "inputs": {"width": width, "height": height, "batch_size": 1},
        },
        "13": {
            "class_type": "UNETLoader",
            "inputs": {
                "unet_name": "flux1-schnell-fp8.safetensors",
                "weight_dtype": "fp8_e4m3fn",
            },
        },
        "16": {
            "class_type": "KSamplerSelect",
            "inputs": {"sampler_name": "euler"},
        },
        "17": {
            "class_type": "BasicScheduler",
            "inputs": {
                "model": ["13", 0],
                "scheduler": "simple",
                "steps": 4,
                "denoise": 1.0,
            },
        },
        "22": {
            "class_type": "BasicGuider",
            "inputs": {"model": ["13", 0], "conditioning": ["6", 0]},
        },
        "25": {
            "class_type": "RandomNoise",
            "inputs": {"noise_seed": seed},
        },
        "3": {
            "class_type": "SamplerCustomAdvanced",
            "inputs": {
                "noise": ["25", 0],
                "guider": ["22", 0],
                "sampler": ["16", 0],
                "sigmas": ["17", 0],
                "latent_image": ["11", 0],
            },
        },
        "20": {
            "class_type": "VAEDecode",
            "inputs": {"samples": ["3", 0], "vae": ["8", 0]},
        },
        "24": {
            "class_type": "SaveImage",
            "inputs": {"filename_prefix": prefix, "images": ["20", 0]},
        },
    }


def post_prompt(workflow: dict, client_id: str) -> str:
    data = json.dumps({"prompt": workflow, "client_id": client_id}).encode("utf-8")
    req = urllib.request.Request(
        f"{COMFY}/prompt",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        resp = json.loads(r.read())
    return resp["prompt_id"]


def wait_for_history(prompt_id: str, timeout_s: int = 600) -> dict:
    t0 = time.time()
    while time.time() - t0 < timeout_s:
        with urllib.request.urlopen(f"{COMFY}/history/{prompt_id}") as r:
            h = json.loads(r.read())
        if prompt_id in h:
            return h[prompt_id]
        time.sleep(1.5)
    raise TimeoutError(f"{prompt_id} did not finish in {timeout_s}s")


def download_image(filename: str, subfolder: str, typ: str, dest: Path):
    q = urllib.parse.urlencode({"filename": filename, "subfolder": subfolder, "type": typ})
    with urllib.request.urlopen(f"{COMFY}/view?{q}") as r:
        dest.write_bytes(r.read())


def generate_one(spec: dict, client_id: str):
    key = spec["key"]
    prefix = f"peel_{key}"
    print(f"  → {key} ({spec['width']}x{spec['height']}, seed={spec['seed']})", flush=True)

    wf = build_workflow(
        prompt_text=spec["prompt"],
        width=spec["width"],
        height=spec["height"],
        seed=spec["seed"],
        prefix=prefix,
    )
    prompt_id = post_prompt(wf, client_id)
    print(f"     queued: {prompt_id}", flush=True)

    hist = wait_for_history(prompt_id)
    outputs = hist.get("outputs", {})
    node24 = outputs.get("24", {})
    images = node24.get("images", [])
    if not images:
        print(f"     ! no images returned", flush=True)
        return None

    img = images[0]
    dest = OUT_DIR / f"{key}.png"
    download_image(img["filename"], img.get("subfolder", ""), img.get("type", "output"), dest)
    print(f"     saved: {dest}", flush=True)
    return dest


def main():
    client_id = str(uuid.uuid4())
    print(f"ComfyUI client: {client_id}")
    print(f"Generating {len(IMAGES)} images → {OUT_DIR}")
    print()

    for i, spec in enumerate(IMAGES, 1):
        dest = OUT_DIR / f"{spec['key']}.png"
        if dest.exists():
            print(f"[{i}/{len(IMAGES)}] {spec['key']} — skipped (exists)")
            print()
            continue
        print(f"[{i}/{len(IMAGES)}]")
        try:
            generate_one(spec, client_id)
        except Exception as e:
            print(f"     ! error: {e}", flush=True)
        print()

    print("Done.")


if __name__ == "__main__":
    main()
