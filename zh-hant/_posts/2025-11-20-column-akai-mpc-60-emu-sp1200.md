---
author: mmr
categories:
- Column
image: ../assets/images/column-akai-mpc-60-emu-sp1200.webp
lang: zh-hant
layout: post
permalink: /zh-hant/column-akai-mpc-60-emu-sp1200/
tags:
- Hiphop
- Electronic
- 80s
- 90s
title: 【專欄】12位元採樣器的黃金時代：MPC60/SP-1200
---


## 第 1 章：簡介 — 為什麼選擇 12 位元？


文字：mmr｜主題：關於 12 位元採樣器，它在 20 世紀 80 年代到 90 年代初期的音樂製作中發揮核心作用。

12 位元取樣器不僅僅是一個“技術中間點”，它還創造了意想不到的聲音特徵，從而產生了新的製作方法和音樂語言。在 16 位元和 24 位元等「高解析度」被理想化之前，12 位元與記憶體限制相結合，產生了獨特的聲音輪廓、失真和量化雜訊。對許多製作人來說，這並不是缺點，而是色調設計的原料。

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


## 第二章：基礎技術知識－採樣理論與12位元特性

### 2.1 抽樣基礎知識

透過將類比訊號分割為固定的時間間隔，將其轉換為數值的過程（取樣）主要有兩個參數：**取樣頻率（Hz）**和**量化位元深度（bit）**。取樣頻率由奈奎斯特理論描述，量化位深與動態範圍和量化雜訊有關。

* **12bit**：理論上動態範圍約為72dB（理想條件）。實際上，由於電路雜訊和類比路徑的影響，有效動態範圍會根據所使用的設備而變化。

### 2.2 12bit聲學特性

* **量化雜訊**往往變得明顯，尤其是對於小訊號。
* **中頻的存在**（強調中頻）相對明顯。
* 音高變換和取樣率轉換過程中發生的混疊和著色會產生獨特的「砂礫」。

### 2.3 硬體因素

影響聲音的不僅是位元深度，還有A/D/D/A電路、類比濾波器（硬體）以及內部記憶體的數量和存取方法的特性。例如，SP-1200 使用 26.04kHz 取樣，已知 E-mu 模擬路徑會強調某些泛音。

---

## 第三章：市場背景－記憶體價格與生產環境

在 20 世紀 80 年代中後期，半導體記憶體的價格比現在高出幾個數量級。在當時，增加 1MB RAM 就價值數百美元，設備製造商選擇了節省採樣時間的設計。這在規格上造成了實際的折衷，例如短採樣時間、低採樣頻率和 12 位元。另一方面，利用約束的創意方法已經發展起來，例如「快速取樣和丟棄樣本（高速取樣→俯仰」）的技術。

---

## 第四章：主要型號說明

### 4.1 E-mu SP-1200 (1987) — 技術與實用細節

* **出版年份**：1987
* **取樣頻率**：26.04kHz
* **位元深度**：12位元
* **總樣本長度**：約 10 秒（單聲道總計）
* **主要特點**：8 軌音序器、濾波器（類比）、獨立輸出

**設計理念及特色**
SP-1200 在設計時考慮了採樣器的時間限制，並針對「切割和排列短樣本」的工作流程進行了最佳化。與內部類比電路結合，結果是具有“粗糙度”或“波動”的厚低頻範圍。根據當時的規格和E-mu的技術文件，可以確認SP-1200的A/D路徑和濾波器設計對聲染色有所貢獻。

**實際使用**

* 布萊克採樣和斬波
* 快速取樣後音高降低（引起低通效應）
* 使用循環調整和定時擺動創建凹槽

<iframe width="560" height="315" src="https://www.youtube.com/embed/6-FLx_gIVCE?si=fHXFlga4-I9RphJZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### 4.2 Akai MPC60 (1988) — 作為樂器的成就

* **出版年份**：1988
* **取樣頻率**：40kHz
* **位元深度**：12位元
* **主要特點**：16 個打擊墊、內建音序器、MIDI 相容

**設計理念及特色**
在 Roger Linn 的設計幫助下，MPC60 的目標是成為「可玩的取樣器」。大打擊墊和強調律動感的音序器極大地提高了即興表演和現場製作的可用性。規格表強調了 MPC60 的音序器精度和焊盤檢測機制。

<iframe width="560" height="315" src="https://www.youtube.com/embed/vnRc56hEMsw?si=65ZvsCS8iGBWfeZW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### 4.3 赤井S900/S950

