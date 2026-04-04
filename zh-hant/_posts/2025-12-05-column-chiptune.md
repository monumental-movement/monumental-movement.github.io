---
author: mmr
categories:
- Column
date: 2025-12-05 00:02:00 +0900
image: ../assets/images/column-chiptune.webp
lang: zh-hant
layout: post
permalink: /zh-hant/column-chiptune/
tags:
- Chiptune
- 8bit
- Game
title: 【專欄】Chiptune/8位音樂的現況與未來
---


## 簡介：為什麼8位音樂在今天能引起共鳴？

文：mmr｜主題：將Famicom/Game Boy聲源重新詮釋到現代的綜合研究

這種被稱為 Chiptune 或 8 位元音樂的聲音已經超越了簡單地讓人想起復古遊戲聲音的懷舊音樂類型的限制，並在現代音樂文化中繼續擁有獨特的力量。原因有很多，但最根本的一個是「約束中誕生的普遍音樂性」**。

Famicom/NES 和 Game Boy 的聲音都是由有限數量的通道、有限的波形和有限的音調範圍構建的。然而，在這些限制下誕生的旋律卻異常令人難忘。它的旋律性極高，任何人聽完後幾秒鐘就能記住旋律。

此外，在現代，這些音調提供的「數位純度」再次受到重視。泛音均衡，聲像簡潔，編曲自由度高。這些品質與當代音樂非常相容，尤其是電子音樂、EDM、超級流行音樂、環境音樂和電子音樂。

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


## 第一章：8位元的起源－Famicom和Game Boy音源晶片

### 1-1.決定Famicom/NES聲音的“Ricoh 2A03”

決定Famicom聲音的是CPU中整合的名為**Ricoh 2A03（日本）/2A07（海外NES）**的音源晶片。該晶片屬於所謂的「PSG（可程式聲音產生器）」。

#### Famicom音源5聲道配置

- **矩形波（Pulse） ×2チャンネル**  
佔空比可選擇12.5%/25%/50%/75%，適合主旋律。

- **三角波(Triangle) x 1通道**
它通常用於低音線，但也用於模擬鼓。

- **噪音×1通道**
負責大部分遊戲製作聲音，例如小鼓、踩鈸和爆炸聲音。

- **DPCM（樣本播放）x 1 通道**
雖然音質較低，接近1位，但可以播放鼓樣本和聲音材料。

這種結構後來成為 Chiptune 的基本格式，現代音樂家在製作時常常牢記這種音調。

---

### 1-2.創造Game Boy (DMG-01) 音色的“LR35902”

Game Boy 配備了名為 **Sharp LR35902** 的 CPU + PSG 音源，有 4 個頻道。

#### Game Boy音源の4チャンネル構成

- **矩形波（Pulse 1）**
- **方波（脈衝2）**
- **波形記憶體（波浪通道）**
  - 讓您自由繪製具有 32 個樣本的 4 位元波形的通道
- **噪音通道**

波形記憶是創造力的核心，即使在現代 Game Boy Chiptune 中，波形通道也被廣泛用於產生低音、主音、大鼓和獨特的音調。低音端的厚度特别有吸引力，包括硬件特有的DAC噪音在内，它作为“Game Boy般的音色”而受到喜爱。

---

## 第二章：波形創造的音樂個性－方波、三角波、雜訊和波形記憶體的結構

### 2-1.方波的魅力（Square/Pulse）

方波比其他波形具有更清晰的泛音結構，可產生遊戲音樂典型的清晰旋律。改變佔空比會大大改變聲音的特性，也會影響情感的表達。

- **12.5%**：薄而鋒利
- **25%**：明亮
- **50%**：標準
- **75%**：厚而柔軟

Chiptune 的大部分“歌曲精神”都集中在這裡。

### 2-2. 三角波（Triangle）の役割

三角波是一種泛音很少的波形，非常適合低音線。由於 Famicom 三角波的音量無法改變，因此開發了一種透過設計每個音符的表達來產生音量差異的技術。

### 2-3.噪音創造的節奏魔力

由於噪音包含隨機頻率成分，因此可以產生許多聲音效果，例如小鼓、踩鈸、風聲和爆炸聲。這就是為什麼遊戲音樂被稱為「由比特組成的打擊樂」。

### 2-4.波形記憶體 (WAVE) 的革命性本質

Game Boy 的 WAVE 通道可讓您建立任意波形而不是固定波形，讓您可以建立各種音調，例如低音、主音、打擊墊、大鼓和效果器。

---

## 第 3 章：Tracker 文化與 Chiptune 製作 - LSDj / Nanoloop / Famitracker

### 3-1. Trackerとは何か？

Tracker 是一個垂直滾動的音序器。
**以十六進位數字輸入音階、音量和效果** 使用方法。

#### 現代代表性追蹤器

- **LSDj（小聲音 DJ）**
- **奈米循環**
- **Famitracker/0CC-Famitracker**
- **除皺面具**

它們是 Chiptune 文化的核心部分，並被世界各地的藝術家所使用。

