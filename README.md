# PPT Art Director

자료 조사, 슬라이드별 기획, 디자인, 피드백 반영, 편집 가능한 PowerPoint 제작을 연결하는 에이전트 스킬입니다. 연구·기술 발표, 논문 세미나, 학회 발표에 특히 맞추었으며 다른 발표 목적에도 적용할 수 있습니다.

이 저장소의 제품은 **`SKILL.md`와 그에 딸린 참고 문서·보조 스크립트**입니다. 별도 모델이나 PPT 생성 서비스가 아니며, 스킬을 읽는 에이전트가 자신의 제작 도구로 작업합니다.

## 하는 일

- 실제 온라인 디자인 사례를 살펴보고 제목뿐 아니라 도표·비교표·방법 설명 슬라이드까지 설계합니다.
- 주제와 사용자 브랜드에 맞는 색상을 선택합니다. 독자적으로 작성한 12개 팔레트와 명시적 색상쌍 대비 검사기를 제공합니다.
- 모든 슬라이드의 실제 문구, 데이터, 출처, 화면 구성, 발표자 노트, 움직임을 담은 기획 파일을 먼저 만듭니다.
- 기본 모드에서는 기획안을 보여준 뒤 피드백을 기다립니다. 사용자가 제작을 지시하는 피드백을 주면 반영하여 완성합니다.
- `원샷`, `one-shot`, `바로 완성`을 요청하면 같은 기획·검증 과정을 거치면서 중간 피드백 단계만 생략합니다.
- 텍스트·차트·표·도식을 가능한 범위에서 편집 가능한 개체로 만들고, 최종 파일의 모든 슬라이드를 렌더링해 확인하도록 안내합니다.
- 설명에 필요한 경우 실제 PPTX 애니메이션을 추가합니다. 번들 도우미는 Windows PowerPoint에서 Fade/Appear와 클릭 순서, Fade 전환을 지원합니다.

## 설치

