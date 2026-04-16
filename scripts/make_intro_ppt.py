"""
Police Frameworks — 소개 슬라이드 생성기 (60대 경찰관 대상)

구조 (22장):
    1    표지
    2    차례
    3-12 사례 5건 × 2장 (상황 / /peel 출력)
    13   공구함 비유
    14   12개 공구 4서랍
    15   서랍 1 상세 (문제 패턴)
    16   서랍 2·3 상세 (조사·위기)
    17   서랍 4 상세 (정당성)
    18   /peel 안내데스크 비유
    19   설치 준비
    20   설치 단계 (GitHub 다운로드 포함)
    21   첫 대화 예시
    22   부탁과 연락처

작성자: 최희철 (경주경찰서 경찰발전협의회 회원, 소프트웨어 개발자)
"""

from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE


# ──────────────────────────────────────────────────────────────
# 색상
# ──────────────────────────────────────────────────────────────

NAVY = RGBColor(0x1A, 0x36, 0x5D)
NAVY_DEEP = RGBColor(0x0F, 0x23, 0x3F)
NAVY_LIGHT = RGBColor(0x2C, 0x51, 0x82)
RED = RGBColor(0xDC, 0x26, 0x26)
GREEN = RGBColor(0x0F, 0x76, 0x42)
GOLD = RGBColor(0xD6, 0x9E, 0x2E)
GRAY_DARK = RGBColor(0x1F, 0x29, 0x37)
GRAY_MID = RGBColor(0x4A, 0x55, 0x68)
GRAY_LIGHT = RGBColor(0xE2, 0xE8, 0xF0)
GRAY_PALE = RGBColor(0xF1, 0xF5, 0xF9)
BG = RGBColor(0xFA, 0xFC, 0xFF)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
YELLOW_HL = RGBColor(0xFE, 0xF3, 0xC7)
GREEN_HL = RGBColor(0xE8, 0xF5, 0xE9)
RED_HL = RGBColor(0xFE, 0xE2, 0xE2)

FONT = "맑은 고딕"
TOTAL_SLIDES = 22

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
        return slide.shapes.add_picture(
            str(path), Inches(left), Inches(top), Inches(width), Inches(height)
        )
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
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = WHITE

    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.name = FONT
        p2.font.size = Pt(13)
        p2.font.color.rgb = GRAY_LIGHT


def add_text(slide, text, left, top, width, height,
             size=18, bold=False, color=GRAY_DARK, align=PP_ALIGN.LEFT,
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
                size=16, color=GRAY_DARK, line_spacing=1.35, bullet="•"):
    tb = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    for i, b in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"{bullet}  " + b
        p.line_spacing = line_spacing
        p.space_after = Pt(4)
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
    p.text = (
        f"Police Frameworks · /peel · 최희철 "
        f"(경주경찰서 경찰발전협의회 회원, 소프트웨어 개발자) · {page_no}/{TOTAL_SLIDES}"
    )
    p.alignment = PP_ALIGN.RIGHT
    p.font.name = FONT
    p.font.size = Pt(9)
    p.font.color.rgb = GRAY_MID


