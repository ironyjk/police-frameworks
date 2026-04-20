"""
우선순위 한국 법령 원문 가져오기 (law.go.kr DRF API 직접 호출).

korean-law-mcp 의 버그 우회: detail API 에 ID= 파라미터 사용 (MST 아님).
"""

import os
import json
import requests
import xml.etree.ElementTree as ET
from pathlib import Path

OC = 'ironyjk'
BASE = 'https://www.law.go.kr/DRF'
OUT = Path(__file__).parent / 'laws'
OUT.mkdir(exist_ok=True)

LAWS = [
    ('경찰관 직무집행법', ['4', '6', '10', '10의2', '10의3', '10의4']),
    ('형사소송법', ['243의2', '244의2', '244의3', '312']),
    ('가정폭력범죄의 처벌 등에 관한 특례법', ['5', '8의2']),
    ('스토킹범죄의 처벌 등에 관한 법률', ['4', '9']),
    ('성폭력범죄의 처벌 등에 관한 특례법', ['30']),
    ('아동학대범죄의 처벌 등에 관한 특례법', ['17']),
    ('학교폭력예방 및 대책에 관한 법률', ['13의2']),
    ('정신건강증진 및 정신질환자 복지서비스 지원에 관한 법률', ['50']),
    ('자살예방 및 생명존중문화 조성을 위한 법률', ['14']),
    ('청소년 보호법', ['28']),
]


def search_law(query):
    """법령 검색 → 법령ID + 이름 반환."""
    r = requests.get(
        f'{BASE}/lawSearch.do',
        params={'OC': OC, 'target': 'law', 'type': 'XML', 'query': query, 'display': '5'},
        timeout=30,
    )
    r.raise_for_status()
    root = ET.fromstring(r.text)
    for law in root.findall('.//law'):
        law_name = (law.findtext('법령명한글') or '').strip()
        law_id = (law.findtext('법령ID') or '').strip()
        if query.replace(' ', '') in law_name.replace(' ', ''):
            return law_id, law_name
    first = root.find('.//law')
    if first is not None:
        return (first.findtext('법령ID') or '').strip(), (first.findtext('법령명한글') or '').strip()
    return None, None


def get_law_detail(law_id):
    """법령 상세 — ID= 파라미터 사용."""
    r = requests.get(
        f'{BASE}/lawService.do',
        params={'OC': OC, 'target': 'law', 'type': 'XML', 'ID': law_id},
        timeout=30,
    )
    r.raise_for_status()
    return r.text


def parse_articles(xml_text):
    """조문 리스트 추출."""
    root = ET.fromstring(xml_text)

    info = {
        '법령ID': root.findtext('.//기본정보/법령ID', ''),
        '법령명': root.findtext('.//기본정보/법령명_한글', ''),
        '시행일자': root.findtext('.//기본정보/시행일자', ''),
        '공포일자': root.findtext('.//기본정보/공포일자', ''),
    }

    articles = []
    for jo in root.findall('.//조문단위'):
        num = (jo.findtext('조문번호') or '').strip()
        gaji = (jo.findtext('조문가지번호') or '').strip()
        full_num = f'{num}의{gaji}' if gaji and gaji != '0' else num
        title = (jo.findtext('조문제목') or '').strip()
        content_parts = []
        for child in jo.iter():
            if child.tag == '조문내용':
                t = (child.text or '').strip()
                if t:
                    content_parts.append(t)
            elif child.tag == '항내용':
                t = (child.text or '').strip()
                if t:
                    content_parts.append(t)
            elif child.tag == '호내용':
                t = (child.text or '').strip()
                if t:
                    content_parts.append(t)
        content = '\n'.join(content_parts)
        articles.append({
            '번호': full_num,
            '제목': title,
            '내용': content,
        })
    return info, articles


def find_target(articles, target):
    """관심 조항 번호 매칭."""
    target_clean = target.replace('제', '').replace('조', '')
    for a in articles:
        if a['번호'] == target_clean:
            return a
    return None


def main():
    print('우선순위 법령 원문 가져오기\n' + '=' * 60)

    for query, targets in LAWS:
        print(f'\n▸ {query}')
        law_id, law_name = search_law(query)
        if not law_id:
            print(f'  ✗ 검색 실패')
            continue
        print(f'  법령ID: {law_id} / 이름: {law_name}')

        try:
            xml_text = get_law_detail(law_id)
        except Exception as e:
            print(f'  ✗ 상세 조회 실패: {e}')
            continue

        info, articles = parse_articles(xml_text)

        # 원본 XML 저장
        fname = query.replace('/', '_').replace(' ', '_')
        (OUT / f'{fname}.xml').write_text(xml_text, encoding='utf-8')

        # JSON 저장
        (OUT / f'{fname}.json').write_text(
            json.dumps({'info': info, 'articles': articles}, ensure_ascii=False, indent=2),
            encoding='utf-8',
        )

        # 관심 조항 요약
        md_lines = [f'# {info["법령명"]}\n']
        md_lines.append(f'- 법령ID: {info["법령ID"]}')
        md_lines.append(f'- 공포: {info["공포일자"]} / 시행: {info["시행일자"]}')
        md_lines.append(f'- 전체 조문 수: {len(articles)}\n\n---\n')

        found = 0
        for t in targets:
            a = find_target(articles, t)
            md_lines.append(f'## 제{t}조')
            if a:
                found += 1
                if a['제목']:
                    md_lines.append(f'**({a["제목"]})**\n')
                md_lines.append(a['내용'][:2500] or '*(내용 없음)*')
                md_lines.append('\n\n---\n')
            else:
                md_lines.append(f'*⚠ 추출 실패 — 전체 조문 목록 확인 필요*\n\n---\n')

        (OUT / f'{fname}_요약.md').write_text('\n'.join(md_lines), encoding='utf-8')
        print(f'  ✓ 조문 {len(articles)}개 / 관심 {found}/{len(targets)} 추출')


if __name__ == '__main__':
    main()