Codex의 현재 로컬 스킬 위치는 사용자 공통용 `$HOME/.agents/skills` 또는 프로젝트용 `.agents/skills`입니다. 이 저장소를 내려받아 **`SKILL.md`가 들어 있는 폴더 전체**를 `ppt-art-director`라는 이름으로 그 아래 두세요. [공식 스킬 문서](https://learn.chatgpt.com/docs/build-skills)

```text
.agents/skills/ppt-art-director/
  SKILL.md
  agents/
  assets/
  references/
  scripts/
```

`tests/`, `README.md`, `.github/`는 저장소 검증과 안내용이며 설치 폴더에 있어도 됩니다. 기존 설치와 중복 등록하지 마세요. 설치한 스킬이 목록에 나타나지 않으면 Codex를 다시 시작하세요. 다른 에이전트에서는 그 제품의 스킬 설치 규칙에 따라 같은 폴더를 등록합니다. 다른 제품에서의 자동 인식은 별도로 확인해야 합니다.

## 사용 예시

기획안부터 검토하기:

```text
$ppt-art-director
첨부 논문으로 연구실 세미나용 한국어 발표 12장을 만들고 싶어.
15분 발표이며 청중은 분야 대학원생이야.
세련되고 절제된 디자인으로, 먼저 각 슬라이드의 내용을 담은 기획안을 보여줘.
```

피드백을 반영하여 제작하기:

```text
S03의 방법을 두 단계로 더 명확히 설명해줘.
S06은 주요 비교표로 바꾸고 전체 12장은 유지해.
이 피드백을 반영해서 최종 PPT를 만들어줘.
```

원샷 제작:

```text
$ppt-art-director
첨부 자료를 바탕으로 10분짜리 기술 발표 PPT 8장을 원샷으로 완성해줘.
디자인과 색상은 주제에 맞게 골라줘. 방법 설명에는 필요한 경우에만
클릭으로 진행되는 애니메이션을 넣고, 불확실한 수치는 만들지 마.
```

## 실행 환경과 한계

| 기능 | 필요한 환경 | 확인해야 할 점 |
|---|---|---|
| 기획·디자인·피드백 | 파일을 읽고 쓰는 에이전트 | 최신 참고 사례를 조사하려면 브라우징 도구 필요 |
| PPTX 제작 | 호스트의 프레젠테이션 도구 또는 문서화된 PPTX 라이브러리 | 이 저장소가 제작 엔진을 번들로 제공하지는 않음 |
| 색상·PPTX 구조 검사 | Python 3.10 이상, 표준 라이브러리 | 전체 접근성·OOXML 스키마·디자인 검증은 아님 |
| 최종 시각 검토 | PPTX 렌더러와 이미지를 확인할 수 있는 도구 | 구조 검사를 통과한 것만으로 검토 완료라고 하지 않음 |
| 번들 네이티브 애니메이션 | Windows, PowerShell, 설치·인증된 Microsoft PowerPoint | 실행 중인 사용자 PowerPoint 세션에는 연결하지 않음 |

호스트가 Presentations 스킬을 제공하면 그 제작·검증 절차를 따릅니다. 그렇지 않으면 [PptxGenJS](https://gitbrent.github.io/PptxGenJS/) 등 사용 가능한 도구를 선택합니다. 특정 비공개 런타임이나 유료 모델 API를 필수로 요구하지 않습니다.

애니메이션 도우미는 Morph, 경로 이동, 문단별·차트 시리즈별 애니메이션을 구현하지 않습니다. Windows PowerPoint가 없는 경우에도 스킬의 기획과 정적 PPT 제작 지침은 사용할 수 있습니다. 저장 후 효과 설정을 재확인하는 것과 실제 슬라이드 쇼를 눈으로 확인하는 것은 별개의 검증입니다. [지원 범위와 실행 예시](references/motion.md)

## 보조 스크립트

저장소 루트에서 실행합니다.

```shell
python scripts/palette_check.py assets/palettes.json
python scripts/pptx_audit.py path/to/deck.pptx --expect-slides 8 --output work/audit.json
python -m unittest discover -s tests -v
```

게시 전 독립 검증의 범위, 발견한 결함, 수정 결과와 미검증 항목은 [VALIDATION.md](VALIDATION.md)에 기록했습니다. 새 세션에서 다시 실행할 [행동 검증 시나리오](tests/scenarios.md)도 포함합니다.

애니메이션 설정 형식과 PowerShell 명령은 [motion.md](references/motion.md)에 있습니다. 먼저 `-DryRun`으로 최종 내보내기 파일의 개체와 계획이 맞는지 검사하세요.

## 참고 자료와 독립 구현

Anthropic의 공개 PPTX 스킬, Google의 Gemini/Slides 공식 설명, MiniMax 및 다른 공개 구현, Pitch·Slidesgo·Canva 디자인 사례, MIT Communication Lab, Microsoft의 PowerPoint 문서를 조사했습니다. 링크·검토한 리비전·참고한 부분·확인하지 못한 부분은 [출처 기록](references/sources.md)과 [디자인 참고 목록](references/reference-library.md)에 명시했습니다.

Anthropic PPTX 스킬의 원문·코드·자산을 복제한 패키지가 아닙니다. Google의 비공개 내부 PPT 생성 스킬을 확보하거나 재현했다고 주장하지 않습니다. 외부 템플릿과 글꼴·이미지는 각 제공자의 이용 조건을 따르며 이 저장소에 포함하지 않습니다. Claude·Gemini와의 통제된 품질 비교 실험은 수행하지 않았습니다.

## 디렉터리

| 경로 | 역할 |
|---|---|
| [SKILL.md](SKILL.md) | 스킬 진입점과 작업 흐름 |
| [기획 템플릿](assets/slide-plan-template.md) | 상세 슬라이드 명세와 피드백 양식 |
| [디자인](references/design.md) | 구성, 타이포그래피, 색상, 도표 설계 |
| [연구 발표](references/research-talks.md) | 논문·실험·수식·연구 그림을 다루는 기준 |
| [제작](references/production.md) | 환경별 도구 선택과 파일 구성 |
| [검증](references/quality.md) | 내용·편집 가능성·시각·움직임 검증 |
| `scripts/` | 색상 대비, PPTX 구조, 네이티브 애니메이션 도우미 |
| `tests/` | 보조 스크립트 회귀 검사 |

## 라이선스

[MIT License](LICENSE). 외부 참고 자료의 권리는 해당 제공자에게 있으며, 이 저장소의 MIT 라이선스가 외부 템플릿·스킬·이미지에 적용되지는 않습니다.