* S900 (1986)：早期的架式採樣器。取樣精度高達12位元頻寬，並具有編輯功能和外部同步功能。
* S950（1988）：S900的高級版本，提供更靈活的時間拉伸功能（儘管是粗略轉換功能）。當時的銷售記錄和文章證實它被廣泛用於俱樂部音樂製作。

### 4.4 安索尼克幻影 (1984)

* 發行年份: 1984
* 位元深度：8bit（非線性採樣特性）
* 價格區間：加速低價區間採樣器的普及

Mirage雖然不是12bit，但作為同時代的低解析度取樣器，其影響力非常大。受到追求粗糙紋理的藝術家的青睞。

### 4.5 時序電路先知 2000 (1985)

* 發行年份: 1985
* 位元深度：12bit
* 特點：將樣本播放與類比濾波器結合，可以合成樣本音調。

---

## 第 5 章：使用 12 位元採樣器的製作工作流程

這裡根據事實詳細列出了假設SP-1200和MPC60的典型生產流程。該描述著重於與實際生產者證詞和設備手冊相符的程序。

### 5.1 取樣程序（SP-1200型）

1. 從唱片中播放所需的中斷
2. 在中斷的中心短暫採樣（1-2 秒）（記住總採樣限制）
3. 降低樣本的音調，並在必要時手動調整循環點
4. 需要使用濾鏡和包絡進行輪廓調整
5. 將它們排列在 8 軌音序器上並微調時序以建立律動。

### 5.2 MPC60生產工作流程（績效導向）

1. 記錄樣本的時間相對較長（MPC60可以比SP-1200記錄更長的時間）
2. 將其加載到打擊墊上並即興進行輸入和過濾操作。
3. 使用內建音序器建立樂句，並透過更改每個音符的速度和位置來添加搖擺
4. 使用 MIDI 同步與其他裝置一起建構

---

## 第六章：音質的科學分析（頻率特性/量化噪音）

在技​​術分析部分，根據一般原理解釋了12位元設備的一般頻率響應、量化雜訊的頻譜趨勢以及變調時的混疊趨勢。這裡的解釋遵循一般趨勢，可以從每台設備的手冊和技術文章中確認。

### 6.1 頻率特性

* SP-1200採用26.04kHz取樣，因此理論奈奎斯特頻率為13.02kHz。由於實際的低通特性和類比電路，透過降低高頻，聲音變得「圓潤」。
* 由於 MPC60 使用 40kHz 樣本，因此仍保留較高頻率，但由於 12 位元量化，高頻解析度受到限制。

### 6.2 量化噪聲

* 量化雜訊可以用訊號雜訊比 (SNR) 來估計。理想的 12 位元 SNR 約為 72dB，但在實際設備中通常低於此值。

---

## 第 7 章：流派的影響（嘻哈/R&B/house/techno）

### 7.1 SP-1200 在嘻哈音樂中的作用

SP-1200 具有針對重新加工盜版和中斷而優化的音色，它成為許多黃金時代嘻哈製作環境中事實上的標準工具。多篇文章證實，Pete Rock、DJ Premier、The Bomb Squad 等製作人都曾進行過 SP 類型的樣本作品。

### 7.2 R&B與MPC的關係

MPC60的高可玩性和MIDI相容性使其在R&B和流行音樂製作網站中廣受歡迎。多次訪談表明，Teddy Riley 等製作人已在他們的製作中使用了 MPC。

### 7.3 House/Techno 和低解析度樣本

低解析度樣本對於創建紋理非常有效，並廣泛用於早期的 house/techno 場景。 Ensoniq 和 Akai 機架式設備成為工作室的必備設備。

---

## 第 8 章：主要藝術家和使用範例

> 以下是基於事實資訊（例如公開採訪、鳴謝、技術文章和官方文件）的用例摘錄。

<div class="mermaid">

flowchart TD
  A["SP-1200"] -->|使用| B["Pete Rock"]
  A -->|使用| C["DJ Premier"]
  A -->|使用| D["Marley Marl"]
  
  E["MPC60"] -->|使用| F["DJ Shadow"]
  E -->|使用| G["Dr. Dre 初期"]
  E -->|使用| H["Teddy Riley"]


</div>

（註：Dr.Dre主要使用MPC3000）

---

## 第 9 章：UI/UX 和儀表 - 使用 MPC 建立效能方法

