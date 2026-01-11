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
title: '[칼럼] 부클라 뮤직 이젤과 ''고독한 연주''의 철학: 아날로그 신디사이저로 즉흥 연주를 재정의하다'
---


## 소개: Buchla Music Easel이란 무엇인가요?

글 : mmr │ 주제 : 현대에도 많은 라이브 아티스트들로부터 “혼자서 연주할 수 있는 가장 작은 오케스트라”라고 칭찬받는 Music Easel


1973년에 등장한 **Buchla Music Easel**은 유명한 아날로그 모듈러 **Buchla 200 시리즈**의 휴대용 버전입니다.
디자이너 **Don Buchla**는 이 악기를 "이동 가능한 작곡 환경"이라고 불렀습니다.
그것은 단순한 작은 모듈이 아니라 '개인적인 즉석 장치'로 생각되었습니다.

> "이젤은 음파 캔버스입니다. 플레이어가 그리는 순간에는 선을 저장할 수 없습니다."
> — 돈 부클라

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

## 1장: Don Buchla와 "무그 반대" 철학

1960년대 초, 전자 악기 개발에 있어서 동서미 지역에서는 두 가지 주요 추세가 나타났습니다.
동쪽에는 무그(Moog), 서쪽에는 부클라(Buchla)가 있습니다.
Buchla는 소리를 "제어"하는 것이 아니라 소리를 "생성"하는 것을 목표로 했습니다.
키보드 대신 터치플레이트를 사용했고, 음높이보다는 **변화율과 우연성**에 퍼포먼스의 초점을 맞추었습니다.

그의 철학은 나중에 Music Easel로 이어졌습니다.
이젤은 인간이 전자회로를 가지고 연주하기 위한 악기이고, 거기에는 '연주자=조작자'가 아닌 '공저자'의 태도가 존재한다.

### 기술적 분석: 파형과 촉각의 관계

Buchla는 "파형 조작 = 촉각 경험"이라고 생각했습니다.
아래 그림은 Complex Oscillator의 FM(주파수 변조)과 파형 출력 간의 관계를 단순화한 모델입니다.

<div class="mermaid">

graph TD
A[Modulation Oscillator] -->|FM Signal| B[Complex Oscillator]
B -->|Wavefolded Output| C[Audio Out]
B --> D[Harmonic Timbre CV]
D -->|Control Voltage| B

</div>

이러한 상호 연결로 인해 단순한 사인파가 하모닉 구조를 갖게 되며, 연주 중 미세한 터치가 음향에 즉시 반영됩니다.

---

## 2장: 뮤직 이젤의 구조와 철학

Music Easel은 두 가지 주요 블록으로 구성됩니다.

- **Buchla 208 내장 프로그램 음원**
- **Buchla 218 터치 키보드 컨트롤러**

### 신호 흐름도(인어)

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

이 구조를 사용하면 클럭 생성 → 변조 → 사운드 출력**을 모두 스스로 완료할 수 있습니다.
이젤 자체는 외부 장비 없이도 "완전한 음악 시스템"으로 기능합니다.

### 기술적 특징

* **복합 발진기**: 파형 폴딩, FM, AM 가능.
* **펄서**: 주기적인 펄스를 생성하고 시계 역할을 합니다.
* **봉투**: 자동으로 제어되고, 게이트되고, 반복 가능합니다.
* **리버브**: 스프링 리버브를 사용한 자연스러운 잔향입니다.

이들을 통일하는 발상은 '휴대성'이 아닌 '즉흥성'으로, 음악 제작의 중심은 '사고'에서 '촉각'으로 옮겨갔다.

---

## 3장: 라이브 악기로서의 이젤

### 사례 1: Suzanne Ciani '이젤 세션'(2016~)

전설적인 여성 일렉트로닉 뮤지션 **Suzanne Ciani**는 2010년대 Easel에서 솔로 라이브 시리즈 "Easel Sessions"를 시작했습니다.
그녀는 노트북을 모두 사용하지 않고 오직 이젤로만 작업합니다.
라이브 공연에서는 손의 압력에 따라 피치가 부드럽게 변하고 FM 변조도 유기적으로 변동합니다.
Ciani는 "Buchla는 호흡 도구입니다."라고 말합니다.

음향학적으로 Easel의 **비동기 변조**는 공간을 떠다니는 듯한 배음의 흐름을 생성합니다.
관객은 '공기 그 자체가 연주되고 있다'는 착각을 갖게 된다.

### 파형 분석: 즉흥 연주 구조의 특성

