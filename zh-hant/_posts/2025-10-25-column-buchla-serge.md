---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-serge.webp
lang: zh-hant
layout: post
permalink: /zh-hant/column-buchla-serge/
tags:
- Synth
- Buchla
- Techno
- Modular
- History
title: '[專欄]Buchla 和 Serge：電子聲學的另一個譜系'
---


## “簡介——什麼是模塊化？”


文字：mmr |主題：西海岸模塊化合成器的精神歷史。 Don Buchler 和 Serge Tocheny 的想法如何融入當今的聲音設計

20 世紀 70 年代初，美國西海岸。
有些人離開了大學的電子音樂工作室，試圖將**一種用於設計聲音的設備**帶回他們的個人創作空間。
他們的名字是 **Don Buchla** 和 **Serge Tcherepnin**。

Buchla 和 Serge 經常被稱為所謂的“模塊化合成器的鼻祖”，但他們實際上脫穎而出，因為他們尋求創造哲學工具而不是商業工具。
他們的設計理念包含“反規範”的聲音視角，這在當今的 Eurorack、Max/MSP，甚至基於人工智能的生成音樂中很常見。

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



## 1.Don Buchler：電子聲音的詩學

### 1-1.從舊金山磁帶音樂中心

20 世紀 60 年代初，在舊金山的磁帶音樂中心，**Morton Subotnick** 和 **Pauline Oliveros** 等藝術家正在探索實驗音樂與技術之間的新關係。
他們尋找的是“一種不是鋼琴或吉他延伸的樂器。”

**Buchla Series 100 (1963–1966)** 應 Subotnick 的請求而出現。
傳統的音樂可操作性被有意避免，例如使用旋鈕和跳線的聲學電路配置，以及觸摸板鍵盤（實際上是一個沒有音階的電壓輸入設備）。

> “沒有黑白鍵。” — 唐·布奇拉

### 1-2. Buchla 的理念：高性能電子產品

布赫拉將樂器設計為“一個控制與生成共存的生態系統。”
聲音並不是直接來自表演者的身體，而是由電壓變化的抽象行為產生的。
因此，表演變成了即興的“表演”，聲音也變得流暢。

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

這個結構象徵著布赫拉“催化聲音而不是操縱聲音”的世界觀。
低通門（一種控制音量和音色的元素）後來成為 Eurorack 文化中的標準哲學設備。

---

## 2. サージ・トチェーニン：民主化されたモジュール

### 2-1. “人民合成器”的誕生

20 世紀 70 年代末，年輕音樂家 Serge Tochenin 對 Don Buchla 的設計理念印象深刻，在 UCLA 學習電子音樂時，他設想了一種“更多人可以使用的類似 Buchla 的設備”。
那就是**Serge 模塊化音樂系統（1974-）**。

Buchler 為藝術家創建了定制機器，而 Serge 植根於 DIY 文化和大學社區，秉承“開放原理圖，以便任何人都可以構建它們”的精神。
這種開源態度是一場概念革命，先於 Eurorack 後來的傳播。

### 2-2. Serge 的理念：補丁可編程性

Serge 的基本理念是**“一個模塊，多種功能”**。
換句話說，這個想法是單個電路可以具有無限多種工作模式，具體取決於它的連接方式。
例如，雙通用斜坡發生器（俗稱“DSG”）
- 信封
- 低頻振盪器
- 觸發延遲
- 時鐘分頻器
- 混沌模塊
功能會根據補丁配置而變化。

這一理念直接延續到今天的 Max/MSP 修補、Reaktor Blocks 和 Eurorack 的 Make Noise“數學”中。

---

## 3. Buchla 和 Serge 的比較：結構和思想

|元素|布赫拉 |謝爾蓋|
|------|---------|---------|
|起點|藝術家的實驗儀器|教育與DIY文化|
|經營理念 |表演性（聲音作為動作）|功能性（結構健全）|
|功能設計|專用模塊配置|組合通用模塊|
|控制|抽象電壓操作|具體信號處理 |
|聲學趨勢 |有機、動感、流暢 |線性、清晰、響應快|
|文化影響 |藝術聲音、裝置|噪音、電子音樂、DIY 電子音樂 |

---

## 4. 技術年表

|年份|活動 |筆記|
|----|--------|------|
| 1963 | Buchla 系列 100 開發開始 | Subotnick 委託製作的第一個模塊 |
| 1966 | Buchla Music Easel 原型亮相 |便攜式合成器的創始人|
| 1974 | Serge 模塊化公告 | “人民的合成器”口號|
| 1980 | Serge 雙斜率發生器簡介 |已完成補丁理念|
| 20 世紀 90 年代 |塞爾日重新評估期 |模擬的複興與復發|
| 2004 | Eurorack 繁榮開始 |繼承Doepfer、Make Noise等|
| 2020 年代 | Buchla 美國/Serge 轉載|原創思想的重新語境化|

---

## 5. 對模塊化文化的影響

布赫勒和薩爾奇的哲學將聲音本身重新定義為“社會行為”。
換句話說，他把關注點從“儀器”轉移到了“環境”和“界面”。

Eurorack的模塊化“無限組合”不僅僅是部件的自由，而是意義的重新配置。
Buchla的“物理性”和Serge的“結構性”已經融合，今天的電子音樂變得越來越“偏心”。

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

## 6. 連接現代：算法與身體之間

Buchla/Serge 精神在 Max/MSP、VCV Rack 甚至人工智能生成的音樂工具中依然生機勃勃。
它不僅僅是一個“模塊的組合”，而是一個連接時間、空間、身體和概率的藝術框架。

模塊化合成器不僅僅是創建聲音的“工具”；
它是一種產生聲音和人之間發生的“事件”的媒介。
Buchla 和 Serge 的設計理念仍然是該媒體理念的萌芽。

<iframe width="560" height="315" src="https://www.youtube.com/embed/GpCdodqTYtE?si=lIQMClxtxuqhBIvc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/QBVCa3RaR0c?si=VWdNaHjNBMK-r8Mj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
---

## 結論——“控制電壓”的詩學

據說唐·布克勒在去世前曾說過這句話。
> “電壓不是一個數字——而是一個手勢。”

中士也說。
> “每個補丁都是一個作品。”

對他們來說，電壓不僅僅是一個信號；更是一個信號。
**這是“一種連接人類意志和機器的詩意語言。”**

即使到了 2025 年，我們仍繼續聆聽那股電壓的詩意。

---