def add_highlight_box(slide, text, left, top, width, height, fill=YELLOW_HL,
                      size=16, border=GOLD):
    box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left), Inches(top), Inches(width), Inches(height),
    )
    box.fill.solid()
    box.fill.fore_color.rgb = fill
    box.line.color.rgb = border
    box.line.width = Pt(1.2)
    box.adjustments[0] = 0.12
    tb = slide.shapes.add_textbox(
        Inches(left + 0.25), Inches(top + 0.16),
        Inches(width - 0.5), Inches(height - 0.32),
    )
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    for i, line in enumerate(text.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.font.name = FONT
        p.font.size = Pt(size)
        p.font.bold = True
        p.font.color.rgb = GRAY_DARK
        p.line_spacing = 1.3


# ──────────────────────────────────────────────────────────────
# 사례 데이터 (5건)
# ──────────────────────────────────────────────────────────────

CASES = [
    {
        "num": 1,
        "title": "성건동 공원",
        "subtitle": "3개월째 같은 민원, 어떻게 풀까",
        "image": "case1_park.png",
        "image_side": "left",
        "situation_title": "이런 상황 있으시죠?",
        "situation": (
            "경주시 성건동 ○○근린공원, 밤 10시부터 새벽 2시.\n"
            "고등학생 대여섯 명이 술·담배·소란.\n"
            "순찰차가 가면 흩어지고, 떠나면 다시 복귀.\n"
            "민원은 3개월째 14건 쌓였습니다.\n\n"
            "한쪽 주민: \"강하게 단속해라\"\n"
            "한쪽 주민: \"우리 애들 낙인찍지 마라\"\n"
            "성건파출소 야간 인력은 상시 배치 불가."
        ),
        "hook": (
            "단속만으로는 옆 동네 공원으로 옮겨갈 뿐.\n"
            "/peel 은 \"단속이 아닌 7개 공구 동시 투입\"을 권합니다."
        ),
        "selected": [
            ("SARA", "4단계 진단 사이클"),
            ("Crime Triangle", "6박스 원인 분해"),
            ("Hot Spots", "시간·공간 집중 확인"),
            ("CPTED", "조명·조경·시야 개선"),
            ("COP", "학교·청소년센터·공원녹지과 연계"),
            ("Procedural Justice", "청소년·주민 존엄 유지"),
            ("Broken Windows 비판", "\"무관용\" 함정 필터"),
        ],
        "excluded": [
            ("PEACE·Cognitive", "조사 단계가 아님"),
            ("BCSM·ICAT", "현장 위기 아님"),
            ("ILP", "단일 지점 전술 문제"),
        ],
        "pipeline": [
            "Scanning\n14건 지도화",
            "Analysis\n6박스 분해",
            "BW 필터\n단속 함정 차단",
            "Response\nCPTED+COP",
            "PJ 삽입\n청소년 존엄",
            "Assessment\n3개월 재측정",
        ],
        "actions": [
            "경주시 공원녹지과에 조명·조경 개선 요청 공문 (1주 내)",
            "인근 중·고교, 청소년상담복지센터와 주간 연계 회의",
            "주민 설명회 — 4요소 언어로 \"단속만 안 하는 이유\" 공유",
        ],
    },
    {
        "num": 2,
        "title": "황리단길 야간",
        "subtitle": "관광지가 된 뒤, 순찰 인력은 그대로",
        "image": "case2_hwangnidan.png",
        "image_side": "right",
        "situation_title": "이번엔 이런 상황",
        "situation": (
            "황남동 황리단길이 관광명소가 된 지 수년.\n"
            "주말 밤마다 관광객·상인·주민이 섞입니다.\n"
            "야간 주취·소란·주차 마찰·소음 신고.\n\n"
            "황남파출소 관할 인력은 그대로인데,\n"
            "유동 인구는 몇 배로 늘었습니다.\n"
            "전부 순찰로 막을 수 있는 규모가 아닙니다.\n"
            "상인은 영업을, 주민은 수면을 요구합니다."
        ),
        "hook": (
            "공간은 좁고 인력은 한정. /peel 은 \"전 관할 순찰\" 대신\n"
            "시간·지점을 좁히고 상인·주민이 함께 움직이는 구조를 권합니다."
        ),
        "selected": [
            ("Hot Spots", "22~02시 × 특정 블록 집중"),
            ("ILP", "데이터로 우선순위 설정"),
            ("COP", "상인협·주민자치위 파트너십"),
            ("Procedural Justice", "상인·주민·관광객 4요소 준수"),
            ("Broken Windows 비판", "\"엄격 단속\" 요구 검토"),
        ],
        "excluded": [
            ("PEACE·Cognitive", "조사 면담 단계 아님"),
            ("BCSM·ICAT", "현장 위기 아님"),
            ("CPTED", "관광지 설계 변경은 주 해법 아님"),
            ("SARA 독자", "Hot Spots가 우선"),
        ],
        "pipeline": [
            "112 분석\n시간·지점",
            "Koper 15분\n순찰 전략",
            "상인·주민\n협의체",
            "PJ 4요소\n접촉 훈련",
            "분기 평가\n체감·신고",
        ],
        "actions": [
            "황남파출소 + 생활안전계: 최근 6개월 야간 신고 유형 분포 분석",
            "상인협의회·주민자치위 첫 간담회 (관광객 관련 문제 공동 의제)",
            "관광 성수기 주말 전용 시간대 집중 순찰 15분 사이클 배치",
        ],
    },
    {
        "num": 3,
        "title": "외동산단 새벽 절도",
        "subtitle": "순찰보다 조명이 더 싸고 강하다",
        "image": "case3_industrial.png",
        "image_side": "left",
        "situation_title": "또 다른 흔한 상황",
        "situation": (
            "외동읍 산업단지 공장 주차장.\n"
            "새벽 시간 차량 내 물품 절도 12건 / 3개월.\n"
            "지금까지 대응: 순찰 강화.\n"
            "결과: 순찰 빠지면 다시 발생.\n\n"
            "외동파출소 새벽 인력은 한계.\n"
            "단지 관리공단은 방범이 주 업무가 아닙니다."
        ),
        "hook": (
            "Sherman·Weisburd 연구: 핫스팟 15분 체류만으로 효과 급증.\n"
            "다만 지속 효과를 위해선 CPTED 환경 개입이 더 쌉니다."
        ),
        "selected": [
            ("SARA", "문제 구조화"),
            ("Crime Triangle", "가해자·대상·장소 분해"),
            ("Hot Spots", "구역 집중 확인"),
            ("CPTED", "조명·CCTV·차단기·시야"),
            ("COP", "단지 관리공단·입주기업 협력"),
        ],
        "excluded": [
            ("PEACE·Cognitive", "조사 면담 단계 아님"),
            ("BCSM·ICAT", "현장 위기 아님"),
            ("Procedural Justice", "주 개입 아님 (단, 기본 전제)"),
            ("Broken Windows", "무질서 프레임 부적절"),
        ],
        "pipeline": [
            "신고 정리\n12건 지도화",
            "6박스\n분해",
            "CPTED\n현장 점검",
            "Response\n조명·CCTV",
            "관리공단\n책임 분담",
            "3개월\n재측정",
        ],
        "actions": [
            "단지 관리공단에 CPTED 점검 요청 공문 (조명 수명·사각지대·차단기 작동)",
            "입주기업 방범 담당자 연락망 구축 — 월 1회 브리핑",
            "조명 교체·CCTV 각도 조정 예산은 관리공단·지자체 협력으로 확보",
        ],
    },
    {
        "num": 4,
        "title": "규정대로 했는데 민원",
        "subtitle": "30년 경력이 가장 억울한 순간",
        "image": "case4_station.png",
        "image_side": "right",
        "situation_title": "이게 제일 억울하지 않으십니까",
        "situation": (
            "지구대에서 주취자를 규정대로 처리.\n"
            "며칠 뒤 \"경찰이 고압적이었다\" 민원.\n\n"
            "내부적으로는 절차 다 지켰습니다.\n"
            "그런데 왜 민원이 나왔을까요?\n\n"
            "Tom Tyler(미국 사회심리학자) 연구:\n"
            "시민은 \"결과\"보다 \"과정\"을 기억합니다.\n"
            "4요소 중 하나라도 부족하면 신뢰가 깨집니다."
        ),
        "hook": (
            "\"규정대로\"는 정당성 언어가 아닙니다.\n"
            "/peel 은 4요소 체크리스트로 사건을 해부해 드립니다."
        ),
        "selected": [
            ("Procedural Justice", "4요소로 사건 해부"),
            ("COP", "지구대장 → 주민 직접 연락"),
            ("SARA", "재발 방지 구조 분석"),
        ],
        "excluded": [
            ("Hot Spots·CPTED", "장소 문제 아님"),
            ("PEACE·Cognitive", "이미 종결"),
            ("BCSM·ICAT", "위기 아님"),
            ("Crime Triangle", "범죄 분석 아님"),
            ("ILP", "데이터 규모 아님"),
            ("Broken Windows", "무관"),
        ],
        "pipeline": [
            "4요소\n사건 평가",
            "Voice\n주민 청취",
            "Respect\n사과 필요 시",
            "SARA\n재발 방지",
            "교육\n언어·태도",
        ],
        "actions": [
            "지구대장이 민원인에게 직접 연락 — 4요소 언어로 사건 재설명",
            "감찰·교육과와 공유 — 유사 민원 빈도 확인 및 재교육",
            "접촉 표준 스크립트 마련 — 발언권·중립성·존중·신뢰 삽입",
        ],
    },
    {
        "num": 5,
        "title": "거래처 사칭 사기",
        "subtitle": "순찰로는 절대 못 잡는 범죄",
        "image": "case5_fraud.png",
        "image_side": "left",
        "situation_title": "경제범죄도 /peel 이 다룹니다",
        "situation": (
            "거래처 구매 담당자를 사칭해\n"
            "\"공사 건이 급해서 자재를 먼저 사서 보내달라\"\n"
            "피해업체가 결제 후 연락 두절.\n\n"
            "카카오톡 프로필 복제, 이메일 도메인 변조\n"
            "(예: samsung → samsnug), 발신번호 변작.\n\n"
            "단일 사건이 아닌 조직·연속·디지털 범죄.\n"
            "물리적 공간이 없어 순찰로 막을 수 없습니다."
        ),
        "hook": (
            "이 범죄는 순찰로 못 잡습니다.\n"
            "/peel 은 데이터(ILP) + 예방(COP) + 진술 인출(Cognitive) 조합을 권합니다."
        ),
        "selected": [
            ("SARA", "문제 정의·분석 구조"),
            ("ILP", "계좌·전화·IP 패턴 분석"),
            ("Crime Triangle", "가해자·대상·통로 분해"),
            ("COP", "조달담당자 교육·조기 경보"),
            ("Cognitive Interview", "피해자 진술 단서 최대 인출"),
            ("PEACE", "검거 시 구조적 면담"),
        ],
        "excluded": [
            ("CPTED·Hot Spots", "물리 공간 범죄 아님"),
            ("BCSM·ICAT", "위기 대응 아님"),
            ("Broken Windows", "해당 없음"),
            ("Procedural Justice", "기본 전제 (2차 가해 금지)"),
        ],
        "pipeline": [
            "SARA\n유형 집계",
            "ILP\n계좌·전화\n클러스터링",
            "Triangle\n통로 차단",
            "COP\n조달교육\nMOU",
            "Cognitive\n진술 인출",
            "PEACE\n검거 면담",
        ],
        "actions": [
            "생활안전계 + 사이버수사대 합동 TF — 3개월 신고 계좌·전화 통합 (1주)",
            "상공회의소·산업단지 조달담당자 실전 교육 자료 개발 (3주)",
            "\"신규 계좌 2인 재확인\" 프로토콜 템플릿 배포 (3주)",
        ],
    },
]


# ──────────────────────────────────────────────────────────────
# 사례 슬라이드 빌더 (A: 상황)
# ──────────────────────────────────────────────────────────────

def make_case_slide_a(prs, case, page_no):
    s = prs.slides.add_slide(blank)
    set_background(s, BG)
    add_title_bar(s, f"사례 {case['num']} · {case['title']}", case["subtitle"])

    img_path = IMG / case["image"]
    if case["image_side"] == "left":
        add_image(s, img_path, 0.5, 1.5, 6.0, 3.5)
        text_x = 6.85
    else:
        add_image(s, img_path, 6.85, 1.5, 6.0, 3.5)
        text_x = 0.6

    add_text(s, case["situation_title"], text_x, 1.5, 6.2, 0.5,
             size=20, bold=True, color=NAVY)
    add_text(s, case["situation"], text_x, 2.1, 6.2, 2.9,
             size=14, color=GRAY_DARK, line_spacing=1.35)

    add_highlight_box(s, case["hook"], 0.6, 5.3, 12.1, 1.55, size=15)

    add_footer(s, page_no)
    return s


# ──────────────────────────────────────────────────────────────
# 사례 슬라이드 빌더 (B: /peel 출력)
# ──────────────────────────────────────────────────────────────

def make_case_slide_b(prs, case, page_no):
    s = prs.slides.add_slide(blank)
    set_background(s, BG)
    add_title_bar(s,
                  f"사례 {case['num']} · /peel 이 내주는 답",
                  "어떤 공구를 꺼내고 어떤 공구는 뺄지")

    # ── 왼쪽: 선정 (녹색) ─────────────────────
    sel_bar = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(1.5), Inches(6.05), Inches(0.4)
    )
    sel_bar.fill.solid()
    sel_bar.fill.fore_color.rgb = GREEN
    sel_bar.line.fill.background()
    add_text(s, "✓ 선정 — 이 공구들을 꺼냅니다",
             0.75, 1.55, 5.9, 0.32, size=13, bold=True, color=WHITE)

    y = 2.0
    for name, reason in case["selected"]:
        add_text(s, f"•  {name}", 0.75, y, 3.2, 0.3,
                 size=13, bold=True, color=GREEN)
        add_text(s, reason, 3.95, y + 0.02, 2.7, 0.3,
                 size=11, color=GRAY_MID)
        y += 0.32

    # ── 오른쪽: 제외 (회색) ────────────────────
    ex_bar = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(6.85), Inches(1.5), Inches(6.05), Inches(0.4)
    )
    ex_bar.fill.solid()
    ex_bar.fill.fore_color.rgb = GRAY_MID
    ex_bar.line.fill.background()
    add_text(s, "✕ 제외 — 이 공구들은 뺐습니다",
             7.0, 1.55, 5.9, 0.32, size=13, bold=True, color=WHITE)

    y = 2.0
    for name, reason in case["excluded"]:
        add_text(s, f"•  {name}", 7.0, y, 3.2, 0.3,
                 size=13, bold=True, color=GRAY_MID)
        add_text(s, reason, 10.2, y + 0.02, 2.7, 0.3,
                 size=11, color=GRAY_MID)
        y += 0.32

    # ── 중간: 파이프라인 (가로 플로우) ─────────
    add_text(s, "→ 이 순서로 진행합니다",
             0.6, 4.45, 12.1, 0.3, size=13, bold=True, color=NAVY)

    steps = case["pipeline"]
    n = len(steps)
    # 박스 하나 폭 계산
    total_w = 12.1
    gap = 0.15
    box_w = (total_w - gap * (n - 1)) / n
    x = 0.6
    for i, step in enumerate(steps):
        box = s.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x), Inches(4.85), Inches(box_w), Inches(1.0)
        )
        box.fill.solid()
        box.fill.fore_color.rgb = NAVY
        box.line.fill.background()
        box.adjustments[0] = 0.15
        add_text(s, step, x + 0.05, 4.95, box_w - 0.1, 0.85,
                 size=10, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, line_spacing=1.2)
        # 화살표 (마지막 제외)
        if i < n - 1:
            arr = s.shapes.add_shape(
                MSO_SHAPE.RIGHT_ARROW,
                Inches(x + box_w + 0.01), Inches(5.22), Inches(0.12), Inches(0.25)
            )
            arr.fill.solid()
            arr.fill.fore_color.rgb = GOLD
            arr.line.fill.background()
        x += box_w + gap

    # ── 하단: 즉시 할 수 있는 행동 ─────────────
    action_box = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.6), Inches(6.1), Inches(12.1), Inches(0.95)
    )
    action_box.fill.solid()
    action_box.fill.fore_color.rgb = YELLOW_HL
    action_box.line.color.rgb = GOLD
    action_box.line.width = Pt(1.2)
    action_box.adjustments[0] = 0.15

    add_text(s, "⚡ 바로 할 수 있는 행동",
             0.85, 6.17, 11.8, 0.3, size=12, bold=True, color=RED)
    tb = s.shapes.add_textbox(
        Inches(0.85), Inches(6.43), Inches(11.8), Inches(0.7)
    )
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, action in enumerate(case["actions"]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"{i+1}.  " + action
        p.line_spacing = 1.15
        p.space_after = Pt(1)
        for run in p.runs:
            run.font.name = FONT
            run.font.size = Pt(11)
            run.font.color.rgb = GRAY_DARK

    add_footer(s, page_no)
    return s


# ══════════════════════════════════════════════════════════════
# 프레젠테이션 생성
# ══════════════════════════════════════════════════════════════

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]


