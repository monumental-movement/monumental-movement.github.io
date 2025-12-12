---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-music-easel.webp
lang: zh-hant
layout: post
permalink: /zh-hant/column-buchla-music-easel/
tags:
- Buchla
- Modular
- Ambient
title: 【コラム】 Buchla Music Easelと“孤高の演奏”の哲学：アナログ・シンセによる即興の再定義
---


## 簡介：Buchla 音樂畫架是什麼？

文：mmr｜主題：音樂畫架，即使在現代也被許多現場藝術家譽為“可以單獨演奏的最小的管弦樂隊”


1973年に登場した **Buchla Music Easel** は、アナログ・モジュラーの名機 **Buchla 200シリーズ** をポータブル化したモデルである。  
設計師 **Don Buchla** 將該樂器稱為“便攜式作曲環境”。
それは単なる小型モジュラーではなく、**“個人の即興装置”** として構想されたものだった。  

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

## 第1章：Don Buchlaと“反Moog”の哲学

1960年代初頭、電子楽器開発の二大潮流が東西アメリカで興った。  
東のMoog、そして西のBuchlaである。  
布赫拉的目的是“產生”聲音而不是“控制”聲音。
鍵盤ではなくタッチプレートを採用し、音程よりも**変化率と偶発性**を演奏の軸に据えた。  

彼の哲学は、後のMusic Easelにも受け継がれた。  
Easelは、**人間が電子回路と共演するための楽器** であり、そこに存在するのは「演奏者＝制御者」ではなく「共作者」としての姿勢だ。

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

この相互接続によって、単純なサイン波が倍音構造を持ち、**演奏中の微細なタッチ**が音響に即反映される。

---

## 第2章：Music Easelの構造と思想

Music Easelは次の二つの主要ブロックから成る。

-  **Buchla 208 Stored Program Sound Source（音源モジュール）**
-  **Buchla 218 Touch Keyboard Controller**

### 信號流圖（美人魚）

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

この構造により、単体で**クロック発生 → モジュレーション → 音出力**まで完結。
外部機材を必要とせず、Easel自身が「完結した音楽系」として機能する。

### 技術的特徴

* **Complex Oscillator**：波形フォルディング、FM、AMが可能。
* **Pulser**：周期的パルスを生成、クロック的役割。
* **Envelope**：自動制御、ゲート反応、ループ可能。
* **混響**：帶有彈簧混響的自然混響。

融合這些的理念不是“便攜性”而是“即興創作”，音樂製作的中心也從“思考”轉向了“觸覺”。

---

## 第3章：ライブ・インストゥルメントとしてのEasel

### 事例1：Suzanne Ciani “Easel Sessions” (2016–)

傳奇女電子音樂家 **Suzanne Ciani** 於 2010 年代在 Easel 開始了她的個人現場系列“Easel Sessions”。
彼女は一切のラップトップを排し、Easel単体で演奏する。
そのライブでは、手の圧力で音程が滑らかに変化し、FM変調が有機的に揺らぐ。
Cianiは「Buchlaは呼吸する楽器」と述べている。

從聲音上來說，Easel 的**異步調製**創造了一種似乎漂浮在空間中的泛音流。
聴衆は“空気そのものが演奏されている”ような錯覚を受ける。

### 波形分析：即興結構的特點

| 要素                          | 技術的要点         | 聴覚印象         |
| ------------------------ | | ------------- | ------------ |
|調製振盪器的FM量的變化|波形隨時間非線性波動 |有機波動|
| Pulser + Envelope connection | Generation of cycles without a sense of beat | Sense of time like “breathing” |
| Reverb混響的自乾擾|泛音的反相生成|漂浮感/混響傳播|

---

## 第四章：獨奏表演的可能性和聲學空間的構建

Easel的吸引力在於無需任何外部效果即可完成聲音雕塑。
Pulserをトリガーとして複数のモジュレーションを連動させることで、
「生成するミニマル・パターン」や「ランダム・リズム構造」を形成できる。

### 案例 2：查爾斯·科恩《圓形大廳現場》(Live at the Rotunda) (2014)

フィラデルフィアの伝説的即興家 **Charles Cohen** は、Buchla Music Easelを40年以上使い続けた。
在他的現場表演中，節奏的概念崩潰了，脈衝器像呼吸一樣膨脹和收縮。
科恩說：“畫架是雕刻時間的工具。”

在他的表演中，複數振盪器的波形折疊導致泛音崩潰並連續再現，
它產生的聲音就像原聲樂器正在自我重建一樣。

### 聲音技術分析：科恩的即興結構

<div class="mermaid">

graph TD
A[Pulser] -->|Irregular Trigger| B[Envelope]
B -->|CV Modulation| C[Complex Oscillator]
C -->|Audio| D[Wavefolder]
D -->|Audio| E[Reverb]
E -->|Stereo Out| F[Audience Space]

</div>

這種異步觸發結構允許 Easel 自行生成“非計量凹槽”。
Cohenはその電流の流れに“身を委ねる”だけで音楽が立ち上がると述べている。

---

## 第5章：現代アーティストとEaselの継承

### 蘇珊·恰尼

→ 聲音女權主義的體現。我將我的身體託付給布奇拉的軟電流。

### Todd Barton

→ 作為一名教育家，他將畫架解釋為“意識與機器之間的接觸點”。
“Don’t play it—listen to it playing you.”（演奏するな、演奏されろ）

### 查爾斯·科恩

→ 即興創作的極端北方。現場表演的目的不是音樂，而是創造一個場所。
即使在他去世後，布赫拉仍將他的補丁重印為“科恩程序卡”。

### 凱特琳·奧里莉亞·史密斯

→ 將 Easel 的理念與數字技術相結合。將自然聲音波動擴展到現代環境音樂。

---

## 第六章：技術與物理性——“玩電流”的行為

Music Easelを演奏することは、スイッチを押すことではなく、
**這是依靠電路反應速度的行為**。
指尖的壓力、濕度和溫度會影響CV值並改變聲音。

換句話說，畫架是一種將人體皮膚變成電路的樂器。
存在的聲音是現象，而不是數據。

在最近的現場表演中，模擬畫架操作並沒有轉換為MIDI，
將其視為純粹電流反應的運動再次引起關注。
這種“反數字”趨勢也是電子音樂回歸物理現實的標誌。

---

## 結論：管弦樂隊的未來

Easel 功能雖小，但表現力無限。
內部閃爍的電流產生與表演者呼吸同步的“活生生的聲音”。

正如查爾斯·科恩所說，“畫架是一個孤獨的談話夥伴”
正如蘇珊·恰尼 (Suzanne Ciani) 所展示的，“它是將人類情感轉化為電子形式的器官。”

在當今以筆記本電腦為主的生活環境中，
Buchla Music Easel 仍然是一個“孤獨的管弦樂隊”。
它將即興創作的未來隱藏在最小的電路單元中。

---

## 附錄：Buchla 音樂畫架年表

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
