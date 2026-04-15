"""
Police Frameworks — 소개 슬라이드 생성기 (60대 경찰관 대상)

사용법:
    python scripts/generate_ppt_images.py   # 먼저 이미지 7장 생성 (ComfyUI 필요)
    python scripts/make_intro_ppt.py        # 슬라이드 생성

결과물:
    docs/intro.pptx (15장, 16:9, 한글)

구조: 사용 사례(4) → 이론(5) → 설치(3) → 부탁 (1) + 표지·차례 (2) = 15장

작성자: 최희철 (경주경찰서 경찰발전협의회 회원, 소프트웨어 개발자)
"""

from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE


# ──────────────────────────────────────────────────────────────
# 색상 및 설정 — 60대 가독성 우선
# ──────────────────────────────────────────────────────────────

NAVY = RGBColor(0x1A, 0x36, 0x5D)
NAVY_DEEP = RGBColor(0x0F, 0x23, 0x3F)
NAVY_LIGHT = RGBColor(0x2C, 0x51, 0x82)
RED = RGBColor(0xDC, 0x26, 0x26)  # 경찰 빨강 계열
GOLD = RGBColor(0xD6, 0x9E, 0x2E)
GRAY_DARK = RGBColor(0x1F, 0x29, 0x37)  # 본문 기본색, 최대 대비
GRAY_MID = RGBColor(0x4A, 0x55, 0x68)
GRAY_LIGHT = RGBColor(0xE2, 0xE8, 0xF0)
GRAY_PALE = RGBColor(0xF1, 0xF5, 0xF9)
BG = RGBColor(0xFA, 0xFC, 0xFF)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
YELLOW_HL = RGBColor(0xFE, 0xF3, 0xC7)  # 강조 하이라이트

FONT = "맑은 고딕"

HERE = Path(__file__).resolve().parent
IMG = HERE.parent / "docs" / "images"


# ──────────────────────────────────────────────────────────────
# 헬퍼
# ──────────────────────────────────────────────────────────────

def set_background(slide, color):
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()
    spTree = bg._element.getparent()
    spTree.remove(bg._element)
    spTree.insert(2, bg._element)
    return bg


def add_image(slide, path, left, top, width, height):
    if Path(path).exists():
        pic = slide.shapes.add_picture(
            str(path), Inches(left), Inches(top), Inches(width), Inches(height)
        )
        return pic
    # fallback: placeholder box
    box = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height)
    )
    box.fill.solid()
    box.fill.fore_color.rgb = GRAY_LIGHT
    box.line.color.rgb = GRAY_MID
    return box


def add_title_bar(slide, title, subtitle=None):
    bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.15)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = NAVY
    bar.line.fill.background()

    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, Inches(1.15), prs.slide_width, Inches(0.06)
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = GOLD
    accent.line.fill.background()

    tb = slide.shapes.add_textbox(
        Inches(0.6), Inches(0.22), Inches(12.2), Inches(0.85)
    )
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = FONT
    p.font.size = Pt(30)
    p.font.bold = True
    p.font.color.rgb = WHITE

    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.name = FONT
        p2.font.size = Pt(14)
        p2.font.color.rgb = GRAY_LIGHT


def add_text(slide, text, left, top, width, height,
             size=20, bold=False, color=GRAY_DARK, align=PP_ALIGN.LEFT,
             line_spacing=1.25):
    tb = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    lines = text.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        p.text = line
        for run in p.runs:
            run.font.name = FONT
            run.font.size = Pt(size)
            run.font.bold = bold
            run.font.color.rgb = color
        if not p.runs:
            p.font.name = FONT
            p.font.size = Pt(size)
            p.font.bold = bold
            p.font.color.rgb = color
    return tb


def add_bullets(slide, bullets, left, top, width, height,
                size=18, color=GRAY_DARK, line_spacing=1.35):
    tb = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    for i, b in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "•  " + b
        p.line_spacing = line_spacing
        p.space_after = Pt(6)
        for run in p.runs:
            run.font.name = FONT
            run.font.size = Pt(size)
            run.font.color.rgb = color
    return tb


def add_footer(slide, page_no):
    tb = slide.shapes.add_textbox(
        Inches(0.5), Inches(7.12), Inches(12.3), Inches(0.35)
    )
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = f"Police Frameworks · /peel · 최희철 (경주경찰서 경찰발전협의회 회원, 소프트웨어 개발자) · {page_no}/15"
    p.alignment = PP_ALIGN.RIGHT
    p.font.name = FONT
    p.font.size = Pt(10)
    p.font.color.rgb = GRAY_MID