# ══════════════════════════════════════════════════════════════
# Slide 1 — 표지
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, NAVY_DEEP)
add_image(s, IMG / "cover.png", 0, 0, 13.333, 7.5)

overlay = s.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, 0, Inches(3.7), prs.slide_width, Inches(3.8)
)
overlay.fill.solid()
overlay.fill.fore_color.rgb = NAVY_DEEP
overlay.line.fill.background()

add_text(s, "POLICE FRAMEWORKS", 0.8, 0.6, 12, 0.4,
         size=14, bold=True, color=GOLD)
add_text(s, "3개월째 똑같은 민원, 이번엔 순서부터",
         0.8, 4.0, 12, 1.0, size=40, bold=True, color=WHITE)
add_text(s, "경찰 프레임워크 툴킷  /  메타 라우터 /peel",
         0.8, 4.95, 12, 0.55, size=22, color=GOLD)
add_text(s,
         "12개 근거기반 경찰활동 프레임워크를, 상황에 맞게 AI가 골라드립니다",
         0.8, 5.6, 12, 0.5, size=16, color=GRAY_LIGHT)

line = s.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.3), Inches(2.0), Inches(0.06)
)
line.fill.solid()
line.fill.fore_color.rgb = GOLD
line.line.fill.background()

add_text(s, "최희철", 0.8, 6.45, 12, 0.4, size=18, bold=True, color=WHITE)
add_text(s,
         "경주경찰서 경찰발전협의회 회원  ·  소프트웨어 개발자  ·  2026년 4월",
         0.8, 6.78, 12, 0.35, size=13, color=GRAY_LIGHT)


