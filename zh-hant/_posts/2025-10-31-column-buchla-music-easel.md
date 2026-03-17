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

文：mmr｜テーマ：現代においても多くのライブ・アーティストが「単体演奏可能な最小のオーケストラ」として評価しているMusic Easel


1973 年出現的 **Buchla Music Easel** 是著名的類比模組 **Buchla 200 系列**的便攜式版本。
設計師 **Don Buchla** 將樂器稱為「便攜式作曲環境」。
它不僅僅是一個小型模組，而且被視為“個人簡易設備”。

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

## 第一章：Don Buchla 和「反穆格」哲學

1960年代初，電子樂器發展的兩大趨勢在東美洲和西美洲出現。
東部是穆格，西部是布赫拉。
Buchlaは、音を「制御」するのではなく「生成する」ことを目的とした。  
使用觸控板代替鍵盤，性能的重點是**變化率和偶然性**而不是音調。

他的哲學被延續到了後來的《音樂畫架》。
畫架是人類利用電子電路進行表演的工具，這裡存在的是「共同作者」的態度，而不是「表演者=控制者」的態度。

### 技術分析：波形と触覚の関係

Buchla 認為「波形操作 = 觸覺體驗」。
下圖是複數振盪器中FM（調頻）與波形輸出關係的簡化模型。

<div class="mermaid">

graph TD
A[Modulation Oscillator] -->|FM Signal| B[Complex Oscillator]
B -->|Wavefolded Output| C[Audio Out]
B --> D[Harmonic Timbre CV]
D -->|Control Voltage| B

</div>

この相互接続によって、単純なサイン波が倍音構造を持ち、**演奏中の微細なタッチ**が音響に即反映される。

---

## 第二章：音樂畫架的結構與哲學

Music Easelは次の二つの主要ブロックから成る。

-  **Buchla 208 儲存程式聲音來源**
-  **Buchla 218 觸控鍵盤控制器**

### シグナル・フロー図（Mermaid）

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

### 技術特點

* **複合振盪器**：可進行波形摺疊、FM、AM。
* **脈衝產生器**：產生週期性脈衝，用作時鐘。
* **信封**：自動控制、門控、可循環。
* **混響**：帶有彈簧混響的自然混響。

融合這些的理念不是“便攜性”而是“即興創作”，音樂製作的中心也從“思考”轉向了“觸覺”。

---

## 第3章：ライブ・インストゥルメントとしてのEasel

### 事例1：Suzanne Ciani “Easel Sessions” (2016–)

傳奇女電子音樂家 **Suzanne Ciani** 於 2010 年代在 Easel 開始了她的個人現場系列“Easel Sessions”。
她沒有使用任何筆記型電腦，只在畫架上表演。
現場演奏時，音高隨著手的壓力平穩變化，FM調製有機地波動。
Ciani 說：“Buchla 是一種呼吸器。”

從聲音上來說，Easel 的**非同步調製**創造了一種似乎漂浮在空間中的泛音流。
觀眾會產生「空氣本身正在被演奏」的錯覺。

### 波形分析：即興結構的特點

| 要素                          | 技術的要点         | 聴覚印象         |
| ------------------------ | | ------------- | ------------ |
| Modulation OscillatorのFM量変化 | 波形が時間的に非線形に変動 | 有機的揺らぎ       |
|脈衝產生器+包絡連接|無節拍感的循環生成 |時間感如「呼吸」 |
| Reverb混響的自乾擾|泛音的反相生成|漂浮感/殘響傳播|

---

## 第四章：獨奏表演的可能性與聲學空間的構建

Easelの魅力は、**外部エフェクトなしで音響彫刻が完結する**点にある。
透過使用脈衝發生器作為觸發器鏈結多個調製，
可以創建“生成的最小模式”和“隨機節奏結構”。

### 事例2：Charles Cohen “Live at the Rotunda” (2014)

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

這種非同步觸發結構允許 Easel 自行產生「非計量凹槽」。
科恩說，音樂只是透過「屈服」於電流的流動而產生的。

---

## 第5章：現代アーティストとEaselの継承

### 蘇珊·恰尼

→ 聲音女性主義的體現。我将我的身体托付给布奇拉的软电流。

### 陶德巴頓

→ 身為教育家，他將畫架解釋為「意識與機器之間的接觸點」。
“別玩它——聽它玩你。”

### 查爾斯·科恩

→ 即興の極北。音楽ではなく「場の生成」としてのライブ。
即使在他去世後，布赫拉仍將他的補丁重印為“科恩程序卡”。

### 凱特琳·奧裡莉亞·史密斯

→ Easelの思想をデジタルと融合。自然音的な揺らぎを現代アンビエントへ拡張。

---

## 第六章：技術與物理性－「玩電流」的行為

玩 Music Easel 並不是按一下開關，而是按一下開關。
**這是依靠電路反應速度的行為**。
指尖的壓力、濕度和溫度會影響CV值並改變聲音。

換句話說，畫架是一種將人體皮膚變成電路的樂器。
存在的聲音是現象，不是數據。

在最近的現場表演中，類比畫架操作並沒有轉換為MIDI，
將其視為純粹電流反應的運動再次引起關注。
この“反デジタル”の流れは、電子音楽に再び**身体的リアル**を取り戻す兆候でもある。

---

## 結論：管弦樂團的未來

Easel 功能雖小，但表現力無限。
その内部で揺らめく電流は、演奏者の呼吸と同期しながら“生きた音”を紡ぐ。

正如查爾斯·科恩所說，“畫架是一個孤獨的談話夥伴”
Suzanne Cianiが示したように、「それは人間の感情を電子に翻訳する器官」である。

在現今以筆記型電腦為主的生活環境中，
Buchla Music Easel 仍然是一個「孤獨的管弦樂團」。
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

### YouTube 播客

*此播客是英文的，但您可以透過自動字幕和翻譯觀看。

<iframe width="560" height="315" src="https://www.youtube.com/embed/ehLVOMR8Txw?si=Pp3UIOfRvj41tH3D" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
