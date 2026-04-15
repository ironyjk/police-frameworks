"""
Police Frameworks — 소개 슬라이드 생성기

사용법:
    python scripts/make_intro_ppt.py

결과물:
    docs/intro.pptx (14장, 16:9, 한글)

작성자: 최희철 (경주경찰서 경찰발전협의회 회원)
"""

from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE


# ──────────────────────────────────────────────────────────────
# 색상 및 설정
# ──────────────────────────────────────────────────────────────

NAVY = RGBColor(0x1A, 0x36, 0x5D)
NAVY_LIGHT = RGBColor(0x2C, 0x51, 0x82)
RED = RGBColor(0xC5, 0x30, 0x30)
GOLD = RGBColor(0xD6, 0x9E, 0x2E)
GRAY_DARK = RGBColor(0x2D, 0x37, 0x48)
GRAY_MID = RGBColor(0x4A, 0x55, 0x68)
GRAY_LIGHT = RGBColor(0xE2, 0xE8, 0xF0)
BG = RGBColor(0xF7, 0xFA, 0xFC)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

FONT = "맑은 고딕"


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
    bg.shadow.inherit = False
    # 배경으로 보내기
    spTree = bg._element.getparent()
    spTree.remove(bg._element)
    spTree.insert(2, bg._element)
    return bg


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
        p2.font.size = Pt(13)
        p2.font.color.rgb = GRAY_LIGHT


def add_text(slide, text, left, top, width, height,
             size=16, bold=False, color=GRAY_DARK, align=PP_ALIGN.LEFT):
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
                size=16, color=GRAY_DARK, line_spacing=1.3):
    tb = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    for i, b in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• " + b if not b.startswith("  ") else b
        p.line_spacing = line_spacing
        p.space_after = Pt(4)
        for run in p.runs:
            run.font.name = FONT
            run.font.size = Pt(size)
            run.font.color.rgb = color
    return tb


def add_box(slide, title, body, left, top, width, height,
            title_color=NAVY, border_color=NAVY):
    box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    box.fill.solid()
    box.fill.fore_color.rgb = WHITE
    box.line.color.rgb = border_color
    box.line.width = Pt(1.2)
    box.adjustments[0] = 0.08

    tb = slide.shapes.add_textbox(
        Inches(left + 0.2), Inches(top + 0.12),
        Inches(width - 0.4), Inches(height - 0.24)
    )
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.text = title
    p.font.name = FONT
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = title_color

    for line in body.split("\n"):
        p = tf.add_paragraph()
        p.text = line
        p.font.name = FONT
        p.font.size = Pt(11)
        p.font.color.rgb = GRAY_MID
        p.line_spacing = 1.25


def add_footer(slide):
    tb = slide.shapes.add_textbox(
        Inches(0.5), Inches(7.1), Inches(12.3), Inches(0.35)
    )
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = "Police Frameworks · /peel · 최희철 (경주경찰서 경찰발전협의회 회원)"
    p.alignment = PP_ALIGN.RIGHT
    p.font.name = FONT
    p.font.size = Pt(9)
    p.font.color.rgb = GRAY_MID


# ──────────────────────────────────────────────────────────────
# 프레젠테이션 생성
# ──────────────────────────────────────────────────────────────

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]


# ══════════════════════════════════════════════════════════════
# Slide 1 — 표지
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, NAVY)

# 장식 줄
line = s.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(2.7), Inches(1.8), Inches(0.08)
)
line.fill.solid()
line.fill.fore_color.rgb = GOLD
line.line.fill.background()

add_text(s, "POLICE FRAMEWORKS",
         0.8, 1.9, 12, 0.8, size=16, bold=True, color=GOLD)
add_text(s, "경찰 프레임워크 툴킷",
         0.8, 2.85, 12, 1.2, size=54, bold=True, color=WHITE)
add_text(s,
         "Claude Code를 위한 12개 근거기반 경찰활동 프레임워크\n"
         "메타 라우터 /peel — 상황 입력 → 최적 프레임워크 선택·시퀀싱",
         0.8, 4.4, 12, 1.2, size=18, color=GRAY_LIGHT)
add_text(s,
         "경찰 실무자에게 드리는 참고 자료 · 경주경찰서 경찰발전협의회 회원이 AI 전문가로서 작성",
         0.8, 5.25, 12, 0.4, size=13, color=GOLD)

# 하단 작성자 정보
add_text(s, "작성 · 최희철 (AI 전문가)",
         0.8, 6.15, 12, 0.4, size=16, bold=True, color=WHITE)
add_text(s, "경주경찰서 경찰발전협의회 회원  ·  2026년 4월",
         0.8, 6.5, 12, 0.4, size=13, color=GRAY_LIGHT)


# ══════════════════════════════════════════════════════════════
# Slide 2 — 왜 만들었는가
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "왜 만들었는가", "문제의식과 목적")

add_text(s, "❶  문제의식",
         0.6, 1.6, 12, 0.4, size=18, bold=True, color=NAVY)