# ══════════════════════════════════════════════════════════════
# Slide 2 — 차례
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "오늘 이야기 순서", "사례 먼저 · 이론은 짧게 · 설치는 천천히")

add_text(s, "결론부터 말씀드립니다.",
         0.6, 1.6, 12, 0.5, size=20, bold=True, color=NAVY)
add_text(s,
         "30년 현장 경험을 부정하는 도구가 아닙니다.\n"
         "여러분이 이미 머리로 하시는 일을 한 장의 수첩처럼 정리해 드리는 도구입니다.",
         0.6, 2.15, 12, 1.2, size=15, color=GRAY_MID)

stages = [
    ("1", "사례 5가지", "경주 현장에서 바로\n있을 만한 이야기\n(각 사례 2장씩)", RED),
    ("2", "이론은 간단히", "12개 '공구'가 뭔지\n한눈에 보여드립니다\n(5장)", NAVY),
    ("3", "설치는 천천히", "노트북에 어떻게 올리는지\n단계별로\n(4장)", GOLD),
]
x = 0.6
for num, title, desc, color in stages:
    circle = s.shapes.add_shape(
        MSO_SHAPE.OVAL, Inches(x + 0.3), Inches(3.8), Inches(1.0), Inches(1.0)
    )
    circle.fill.solid()
    circle.fill.fore_color.rgb = color
    circle.line.fill.background()
    add_text(s, num, x + 0.3, 3.92, 1.0, 0.8,
             size=36, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    box = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(5.1), Inches(4.0), Inches(1.85)
    )
    box.fill.solid()
    box.fill.fore_color.rgb = WHITE
    box.line.color.rgb = color
    box.line.width = Pt(2)
    box.adjustments[0] = 0.1
    add_text(s, title, x + 0.2, 5.22, 3.6, 0.5,
             size=20, bold=True, color=color, align=PP_ALIGN.CENTER)
    add_text(s, desc, x + 0.2, 5.8, 3.6, 1.1,
             size=13, color=GRAY_MID, align=PP_ALIGN.CENTER)
    x += 4.3