def add_highlight_box(slide, text, left, top, width, height, fill=YELLOW_HL, size=18):
    box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left), Inches(top), Inches(width), Inches(height),
    )
    box.fill.solid()
    box.fill.fore_color.rgb = fill
    box.line.color.rgb = GOLD
    box.line.width = Pt(1.2)
    box.adjustments[0] = 0.12
    tb = slide.shapes.add_textbox(
        Inches(left + 0.25), Inches(top + 0.18),
        Inches(width - 0.5), Inches(height - 0.36),
    )
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = text
    p.font.name = FONT
    p.font.size = Pt(size)
    p.font.bold = True
    p.font.color.rgb = GRAY_DARK
    p.line_spacing = 1.3


# ──────────────────────────────────────────────────────────────
# 프레젠테이션 생성
# ──────────────────────────────────────────────────────────────

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]


# ══════════════════════════════════════════════════════════════
# Slide 1 — 표지 (cover.png 배경)
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, NAVY_DEEP)

# 풀블리드 배경 이미지
add_image(s, IMG / "cover.png", 0, 0, 13.333, 7.5)

# 하단 어둠 오버레이
overlay = s.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, 0, Inches(3.7), prs.slide_width, Inches(3.8)
)
overlay.fill.solid()
overlay.fill.fore_color.rgb = NAVY_DEEP
overlay.line.fill.background()
# 투명도 흉내: 덧칠
# (pptx는 shape 투명도 제어가 번거로워, 단색 오버레이로 처리)

# 상단 작은 라벨
add_text(s, "POLICE FRAMEWORKS", 0.8, 0.6, 12, 0.4,
         size=14, bold=True, color=GOLD)

# 메인 제목
add_text(s, "3개월째 똑같은 민원, 이번엔 순서부터",
         0.8, 4.0, 12, 1.0, size=40, bold=True, color=WHITE)

add_text(s, "경찰 프레임워크 툴킷  /  메타 라우터 /peel",
         0.8, 4.95, 12, 0.55, size=22, color=GOLD)

add_text(s,
         "12개 근거기반 경찰활동 프레임워크를, 상황에 맞게 AI가 골라드립니다",
         0.8, 5.6, 12, 0.5, size=16, color=GRAY_LIGHT)

# 금색 구분선
line = s.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.3), Inches(2.0), Inches(0.06)
)
line.fill.solid()
line.fill.fore_color.rgb = GOLD
line.line.fill.background()

# 저자
add_text(s, "최희철", 0.8, 6.45, 12, 0.4, size=18, bold=True, color=WHITE)
add_text(s,
         "경주경찰서 경찰발전협의회 회원  ·  소프트웨어 개발자  ·  2026년 4월",
         0.8, 6.78, 12, 0.35, size=13, color=GRAY_LIGHT)


# ══════════════════════════════════════════════════════════════
# Slide 2 — 오늘 이야기 순서
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "오늘 이야기 순서", "사례 먼저 보시고, 이론은 짧게, 설치는 천천히")

add_text(s,
         "바쁘신 분들을 위해 결론부터 말씀드리겠습니다.",
         0.6, 1.7, 12, 0.5, size=20, bold=True, color=NAVY)
add_text(s,
         "30년 현장 경험을 부정하는 도구가 아닙니다.\n"
         "여러분이 이미 머리로 하고 계신 일을, 한 장의 수첩처럼 정리해 드리는 도구입니다.",
         0.6, 2.25, 12, 1.2, size=16, color=GRAY_MID)

# 3단계 플로우
stages = [
    ("1", "먼저 사례 4가지", "경주 현장에서 바로\n있을 만한 이야기", RED),
    ("2", "이론은 간단히", "12개 '공구'가 뭔지\n한눈에 보여드립니다", NAVY),
    ("3", "설치는 천천히", "노트북에 어떻게 올리는지\n4단계로 알려드립니다", GOLD),
]
x = 0.6
for num, title, desc, color in stages:
    # 번호 원
    circle = s.shapes.add_shape(
        MSO_SHAPE.OVAL, Inches(x + 0.3), Inches(4.0), Inches(1.0), Inches(1.0)
    )
    circle.fill.solid()
    circle.fill.fore_color.rgb = color
    circle.line.fill.background()
    add_text(s, num, x + 0.3, 4.12, 1.0, 0.8,
             size=36, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    # 박스
    box = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(5.3), Inches(4.0), Inches(1.6)
    )
    box.fill.solid()
    box.fill.fore_color.rgb = WHITE
    box.line.color.rgb = color
    box.line.width = Pt(2)
    box.adjustments[0] = 0.1

    add_text(s, title, x + 0.2, 5.4, 3.6, 0.5,
             size=20, bold=True, color=color, align=PP_ALIGN.CENTER)
    add_text(s, desc, x + 0.2, 5.95, 3.6, 0.9,
             size=14, color=GRAY_MID, align=PP_ALIGN.CENTER)
    x += 4.3