add_bullets(s, [
    "한국 경찰 현장에는 뛰어난 실무 지식이 있지만, 이를 체계화한 분석 도구가 개인 머릿속에만 존재",
    "영미권에서 40년 이상 축적된 근거기반 경찰활동 프레임워크는 한국어 자료가 적고 산재",
    "일선 대응의 기본값이 \"순찰 강화\"와 \"단속\"에 머물러 제3의 대안 제시가 제한적",
    "\"무관용\" 요구가 절차적 정의·지역사회 신뢰를 훼손해도 걸러낼 이론적 장치 부재",
], 0.9, 2.1, 12, 2.0, size=14)

add_text(s, "❷  이 도구의 위치 (작성자의 역할)",
         0.6, 4.15, 12, 0.4, size=18, bold=True, color=NAVY)
add_bullets(s, [
    "작성자는 **AI 전문가**입니다. 경찰 실무자가 아닙니다.",
    "경주경찰서 경찰발전협의회 회원이지만, 경발협은 봉사단체이며 범죄 분석·수사는 경찰의 몫",
    "이 도구는 **경찰 실무자에게 드리는 참고 자료** — 경발협이 직접 쓰는 도구가 아님",
    "12개 프레임워크를 한국 경찰 맥락으로 \"재작성\"해, 지구대·경찰서가 참고할 수 있게 정리",
    "모든 적용은 경찰이 소속 기관 지침·법령·현장 판단과 결합해 검증해야 함",
], 0.9, 4.65, 12, 2.3, size=13)

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 3 — /peel 이란
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "/peel 이란 무엇인가", "메타 라우터의 개념")

add_text(s,
         "상황을 설명하면, 12개 프레임워크 중 어떤 것을 어떤 순서로 적용할지\n"
         "자동으로 선택·시퀀싱해 주는 지능형 라우팅 계층",
         0.6, 1.55, 12.2, 1.0, size=17, bold=True, color=NAVY)

# 파이프라인 다이어그램
stages = [
    ("상황 입력", "반복 민원, 현장 위기,\n조사 면담, 지역 불신…"),
    ("문제 분류", "반복/단일, 사람/환경,\n사전/현장/사후"),
    ("프레임워크 선정", "12개 중 2~4개 조합\n+ 제외 프레임워크 이유"),
    ("파이프라인", "적용 순서 + 단계별\n체크리스트 제공"),
]
x = 0.6
for i, (t, b) in enumerate(stages):
    add_box(s, t, b, x, 3.1, 2.85, 1.55)
    x += 3.0
    if i < 3:
        arrow = s.shapes.add_shape(
            MSO_SHAPE.RIGHT_ARROW,
            Inches(x - 0.18), Inches(3.7), Inches(0.25), Inches(0.35)
        )
        arrow.fill.solid()
        arrow.fill.fore_color.rgb = NAVY
        arrow.line.fill.background()

add_text(s, "❖  같은 계열 도구",
         0.6, 5.1, 12, 0.4, size=14, bold=True, color=NAVY)
add_bullets(s, [
    "/think   — 경영 전략 프레임워크 메타 라우터 (47개, Porter/Drucker/BSC 등)",
    "/counsel — 심리 상담 프레임워크 메타 라우터 (14개, CBT/ACT/IFS 등)",
    "/peel    — 경찰활동 프레임워크 메타 라우터 (12개, 본 프로젝트)",
], 0.9, 5.55, 12, 1.4, size=13)

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 4 — 왜 /peel 인가 (Robert Peel)
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "왜 /peel 인가", "현대 경찰의 창시자, Sir Robert Peel (1788–1850)")

add_text(s,
         "1829년 런던경찰청 창설, 현대 경찰의 아버지",
         0.6, 1.55, 12, 0.4, size=16, bold=True, color=NAVY)
add_text(s,
         "그의 9대 원칙(Peelian Principles)은 200년이 지난 지금도\n"
         "절차적 정의·지역사회 경찰활동·정당성 이론의 뿌리입니다.",
         0.6, 2.0, 12, 0.8, size=13, color=GRAY_MID)

# 핵심 3원칙 박스
add_box(s, "제1원칙 — 예방",
        "경찰의 기본 임무는 범죄와\n무질서의 예방이다.\n무력 진압이 아니다.",
        0.6, 3.15, 4.0, 1.7, title_color=RED)
add_box(s, "제7원칙 — 경찰=시민",
        "\"경찰은 시민이고\n시민은 경찰이다.\"\n경찰은 시민의 대리인일 뿐.",
        4.77, 3.15, 4.0, 1.7, title_color=RED)
add_box(s, "제9원칙 — 측정",
        "효율성의 척도는 범죄의 부재이지\n가시적 경찰 활동이 아니다.\n조용한 동네 = 성공한 경찰.",
        8.93, 3.15, 4.0, 1.7, title_color=RED)