MPC 系列普及了「採樣器=要演奏的樂器」的概念。特別是，16 個打擊墊、打擊墊靈敏度、即時播放的低延遲和內置音序器使即興演奏成為可能，並且其在現場表演和即興演奏中的用途已擴大。 Roger Linn 的設計理念（強調人類的性能感）與 Akai 的產品設計的融合支持了 MPC60 的成功，這一事實得到了多個開發人員訪談的支持。

---

## 第10章：繼承與轉載（插件/硬轉載）

自2010年代以來，模仿SP-1200和MPC「聲音」的插件和硬體再現產品不斷增加，以數位方式再現當時的「12位元感覺」已變得普遍。主要趨勢是官方硬體重製版（例如 Akai Professional 的 MPC 系列的現代版本）和透過外掛程式進行模擬（飽和度、低保真引擎）。

---

## 第 11 章：材料/參考文獻

* E-mu SP-1200 服務手冊（技術規格）
* Akai MPC60 User Manual（製品マニュアル）
* 當時的音樂科技雜誌（1987-1995 年）
* 製作人訪談（Pete Rock、DJ Premier、Dr. Dre 等）

---

## 第12章：總結與展望

12 位元採樣器是技術限制如何激發創造力的一個很好的例子。 SP-1200 和 MPC60 不再只是工具，而是形成了特定時代的音樂表現。在當今的生產環境中，有多種方法可以有意地重新創建“低保真”和“堅韌”，但是當您追溯它們的根源時，您總是會回到這些設備。

---


### YouTube 播客

*此播客是英文的，但您可以透過自動字幕和翻譯觀看。

<iframe width="560" height="315" src="https://www.youtube.com/embed/6Yr86z5Clz8?si=lRR5xNgILcSUnEQ3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### 附錄：功能關係/工作流程

#### 工作流程概念圖

<div class="mermaid">
    
flowchart TD
  SR["Record Source（レコード等）"] --> SAMP["サンプリング"]
  SAMP --> EDIT["編集（チョップ／ピッチ調整）"]
  EDIT --> PAD["パッドに配置（MPC）／シーケンスへ（SP）"]
  PAD --> SEQ["シーケンサー"]
  SEQ --> MIX["ミックスダウン"]
  MIX --> MASTER["マスタリング"]

</div>

---

#### 設備間對比圖

<div class="mermaid">
    
flowchart LR
  SP["SP-1200"]
  MPC["MPC60"]
  S950["S950"]
  Mirage["Mirage"]
  
  SP ---|低サンプルレート| Mirage
  MPC ---|演奏性| SP
  S950 ---|ラック型プロダクション| MPC

</div>

---


### SP-1200內部結構（概念圖）

<div class="mermaid">
    
flowchart TD
    A["入力段: ADC 12bit/26kHz"] --> B["サンプルRAM: 10秒分"]
    B --> C["DAC出力: ローパス特性"]
    C --> D["SSM2044 アナログローパスフィルタ"]
    D --> E["出力アンプ"]

</div>

---

### MPC60內部結構

<div class="mermaid">
    
flowchart TD
    A["入力段: 12bit ADC 40kHz"] --> B["サンプルメモリ"]
    B --> C["パッドスキャン回路"]
    C --> D["シーケンサーCPU"]
    D --> E["DAC/ミキサー部"]

</div>

---

## 範例波形/頻率分析

### SP-1200大鼓分析

<div class="mermaid">
    
graph LR
    A["元波形"] --> B["高速サンプリング後の波形"]
    B --> C["低域強調と歪み成分追加"]

</div>

---

### MPC60小鼓分析

<div class="mermaid">
    
flowchart TD
    A["元スネア"] -->|サンプリング| B["帯域の変化"]
    B --> C["高域のロールオフ"]
    C --> D["中域のクリアさ"]

</div>

---

## 12 位採樣器留下的技術遺產

### 硬體特性的繼承

<div class="mermaid">
    
flowchart TD
    A["12bit質感"] --> B["現代のエミュレーションプラグイン"]
    A --> C["ハードウェアリイシュー"]
    C --> D["SP1200 Reissue"]

</div>

## 各型號內部電路詳細說明（CPU/ROM/DAC）

### SP-1200內部區塊

<div class="mermaid">
    
