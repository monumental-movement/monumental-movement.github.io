---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-serge.webp
lang: ko
layout: post
permalink: /ko/column-buchla-serge/
tags:
- Synth
- Buchla
- Techno
- Modular
- History
title: '[칼럼] Buchla와 Serge: 전자 음향학의 또 다른 계보'
---


## "소개 — 모듈러란 무엇입니까?"


텍스트: mmr | 주제: West Coast 모듈러 신디사이저의 영적 역사. Don Buchler와 Serge Tocheny의 아이디어가 오늘날의 사운드 디자인에 어떻게 적용되었는지

1970년대 초, 미국 서부해안.
대학의 전자 음악 스튜디오를 떠나 **사운드를 디자인하는 장치**를 개인 창작 공간으로 다시 가져오려는 사람들이 있었습니다.
그들의 이름은 **Don Buchla**와 **Serge Tcherepnin**입니다.

Buchla와 Serge는 소위 "모듈형 신디사이저의 창시자"로 종종 언급되지만, 실제로는 상업적인 악기가 아닌 철학적인 도구를 만들려고 했다는 점에서 두각을 나타냅니다.
그들의 디자인 철학에는 오늘날의 Eurorack, Max/MSP, 심지어 AI 기반 생성 음악에 공통적으로 적용되는 "비표준적인" 음향 관점이 포함되어 있습니다.

---

<style type="text/css">

table, td, th {
border: 2px #111 solid;
width: auto;
padding: 10px; 
}
th {
background-color: #111;
color: #fff;
}
</style>



## 1. 돈 부클러(Don Buchler): 일렉트로닉 사운드의 시학

### 1-1. 샌프란시스코 테이프 뮤직 센터에서

1960년대 초 샌프란시스코의 테이프 음악 센터에서 **Morton Subotnick** 및 **Pauline Oliveros**와 같은 아티스트들은 실험적인 음악과 기술 간의 새로운 관계를 탐구하고 있었습니다.
그들이 찾고 있던 것은 '피아노나 기타의 연장선이 아닌 악기'였습니다.

**Buchla Series 100(1963~1966)**은 Subotnick의 요청에 따라 등장했습니다.
노브와 패치 케이블을 사용한 음향 회로 구성, 터치 플레이트 키보드(실제로는 스케일이 없는 전압 입력 장치) 등 전통적인 음악적 조작성을 의도적으로 피했습니다.

> "흑백 키는 없습니다." — 돈 부클라

### 1-2. Buchla의 철학: Performative Electronics

Buchla는 악기를 '제어와 세대가 공존하는 생태계'로 설계했습니다.
소리는 연주자의 신체에서 직접 나오는 것이 아니라 전압 변화의 추상적인 동작에 의해 생성됩니다.
따라서 연주는 즉흥적인 '행위'가 되고 소리는 유동적입니다.

---

<div class="mermaid">

flowchart LR
  subgraph Buchla_System["Buchla System 100/200 概念構造"]
    direction LR
    CV["Voltage Source<br>(コントロール電圧)"] --> MOD["Modulation Bus<br>(変調経路)"]
    MOD --> OSC["Complex Oscillator<br>(複雑発振)"]
    OSC --> LPG["Low Pass Gate<br>(音色・音量連動)"]
    LPG --> OUT["Audio Out"]
  end
  style Buchla_System fill:#f0f8ff,stroke:#003366,stroke-width:1px;

</div>

이 구조는 "소리를 조작하기보다는 촉매한다"는 Buchla의 세계관을 상징합니다.
로우 패스 게이트(볼륨과 음색을 모두 제어하는 ​​요소)는 나중에 Eurorack 문화의 표준 철학적 장치가 되었습니다.

---

## 2. Serge Tochenin: 민주화된 모듈

### 2-1. 국민신디사이저 탄생

1970년대 후반, 젊은 음악가 Serge Tochenin은 Don Buchla의 디자인 철학에 깊은 인상을 받았고, UCLA에서 전자음악을 공부하면서 '더 많은 사람들이 접근할 수 있는 Buchla와 같은 장치'를 구상했습니다.
그것이 바로 **Serge Modular Music System(1974~)**입니다.

Buchler가 예술가를 위한 맞춤형 기계를 만든 반면, Serge는 DIY 문화와 대학 커뮤니티에 뿌리를 두고 있으며 '누구나 만들 수 있도록 설계도를 공개하라'는 정신을 갖고 있습니다.
이러한 오픈 소스 태도는 나중에 Eurorack이 확산되기 이전에 일어난 개념적 혁명이었습니다.