add_text(s, "❖  /peel 이라는 이름의 이유",
         0.6, 5.15, 12, 0.4, size=14, bold=True, color=NAVY)
add_bullets(s, [
    "경찰관이 /police 를 입력해 자기 자신을 호출하는 어색함을 피합니다",
    "이 툴킷 전체의 철학적 뿌리를 계승 — PEACE, ICAT, COP, 절차적 정의 모두 Peel 제7원칙으로 수렴",
    "짧고, 역사적 무게가 있고, 자기지시어가 아니고, 기억하기 쉬움",
], 0.9, 5.6, 12, 1.5, size=13)

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 5 — 4개 축 × 12개 프레임워크 (개관)
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "4개 축 × 12개 프레임워크", "Police Frameworks 전체 지도")

axes = [
    ("축 1  ·  문제지향 경찰활동",
     "반복 문제의 근본 해결 · 예방 설계",
     ["SARA", "Crime Triangle", "CPTED", "Hot Spots", "ILP"],
     NAVY),
    ("축 2  ·  조사 · 면담",
     "비강압적 정보 수집 · 기억 인출",
     ["PEACE Model", "Cognitive Interview"],
     NAVY_LIGHT),
    ("축 3  ·  현장 대응 · 위기",
     "디에스컬레이션 · 위기 협상",
     ["BCSM", "ICAT"],
     RED),
    ("축 4  ·  정당성 · 지역사회",
     "신뢰 · 협력 · 무질서 함정 회피",
     ["Procedural Justice", "COP", "Broken Windows (비판적)"],
     GOLD),
]

y = 1.55
for axis_name, axis_desc, fws, color in axes:
    # 축 제목 박스
    bar = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(y), Inches(4.4), Inches(1.25)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = color
    bar.line.fill.background()
    add_text(s, axis_name, 0.75, y + 0.18, 4.2, 0.4,
             size=15, bold=True, color=WHITE)
    add_text(s, axis_desc, 0.75, y + 0.68, 4.2, 0.4,
             size=11, color=GRAY_LIGHT)
    # 프레임워크 chips
    cx = 5.25
    for fw in fws:
        chip = s.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(cx), Inches(y + 0.28), Inches(2.35), Inches(0.7)
        )
        chip.fill.solid()
        chip.fill.fore_color.rgb = WHITE
        chip.line.color.rgb = color
        chip.line.width = Pt(1.5)
        chip.adjustments[0] = 0.3
        add_text(s, fw, cx + 0.1, y + 0.42, 2.15, 0.4,
                 size=12, bold=True, color=color, align=PP_ALIGN.CENTER)
        cx += 2.5
    y += 1.42

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 6 — 축 1 문제지향
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "축 1 · 문제지향 경찰활동", "Problem-Oriented Policing — 반복 문제의 근본 해결")

fws = [
    ("SARA",
     "Goldstein 1979 · Eck & Spelman 1987",
     "Scanning → Analysis → Response → Assessment.\n"
     "4단계 반복 사이클로 반복 민원·문제를\n근본적으로 해결."),
    ("Crime Triangle",
     "Cohen & Felson · Clarke & Eck",
     "가해자·대상·장소 3요소 + 각 억제자.\n"
     "6박스 분해로 \"어디를 움직이면\n가장 효과적인가\" 파악."),
    ("CPTED",
     "Jeffery 1971 · Newman · Crowe",
     "자연감시·접근통제·영역성·활동지원·\n유지관리·표적경화 6원칙.\n환경설계로 범죄 기회 제거."),
    ("Hot Spots",
     "Sherman · Weisburd",
     "범죄의 장소 집중 법칙(상위 5%에 50%).\n"
     "Koper 15분 규칙.\n28개 RCT 메타분석 효과 입증."),
    ("ILP",
     "Ratcliffe · UK NIM",
     "Intelligence-Led Policing.\n"
     "3i 모델(Interpret-Influence-Impact).\n상습자·반복피해자·핫스팟 집중."),
]

positions = [
    (0.6, 1.6, 4.0, 2.6),
    (4.77, 1.6, 4.0, 2.6),
    (8.93, 1.6, 4.0, 2.6),
    (0.6, 4.35, 4.0, 2.6),
    (4.77, 4.35, 4.0, 2.6),
]

for (name, author, body), (x, y, w, h) in zip(fws, positions):
    box = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)
    )
    box.fill.solid()
    box.fill.fore_color.rgb = WHITE
    box.line.color.rgb = NAVY
    box.line.width = Pt(1.2)
    box.adjustments[0] = 0.06

    tb = s.shapes.add_textbox(
        Inches(x + 0.25), Inches(y + 0.2), Inches(w - 0.5), Inches(h - 0.4)
    )
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = name
    p.font.name = FONT
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = NAVY

    p = tf.add_paragraph()
    p.text = author
    p.font.name = FONT
    p.font.size = Pt(10)
    p.font.italic = True
    p.font.color.rgb = GRAY_MID
    p.space_after = Pt(8)

    for line in body.split("\n"):
        p = tf.add_paragraph()
        p.text = line
        p.font.name = FONT
        p.font.size = Pt(12)
        p.font.color.rgb = GRAY_DARK
        p.line_spacing = 1.25