add_footer(s, 2)


# ══════════════════════════════════════════════════════════════
# Slide 3-12 — 사례 5건 × 2장
# ══════════════════════════════════════════════════════════════
page = 3
for case in CASES:
    make_case_slide_a(prs, case, page)
    make_case_slide_b(prs, case, page + 1)
    page += 2


# ══════════════════════════════════════════════════════════════
# Slide 13 — 이게 뭔데요? (공구함 비유)
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "그래서 이게 뭔가요?", "30년 수첩을 한 장으로, 공구함과 공구처럼")

add_image(s, IMG / "toolbox.png", 6.85, 1.5, 6.0, 4.5)

add_text(s, "비유 — 고참 반장님의 수첩", 0.6, 1.6, 6.2, 0.6,
         size=20, bold=True, color=NAVY)
body = (
    "30년 현장을 뛴 반장이 \"이런 민원엔 이렇게\"\n"
    "라고 적어둔 노트가 있다고 합시다.\n\n"
    "이 도구는 그 노트를 — 세계 여러 나라 경찰 연구로\n"
    "검증된 — 12개의 공구로 정리한 것입니다.\n\n"
    "그리고 /peel 이라는 안내 데스크가\n"
    "상황에 맞는 공구를 골라드립니다.\n\n"
    "볼트엔 렌치, 나사엔 드라이버.\n"
    "민원엔 절차적 정의, 반복엔 SARA."
)
add_text(s, body, 0.6, 2.3, 6.2, 4.7,
         size=15, color=GRAY_DARK, line_spacing=1.4)

add_footer(s, 13)


# ══════════════════════════════════════════════════════════════
# Slide 14 — 12개 공구 4개 서랍 (OVERFLOW FIX)
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "12개 공구, 4개 서랍", "상황에 맞게 골라 쓰는 공구함")

drawers = [
    ("문제 패턴을 분석할 때",
     ["SARA", "범죄삼각형", "CPTED", "핫스팟", "ILP"],
     "반복 민원·핫스팟·환경 개선",
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
     ["절차적 정의", "COP", "깨진유리창(비판)"],
     "민원 응대, 주민 관계, \"단속 요구\" 검토",
     GOLD),
]

# 공간 계산
CHIP_AREA_X = 4.7        # chips 시작
CHIP_AREA_END = 12.95    # chips 끝
CHIP_AREA_W = CHIP_AREA_END - CHIP_AREA_X  # 8.25
CHIP_GAP = 0.12

y = 1.55
for title, tools, desc, color in drawers:
    # 서랍 제목 바
    bar = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(y), Inches(4.0), Inches(1.3)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = color
    bar.line.fill.background()
    add_text(s, title, 0.75, y + 0.22, 3.8, 0.45,
             size=16, bold=True, color=WHITE)
    add_text(s, desc, 0.75, y + 0.74, 3.8, 0.5,
             size=11, color=GRAY_LIGHT)

    # 공구 chips — 개수에 따라 폭 동적 계산
    n = len(tools)
    chip_w = (CHIP_AREA_W - CHIP_GAP * (n - 1)) / n
    tx = CHIP_AREA_X
    # 공구 개수에 따른 폰트
    chip_font = 11 if n >= 5 else (14 if n == 3 else 17)

    for t in tools:
        chip = s.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(tx), Inches(y + 0.3), Inches(chip_w), Inches(0.7),
        )
        chip.fill.solid()
        chip.fill.fore_color.rgb = WHITE
        chip.line.color.rgb = color
        chip.line.width = Pt(1.8)
        chip.adjustments[0] = 0.3
        add_text(s, t, tx + 0.05, y + 0.45, chip_w - 0.1, 0.4,
                 size=chip_font, bold=True, color=color, align=PP_ALIGN.CENTER)
        tx += chip_w + CHIP_GAP

    y += 1.42

