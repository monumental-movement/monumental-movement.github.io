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
title: 【專欄】Buchla Music Easel與“孤獨表演”的哲學：用模擬合成器重新定義即興創作
---


## 簡介：Buchla 音樂畫架是什麼？

文：mmr｜主題：音樂畫架，即使在現代也被許多現場藝術家譽為“可以單獨演奏的最小的管弦樂隊”


1973 年出現的 **Buchla Music Easel** 是著名的模擬模塊 **Buchla 200 系列**的便攜式版本。
設計師 **Don Buchla** 將該樂器稱為“便攜式作曲環境”。
它不僅僅是一個小型模塊，而且被視為“個人簡易設備”。

> “畫架是一塊聲音畫布。你無法保存當下所畫的線條。”
> — 唐·布奇拉

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

## 第一章：Don Buchla 和“反穆格”哲學

20世紀60年代初，電子樂器發展的兩大趨勢在東美和西美出現。
東部是穆格，西部是布赫拉。
布赫拉的目的是“產生”聲音而不是“控制”聲音。
使用觸摸板代替鍵盤，性能的重點是**變化率和偶然性**而不是音高。

他的哲學被延續到了後來的《音樂畫架》中。
畫架是人類利用電子電路進行表演的工具，這裡存在的是“共同作者”的態度，而不是“表演者=控制者”的態度。

### 技術分析：波形與觸感的關係

Buchla 認為“波形操作 = 觸覺體驗”。
下圖是複數振盪器中FM（調頻）與波形輸出關係的簡化模型。

<div class="mermaid">

graph TD
A[Modulation Oscillator] -->|FM Signal| B[Complex Oscillator]
B -->|Wavefolded Output| C[Audio Out]
B --> D[Harmonic Timbre CV]
D -->|Control Voltage| B

</div>

由於這種相互聯繫，簡單的正弦波具有諧波結構，演奏過程中的微小觸動會立即反映在聲學中。

---

## 第二章：音樂畫架的結構和哲學

音樂畫架由兩個主要塊組成：

-  **Buchla 208 存儲程序聲源**
-  **Buchla 218 觸摸鍵盤控制器**

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

這種結構可以讓您自行完成時鐘生成→調製→聲音輸出**。
Easel本身就可以充當“完整的音樂系統”，無需外部設備。

### 技術特點

* **複合振盪器**：可以進行波形折疊、FM、AM。
* **脈衝發生器**：產生週期性脈衝，用作時鐘。
* **信封**：自動控制、門控、可循環。
* **混響**：帶有彈簧混響的自然混響。

融合這些的理念不是“便攜性”而是“即興創作”，音樂製作的中心也從“思考”轉向了“觸覺”。

---

## 第 3 章：畫架作為現場樂器

### 案例1：Suzanne Ciani“畫架會議”（2016年至今）

傳奇女電子音樂家 **Suzanne Ciani** 於 2010 年代在 Easel 開始了她的個人現場系列“Easel Sessions”。
她沒有使用任何筆記本電腦，只在畫架上表演。
現場演奏時，音高隨著手的壓力平穩變化，FM調製有機地波動。
Ciani 說：“Buchla 是一種呼吸器。”

從聲音上來說，Easel 的**異步調製**創造了一種似乎漂浮在空間中的泛音流。
觀眾會產生“空氣本身正在被演奏”的錯覺。

### 波形分析：即興結構的特點

|元素|技術要點|聽覺印象 |
| ------------------------ | | ------------- | ------------ |
|調製振盪器的FM量的變化|波形隨時間非線性波動 |有機波動|
|脈衝發生器+包絡連接|無節拍感的循環生成 |時間感如“呼吸” |
| Reverb混響的自乾擾|泛音的反相生成|漂浮感/混響傳播|

---

## 第四章：獨奏表演的可能性和聲學空間的構建

Easel的吸引力在於無需任何外部效果即可完成聲音雕塑。
通過使用脈衝發生器作為觸發器鏈接多個調製，
可以創建“生成的最小模式”和“隨機節奏結構”。

### 案例 2：查爾斯·科恩《圓形大廳現場》(Live at the Rotunda) (2014)

費城傳奇即興演奏家 **查爾斯·科恩** 使用 Buchla 音樂畫架 40 多年。
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
科恩說，音樂只是通過“屈服”於電流的流動而產生的。

---

## 第五章 當代藝術家與畫架的傳承

### 蘇珊·恰尼

→ 聲音女權主義的體現。我將我的身體託付給布奇拉的軟電流。

### 托德·巴頓

→ 作為一名教育家，他將畫架解釋為“意識與機器之間的接觸點”。
“別玩它——聽它玩你。”

### 查爾斯·科恩

→ 即興創作的極端北方。現場表演的目的不是音樂，而是創造一個場所。
即使在他去世後，布赫拉仍將他的補丁重印為“科恩程序卡”。

### 凱特琳·奧里莉亞·史密斯

→ 將 Easel 的理念與數字技術相結合。將自然聲音波動擴展到現代環境音樂。

---

## 第六章：技術與物理性——“玩電流”的行為

玩 Music Easel 並不是按一下開關，而是按一下開關。
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