add_footer(s, 2)


# ══════════════════════════════════════════════════════════════
# Slide 3 — 사례 1: 성건동 공원 청소년
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "사례 1 · 성건동 공원", "3개월째 같은 민원, 어떻게 풀까")

# 왼쪽: 이미지
add_image(s, IMG / "case1_park.png", 0.5, 1.5, 6.0, 3.4)

# 오른쪽: 상황 요약
add_text(s, "이런 상황 있으시죠?", 6.85, 1.5, 6.2, 0.5,
         size=20, bold=True, color=NAVY)
situation = (
    "성건동 근린공원, 밤 10시부터 새벽 2시.\n"
    "고등학생 대여섯 명이 술·담배·소란.\n"
    "순찰 차가 가면 흩어지고, 떠나면 복귀.\n"
    "민원은 3개월째 14건 쌓였습니다.\n\n"
    "한쪽 주민은 \"강하게 단속해라\"\n"
    "한쪽 주민은 \"우리 애들 낙인찍지 마라\""
)
add_text(s, situation, 6.85, 2.1, 6.2, 3.0,
         size=15, color=GRAY_DARK, line_spacing=1.35)

# 하단 강조 박스 — 킬러 메시지
add_highlight_box(
    s,
    "단속만으로는 이 아이들을 옆 동네 공원으로 옮길 뿐입니다.\n"
    "/peel 이 권하는 건 순찰 강화가 아니라 — 조명 · 학교 · 편의점 · 존중 네 가지의 동시 개입입니다.",
    0.6, 5.3, 12.1, 1.6, size=16
)

add_footer(s, 3)


# ══════════════════════════════════════════════════════════════
# Slide 4 — 사례 2: 황리단길 야간
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "사례 2 · 황리단길 야간", "관광지가 된 뒤, 순찰 인력은 그대로")

# 오른쪽 이미지 (구도 변화)
add_image(s, IMG / "case2_hwangnidan.png", 6.85, 1.5, 6.0, 3.4)

add_text(s, "이번엔 이런 상황입니다", 0.6, 1.5, 6.2, 0.5,
         size=20, bold=True, color=NAVY)
situation = (
    "황리단길이 관광명소가 된 지 수년.\n"
    "주말 밤마다 관광객·상인·주민이 섞입니다.\n"
    "야간 주취 민원, 주차 마찰, 소음 신고.\n\n"
    "황남파출소 관할 인력은 그대로인데,\n"
    "유동 인구는 몇 배로 늘었습니다.\n"
    "전부 순찰로 막을 수 있는 규모가 아닙니다."
)
add_text(s, situation, 0.6, 2.1, 6.2, 3.0,
         size=15, color=GRAY_DARK, line_spacing=1.35)

add_highlight_box(
    s,
    "이럴 때 /peel 은 Hot Spots(집중 지점)로 시간·장소를 좁히고,\n"
    "상인·주민·경찰 셋이 함께 움직이는 COP(지역사회 경찰활동)로 정리해 드립니다.",
    0.6, 5.3, 12.1, 1.6, size=16
)

add_footer(s, 4)


# ══════════════════════════════════════════════════════════════
# Slide 5 — 사례 3: 외동산단 새벽 절도
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "사례 3 · 외동산단 새벽 절도", "순찰보다 조명이 더 싸고 강하다")

add_image(s, IMG / "case3_industrial.png", 0.5, 1.5, 6.0, 3.4)

add_text(s, "또 다른 흔한 상황", 6.85, 1.5, 6.2, 0.5,
         size=20, bold=True, color=NAVY)
situation = (
    "외동읍 산업단지 공장 주차장.\n"
    "새벽 시간 차량 내 물품 절도가\n"
    "3개월간 12건 접수.\n\n"
    "지금까지 대응은 — 순찰 강화.\n"
    "결과는 — 순찰 빠지면 다시 발생."
)
add_text(s, situation, 6.85, 2.1, 6.2, 2.8,
         size=15, color=GRAY_DARK, line_spacing=1.35)

add_highlight_box(
    s,
    "이 경우 /peel 은 CPTED(환경 설계)부터 점검합니다.\n"
    "조명 교체, CCTV 각도 조정, 관리 주체 협조 — 순찰 강화보다 장기적으로 더 싸고 더 강합니다.",
    0.6, 5.3, 12.1, 1.6, size=16
)

