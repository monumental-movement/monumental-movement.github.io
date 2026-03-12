---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-music-easel.webp
lang: ko
layout: post
permalink: /ko/column-buchla-music-easel/
tags:
- Buchla
- Modular
- Ambient
title: '【칼럼】 Buchla Music Easel과 “고고의 연주”의 철학: 아날로그 신디에 의한 즉흥의 재정의'
---


## 서장 : Buchla Music Easel이란 무엇입니까?

문장：mmr｜테마：현대에 있어서도 많은 라이브 아티스트가 「단체 연주 가능한 최소의 오케스트라」로서 평가하고 있는 Music Easel


1973년에 등장한 **Buchla Music Easel**은 아날로그 모듈러의 명기 **Buchla 200 시리즈**를 휴대용화한 모델이다.
디자이너 **Don Buchla**는이 악기를 "휴대할 수있는 작곡 환경"이라고 불렀다.
그것은 단순한 소형 모듈러가 아니라 **“개인의 즉흥 장치”**로서 구상된 것이었다.

> "Easel은 소리의 캔버스다. 플레이어가 그 순간에 그리는 선을 저장할 수 없다."
> — Don Buchla

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


---

## 1장: Don Buchla와 "반 Moog"의 철학

1960년대 초, 전자 악기 개발의 2대 조류가 동서 미국에서 흥분했다.
동쪽 Moog, 그리고 서쪽 Buchla이다.
Buchla는 소리를 "제어"하는 대신 "생성"하는 것을 목표로 했다.
건반이 아닌 터치 플레이트를 채용해, 음정보다 **변화율과 우발성**을 연주의 축에 설치했다.

그의 철학은 나중에 Music Easel에도 계승되었다.
Easel은 **인간이 전자회로와 공연하기 위한 악기**이며, 거기에 존재하는 것은 '연주자=제어자'가 아니라 '공작자'로서의 자세다.

### 기술 분석 : 파형과 촉각의 관계

Buchla는 "파형 조작 = 촉각 체험"이라고 생각했다.
아래 그림은 Complex Oscillator에서 FM (주파수 변조)과 파형 출력 간의 관계의 단순화 된 모델입니다.

<div class="mermaid">

graph TD
A[Modulation Oscillator] -->|FM Signal| B[Complex Oscillator]
B -->|Wavefolded Output| C[Audio Out]
B --> D[Harmonic Timbre CV]
D -->|Control Voltage| B

</div>

이 상호 연결은 간단한 사인파가 배음 구조를 가지며 ** 연주중인 미세한 터치 **를 음향에 즉시 반영합니다.

---

## 2장: Music Easel의 구조와 사상

Music Easel는 다음 두 가지 주요 블록으로 구성됩니다.

- **Buchla 208 Stored Program Sound Source(음원 모듈)**
- **Buchla 218 Touch Keyboard Controller**

### 신호 흐름 다이어그램(Mermaid)

<div class="mermaid">

graph LR
A[Touch Keyboard 218] -->|CV/Gate| B[Complex Oscillator]
B -->|Audio| C[Mixer & Output]
A -->|Pressure CV| D[Modulation Oscillator]
D -->|FM| B
E[Pulser] -->|Trigger| F[Envelope Generator]
F -->|CV| B
B --> G[Reverb Unit]
G --> H[Main Out]

</div>

이 구조로 단독으로 ** 클럭 발생 → 모듈레이션 → 소리 출력 **까지 완결.
외부기재를 필요로 하지 않고, Easel 자신이 「완결한 음악계」로서 기능한다.

### 기술적 특징

***Complex Oscillator**: 파형 폴딩, FM, AM이 가능.
* **Pulser** : 주기적 펄스를 생성, 클럭 역할.
***Envelope**: 자동 제어, 게이트 반응, 루프 가능.
***Reverb**: 스프링 리버브로 인한 자연스러운 잔향.

이들을 통합하는 사상은 '가반성'이 아니라 '즉흥성'이며 음악 제작의 중심을 '사고'에서 '촉각'으로 전환했다.

---

## 3장: 라이브 악기로서의 Easel

### 사례 1: Suzanne Ciani “Easel Sessions” (2016–)

전설적 여성 전자 음악가 **Suzanne Ciani**는 2010년대에 Easel에서 솔로 라이브 시리즈 “Easel Sessions”를 시작했다.
그녀는 일체의 노트북을 배제하고 Easel 단체로 연주한다.
그 라이브에서는 손의 압력으로 음정이 부드럽게 변화하고 FM 변조가 유기적으로 흔든다.
Ciani는 "Buchla는 호흡하는 악기"라고 말했다.

음향적으로는, Easel의 **비동기 모듈레이션**이 공간을 풍기는 배음의 흐름을 낳고,
청중은 “공기 자체가 연주되고 있다” 같은 착각을 받는다.

### 파형 분석 : 즉흥 구조의 특징

| 요소 | 기술적 요점 | 청각 인상 |
| --------------------------- | ------------- | ------------ |
| Modulation Oscillator의 FM량 변화 | 파형이 시간적으로 비선형으로 변동 | 유기적 변동 |
Pulser+Envelope 연결 | 박감이 없는 주기의 생성 | “호흡”과 같은 시간 감각 |
| Reverb 잔향의 자기 간섭 | 배음의 역상 생성 |