add_footer(s, 14)


# ══════════════════════════════════════════════════════════════
# Slide 15 — 서랍 1 상세
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "서랍 1 · 문제 패턴 분석", "반복되는 민원의 뿌리를 찾을 때")

tools = [
    ("SARA",
     "탐색 → 분석 → 대응 → 평가 4단계.\n반복 민원을 근본부터 푸는 기본 순서표."),
    ("범죄 삼각형",
     "가해자·대상·장소 세 꼭짓점 + 각 억제자. 어디를 움직이면 가장 효과적인지 6박스로 본다."),
    ("CPTED",
     "환경 설계로 범죄 기회 제거. 조명·시야·관리 주체·활동 유치 6원칙."),
    ("핫스팟 경찰활동",
     "범죄는 관할 전역이 아니라 몇 블록에 집중. Koper 15분 규칙."),
    ("ILP",
     "데이터로 우선순위 정하기. 상습 가해자·반복 피해자·핫스팟 3대 대상."),
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
    name_bar = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0.6), Inches(y), Inches(2.8), Inches(1.0),
    )
    name_bar.fill.solid()
    name_bar.fill.fore_color.rgb = NAVY
    name_bar.line.fill.background()
    add_text(s, name, 0.78, y + 0.3, 2.6, 0.5,
             size=16, bold=True, color=WHITE)
    add_text(s, desc, 3.6, y + 0.18, 9.0, 0.8,
             size=13, color=GRAY_DARK, line_spacing=1.3)
    y += 1.08

add_footer(s, 15)


# ══════════════════════════════════════════════════════════════
# Slide 16 — 서랍 2·3 상세
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "서랍 2·3 · 조사와 위기", "사람과 마주 앉을 때, 현장이 급할 때")

# 서랍 2
add_text(s, "서랍 2 — 조사·면담", 0.6, 1.55, 12, 0.4,
         size=17, bold=True, color=NAVY_LIGHT)
box = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.6), Inches(2.0), Inches(12.1), Inches(1.9),
)
box.fill.solid()
box.fill.fore_color.rgb = WHITE
box.line.color.rgb = NAVY_LIGHT
box.line.width = Pt(1.5)
box.adjustments[0] = 0.06

add_text(s, "PEACE 모델  ·  1992년 영국, 강압 없는 면담 5단계",
         0.85, 2.1, 11.8, 0.4, size=15, bold=True, color=NAVY)
add_text(s,
         "Planning → Engage → Account → Closure → Evaluate. 자백 압박이 아닌 진실 수집.\n"
         "허위자백 스캔들(Guildford Four 등) 이후 Reid 기법을 대체한 윤리적 모델.",
         0.85, 2.48, 11.8, 0.7, size=12, color=GRAY_MID, line_spacing=1.3)
add_text(s, "인지 면담  ·  피해자·목격자 기억 인출 극대화",
         0.85, 3.2, 11.8, 0.4, size=15, bold=True, color=NAVY)
add_text(s,
         "문맥 복원·모든 세부·역순·관점 전환 4기법. 메타분석 25~85% 더 많은 정확한 정보.",
         0.85, 3.55, 11.8, 0.3, size=12, color=GRAY_MID)

# 서랍 3
add_text(s, "서랍 3 — 현장 위기", 0.6, 4.15, 12, 0.4,
         size=17, bold=True, color=RED)
box2 = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.6), Inches(4.6), Inches(12.1), Inches(2.1),
)
box2.fill.solid()
box2.fill.fore_color.rgb = WHITE
box2.line.color.rgb = RED
box2.line.width = Pt(1.5)
box2.adjustments[0] = 0.06

add_text(s, "BCSM  ·  FBI 위기협상 5단계 계단",
         0.85, 4.7, 11.8, 0.4, size=15, bold=True, color=RED)
add_text(s,
         "경청 → 공감 → 신뢰 → 영향 → 행동 변화. 계단은 건너뛸 수 없음.\n자살·인질·농성 협상.",
         0.85, 5.05, 11.8, 0.7, size=12, color=GRAY_MID, line_spacing=1.3)
add_text(s, "ICAT  ·  PERF 디에스컬레이션 훈련",
         0.85, 5.8, 11.8, 0.4, size=15, bold=True, color=RED)
add_text(s,
         "시간·거리·엄폐. 루이빌 실험: 물리력 28% ↓, 시민 부상 26% ↓, 경찰관 부상 36% ↓.",
         0.85, 6.15, 11.8, 0.4, size=12, color=GRAY_MID)

add_footer(s, 16)


# ══════════════════════════════════════════════════════════════
# Slide 17 — 서랍 4 상세
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "서랍 4 · 정당성과 지역사회", "규정만으로는 부족할 때")

add_text(s, "절차적 정의 — 네 가지를 다 지키셔야 신뢰가 쌓입니다",
         0.6, 1.55, 12, 0.4, size=16, bold=True, color=NAVY)

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
             size=12, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    add_text(s, kr, x + 0.1, 2.5, 2.8, 0.5,
             size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, desc, x + 0.1, 3.1, 2.8, 0.9,
             size=12, color=GRAY_LIGHT, align=PP_ALIGN.CENTER)
    x += 3.15

box = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.6), Inches(4.3), Inches(6.0), Inches(2.3)
)
box.fill.solid()
box.fill.fore_color.rgb = WHITE
box.line.color.rgb = GOLD
box.line.width = Pt(1.5)
box.adjustments[0] = 0.06
add_text(s, "COP  ·  지역사회 경찰활동",
         0.85, 4.45, 5.5, 0.4, size=16, bold=True, color=NAVY)