add_footer(s, 5)


# ══════════════════════════════════════════════════════════════
# Slide 6 — 사례 4: "경찰이 무례하다" 민원
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "사례 4 · 규정대로 했는데 민원", "30년 경력이 가장 억울한 순간")

add_image(s, IMG / "case4_station.png", 6.85, 1.5, 6.0, 3.4)

add_text(s, "이게 제일 억울하지 않으십니까", 0.6, 1.5, 6.2, 0.5,
         size=20, bold=True, color=NAVY)
situation = (
    "지구대에서 주취자를 규정대로 처리.\n"
    "며칠 뒤 \"경찰이 고압적이었다\" 민원.\n\n"
    "내부적으로는 절차 다 지켰습니다.\n"
    "그런데 왜 민원이 나왔을까요?\n\n"
    "Tom Tyler(미국 사회심리학자) 연구:\n"
    "시민은 \"결과\"보다 \"과정\"을 기억합니다."
)
add_text(s, situation, 0.6, 2.1, 6.2, 3.0,
         size=15, color=GRAY_DARK, line_spacing=1.35)

add_highlight_box(
    s,
    "절차적 정의 4가지: 발언권 · 중립성 · 존중 · 신뢰.\n"
    "하나라도 빠지면 — 규정을 지켰어도 — 신뢰는 깨집니다. /peel 이 이걸 체크해 드립니다.",
    0.6, 5.3, 12.1, 1.6, size=16
)

add_footer(s, 6)


# ══════════════════════════════════════════════════════════════
# Slide 7 — 이게 뭔데요? (공구함 비유)
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "그래서 이게 뭔가요?", "30년 수첩을, 한 장으로")

add_image(s, IMG / "toolbox.png", 6.85, 1.5, 6.0, 4.5)

add_text(s,
         "고참 반장님의 수첩을 상상해 보십시오.",
         0.6, 1.6, 6.2, 0.6, size=20, bold=True, color=NAVY)

body = (
    "30년 현장을 뛴 반장이\n"
    "\"이런 민원 들어오면 이렇게 풀어라\"\n"
    "라고 적어둔 노트가 있다고 합시다.\n\n"
    "이 도구는 그 노트를\n"
    "— 세계 여러 나라 경찰 연구로 검증된 —\n"
    "12개의 공구로 정리한 것입니다.\n\n"
    "그리고 /peel 이라는 안내 데스크가\n"
    "상황에 맞는 공구를 골라드립니다."
)
add_text(s, body, 0.6, 2.3, 6.2, 4.0,
         size=16, color=GRAY_DARK, line_spacing=1.4)

add_footer(s, 7)


# ══════════════════════════════════════════════════════════════
# Slide 8 — 12개 공구함 한눈에
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "12개 공구, 4개 서랍", "볼트엔 렌치, 나사엔 드라이버")

drawers = [
    ("문제 패턴을 분석할 때",
     ["SARA", "Crime Triangle", "CPTED", "Hot Spots", "ILP"],
     "반복 민원, 핫스팟, 환경 개선",
     NAVY),
    ("조사 · 면담할 때",
     ["PEACE 모델", "인지 면담"],
     "피의자·피해자 진술, 강압 없는 면담",
     NAVY_LIGHT),
    ("현장 위기 대응할 때",
     ["BCSM", "ICAT"],
     "자살·인질·정신건강 위기, 물리력 최소화",
     RED),
    ("신뢰 · 지역사회",
     ["절차적 정의", "COP", "깨진 유리창(비판)"],
     "민원 응대, 주민 관계, \"단속 요구\" 검토",
     GOLD),
]

y = 1.55
for title, tools, desc, color in drawers:
    # 서랍 제목 바
    bar = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(y), Inches(4.5), Inches(1.3)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = color
    bar.line.fill.background()

    add_text(s, title, 0.78, y + 0.2, 4.3, 0.4,
             size=17, bold=True, color=WHITE)
    add_text(s, desc, 0.78, y + 0.75, 4.3, 0.4,
             size=12, color=GRAY_LIGHT)

    # 공구 목록
    tx = 5.35
    for t in tools:
        chip_w = 2.4
        chip = s.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(tx), Inches(y + 0.35), Inches(chip_w), Inches(0.6),
        )
        chip.fill.solid()
        chip.fill.fore_color.rgb = WHITE
        chip.line.color.rgb = color
        chip.line.width = Pt(1.8)
        chip.adjustments[0] = 0.3
        add_text(s, t, tx + 0.05, y + 0.48, chip_w - 0.1, 0.4,
                 size=14, bold=True, color=color, align=PP_ALIGN.CENTER)
        tx += chip_w + 0.15

    y += 1.42

