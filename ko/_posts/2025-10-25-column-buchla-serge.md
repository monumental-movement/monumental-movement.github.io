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
title: '【칼럼】 Buchla와 Serge : 전자 음향의 또 다른 계보'
---


## "시작하기 — 모듈러란 무엇인가"


문장：mmr｜테마：서해안 모듈러 신디의 정신사. 돈 북라와 서지 토체니의 사상이 어떻게 오늘의 사운드 디자인에 계승되었는가

1970년대 초, 미국 서해안.
대학의 전자음악 스튜디오를 떠나 **'소리를 디자인하는 장치'**를 개인의 창조공간으로 가져오려고 한 사람들이 있었다.
그들의 이름은 **Don Buchla(돈 북라)**와 **Serge Tcherepnin(서지 토체닌)**.

Buchla와 Serge는 이른바 '모듈러 신디의 시조'라고 하는 경우가 많지만, 실제로는 **상업 악기가 아니라 철학적 도구**를 만들려는 점에서 이채를 내고 있다.
그들의 설계 사상은 오늘의 Eurorack이나 Max/MSP, 혹은 AI를 이용한 생성 음악에도 통저하는 '반·규범적'인 음향관을 갖고 있었다.

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



## 1. 돈 북라 : 전자음 시학

### 1-1. 샌프란시스코 테이프 뮤직 센터에서

1960년대 초, 샌프란시스코의 테이프 뮤직 센터에서는 **Morton Subotnick**과 **Pauline Oliveros** 등이 실험 음악과 기술의 새로운 관계를 모색하고 있었다.
그들이 요구한 것은, 「피아노나 기타의 연장이 아닌 악기」였다.

Subotnick의 의뢰에 응하여 등장한 것이 **Buchla Series 100(1963-1966)**이다.
노브와 패치 케이블에 의한 음향 회로의 구성, 터치 플레이트식 키보드(실제로는 「음계를 가지지 않는 전압 입력 디바이스」) 등, 종래의 악기적 조작성을 의도적으로 배제하고 있었다.

> “No black and white keys.” — Don Buchla

### 1-2. Buchla의 사상: Performative Electronics

Buchla는 악기를 ** "제어와 생성이 동거하는 생태계"**로 설계했다.
소리는 연주자의 몸에서 직접 나오는 것이 아니라 전압 변화라고 하는 '추상적인 행동'에 의해 생성된다.
그 때문에, 연주는 즉흥적인 “행위”가 되어, 소리는 유동한다.

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

이 구조야말로, 「**소리를 조작하는 것이 아니라, 소리를 촉매하는**」라고 하는 Buchla의 세계관을 상징하고 있다.
Low Pass Gate(음량과 음색을 일체 제어하는 ​​소자)는 나중에 Eurorack 문화에서도 스테디셀러 철학 장치가 되었다.

---

## 2. 서지 토체닌: 민주화된 모듈

### 2-1. “The People’s Synthesizer”의 탄생

1970년대 후반 돈 북라의 설계 사상에 감명을 받은 젊은 음악가 서지 토체닌은 UCLA에서 전자 음악을 배우면서 '더 많은 사람이 손에 넣을 수 있는 Buchla적 장치'를 구상했다.
그것이 **Serge Modular Music System(1974–)**이다.

북라가 예술가를 위한 특주기를 만들었던 반면 세르게는 DIY문화와 대학 커뮤니티에 뿌리를 두고 **'회로도를 공개하고 누구나 만들 수 있다'**라는 정신을 내걸었다.
이 오픈소스적인 자세는 이후의 유로락 보급에 앞선 개념적 혁명이었다.

### 2-2. Serge의 철학: Patch Programmability

Serge의 근본 사상은 **“One module, many functions”**.
즉, 단일 회로가 접속 방법에 따라 무수한 동작 모드를 갖는다는 생각이다.
예를 들어 Dual Universal Slope Generator(통칭 「DSG」)는,
- 봉투
- LFO
- 트리거 지연
- 클럭 분배기
- 혼돈 모듈
패치 구성에 따라 기능이 변경됩니다.

