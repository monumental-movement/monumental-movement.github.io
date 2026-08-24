---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-music-easel.webp
lang: en
layout: post
tags:
- Buchla
- Modular
- Ambient
title: 【コラム】 Buchla Music Easelと“孤高の演奏”の哲学：アナログ・シンセによる即興の再定義
---


## 序章：Buchla Music Easelとは何か

Text: mmr｜Theme: Music Easel, which even today is praised by many live artists as the "smallest orchestra that can perform on its own"


1973年に登場した **Buchla Music Easel** は、アナログ・モジュラーの名機 **Buchla 200シリーズ** をポータブル化したモデルである。  
設計者 **Don Buchla** は、この楽器を「携帯できる作曲環境」と呼んだ。  
It was not just a small modular, but was conceived as a ""personal improvised device.''

> 「Easelは音のキャンバスだ。プレイヤーがその瞬間に描く線を保存することはできない。」  
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

## Chapter 1: Don Buchla and the "Anti-Moog" Philosophy

1960年代初頭、電子楽器開発の二大潮流が東西アメリカで興った。  
東のMoog、そして西のBuchlaである。  
Buchlaは、音を「制御」するのではなく「生成する」ことを目的とした。  
鍵盤ではなくタッチプレートを採用し、音程よりも**変化率と偶発性**を演奏の軸に据えた。  

彼の哲学は、後のMusic Easelにも受け継がれた。  
Easel is an instrument for humans to perform with electronic circuits, and what exists there is the attitude of a ""co-author" rather than a ""performer = controller."

### 技術分析：波形と触覚の関係

Buchlaは「波形操作＝触覚体験」であると考えた。  
下図は、Complex OscillatorにおけるFM（周波数変調）と波形出力の関係の簡略モデルである。

<div class="mermaid">

graph TD
A[Modulation Oscillator] -->|FM Signal| B[Complex Oscillator]
B -->|Wavefolded Output| C[Audio Out]
B --> D[Harmonic Timbre CV]
D -->|Control Voltage| B

</div>

Due to this interconnection, a simple sine wave has a harmonic structure, and the minute touches during performance are immediately reflected in the sound.

---

## 第2章：Music Easelの構造と思想

Music Easelは次の二つの主要ブロックから成る。

-  **Buchla 208 Stored Program Sound Source（音源モジュール）**
-  **Buchla 218 Touch Keyboard Controller**

### Signal flow diagram (Mermaid)

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

This structure allows you to complete clock generation → modulation → sound output** all by itself.
外部機材を必要とせず、Easel自身が「完結した音楽系」として機能する。

### 技術的特徴

* **Complex Oscillator**：波形フォルディング、FM、AMが可能。
* **Pulser**：周期的パルスを生成、クロック的役割。
* **Envelope**：自動制御、ゲート反応、ループ可能。
* **Reverb**: Natural reverberation with spring reverb.

これらを統合する思想は「可搬性」ではなく「即興性」であり、音楽制作の中心を“思考”から“触覚”へと転換した。

---

## 第3章：ライブ・インストゥルメントとしてのEasel

### Case 1: Suzanne Ciani "Easel Sessions" (2016–)

伝説的女性電子音楽家 **Suzanne Ciani** は、2010年代にEaselでのソロライブシリーズ “Easel Sessions” を開始した。
彼女は一切のラップトップを排し、Easel単体で演奏する。
At the live performance, the pitch changes smoothly with the pressure of the hands, and the FM modulation organically fluctuates.
Ciani says, ""Buchla is a breathing instrument.''

Sonically, Easel's **asynchronous modulation** creates a flow of overtones that seems to float through space.
The audience gets the illusion that ""the air itself is being played.''

### 波形分析：即興構造の特徴

| Elements | Technical Points | Auditory Impressions |
| --------------------------- | ------------- | ------------ |
| Change in FM amount of Modulation Oscillator | Waveform fluctuates nonlinearly over time | Organic fluctuation |
| Pulser＋Envelope連結           | 拍感を持たない周期の生成  | “呼吸”のような時間感覚 |
| Reverb残響の自己干渉               | 倍音の逆相生成       | 浮遊感・残響的広がり   |

---

## 第4章：単体演奏の可能性と音響空間の構築

Easelの魅力は、**外部エフェクトなしで音響彫刻が完結する**点にある。
By linking multiple modulations using Pulser as a trigger,
「生成するミニマル・パターン」や「ランダム・リズム構造」を形成できる。

### Case 2: Charles Cohen "Live at the Rotunda" (2014)

Legendary Philadelphia improviser **Charles Cohen** used the Buchla Music Easel for over 40 years.
At his live shows, the concept of tempo collapses, and Pulser expands and contracts like breathing.
Cohenは「Easelは時間を彫刻する道具」と語った。

彼の演奏では、Complex Oscillatorの波形フォルディングによって倍音が連続的に崩壊・再生し、
It produces a sound that is as if an acoustic instrument were reconstructing itself.

### 音響技術分析：Cohenの即興構造

<div class="mermaid">

graph TD
A[Pulser] -->|Irregular Trigger| B[Envelope]
B -->|CV Modulation| C[Complex Oscillator]
C -->|Audio| D[Wavefolder]
D -->|Audio| E[Reverb]
E -->|Stereo Out| F[Audience Space]

</div>

この非同期トリガー構造により、Easel単体で「非拍節的グルーヴ」が生成される。
Cohenはその電流の流れに“身を委ねる”だけで音楽が立ち上がると述べている。

---

## 第5章：現代アーティストとEaselの継承

### Suzanne Ciani

→ 音響的フェミニズムの具現化。Buchlaの柔らかい電流に身体性を託す。

### Todd Barton

→ 教育者として、Easelを「意識と機械の接点」として解説。
“Don’t play it—listen to it playing you.”（演奏するな、演奏されろ）

### Charles Cohen

→ 即興の極北。音楽ではなく「場の生成」としてのライブ。
彼の没後もBuchla社は彼のパッチを「Cohen Program Card」として復刻。

### Kaitlyn Aurelia Smith

→ Integrating Easel's philosophy with digital technology. Extending natural sound fluctuations to modern ambient music.

---

## 第6章：テクノロジーと身体性 ― “電流を演奏する”という行為

Playing Music Easel isn't about flipping a switch;
**It is the act of relying on the reaction speed of an electric circuit**.
指先の圧、湿度、温度がCV値に影響し、音が変化する。

つまり、Easelは「人間の皮膚が回路になる」楽器であり、
そこに存在する音は**データではなく現象**である。

近年のライブパフォーマンスでは、アナログEaselの操作をMIDI化せず、
あえて純粋な電流応答として扱う動きが再び注目されている。
This "anti-digital" trend is also a sign of bringing back physical reality to electronic music.

---

## Conclusion: The future as an orchestra

Easel is functionally small and expressively limitless.
その内部で揺らめく電流は、演奏者の呼吸と同期しながら“生きた音”を紡ぐ。

Charles Cohenが語ったように、「Easelは孤独な会話の相手」であり、
As Suzanne Ciani has shown, "it is the organ that translates human emotions into electronic form."

ラップトップが支配する現代のライブ環境の中で、
Buchla Music Easel remains a "solitary orchestra".
It holds the future of improvisation hidden within the smallest unit of circuitry.

---

## Appendix: Buchla Music Easel Chronology

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

*This podcast is in English, but you can watch it with automatic subtitles and translation.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ehLVOMR8Txw?si=Pp3UIOfRvj41tH3D" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