### 3-2. LSDj - Game Boy 音樂之王

LSDj 是一款高度完整的便携式跟踪器，可直接控制实际 Game Boy 的声源。巧妙地使用WAVE通道的低音、用噪音創造的節奏以及由時鐘波動引起的獨特波動很受歡迎。

### 3-3. Famitracker - 忠實再現 NES 聲源

Famitracker 準確地再現了 NES APU 聲源，並被世界各地的作曲家用來編曲遊戲音樂和創作原創 Chiptunes。

### 3-4. Nanoloop - 最小的美學

Nanoloop 製作最少的電子音樂，具有漂亮的介面，已精簡到最低限度。

---

## 第 4 章：使用 DAW 建立 Chiptune - 現代插件和聲源再現

### 4-1. 代表的プラグイン

- **Plogue 晶片合成器 2A03**
- **Plogue 晶片合成器 MD**
- **Plogue 晶片合成器 C64**
- **YMCK 神奇 8 位元插頭**
- **NES VST / GameBoy VST**

Plogueは音源チップを回路レベルから再現するため、実機とほぼ同じ音が出せる。

### 4-2.使用 Ableton/Logic/FL Studio 進行製作

DAW 讓您可以自由處理效果，使其成為將 Chiptune 與現代電子音樂融合的理想選擇。

例子：
- 將延遲/殘響新增至 8 位元主音以建立合成器主音
- 處理噪音通道並將其應用於 Trap 的軍鼓
- 矩形波ベースをサイドチェインでEDM風に  

這些「擴展晶片」最近已成為主流。

---

## 第 5 章：遊戲音樂混音文化與 Chiptune 的交集

YouTube 和社群媒體上有大量的遊戲音樂編排。
Chiptune 在這方面發揮著特殊的作用。

原因：

- 重新配置舊遊戲聲源，使其聽起來像不同的硬體
- 與 EDM/Lo-Fi/Trap 融合
- 8位紋理賦予其強烈的標誌性特徵
- 易於編排，只需少量音符即可實現

Chiptune絕不局限於“遊戲音樂的再現”，而是在現代音樂文化中積極詮釋。

---

## 第六章：Chiptune技術分析及構成方法

### 6-1.建構主旋律

- 使用佔空比為25%/50%的方波
- 滑音和顫音保留了音源晶片的特性
- 透過重複簡短的短語給人留下深刻的印象

### 6-2.如何建立基線

- Famicom：三角波
- Game Boy：WAVE 頻道

### 6-3.如何創造節奏

- 調整噪音通道長度和頻率
- 透過音高下降再現踢腿
- 小鼓結合了短噪聲和方波

---

## 第7章：奇普納族譜

<div class="mermaid">
flowchart TD
    A["Famicom 2A03"] --> X["8-bit Game Music"]
    B["Game Boy LR35902"] --> X
    C["Tracker Culture"] --> Y["Modern Chiptune"]
    Y --> Z["Electronic Music"]
    Y --> R["Game Music Remix"]
    R --> S["YouTube / SNS Culture"]
</div>


---

## 第8章：世界のChiptuneシーンとアーティスト文化

Chiptune 的社群遍佈世界各地。
其特點如下。

- 使用真實的 Game Boy 或 NES 進行現場表演
- 使用 Tracker 進行構圖是世界標準
- 與插圖、視訊和像素藝術高度相容
- DIY精神與開放文化

它不僅被認為是一種音樂流派，而且是一種綜合的表達形式。

---

## 第9章：現代生產環境－實際設備、軟體、硬體

### 9-1。使用實際設備進行生產

- Game Boy DMG-01改裝
- EverDrive・快閃記憶體車
- 更換易損零件
- 如何一次錄製一個聲道的立體聲

### 9-2.基於 DAW 的製作

- Plogue chipsynthで原音完全再現  
- 側鏈/EQ校正
- 像多麥克風一樣獨立的聲音來源
- 32bit浮點錄音調整聲像

---

## 第10章：Chiptuneの将来と8-bit美学の行方

8位音樂不再是復古的象徵；
**作為「受限美學集群」為現代時代提供新想法的實體**
已經成為了。

- 用於 Hyperpop 和 EDM
- 低保真嘻哈 8 位元紋理
- 強化影像作品的世界觀
- 結合像素藝術的綜合製作

8 位元聲音將繼續對文化和技術方面產生影響。

---

## 結論：Chiptune 是未來的音樂語言

**Chiptune 不是“過去的音樂”，而是“未來創作者將繼續使用的音樂語言”。 **

矩形波は消えない。  
噪音通道上的軍鼓仍然是新的。
Wave通道的自由是數位音樂的起源。

> 8 位元音樂將繼續在全世界引起共鳴。

---


### YouTube 播客

*此播客是英文的，但您可以透過自動字幕和翻譯觀看。

<iframe width="560" height="315" src="https://www.youtube.com/embed/aO1nwUlb9NY?si=UIFZl3C_-Ys-NfHH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