add_footer(s, 8)


# ══════════════════════════════════════════════════════════════
# Slide 9 — 서랍 1 상세: 문제 패턴 분석
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "서랍 1 · 문제 패턴 분석", "반복되는 민원의 뿌리를 찾을 때")

tools = [
    ("SARA",
     "탐색 → 분석 → 대응 → 평가 4단계.\n반복 민원을 근본부터 푸는 기본 순서표."),
    ("범죄 삼각형",
     "가해자·대상·장소 세 꼭짓점으로 쪼개기.\n어디를 움직이면 가장 효과적인지 본다."),
    ("CPTED",
     "환경 설계로 범죄 기회 제거.\n조명 · 시야 · 관리 주체 · 활동 유치."),
    ("Hot Spots",
     "범죄는 관할 전역이 아니라 몇 블록에 집중.\n그 블록에 15분씩 머물면 효과가 급증."),
    ("ILP",
     "데이터로 우선순위 정하기.\n상습 가해자 · 반복 피해자 · 핫스팟."),
]

y = 1.55
for name, desc in tools:
    box = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.6), Inches(y), Inches(12.1), Inches(1.0)
    )
    box.fill.solid()
    box.fill.fore_color.rgb = WHITE
    box.line.color.rgb = NAVY
    box.line.width = Pt(1.2)
    box.adjustments[0] = 0.15

    # 왼쪽 이름 박스
    name_bar = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0.6), Inches(y), Inches(2.8), Inches(1.0),
    )
    name_bar.fill.solid()
    name_bar.fill.fore_color.rgb = NAVY
    name_bar.line.fill.background()
    add_text(s, name, 0.78, y + 0.28, 2.6, 0.5,
             size=18, bold=True, color=WHITE)

    # 오른쪽 설명
    add_text(s, desc, 3.6, y + 0.15, 9.0, 0.85,
             size=14, color=GRAY_DARK, line_spacing=1.3)
    y += 1.08

add_footer(s, 9)


# ══════════════════════════════════════════════════════════════
# Slide 10 — 서랍 2·3 상세: 조사·면담, 현장 위기
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "서랍 2·3 · 조사와 위기", "사람과 마주 앉을 때, 현장이 급할 때")

# 서랍 2
add_text(s, "서랍 2 — 조사 · 면담", 0.6, 1.55, 12, 0.4,
         size=18, bold=True, color=NAVY_LIGHT)

box = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.6), Inches(2.0), Inches(12.1), Inches(2.0),
)
box.fill.solid()
box.fill.fore_color.rgb = WHITE
box.line.color.rgb = NAVY_LIGHT
box.line.width = Pt(1.5)
box.adjustments[0] = 0.06

add_text(s, "PEACE 모델  ·  1992년 영국에서 만든 비강압 면담법",
         0.85, 2.1, 11.8, 0.4, size=16, bold=True, color=NAVY)
add_text(s,
         "Planning(준비) → Engage(관계 맺기) → Account(진술 듣기) → Closure(마무리) → Evaluate(평가).\n"
         "자백을 압박하지 않고, 진실을 수집하는 윤리적 방법입니다. Reid 같은 강압 기법은 제외했습니다.",
         0.85, 2.48, 11.8, 0.7, size=13, color=GRAY_MID, line_spacing=1.3)

add_text(s, "인지 면담  ·  피해자·목격자 기억을 끌어내는 기법",
         0.85, 3.25, 11.8, 0.4, size=16, bold=True, color=NAVY)
add_text(s,
         "당시 상황을 떠올리게 하고, 사소한 것도 다 말하게 하고, 역순으로 되짚기. 메타분석: 25~85% 더 많은 정확한 정보.",
         0.85, 3.6, 11.8, 0.4, size=13, color=GRAY_MID)

# 서랍 3
add_text(s, "서랍 3 — 현장 위기", 0.6, 4.25, 12, 0.4,
         size=18, bold=True, color=RED)

box2 = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.6), Inches(4.7), Inches(12.1), Inches(2.0),
)
box2.fill.solid()
box2.fill.fore_color.rgb = WHITE
box2.line.color.rgb = RED
box2.line.width = Pt(1.5)
box2.adjustments[0] = 0.06

add_text(s, "BCSM  ·  FBI 위기협상 5단계 계단 모델",
         0.85, 4.8, 11.8, 0.4, size=16, bold=True, color=RED)
add_text(s,
         "경청 → 공감 → 신뢰 → 영향 → 행동 변화. 계단을 건너뛰면 설득이 먹히지 않습니다. 자살·인질·농성에 사용.",
         0.85, 5.18, 11.8, 0.4, size=13, color=GRAY_MID)