add_text(s,
         "1829년 Robert Peel의 9대 원칙으로 회귀.\n"
         "\"경찰은 시민이고 시민은 경찰이다.\"\n\n"
         "지구대 밀착, 주민 협력, 문제해결 3축.",
         0.85, 4.85, 5.5, 1.7, size=13, color=GRAY_DARK, line_spacing=1.3)

box2 = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(6.85), Inches(4.3), Inches(6.0), Inches(2.3)
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
         "뉴욕 Stop-and-Frisk 같은 실패 사례가 나옴.\n\n"
         "이 도구는 \"엄격 단속\" 요구가 들어올 때\n"
         "경고 필터 역할을 합니다.",
         7.1, 4.85, 5.5, 1.7, size=13, color=GRAY_DARK, line_spacing=1.3)

add_footer(s, 17)


# ══════════════════════════════════════════════════════════════
# Slide 18 — /peel 안내데스크
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "/peel 이 어떻게 고르나", "종합병원 안내 데스크와 같습니다")

add_text(s, "비유 — 종합병원 안내 데스크",
         0.6, 1.6, 12, 0.5, size=20, bold=True, color=NAVY)
add_text(s,
         "환자가 \"허리가 아파요\" 하면 안내 데스크가 정형외과·신경외과·재활의학과\n"
         "어디로 가야 할지 정해줍니다. /peel 도 똑같습니다.",
         0.6, 2.1, 12, 1.1, size=15, color=GRAY_MID, line_spacing=1.4)

stages = [
    ("1단계", "상황 분류",
     "반복 패턴?\n단일 사건?\n현장 위기?"),
    ("2단계", "공구 고르기",
     "12개 중 2~4개 조합\n(나머지는 뺌)"),
    ("3단계", "순서 잡기",
     "어느 공구를\n먼저 · 나중에"),
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
    lbl = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(x), Inches(3.4), Inches(2.9), Inches(0.6)
    )
    lbl.fill.solid()
    lbl.fill.fore_color.rgb = NAVY
    lbl.line.fill.background()
    add_text(s, label, x + 0.1, 3.52, 2.7, 0.4,
             size=13, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    add_text(s, title, x + 0.1, 4.15, 2.7, 0.5,
             size=17, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
    add_text(s, desc, x + 0.1, 4.75, 2.7, 1.4,
             size=12, color=GRAY_MID, align=PP_ALIGN.CENTER, line_spacing=1.35)
    if x < 9:
        arr = s.shapes.add_shape(
            MSO_SHAPE.RIGHT_ARROW,
            Inches(x + 2.95), Inches(4.6), Inches(0.22), Inches(0.45)
        )
        arr.fill.solid()
        arr.fill.fore_color.rgb = GOLD
        arr.line.fill.background()
    x += 3.15

add_highlight_box(
    s,
    "경찰 실무자 눈높이에서 자동으로 초안이 나옵니다.\n"
    "여러분이 그 초안을 현장 경험으로 고쳐서 쓰시면 됩니다.",
    0.6, 6.5, 12.1, 0.9, size=13
)

add_footer(s, 18)


# ══════════════════════════════════════════════════════════════
# Slide 19 — 설치 준비물 (Max 추천)
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "설치 준비물", "노트북 한 대면 됩니다")

add_image(s, IMG / "install_desk.png", 7.3, 1.5, 5.6, 3.4)

add_text(s, "먼저 준비해 두실 것",
         0.6, 1.55, 7.0, 0.5, size=19, bold=True, color=NAVY)
add_bullets(s,
    [
        "노트북 한 대 (윈도우·맥 모두 됩니다)",
        "인터넷 연결",
        "이메일 주소 하나 (구글·카카오 가능)",
        "월 구독료 — 아래 권장 참조",
    ],
    0.8, 2.1, 6.8, 2.4, size=15
)

# Max 추천 박스
max_box = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.6), Inches(4.65), Inches(6.5), Inches(1.4)
)
max_box.fill.solid()
max_box.fill.fore_color.rgb = YELLOW_HL
max_box.line.color.rgb = GOLD
max_box.line.width = Pt(2)
max_box.adjustments[0] = 0.1
add_text(s, "구독 권장  ·  Claude Max", 0.8, 4.78, 6.1, 0.4,
         size=14, bold=True, color=RED)
add_text(s,
         "Claude Pro (월 ~2.8만 원) 도 Skills 기능이 됩니다.\n"
         "다만 본격 업무 사용이면 Max (월 ~14만 원) 가 편합니다 — 사용량 5배.",
         0.8, 5.15, 6.1, 0.85, size=12, color=GRAY_DARK, line_spacing=1.3)

add_highlight_box(
    s,
    "\"컴퓨터 잘 모르는데요?\" — 괜찮습니다.\n"
    "1~4단계는 혼자, 5~7단계만 가족·직원·IT 담당에게 10분 부탁하시면 됩니다.",
    0.6, 6.15, 12.1, 0.9, size=14
)

add_footer(s, 19)


# ══════════════════════════════════════════════════════════════
# Slide 20 — 설치 7단계 (GitHub 다운로드 포함)
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "설치 7단계  ·  순서대로만 따라오세요",
              "1~4 혼자 · 5~7 도움받기")