# 하이라이트 박스
add_box(s, "축 1의 핵심 메시지",
        "\"순찰 강화\"는 많은 경우 비용 대비 효과가\n낮습니다. 분석 → 환경 개입 → 제3자 협조가\n지속가능한 해결의 길입니다.",
        8.93, 4.35, 4.0, 2.6, title_color=RED, border_color=RED)

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 7 — 축 2 조사/면담
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "축 2 · 조사 · 면담", "Investigative Interviewing — 강압이 아닌 정보 수집")

# PEACE 박스
box = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.55),
    Inches(6.05), Inches(5.4)
)
box.fill.solid()
box.fill.fore_color.rgb = WHITE
box.line.color.rgb = NAVY
box.line.width = Pt(1.5)
box.adjustments[0] = 0.04

add_text(s, "PEACE Model", 0.85, 1.75, 5.5, 0.5,
         size=24, bold=True, color=NAVY)
add_text(s, "UK Home Office, 1992 · 허위자백 스캔들에 대한 응답",
         0.85, 2.25, 5.5, 0.4, size=11, color=GRAY_MID)

peace = [
    ("P  Planning & Preparation", "면담 성공의 70%는 준비 단계에서 결정"),
    ("E  Engage & Explain", "Rapport 구축, 목적·권리 설명"),
    ("A  Account / Clarify / Challenge", "Free recall → 질문 → 전략적 증거 제시"),
    ("C  Closure", "질서 있는 종결, 요약, 다음 단계 안내"),
    ("E  Evaluation", "면담 후 학습 — 가장 자주 생략되는 단계"),
]
y = 2.75
for title, desc in peace:
    add_text(s, title, 0.85, y, 5.5, 0.35, size=14, bold=True, color=NAVY_LIGHT)
    add_text(s, desc, 0.85, y + 0.32, 5.5, 0.35, size=11, color=GRAY_MID)
    y += 0.75

add_text(s, "※  Reid 기법 같은 압박·유도 자백 유도는 이 툴킷에서 의도적으로 배제",
         0.85, 6.55, 5.5, 0.35, size=10, bold=True, color=RED)

# Cognitive Interview 박스
box2 = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.85), Inches(1.55),
    Inches(6.05), Inches(5.4)
)
box2.fill.solid()
box2.fill.fore_color.rgb = WHITE
box2.line.color.rgb = NAVY
box2.line.width = Pt(1.5)
box2.adjustments[0] = 0.04

add_text(s, "Cognitive Interview", 7.1, 1.75, 5.5, 0.5,
         size=24, bold=True, color=NAVY)
add_text(s, "Fisher & Geiselman, 1984 · 피해자·목격자 기억 인출 최대화",
         7.1, 2.25, 5.5, 0.4, size=11, color=GRAY_MID)

ci = [
    ("맥락 복원", "사건 당시의 물리·감정 환경을 마음속에서 재현"),
    ("모든 세부 보고", "사소하거나 확신 없는 정보도 검열 없이 보고"),
    ("역순 회상", "끝에서부터 거꾸로 — 스크립트 우회, 일관성 검증"),
    ("관점 전환", "다른 사람 시점에서 재구성 (아동에는 신중히)"),
]
y = 2.75
for title, desc in ci:
    add_text(s, title, 7.1, y, 5.5, 0.35, size=14, bold=True, color=NAVY_LIGHT)
    add_text(s, desc, 7.1, y + 0.32, 5.5, 0.35, size=11, color=GRAY_MID)
    y += 0.8

add_text(s, "메타분석: 일반 면담 대비 25~85% 더 많은 정확한 정보",
         7.1, 6.55, 5.5, 0.35, size=10, bold=True, color=RED)

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 8 — 축 3 현장대응/위기
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "축 3 · 현장 대응 · 위기", "디에스컬레이션과 위기 협상")

# BCSM 박스
box = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.55),
    Inches(6.05), Inches(5.4)
)
box.fill.solid()
box.fill.fore_color.rgb = WHITE
box.line.color.rgb = NAVY
box.line.width = Pt(1.5)
box.adjustments[0] = 0.04

add_text(s, "BCSM", 0.85, 1.75, 5.5, 0.5, size=24, bold=True, color=NAVY)
add_text(s, "FBI Crisis Negotiation Unit · Behavioral Change Stairway Model",
         0.85, 2.25, 5.5, 0.4, size=11, color=GRAY_MID)
add_text(s,
         "자살·인질·농성 등 위기 협상 5단계 계단 모델.\n"
         "핵심: 계단을 건너뛰면 마지막에 도달할 수 없다.",
         0.85, 2.6, 5.5, 0.8, size=12, color=GRAY_DARK)