이 사상은 오늘의 Max/MSP 패칭, Reaktor Blocks, 혹은 Eurorack의 Make Noise 「Maths」에 직계로 계승되고 있다.

---

## 3. Buchla와 Serge 비교 : 구조와 사상

| 요소 | Buchla | Serge |
|------|--------|--------|
| 출발점 | 예술가를위한 실험 악기 | 교육 및 DIY 문화 |
| 조작 사상 | Performative(행위로서의 소리) | Functional(구조로서의 소리) |
| 기능 설계 | 전용 모듈 구성 | 범용 모듈 조합 |
| 제어 | 추상 전압 동작 | 구체적인 신호 조작 |
| 음향 경향 | 유기 · 동적 · 매끄러운 | 선형 · 명쾌 · 고속 응답 |
| 문화적 영향 | 아트 사운드, 설치 | 노이즈, 테크노, DIY 전자 음악 |

---

## 4. 기술 연표

| 년 | 사건 | 비고 |
|----|--------|------|
1963 | Buchla Series 100 개발 개시 | Subotnick 위탁에 의한 최초의 모듈러 |
1966 | Buchla Music Easel 원형 등장 | 휴대용 신스의 시조 |
| 1974 | Serge Modular 발표 | “People’s Synthesizer”의 슬로건 |
| 1980 | Serge Dual Slope Generator 등장 | 패치 철학의 완성형 |
| 1990s | Serge 재평가기 | 아날로그 리바이벌과 재발 |
| 2004 | Eurorack 붐 시작 | Doepfer, Make Noise 등에 상속 |
| 2020s | Buchla USA / Serge 복각 | 원래 사상의 재 문맥화 |

---

## 5. 모듈형 문화에 미치는 영향

북라와 서지의 철학은 **음향 자체를 '사회적 행위'로 재정의**했다.
즉, 「악기」로부터 「환경」 「인터페이스」로 시점을 옮긴 것이다.

Eurorack의 모듈러의 "무한 조합"은 단순히 부품의 자유가 아니라 ** 의미의 재구성 ** 자체입니다.
Buchla의 "신체성", Serge의 "구조성"이 융합되어 오늘날의 전자 음악은 점점 "비중심적"이되고 있습니다.

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

## 6. 현대에 연결 : 알고리즘과 신체 사이

Max/MSP나 VCV Rack, 심지어는 AI 생성 음악 툴에서도 Buchla/Serge의 정신은 살아 있다.
그것은 단순한 "모듈 조합"이 아니라 ** 시간, 공간, 신체 및 확률을 연결하는 아트 프레임 **입니다.

모듈러 신디는 소리를 만들기 위한 "도구"가 아니라,
소리와 사람 사이에 태어난 '사건'을 생성하는 언론이다.
Buchla와 Serge의 디자인 사상은 바로 그 미디어 철학의 모에 계속되고 있습니다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GpCdodqTYtE?si=lIQMClxtxuqhBIvc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/QBVCa3RaR0c?si=VWdNaHjNBMK-r8Mj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
---

## 결어 — “Control Voltage” 시학

돈 북라는 생전에 이렇게 말했다고 한다.
> “Voltage is not a number — it’s a gesture.”

서지 또한 말한다.
> “Every patch is a composition.”

이들에게는 전압이란 단순한 신호가 아니라,
**"인간의 의지와 기계 사이를 연결하는 시적인 언어"**였다.

2025년의 지금도, 우리는 그 전압의 시를 계속 듣고 있다.

---

### YouTube Podcast

※이 Podcast는 영어입니다만, 자동 자막・번역으로 시청할 수 있습니다

<iframe width="560" height="315" src="https://www.youtube.com/embed/bVHO4y4znW8?si=8bfuNpxwJy43R_SL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