---

## 4장: 단위 연주 가능성과 음향 공간 구축

Easel의 매력은 **외부 효과 없이 음향 조각이 완결되는 **점에 있다.
Pulser를 트리거로 하여 복수의 모듈레이션을 연동시킴으로써,
"생성하는 최소 패턴"과 "랜덤 리듬 구조"를 형성 할 수 있습니다.

### 사례 2: Charles Cohen “Live at the Rotunda” (2014)

필라델피아의 전설적 즉흥가 ** Charles Cohen **은 Buchla Music Easel을 40 년 이상 사용했습니다.
그의 라이브에서는 템포의 개념이 무너지고, Pulser가 호흡처럼 신축한다.
Cohen은 "Easel은 시간을 조각하는 도구"라고 말했다.

그의 연주에서는, Complex Oscillator의 파형 폴딩에 의해 배음이 연속적으로 붕괴·재생해,
마치 어쿠스틱 악기가 스스로 재구축되는 음향을 낳는다.

### 음향 기술 분석 : Cohen의 즉흥 구조

<div class="mermaid">

graph TD
A[Pulser] -->|Irregular Trigger| B[Envelope]
B -->|CV Modulation| C[Complex Oscillator]
C -->|Audio| D[Wavefolder]
D -->|Audio| E[Reverb]
E -->|Stereo Out| F[Audience Space]

</div>

이 비동기 트리거 구조는 Easel 단독으로 "비 박절 그루브"를 생성합니다.
Cohen은 그 전류의 흐름에 "몸을 맡긴다"만으로 음악이 일어난다고 말하고 있다.

---

## 5장: 현대 아티스트와 Easel의 상속

### Suzanne Ciani

→ 음향적 페미니즘의 구현화. Buchla의 부드러운 전류에 신체성을 투입한다.

### Todd Barton

→ 교육자로서, Easel을 「의식과 기계의 접점」으로서 해설.
“Don’t play it—listen to it playing you.” (연주하지 마라.

### Charles Cohen

→ 즉흥의 극북. 음악이 아니라 「장의 생성」으로서의 라이브.
그의 몰후도 Buchla사는 그의 패치를 "Cohen Program Card"로 복각.

### Kaitlyn Aurelia Smith

→ Easel의 사상을 디지털과 융합. 자연음적인 흔들림을 현대 앰비언트로 확장.

---

## 제6장: 기술과 신체성—“전류를 연주한다”는 행위

Music Easel을 연주하는 것은 스위치를 누르는 것이 아니라,
**전기회로의 반응속도에 몸을 맡기는 행위**이다.
손가락 끝의 압력, 습도, 온도가 CV 값에 영향을 미치고 소리가 변합니다.

즉, Easel은 “인간의 피부가 회로가 되는” 악기이며,
거기에 존재하는 소리는 **데이터가 아니라 현상**이다.

최근의 라이브 퍼포먼스에서는, 아날로그 Easel의 조작을 MIDI화하지 않고,
굳이 순수한 전류 응답으로서 취급하는 움직임이 다시 주목되고 있다.
이 '반디지털'의 흐름은 전자 음악에 다시 **신체적 리얼**을 되찾는 징후이기도 하다.

---

## 결장 : 한 오케스트라로서의 미래

Easel은 기능적으로 작고 표현적으로 무한합니다.
그 내부에서 흔들리는 전류는 연주자의 호흡과 동기하면서 "살아있는 소리"를 방사한다.

Charles Cohen이 말했듯이, "Easel은 외로운 대화 상대"이며,
Suzanne Ciani가 보여준 바와 같이, "인간의 감정을 전자로 번역하는 기관"이다.

노트북이 지배하는 현대의 라이브 환경 속에서
Buchla Music Easel은 여전히 ​​'고고의 오케스트라'로 남아 있습니다.
그것은 즉흥 연주의 미래를 최소 단위의 회로 속에 숨기고 있다.

---

## 부록: Buchla Music Easel 연표

<div class="mermaid">

timeline
    title Buchla Music Easel 年表
    1963 : Don Buchla、Buchla 100シリーズ開発開始（Moogと同時期）
    1966 : San Francisco Tape Music Centerで実験音楽家と共同研究
    1973 : Music Easel（Model 208/218）登場
    1975 : Suzanne Ciani、Buchlaによる初ライブパフォーマンス
    1980 : Charles Cohen、Easelを用いた即興ライブ開始
    1990 : Easelがアンダーグラウンド実験音楽シーンで再評価
    2013 : Easel復刻版（BEMI）発売
    2014 : Charles Cohen “Live at the Rotunda”発表
    2018 : Easel Command（208c）リリース
    2022 : 新世代アーティストによるBuchlaライブ・ムーブメント拡大

</div>

---

### YouTube Podcast

※이 Podcast는 영어입니다만, 자동 자막・번역으로 시청할 수 있습니다

<iframe width="560" height="315" src="https://www.youtube.com/embed/ehLVOMR8Txw?si=Pp3UIOfRvj41tH3D" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