stairway = [
    ("5", "Behavioral Change", "행동 변화"),
    ("4", "Influence", "영향 — 제안이 받아들여짐"),
    ("3", "Rapport", "신뢰 구축"),
    ("2", "Empathy", "공감 — 이해받았다는 느낌"),
    ("1", "Active Listening", "능동적 경청"),
]
y = 3.6
for num, en, kr in stairway:
    step = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.85), Inches(y), Inches(5.55), Inches(0.55)
    )
    step.fill.solid()
    step.fill.fore_color.rgb = NAVY_LIGHT if int(num) % 2 == 0 else NAVY
    step.line.fill.background()
    add_text(s, f"{num}  {en}  ·  {kr}", 1.0, y + 0.13, 5.3, 0.4,
             size=12, bold=True, color=WHITE)
    y += 0.62

# ICAT 박스
box2 = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.85), Inches(1.55),
    Inches(6.05), Inches(5.4)
)
box2.fill.solid()
box2.fill.fore_color.rgb = WHITE
box2.line.color.rgb = NAVY
box2.line.width = Pt(1.5)
box2.adjustments[0] = 0.04

add_text(s, "ICAT", 7.1, 1.75, 5.5, 0.5, size=24, bold=True, color=NAVY)
add_text(s, "PERF, 2016 · 단계적 대응 · 디에스컬레이션 훈련",
         7.1, 2.25, 5.5, 0.4, size=11, color=GRAY_MID)
add_text(s,
         "Integrating Communications, Assessment, and Tactics.\n"
         "정신질환·비무기 저항에 물리력 회피 훈련.",
         7.1, 2.6, 5.5, 0.8, size=12, color=GRAY_DARK)

add_text(s, "핵심 원칙 · 시간 · 거리 · 엄폐",
         7.1, 3.55, 5.5, 0.4, size=14, bold=True, color=NAVY_LIGHT)
add_bullets(s, [
    "Time — 서두르지 않고 시간 만들기",
    "Distance — 물러서기는 패배가 아닌 전술",
    "Cover — 엄폐로 물리력 사용 압박 감소",
    "CDMM — 정보·위협·권한·목표·옵션·행동 순환",
], 7.2, 3.95, 5.5, 2.0, size=11)

add_text(s, "루이빌 PD 실증: 물리력 28% ↓, 시민 부상 26% ↓, 경찰관 부상 36% ↓",
         7.1, 6.55, 5.5, 0.35, size=10, bold=True, color=RED)

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 9 — 축 4 정당성/지역사회
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "축 4 · 정당성 · 지역사회", "과정이 결과보다 중요하다")

# Procedural Justice — 큰 박스
box = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.55),
    Inches(6.05), Inches(5.4)
)
box.fill.solid()
box.fill.fore_color.rgb = WHITE
box.line.color.rgb = GOLD
box.line.width = Pt(2)
box.adjustments[0] = 0.04

add_text(s, "Procedural Justice", 0.85, 1.75, 5.5, 0.5,
         size=22, bold=True, color=NAVY)
add_text(s, "Tom Tyler · 결과보다 과정의 공정성이 정당성을 결정",
         0.85, 2.25, 5.5, 0.4, size=11, color=GRAY_MID)

pj = [
    ("Voice", "발언권", "시민이 자기 입장을\n충분히 말할 기회"),
    ("Neutrality", "중립성", "사실·규칙 기반\n일관된 판단"),
    ("Respect", "존중", "존엄을 침해하지 않는\n언어와 태도"),
    ("Trust", "신뢰", "선의로 시민 이익을\n고려한다는 인상"),
]
x = 0.85
for en, kr, desc in pj:
    c = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(2.75), Inches(1.4), Inches(1.6)
    )
    c.fill.solid()
    c.fill.fore_color.rgb = NAVY
    c.line.fill.background()
    c.adjustments[0] = 0.15
    add_text(s, en, x + 0.05, 2.85, 1.3, 0.4,
             size=12, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    add_text(s, kr, x + 0.05, 3.15, 1.3, 0.4,
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, desc, x + 0.05, 3.55, 1.3, 0.7,
             size=9, color=GRAY_LIGHT, align=PP_ALIGN.CENTER)
    x += 1.45

add_text(s, "❖ 핵심 통찰", 0.85, 4.55, 5.5, 0.4, size=12, bold=True, color=RED)
add_text(s,
         "사람들은 법정에서 져도 과정이 공정했다고 느끼면\n"
         "결과를 수용합니다. 반대로 이겨도 과정이 불공정하면\n"
         "법 체계를 신뢰하지 못합니다. \"규정대로 했다\"는\n"
         "방어는 정당성 언어와 무관합니다.",
         0.85, 4.9, 5.8, 1.8, size=11, color=GRAY_DARK)

# COP + Broken Windows
add_box(s, "COP  ·  지역사회 경찰활동",
        "Peel 제7원칙으로 회귀.\n파트너십 · 조직변화 · 문제해결 3축.\n"
        "한국의 자율방범대·경찰발전협의회가\n이 철학의 부분 구현.",
        6.85, 1.55, 6.05, 2.6)

add_box(s, "Broken Windows  ·  비판적 재해석",
        "Wilson & Kelling 1982의 원이론은 오해되어\n"
        "Zero Tolerance로 변질.\n"
        "이 툴킷은 \"무관용 단속\"이 아니라\n"
        "CPTED + 복지 연계로 재해석.\n"
        "주민 측 \"엄격 단속\" 요구에\n"
        "경찰이 즉답하지 않도록 경고 필터 역할.",
        6.85, 4.35, 6.05, 2.6,
        title_color=RED, border_color=RED)

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 10 — 샘플: 시나리오 (입력)
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "샘플 테스트 · 시나리오 입력",
              "성건파출소가 /peel 에 반복 민원을 입력하면")