### 2-2. Serge의 철학: 패치 프로그래밍 가능성

Serge의 기본 철학은 **“하나의 모듈, 많은 기능”**입니다.
즉, 단일 회로는 연결 방식에 따라 무한한 수의 작동 모드를 가질 수 있다는 아이디어입니다.
예를 들어, 이중 범용 경사 생성기(일반적으로 "DSG"로 알려짐)
- 봉투
-LFO
- 트리거 지연
- 시계 분배기
- 카오스 모듈
패치 구성에 따라 기능이 변경됩니다.

이 철학은 오늘날의 Max/MSP 패치, Reaktor Blocks 및 Eurorack의 Make Noise "Maths"에 직접적으로 적용됩니다.

---

## 3. Buchla와 Serge의 비교: 구조와 이념

| 요소 | 부츨라 | 서지 |
|------|---------|---------|
| 출발점 | 예술가를 위한 실험 도구 | 교육과 DIY 문화 |
| 운영철학 | 수행적(소리를 행동으로) | 기능적(구조로서의 소리) |
| 기능적인 디자인 | 전용 모듈 구성 | 범용 모듈 결합 |
| 제어 | 추상 전압 작동 | 구체적인 신호 조작 |
| 음향 동향 | 유기적이고 역동적이며 부드럽습니다 | 선형적이고 명확하며 빠른 응답 |
| 문화적 영향 | 아트 사운드, 설치 | 소음, 테크노, DIY 전자음악 |

---

## 4. 기술 연대기

| 연도 | 이벤트 | 메모 |
|----|---------|------|
| 1963년 | Buchla 시리즈 100 개발 시작 | Subotnick이 의뢰한 최초의 모듈식 |
| 1966년 | Buchla Music 이젤 프로토타입 데뷔 | 휴대용 신디사이저의 창시자 |
| 1974년 | Serge 모듈식 발표 | '인민통합' 슬로건 |
| 1980 | Serge 이중 경사 생성기 소개 | 완성된 패치 철학 |
| 1990년대 | 서지 재평가 기간 | 아날로그 부활과 재발 |
| 2004년 | Eurorack 붐이 시작됩니다 | Doepfer, Make Noise 등에 의해 상속됨 |
| 2020년대 | Buchla USA / Serge 재판 | 독창적인 사고의 재맥락화 |

---

## 5. 모듈 문화에 미치는 영향

Buchler와 Sarge의 철학은 소리 자체를 "사회적 행위"로 재정의했습니다.
즉, 그는 '도구'에서 '환경'과 '인터페이스'로 초점을 옮겼다.

Eurorack의 모듈식 "무한 조합"은 단순히 부품의 자유가 아니라 의미의 재구성입니다.
Buchla의 '물리성'과 Serge의 '구조성'이 합쳐져 오늘날의 전자음악은 점점 더 '탈중심적'이 되어가고 있습니다.

---

<div class="mermaid">

timeline
  title Buchla / Serge: Evolution of Modular Thinking
  1963 : Buchla Series 100 開発
  1969 : Buchla 200 シリーズ
  1974 : Serge Modular 初期版
  1980 : Serge Dual Slope Generator
  1990 : Buchla 400 / MIDI実験
  2004 : Eurorackブーム
  2020 : Buchla USA / Serge再評価

</div>

---

## 6. 현대 시대로의 연결: 알고리즘과 신체 사이

Buchla/Serge 정신은 Max/MSP, VCV Rack 및 AI 생성 음악 도구에도 생생하게 살아 있습니다.
단순한 '모듈의 결합'이 아닌, 시간과 공간, 신체와 확률을 연결하는 예술적 프레임이다.

모듈러 신디사이저는 단지 사운드를 생성하기 위한 "도구"가 아닙니다.
소리와 사람 사이에서 발생하는 '이벤트'를 발생시키는 매체입니다.
Buchla와 Serge의 디자인 철학은 계속해서 미디어 철학의 싹이 되고 있습니다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GpCdodqTYtE?si=lIQMClxtxuqhBIvc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/QBVCa3RaR0c?si=VWdNaHjNBMK-r8Mj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
---

## 결론 - "제어 전압"의 시학

돈 부클러(Don Buchler)는 죽기 전에 이렇게 말했다고 합니다.
> "전압은 숫자가 아니라 제스처입니다."

사지도 말한다.
> “모든 패치는 하나의 합성물입니다.”

그들에게 전압은 단순한 신호가 아닙니다.
**``인간의 의지와 기계를 연결하는 시적 언어''였습니다**

2025년인 지금도 우리는 그 전압의 시를 계속해서 듣고 있습니다.

---