add_text(s, "ICAT  ·  미국 경찰연구포럼 디에스컬레이션 훈련",
         0.85, 5.68, 11.8, 0.4, size=16, bold=True, color=RED)
add_text(s,
         "시간을 만들고 · 거리를 두고 · 엄폐하고. 루이빌 실험: 물리력 28% ↓, 시민 부상 26% ↓, 경찰관 부상 36% ↓.",
         0.85, 6.05, 11.8, 0.5, size=13, color=GRAY_MID, line_spacing=1.3)

add_footer(s, 10)


# ══════════════════════════════════════════════════════════════
# Slide 11 — 서랍 4 상세: 정당성·지역사회
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "서랍 4 · 정당성과 지역사회", "규정만으로는 부족할 때")

# 절차적 정의 4원칙 카드
add_text(s, "절차적 정의 — 네 가지를 다 지키셔야 신뢰가 쌓입니다",
         0.6, 1.55, 12, 0.4, size=17, bold=True, color=NAVY)

pj = [
    ("Voice", "발언권", "시민이 자기 입장을\n충분히 말할 기회"),
    ("Neutrality", "중립성", "사실과 규칙에 기반한\n일관된 판단"),
    ("Respect", "존중", "존엄을 침해하지 않는\n언어와 태도"),
    ("Trust", "신뢰", "선의로 시민 편에 선다는\n인상을 주기"),
]
x = 0.6
for en, kr, desc in pj:
    card = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(2.0), Inches(3.0), Inches(2.0)
    )
    card.fill.solid()
    card.fill.fore_color.rgb = NAVY
    card.line.color.rgb = GOLD
    card.line.width = Pt(2)
    card.adjustments[0] = 0.1
    add_text(s, en, x + 0.1, 2.15, 2.8, 0.4,
             size=13, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    add_text(s, kr, x + 0.1, 2.5, 2.8, 0.5,
             size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, desc, x + 0.1, 3.1, 2.8, 0.9,
             size=12, color=GRAY_LIGHT, align=PP_ALIGN.CENTER)
    x += 3.15

# 나머지 두 공구
box = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.6), Inches(4.3), Inches(6.0), Inches(2.2)
)
box.fill.solid()
box.fill.fore_color.rgb = WHITE
box.line.color.rgb = GOLD
box.line.width = Pt(1.5)
box.adjustments[0] = 0.06
add_text(s, "COP  ·  지역사회 경찰활동",
         0.85, 4.45, 5.5, 0.4, size=16, bold=True, color=NAVY)
add_text(s,
         "1829년 Robert Peel의 9대 원칙으로 회귀 —\n"
         "\"경찰은 시민이고 시민은 경찰이다.\"\n\n"
         "지구대 밀착, 주민 협력, 문제해결 3축.",
         0.85, 4.85, 5.5, 1.6, size=13, color=GRAY_DARK, line_spacing=1.3)

box2 = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(6.85), Inches(4.3), Inches(6.0), Inches(2.2)
)
box2.fill.solid()
box2.fill.fore_color.rgb = WHITE
box2.line.color.rgb = RED
box2.line.width = Pt(1.5)
box2.adjustments[0] = 0.06
add_text(s, "깨진 유리창  ·  비판적으로 다시 읽기",
         7.1, 4.45, 5.5, 0.4, size=16, bold=True, color=RED)
add_text(s,
         "원래 이론이 \"무관용 단속\"으로 오해되면서\n"
         "뉴욕의 실패 사례가 나왔습니다.\n\n"
         "이 도구는 \"엄격한 단속\" 요구가 들어올 때\n"
         "경고 필터 역할을 합니다.",
         7.1, 4.85, 5.5, 1.7, size=13, color=GRAY_DARK, line_spacing=1.3)

add_footer(s, 11)


# ══════════════════════════════════════════════════════════════
# Slide 12 — 안내데스크: /peel 이 어떻게 고르나
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "/peel 이 어떻게 고르나", "종합병원 안내 데스크와 같습니다")

add_text(s, "비유 — 종합병원 안내 데스크",
         0.6, 1.6, 12, 0.5, size=20, bold=True, color=NAVY)
add_text(s,
         "환자가 \"허리가 아파요\" 하면 안내 데스크가\n"
         "정형외과인지 신경외과인지 재활의학과인지 정해줍니다.\n"
         "/peel 도 똑같습니다.",
         0.6, 2.1, 12, 1.1, size=16, color=GRAY_MID, line_spacing=1.4)