# 큰 입력 박스
box = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.6),
    Inches(12.3), Inches(4.0)
)
box.fill.solid()
box.fill.fore_color.rgb = WHITE
box.line.color.rgb = NAVY
box.line.width = Pt(1.5)
box.adjustments[0] = 0.03

add_text(s, "▸ 입력 (성건파출소 접수 반복 민원 · 3개월 누적 14건)",
         0.85, 1.75, 12, 0.4, size=14, bold=True, color=NAVY)

scenario = (
    "경주시 성건동 ○○근린공원에서 지난 3개월간 야간 시간대(22~02시)에\n"
    "청소년 집단(15~18세 추정, 5~10명) 음주·흡연·소란 민원이 반복 접수되고 있다.\n"
    "주민 민원 총 14건. 순찰차가 접근하면 흩어지고, 떠나면 복귀하는 패턴.\n"
    "주변 편의점에서 청소년 주류 판매 의심 정황도 있음.\n\n"
    "일부 주민은 \"무관용 단속\"을 강하게 요구하고 있고,\n"
    "다른 주민은 \"우리 애들인데 범죄자 취급하지 말라\"는 입장.\n"
    "성건파출소 인력으로는 야간 상시 배치 불가능."
)
add_text(s, scenario, 0.85, 2.2, 12, 3.4, size=13, color=GRAY_DARK)

# 분류 결과
add_text(s, "▸ 라우터의 1차 분류",
         0.6, 5.85, 12, 0.4, size=14, bold=True, color=NAVY)

chips = [
    ("반복 패턴 · 3개월", NAVY),
    ("장소 집중", NAVY),
    ("청소년 요소", NAVY_LIGHT),
    ("주민 의견 분열", NAVY_LIGHT),
    ("\"무관용\" 요구 → BW 필터 필수", RED),
]
x = 0.6
for text, color in chips:
    w = 2.45 if "필터" not in text else 3.3
    chip = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(6.3), Inches(w), Inches(0.55)
    )
    chip.fill.solid()
    chip.fill.fore_color.rgb = color
    chip.line.fill.background()
    chip.adjustments[0] = 0.3
    add_text(s, text, x + 0.1, 6.43, w - 0.2, 0.4,
             size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    x += w + 0.1

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 11 — 샘플: 라우터 출력 (프레임워크 선정)
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "샘플 테스트 · 프레임워크 선정",
              "12개 중 7개 선정 · 5개 제외")

# 선정 (왼쪽)
add_text(s, "✓ 선정된 프레임워크",
         0.6, 1.55, 6, 0.4, size=16, bold=True, color=NAVY)

selected = [
    ("SARA", "전체 진단·개입 사이클"),
    ("Crime Triangle", "원인 6박스 분해"),
    ("Hot Spots", "공간·시간 집중 확인"),
    ("CPTED", "환경 개입 (조명·조경)"),
    ("COP", "학교·구청·편의점 협력"),
    ("Procedural Justice", "청소년·주민 대응 원칙"),
    ("Broken Windows", "\"무관용\" 요구 필터 (비판)"),
]
y = 2.05
for name, why in selected:
    mark = s.shapes.add_shape(
        MSO_SHAPE.OVAL, Inches(0.65), Inches(y + 0.1),
        Inches(0.3), Inches(0.3)
    )
    mark.fill.solid()
    mark.fill.fore_color.rgb = NAVY
    mark.line.fill.background()
    add_text(s, "✓", 0.65, y + 0.05, 0.3, 0.3,
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, name, 1.1, y + 0.05, 3.5, 0.4, size=14, bold=True, color=NAVY)
    add_text(s, why, 4.2, y + 0.08, 2.7, 0.4, size=11, color=GRAY_MID)
    y += 0.6

# 제외 (오른쪽)
add_text(s, "✕ 제외된 프레임워크",
         7.0, 1.55, 6, 0.4, size=16, bold=True, color=GRAY_MID)