flowchart TD
    A["Input Preamp\nオペアンプ: NE5532系"] --> B["ADC: Philips TDA1543系 12bit"]
    B --> C["Sample RAM: 256KB SRAM\n合計約10秒"]
    C --> D["CPU: Motorola 6809E 8-bit MCU"]
    D --> E["System ROM: 32KB EPROM\nOS/サンプル管理"]
    E --> F["DAC: SSM2024系 12bit"]
    F --> G["Analog LPF: SSM2044 (24dB/oct)"]
    G --> H["Output Amplifier: Discrete OpAmp"]

</div>

---

### MPC60內部區塊

<div class="mermaid">
    
flowchart TD
    A["Input Preamp\n高S/N回路"] --> B["ADC: AKAI独自 12bit/40kHz"]
    B --> C["Sample DRAM: 768KB 〜 拡張で1.5MB"]
    C --> D["CPU1: Hitachi HD63B03 8-bit"]
    D --> E["CPU2: Intel 8086 派生\nシーケンサー専用"]
    E --> F["OS ROM: EPROM 256KB"]
    F --> G["DAC: 12bit DAC\n+ ミキサー IC"]
    G --> H["Output Stage\nローパス特性"]

</div>

---

## 軌道/波形/頻率分析部分

### 公敵（拆彈小隊）SP-1200的分層分析

<div class="mermaid">
    
flowchart TD
    A["サンプル1: James Brown Snare"] --> D["周波数特性: 中域強調 1.5kHz"]
    B["サンプル2: ノイズ+ヒット音"] --> D
    C["サンプル3: ターンテーブルスクラッチ"] --> E["アタック強化"]
    D --> F["SP-1200での合成: 低域が丸まる"]
    F --> G["最終ミックス: Bomb Squad特有の密度"]

</div>

---

### Pete Rock - 基於 MPC60 的“These Reminisce Over You”分析

<div class="mermaid">
    
flowchart TD
    A["Tom Scottのサックスサンプル"] --> B["12bit化による丸み"]
    B --> C["帯域: 200Hz〜2kHzが前に出る"]
    C --> D["MPC60内部パッド経由のベロシティ変化"]
    D --> E["最終ビート: Pete Rockの柔らかい質感"]

</div>

---

### DJ Premier 的 MPC60 斬波方法

<div class="mermaid">
    
graph LR
    A["短いVinyl Hit"] --> B["高速チョップ"]
    B --> C["12bit変換によるザラつき"]
    C --> D["ハイハットの分離強調"]
    D --> E["Premo特有の“間”を形成"]

</div>

---

### DJ Shadow - Endtroducing (MPC60) 深度解析

<div class="mermaid">
    
flowchart TD
    A["ドラムブレイク"] --> B["40kHz→12bit変換で高域ロールオフ"]
    B --> C["残響成分のビット化による曇り"]
    C --> D["Shadowのレイヤー: 複数パッドに分解"]
    D --> E["ミックスで空間が圧縮される"]

</div>

---


### 加註1：12bit和16bit量化的比較

<div class="mermaid">
    
graph LR
    A["12bit 4096段階"] --> C["粗いステップ"]
    B["16bit 65536段階"] --> D["滑らかなステップ"]

</div>

---

### 補充2：SP-1200濾波器曲線概念

<div class="mermaid">
    
flowchart TD
    A["入力音"] --> B["LPF 12kHz付近で急激減衰"]
    B --> C["出力: 暗いトーン"]

</div>

---

### 補充3：MPC60音序器結構

<div class="mermaid">
    
graph LR
    A["Pad Input"] --> B["CPU"] --> C["Timing Correct"] --> D["Output Groove"]

</div>

---

### 新增 4：採樣器訊號路徑（按產生）

<div class="mermaid">
    
flowchart TD
    A["Early 8bit"] --> B["12bit Sampler"] --> C["16bit Sampler"] --> D["Software Era"]

</div>

---

### 補充5：SP-1200時間拉伸法（節距換算）

<div class="mermaid">
    
flowchart TD
    A["低速サンプル取り込み"] --> B["再生時ピッチUP"] --> C["粗さ+高域ノイズ"]

</div>

---

### 附加6：MPC60鼓層模型

<div class="mermaid">
    
flowchart TD
    A["Kick Layer1"] --> D["Final Mix"]
    B["Kick Layer2"] --> D
    C["Room Layer"] --> D

</div>

---

### 新增7：Vinyl→取樣器→混合器流程

<div class="mermaid">
    
flowchart TD
    A["Vinyl"] --> B["Sampler"] --> C["Mixer"] --> D["Recorder"]

</div>


---