| 요소 | 기술 포인트 | 청각적 인상 |
| -------------- | ------------- | ------------ |
| 변조 발진기의 FM량 변화 | 시간이 지남에 따라 파형이 비선형적으로 변동함 | 유기적 변동 |
| 펄서 + 엔벨로프 연결 | 비트감이 없는 사이클의 생성 | '호흡' 같은 시간감 |
| 잔향잔향의 자기간섭 | 배음의 반대 위상 생성 | 부유감/잔향 확산 |

---

## 제4장: 솔로 연주의 가능성과 음향 공간의 구축

이젤의 매력은 외부의 영향 없이 사운드 조각품을 완성할 수 있다는 점이다.
Pulser를 트리거로 사용하여 여러 변조를 연결함으로써,
"생성된 최소 패턴"과 "임의의 리듬 구조"를 생성하는 것이 가능합니다.

### 사례 2: 찰스 코헨 'Live at the Rotunda'(2014)

필라델피아의 전설적인 즉흥 연주자 **Charles Cohen**은 40년 넘게 Buchla Music Easel을 사용해 왔습니다.
그의 라이브 쇼에서는 템포의 개념이 무너지고, Pulser는 호흡처럼 팽창하고 수축합니다.
코헨은 '이젤은 시간을 조각하는 도구'라고 말했다.

그의 연주에서는 Complex Oscillator의 파형 접힘으로 인해 배음이 붕괴되고 연속적으로 재생됩니다.
마치 어쿠스틱 악기가 스스로 재구성되는 듯한 사운드를 만들어냅니다.

### 사운드 기술 분석: 코헨의 즉흥적 구조

<div class="mermaid">

graph TD
A[Pulser] -->|Irregular Trigger| B[Envelope]
B -->|CV Modulation| C[Complex Oscillator]
C -->|Audio| D[Wavefolder]
D -->|Audio| E[Reverb]
E -->|Stereo Out| F[Audience Space]

</div>

이 비동기식 트리거 구조를 통해 이젤은 자체적으로 "비미터형 그루브"를 생성할 수 있습니다.
코헨은 흐름에 자신을 "내맡김"으로써 음악이 탄생한다고 말합니다.

---

## 5장: 현대 예술가와 이젤의 계승

### 수잔 치아니

→ 음향 페미니즘의 구체화. 나는 부클라의 부드러운 전류에 나의 육체를 맡긴다.

### 토드 바튼

→ 교육자로서 그는 이젤을 "의식과 기계의 접점"으로 설명합니다.
"재생하지 마세요. 재생되는 것을 들어보세요."

### 찰스 코헨

→ 즉흥 연주의 극북. 라이브 공연은 음악이 아니라 장소를 만드는 것입니다.
Buchla는 그의 죽음 이후에도 그의 패치를 "Cohen Program Card"로 재인쇄했습니다.

### 케이틀린 아우렐리아 스미스

→ 이젤의 철학을 디지털 기술과 접목. 자연스러운 사운드 변동을 현대적인 주변 음악으로 확장합니다.

---

## 6장: 기술과 물리성 - '전류를 연주하는 행위'

Music Easel을 재생하는 것은 스위치를 바꾸는 것이 아닙니다.
**전기회로의 반응속도에 의존하는 행위입니다**.
손끝의 압력, 습도, 온도는 CV 값에 영향을 미치고 소리를 변화시킵니다.

즉, 이젤은 인간의 피부가 회로가 되는 악기이다.
거기에 존재하는 소리는 데이터가 아니라 현상이다.

최근 라이브 공연에서는 아날로그 Easel 조작이 MIDI로 변환되지 않고,
이를 순수한 전류반응으로 다루려는 움직임이 다시 한번 주목받고 있다.
이러한 "반디지털" 추세는 전자 음악에 물리적 현실을 다시 가져오는 신호이기도 합니다.

---

## 결론: 오케스트라로서의 미래

이젤은 기능적으로 작고 표현력이 무한합니다.
내부에서 깜박이는 전류가 연주자의 호흡에 맞춰 '살아있는 소리'를 만들어냅니다.

찰스 코헨(Charles Cohen)이 말했듯이 "이젤은 외로운 대화 파트너이다"
Suzanne Ciani가 보여준 것처럼 "인간의 감정을 전자 형태로 변환하는 기관입니다."

오늘날 노트북이 지배하는 라이브 환경에서는
Buchla Music Easel은 "고독한 오케스트라"로 남아 있습니다.
그것은 가장 작은 회로 단위 안에 숨겨진 즉흥 연주의 미래를 담고 있습니다.

---

## 부록: Buchla Music Easel 연대기

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