excluded = [
    ("PEACE Model", "조사 면담 단계 아님"),
    ("Cognitive Interview", "피해자 면담 단계 아님"),
    ("BCSM", "위기 협상 상황 아님"),
    ("ICAT", "현장 물리력 판단 상황 아님"),
    ("ILP", "전략 수준 프로파일링 과대 적용"),
]
y = 2.05
for name, why in excluded:
    mark = s.shapes.add_shape(
        MSO_SHAPE.OVAL, Inches(7.05), Inches(y + 0.1),
        Inches(0.3), Inches(0.3)
    )
    mark.fill.solid()
    mark.fill.fore_color.rgb = GRAY_MID
    mark.line.fill.background()
    add_text(s, "×", 7.05, y + 0.0, 0.3, 0.3,
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, name, 7.5, y + 0.05, 3.5, 0.4, size=14, bold=True, color=GRAY_MID)
    add_text(s, why, 10.6, y + 0.08, 2.7, 0.4, size=11, color=GRAY_MID)
    y += 0.6

# 강조 메시지
msg = s.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.6), Inches(6.2), Inches(12.3), Inches(0.75)
)
msg.fill.solid()
msg.fill.fore_color.rgb = RED
msg.line.fill.background()
msg.adjustments[0] = 0.3
add_text(s,
         "▶  \"제외된 프레임워크\"를 명시적으로 보여주는 것이 핵심 — "
         "왜 안 쓰는지 설명할 수 있어야 토의가 진전됩니다.",
         0.85, 6.37, 12, 0.4,
         size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 12 — 샘플: 실행 파이프라인
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "샘플 테스트 · 실행 파이프라인",
              "선정된 프레임워크의 적용 순서")

phases = [
    ("Phase 1", "문제 정의",
     "SARA-Scanning + Hot Spots",
     "14건 데이터·지도화\n목·금·토 22–02시 북측 놀이터 집중 확인"),
    ("Phase 2", "원인 분석",
     "Crime Triangle · CPTED 현장점검",
     "6박스 분해 → Handler·Place·Manager가 개입지점\nCPTED 6원칙 체크리스트"),
    ("Phase 3a", "필터링",
     "Broken Windows 비판적 검토",
     "\"무관용 단속\" 요구의 함정 설명\n차별·이동·신뢰훼손 경고"),
    ("Phase 3b", "개입 설계",
     "CPTED + COP + Procedural Justice",
     "조명·조경 / 학교·센터·편의점·공원녹지과 협력 /\n청소년·주민 대응 4요소 삽입"),
    ("Phase 4", "평가",
     "SARA-Assessment",
     "3개월 후 민원·이동·체감 측정\n결과에 따라 사이클 재시작"),
]

y = 1.55
for phase, name, frameworks, desc in phases:
    # Phase 라벨
    label = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.6), Inches(y), Inches(1.5), Inches(0.95)
    )
    label.fill.solid()
    label.fill.fore_color.rgb = NAVY
    label.line.fill.background()
    label.adjustments[0] = 0.2
    add_text(s, phase, 0.6, y + 0.12, 1.5, 0.4,
             size=12, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    add_text(s, name, 0.6, y + 0.42, 1.5, 0.4,
             size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    # 내용 박스
    content = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(2.25), Inches(y), Inches(10.65), Inches(0.95)
    )
    content.fill.solid()
    content.fill.fore_color.rgb = WHITE
    content.line.color.rgb = NAVY
    content.line.width = Pt(1)
    content.adjustments[0] = 0.15

    add_text(s, frameworks, 2.45, y + 0.08, 10.3, 0.4,
             size=12, bold=True, color=NAVY)
    add_text(s, desc, 2.45, y + 0.38, 10.3, 0.55,
             size=10, color=GRAY_MID)

    y += 1.08

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 13 — 경찰발전협의회 활용 가이드
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "경찰 실무 활용 가이드",
              "지구대·경찰서 각 부서별 권장 프레임워크 조합")

# 활용 표
rows = [
    ("지구대 · 반복 민원 분석", "SARA + Crime Triangle + CPTED", "근본 원인과 환경 개입"),
    ("생활안전계 · 관할 치안 전략", "Hot Spots + ILP + SARA", "데이터 기반 우선순위"),
    ("범죄예방진단팀 · 환경 점검", "CPTED + Crime Triangle", "물리 환경 개선"),
    ("감찰 · 민원 사후 검토", "Procedural Justice + COP", "신뢰 회복 진단"),
    ("여성청소년과 · 청소년 이슈", "Broken Windows(비판) + COP", "\"단속\" 함정 회피"),
    ("수사과 · 조사·면담", "PEACE + Cognitive Interview", "비강압 진술 확보"),
    ("위기협상요원 · 정신건강 위기", "ICAT + BCSM", "물리력 최소화"),
]

# 헤더
header = s.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(1.55),
    Inches(12.3), Inches(0.5)
)
header.fill.solid()
header.fill.fore_color.rgb = NAVY
header.line.fill.background()
add_text(s, "부서 · 상황", 0.8, 1.65, 4.5, 0.3,
         size=12, bold=True, color=WHITE)