steps = [
    ("1", "claude.ai 접속 · 회원가입", "이메일 또는 구글 계정", "혼자"),
    ("2", "Claude Max 구독 (월 약 14만 원)", "Pro도 가능하지만 실전은 Max 권장", "혼자"),
    ("3", "claude.com/download → Claude Desktop 설치", "일반 프로그램처럼 더블클릭", "혼자"),
    ("4", "Claude Desktop 로그인", "1단계 계정으로", "혼자"),
    ("5", "github.com/ironyjk/police-frameworks 접속", "초록색 Code 버튼 → Download ZIP", "도움"),
    ("6", "Claude Desktop 설정 → Skills → Upload", "zip 그대로 올림 (풀지 마세요)", "도움"),
    ("7", "새 대화 창에서 peel 호출", "\"peel 로 이 민원 분석해줘\" 로 시작", "도움"),
]

y = 1.45
for num, title, desc, who in steps:
    color = NAVY if who == "혼자" else GOLD
    label_color = WHITE if who == "혼자" else NAVY

    circle = s.shapes.add_shape(
        MSO_SHAPE.OVAL, Inches(0.6), Inches(y + 0.1), Inches(0.75), Inches(0.75)
    )
    circle.fill.solid()
    circle.fill.fore_color.rgb = color
    circle.line.fill.background()
    add_text(s, num, 0.6, y + 0.22, 0.75, 0.55,
             size=22, bold=True, color=label_color, align=PP_ALIGN.CENTER)

    box = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(1.5), Inches(y), Inches(9.5), Inches(0.95)
    )
    box.fill.solid()
    box.fill.fore_color.rgb = WHITE
    box.line.color.rgb = color
    box.line.width = Pt(1.2)
    box.adjustments[0] = 0.2
    add_text(s, title, 1.7, y + 0.1, 9.1, 0.4,
             size=15, bold=True, color=NAVY)
    add_text(s, desc, 1.7, y + 0.45, 9.1, 0.4,
             size=12, color=GRAY_MID)

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

    y += 0.82

add_footer(s, 20)


# ══════════════════════════════════════════════════════════════
# Slide 21 — 첫 대화 예시
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "첫 대화 예시", "슬래시 명령어 몰라도 됩니다")

add_text(s, "Claude Desktop 대화창에 이렇게 적으시면 됩니다",
         0.6, 1.55, 12, 0.5, size=17, bold=True, color=NAVY)

# 입력창 모방 박스
chat_box = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.6), Inches(2.15), Inches(12.1), Inches(2.9)
)
chat_box.fill.solid()
chat_box.fill.fore_color.rgb = GRAY_PALE
chat_box.line.color.rgb = NAVY
chat_box.line.width = Pt(1.5)
chat_box.adjustments[0] = 0.05

add_text(s, "  📝  대화창 입력",
         0.75, 2.25, 11.8, 0.35, size=11, color=GRAY_MID)

example = (
    "peel 스킬로 아래 민원을 분석해 주세요.\n\n"
    "경주 성건동 근린공원에서 3개월째 야간에 청소년 집단\n"
    "음주·소란 민원이 반복되고 있습니다. 14건 누적.\n"
    "순찰 가면 흩어지고, 돌아오면 다시 모입니다.\n"
    "한쪽 주민은 단속 강화를 요구하고, 다른 쪽은 낙인을\n"
    "반대합니다. 우리 지구대에서 어떻게 접근할까요?"
)
add_text(s, example, 0.9, 2.65, 11.8, 2.3,
         size=14, color=GRAY_DARK, line_spacing=1.45)

# 기대 결과
add_text(s, "그러면 /peel 이 이런 초안을 만들어 드립니다",
         0.6, 5.2, 12, 0.4, size=15, bold=True, color=NAVY)

bullets = [
    "선정 공구: SARA · Crime Triangle · Hot Spots · CPTED · COP · Procedural Justice · Broken Windows(비판)",
    "제외 공구: PEACE·Cognitive (조사 단계 아님) / BCSM·ICAT (위기 아님) / ILP (단일 지점)",
    "단계별 체크리스트와 \"경찰이 바로 할 수 있는 행동\" 제시",
]
add_bullets(s, bullets, 0.85, 5.6, 12.1, 1.5, size=12)

add_footer(s, 21)


# ══════════════════════════════════════════════════════════════
# Slide 22 — 부탁과 연락처
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, NAVY_DEEP)

top_line = s.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, 0, Inches(0.8), prs.slide_width, Inches(0.08)
)
top_line.fill.solid()
top_line.fill.fore_color.rgb = GOLD
top_line.line.fill.background()

add_text(s, "부탁드리는 한 가지",
         0.8, 1.1, 12, 0.6, size=20, color=GOLD)
add_text(s, "써 보시고 고쳐주십시오.",
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

add_text(s, "만든 사람", 1.1, 5.2, 5, 0.4, size=13, color=GOLD)
add_text(s, "최희철", 1.1, 5.5, 5, 0.6, size=26, bold=True, color=WHITE)
add_text(s,
         "경주경찰서 경찰발전협의회 회원",
         1.1, 6.1, 5.5, 0.4, size=13, color=GRAY_LIGHT)
add_text(s,
         "평소 AI 도구를 만드는 개발자",
         1.1, 6.4, 5.5, 0.4, size=13, color=GRAY_LIGHT)

add_text(s, "다운로드 · 피드백", 7.5, 5.2, 5, 0.4,
         size=13, color=GOLD)
add_text(s, "github.com/ironyjk/", 7.5, 5.55, 5, 0.4,
         size=16, bold=True, color=WHITE)
add_text(s, "police-frameworks", 7.5, 5.85, 5, 0.4,
         size=16, bold=True, color=WHITE)
add_text(s, "GitHub Issues 또는 직접 연락 주십시오.", 7.5, 6.2, 5.5, 0.4,
         size=12, color=GRAY_LIGHT)

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