# 3단계 화살표 플로우
stages = [
    ("1단계", "상황 분류",
     "반복 패턴?\n단일 사건?\n현장 위기?"),
    ("2단계", "공구 고르기",
     "12개 중\n2~4개 조합\n(나머지는 뺌)"),
    ("3단계", "순서 잡기",
     "어느 공구를\n먼저 · 나중에\n적용할지"),
    ("결과", "체크리스트",
     "각 단계에서\n물어야 할 질문\n제시"),
]
x = 0.6
for label, title, desc in stages:
    box = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(3.4), Inches(2.9), Inches(2.9)
    )
    box.fill.solid()
    box.fill.fore_color.rgb = WHITE
    box.line.color.rgb = NAVY
    box.line.width = Pt(1.8)
    box.adjustments[0] = 0.08

    # 라벨
    lbl = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(x), Inches(3.4), Inches(2.9), Inches(0.6)
    )
    lbl.fill.solid()
    lbl.fill.fore_color.rgb = NAVY
    lbl.line.fill.background()
    add_text(s, label, x + 0.1, 3.52, 2.7, 0.4,
             size=14, bold=True, color=GOLD, align=PP_ALIGN.CENTER)

    add_text(s, title, x + 0.1, 4.15, 2.7, 0.5,
             size=18, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
    add_text(s, desc, x + 0.1, 4.75, 2.7, 1.4,
             size=13, color=GRAY_MID, align=PP_ALIGN.CENTER, line_spacing=1.35)

    # 화살표 (마지막 제외)
    if x < 9:
        arrow = s.shapes.add_shape(
            MSO_SHAPE.RIGHT_ARROW,
            Inches(x + 2.95), Inches(4.6), Inches(0.22), Inches(0.45)
        )
        arrow.fill.solid()
        arrow.fill.fore_color.rgb = GOLD
        arrow.line.fill.background()
    x += 3.15

add_highlight_box(
    s,
    "기자·공무원이 아닌, 경찰 실무자 눈높이에서 자동으로 초안이 나옵니다.\n"
    "여러분이 그 초안을 현장 경험으로 고쳐서 쓰시면 됩니다.",
    0.6, 6.5, 12.1, 0.9, size=14
)

add_footer(s, 12)


# ══════════════════════════════════════════════════════════════
# Slide 13 — 설치 준비
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "설치 준비 · 아드님 한 번만 부탁하세요", "혼자 1~4단계, 도움은 5~7단계")

add_image(s, IMG / "install_desk.png", 7.3, 1.5, 5.6, 3.4)

add_text(s, "먼저 준비해 두실 것",
         0.6, 1.55, 7.0, 0.5, size=20, bold=True, color=NAVY)
add_bullets(s,
    [
        "노트북 한 대 (윈도우 또는 맥, 둘 다 됩니다)",
        "인터넷 연결",
        "이메일 주소 하나 (구글·카카오도 가능)",
        "월 구독료 약 2만 8천 원 (Claude Pro)",
    ],
    0.8, 2.1, 6.8, 2.6, size=16
)

add_highlight_box(
    s,
    "\"컴퓨터 잘 모르는데요?\" — 괜찮습니다.\n"
    "1~4단계는 혼자 하실 수 있고, 5~7단계만 가족·직원·IT 담당에게 화면 공유로 10분 부탁하시면 됩니다.",
    0.6, 5.3, 12.1, 1.6, size=15
)

add_footer(s, 13)


# ══════════════════════════════════════════════════════════════
# Slide 14 — 설치 7단계
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "설치 7단계 · 순서대로만 따라오세요",
              "1~4 혼자 · 5~7 도움받기")

steps = [
    ("1", "claude.ai 접속 · 회원가입", "이메일 또는 구글 계정", "혼자"),
    ("2", "Claude Pro 구독 (월 2만 8천 원)", "Skills 기능은 Pro부터 가능", "혼자"),
    ("3", "claude.com/download 접속", "Claude Desktop 앱 내려받기", "혼자"),
    ("4", "앱 설치 · 로그인", "일반 프로그램처럼 더블클릭", "혼자"),
    ("5", "zip 파일 받기 (최희철 전달)", "카톡 또는 이메일로 전달", "도움"),
    ("6", "앱에서 설정 → 스킬 → 업로드", "zip 그대로 선택, 풀지 마세요", "도움"),
    ("7", "첫 대화 열어 민원 붙여넣기", "슬래시 명령어 몰라도 됩니다", "도움"),
]