add_text(s, "권장 프레임워크", 5.5, 1.65, 4.5, 0.3,
         size=12, bold=True, color=WHITE)
add_text(s, "핵심 효과", 10.2, 1.65, 3.0, 0.3,
         size=12, bold=True, color=WHITE)

y = 2.1
for i, (topic, fws, effect) in enumerate(rows):
    row = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(y),
        Inches(12.3), Inches(0.45)
    )
    row.fill.solid()
    row.fill.fore_color.rgb = WHITE if i % 2 == 0 else GRAY_LIGHT
    row.line.fill.background()
    add_text(s, topic, 0.8, y + 0.08, 4.7, 0.3, size=11, bold=True, color=NAVY)
    add_text(s, fws, 5.5, y + 0.08, 4.7, 0.3, size=11, color=GRAY_DARK)
    add_text(s, effect, 10.2, y + 0.08, 3.0, 0.3, size=10, color=GRAY_MID)
    y += 0.45

# 사용 팁
add_text(s, "❖  적용 팁 (경찰 실무자용)",
         0.6, 5.4, 12, 0.4, size=14, bold=True, color=NAVY)
tips = [
    "사건 분석 전 /peel 을 돌려 권장 프레임워크와 제외 프레임워크를 먼저 확인",
    "선정된 프레임워크의 체크리스트를 회의에 띄우고 항목별 논의",
    "\"느낌\" 대신 프레임워크 항목에 대한 답변으로 정리",
    "결론은 \"순찰 강화\"가 아닌 다음 단계(담당·일정·지표) 형태로 기록",
    "KICS 분석이 필요한 질문은 따로 분리해 범죄예방진단팀·생활안전계에 할당",
]
add_bullets(s, tips, 0.9, 5.85, 12, 1.8, size=12)

add_footer(s)


# ══════════════════════════════════════════════════════════════
# Slide 14 — 설계 원칙 + 다음 단계
# ══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
set_background(s, BG)
add_title_bar(s, "설계 원칙 · 다음 단계",
              "이 도구가 약속하는 것과 약속하지 않는 것")

add_text(s, "✦  설계 원칙", 0.6, 1.55, 12, 0.4,
         size=16, bold=True, color=NAVY)

principles = [
    ("근거 기반만",
     "동료심사 연구 또는 공식 교리(FBI, 영국 College of Policing, PERF, Home Office)만 수록"),
    ("강압 기법 의도적 배제",
     "Reid 기법 등 허위 자백 유발 기법은 포함하지 않음 — PEACE가 윤리적·실증적 대안"),
    ("한국 맥락 재작성",
     "단순 번역이 아닌 한국 경찰(경찰청·경찰서·지구대·파출소·KICS) 실무 맥락 기준"),
    ("효율보다 정당성",
     "절차적 정의 연구는 \"무엇을\" 보다 \"어떻게\"가 정당성을 결정함을 보여줌"),
]
y = 2.05
for title, body in principles:
    mark = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.65), Inches(y + 0.1),
        Inches(0.08), Inches(0.3)
    )
    mark.fill.solid()
    mark.fill.fore_color.rgb = GOLD
    mark.line.fill.background()
    add_text(s, title, 0.9, y, 12, 0.4, size=14, bold=True, color=NAVY)
    add_text(s, body, 0.9, y + 0.32, 12, 0.5, size=11, color=GRAY_MID)
    y += 0.85

add_text(s, "✦  다음 단계",
         0.6, 5.6, 12, 0.4, size=16, bold=True, color=NAVY)
steps = [
    "1.  경주경찰서 경찰 실무자(생활안전계·지구대·범죄예방진단팀) 피드백 수집",
    "2.  경주 지역 공공데이터 핫스팟 브리핑(docs/gyeongju-hotspots.md) 검토",
    "3.  한국 경찰 실제 사례로 각 프레임워크 문서 보강 — 현장 용어·절차 반영",
    "4.  개선 후 GitHub 공개 — 전국 지구대·경찰서·훈련과정이 참고할 수 있도록",
]
add_bullets(s, steps, 0.9, 6.1, 12, 1.4, size=12)

# 연락처 블록
contact = s.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, Inches(0.0), Inches(7.0),
    prs.slide_width, Inches(0.5)
)
contact.fill.solid()
contact.fill.fore_color.rgb = NAVY
contact.line.fill.background()
add_text(s,
         "작성 · 최희철  ·  경주경찰서 경찰발전협의회 회원  ·  github.com/ironyjk/police-frameworks",
         0.6, 7.12, 12.3, 0.3,
         size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)


# ──────────────────────────────────────────────────────────────
# 저장
# ──────────────────────────────────────────────────────────────

here = Path(__file__).resolve().parent
out = here.parent / "docs" / "intro.pptx"
out.parent.mkdir(exist_ok=True)
prs.save(str(out))
print(f"✓ Saved: {out}")
print(f"  Slides: {len(prs.slides)}")