y = 1.55
for num, title, desc, who in steps:
    color = NAVY if who == "혼자" else GOLD
    label_color = WHITE if who == "혼자" else NAVY

    # 번호 원
    circle = s.shapes.add_shape(
        MSO_SHAPE.OVAL, Inches(0.6), Inches(y + 0.1), Inches(0.75), Inches(0.75)
    )
    circle.fill.solid()
    circle.fill.fore_color.rgb = color
    circle.line.fill.background()
    add_text(s, num, 0.6, y + 0.2, 0.75, 0.55,
             size=22, bold=True, color=label_color, align=PP_ALIGN.CENTER)

    # 내용 박스
    box = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(1.5), Inches(y), Inches(9.5), Inches(0.95)
    )
    box.fill.solid()
    box.fill.fore_color.rgb = WHITE
    box.line.color.rgb = color
    box.line.width = Pt(1.2)
    box.adjustments[0] = 0.2
    add_text(s, title, 1.7, y + 0.12, 9.1, 0.4,
             size=16, bold=True, color=NAVY)
    add_text(s, desc, 1.7, y + 0.48, 9.1, 0.4,
             size=13, color=GRAY_MID)

    # 혼자/도움 라벨
    tag = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(11.15), Inches(y + 0.25), Inches(1.55), Inches(0.5)
    )
    tag.fill.solid()
    tag.fill.fore_color.rgb = color
    tag.line.fill.background()
    tag.adjustments[0] = 0.4
    add_text(s, who, 11.15, y + 0.33, 1.55, 0.35,
             size=13, bold=True, color=label_color, align=PP_ALIGN.CENTER)

    y += 0.78

add_footer(s, 14)


# ══════════════════════════════════════════════════════════════
# Slide 15 — 부탁과 연락처
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, NAVY_DEEP)

# 상단 금색 라인
top_line = s.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, 0, Inches(0.8), prs.slide_width, Inches(0.08)
)
top_line.fill.solid()
top_line.fill.fore_color.rgb = GOLD
top_line.line.fill.background()

add_text(s, "부탁드리는 한 가지",
         0.8, 1.1, 12, 0.6, size=20, color=GOLD)

add_text(s,
         "써 보시고 고쳐주십시오.",
         0.8, 1.75, 12, 1.0, size=46, bold=True, color=WHITE)

add_text(s,
         "이 도구는 완성품이 아닙니다. 초안입니다.\n"
         "여러분의 현장 경험으로 틀린 부분을 지적해 주시면,\n"
         "그게 다음 버전에 반영됩니다. 그게 가장 큰 기여입니다.",
         0.8, 3.1, 12, 1.6, size=17, color=GRAY_LIGHT, line_spacing=1.45)

# 연락처 박스
contact_box = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.8), Inches(5.0), Inches(11.8), Inches(1.7)
)
contact_box.fill.solid()
contact_box.fill.fore_color.rgb = NAVY
contact_box.line.color.rgb = GOLD
contact_box.line.width = Pt(1.5)
contact_box.adjustments[0] = 0.1

add_text(s, "만든 사람", 1.1, 5.2, 5, 0.4,
         size=13, color=GOLD)
add_text(s, "최희철", 1.1, 5.5, 5, 0.6,
         size=26, bold=True, color=WHITE)
add_text(s,
         "경주경찰서 경찰발전협의회 회원",
         1.1, 6.1, 5.5, 0.4, size=13, color=GRAY_LIGHT)
add_text(s,
         "소프트웨어 개발자 (평소 AI 도구를 만듭니다)",
         1.1, 6.4, 5.5, 0.4, size=13, color=GRAY_LIGHT)

# 오른쪽 안내
add_text(s, "피드백 주실 때", 7.5, 5.2, 5, 0.4,
         size=13, color=GOLD)
add_text(s, "어느 슬라이드의", 7.5, 5.55, 5, 0.4,
         size=15, color=WHITE)
add_text(s, "어떤 부분이 현장과 다른지", 7.5, 5.85, 5, 0.4,
         size=15, color=WHITE)
add_text(s, "한 줄만 알려주셔도 충분합니다.", 7.5, 6.15, 5, 0.4,
         size=15, bold=True, color=GOLD)

# 하단
add_text(s,
         "\"경찰은 시민이고, 시민은 경찰이다.\"  — Robert Peel, 1829",
         0.8, 6.95, 12, 0.4, size=13, color=GRAY_LIGHT, align=PP_ALIGN.CENTER)


# ──────────────────────────────────────────────────────────────
# 저장
# ──────────────────────────────────────────────────────────────

out = HERE.parent / "docs" / "intro.pptx"
out.parent.mkdir(exist_ok=True)
prs.save(str(out))
print(f"OK Saved: {out}")
print(f"   Slides: {len(prs.slides)}")
