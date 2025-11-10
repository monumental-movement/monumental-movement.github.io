---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-serge.webp
lang: en
layout: post
tags:
- Synth
- Techno
- History
title: '[Column] Buchla and Serge: Another genealogy of electronic acoustics'
---


## 「はじめに — モジュラーとは何か」

文：mmr｜テーマ：西海岸モジュラーシンセの精神史。ドン・ブックラとサージ・トチェーニーの思想が、どのように今日のサウンドデザインへ継承されたのか

1970年代初頭、アメリカ西海岸。  
大学の電子音楽スタジオを離れ、**「音をデザインする装置」**を個人の創造空間へと持ち帰ろうとした人々がいた。  
彼らの名前は **Don Buchla（ドン・ブックラ）** と **Serge Tcherepnin（サージ・トチェーニン）**。  

BuchlaとSergeは、いわゆる「モジュラーシンセの始祖」として語られることが多いが、実際には**商業楽器ではなく、哲学的な道具**を作ろうとした点で異彩を放っている。  
彼らの設計思想は、今日のEurorackやMax/MSP、あるいはAIを用いた生成音楽にも通底する“反・規範的”な音響観を宿していた。

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

## 1. ドン・ブックラ：電子音の詩学

### 1-1. サンフランシスコ・テープ・ミュージック・センターから

1960年代初期、サンフランシスコのテープ・ミュージック・センターでは、**Morton Subotnick** や **Pauline Oliveros** らが、実験音楽とテクノロジーの新しい関係を模索していた。  
彼らが求めたのは、「ピアノやギターの延長ではない楽器」だった。

Subotnickの依頼に応えて登場したのが、**Buchla Series 100（1963–1966）**である。  
ノブとパッチケーブルによる音響回路の構成、タッチプレート式キーボード（実際には「音階を持たない電圧入力デバイス」）など、従来の楽器的操作性を意図的に排していた。

> “No black and white keys.” — Don Buchla

### 1-2. Buchlaの思想：Performative Electronics

Buchlaは楽器を**「制御と生成が同居する生態系」**として設計した。  
音は演奏者の身体から直接出るのではなく、電圧変化という**抽象的な振る舞い**によって生成される。  
そのため、演奏は即興的な“行為”となり、音は流動する。

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

この構造こそが、「**音を操作するのではなく、音を触媒する**」というBuchlaの世界観を象徴している。  
Low Pass Gate（音量と音色を一体制御する素子）は、後にEurorack文化でも定番の哲学装置となった。

---

## 2. サージ・トチェーニン：民主化されたモジュール

### 2-1. “The People’s Synthesizer” の誕生

1970年代後半、ドン・ブックラの設計思想に感銘を受けた若き音楽家サージ・トチェーニンは、UCLAで電子音楽を学びながら「より多くの人が手にできるBuchla的装置」を構想した。  
それが **Serge Modular Music System（1974–）**である。

ブックラが芸術家のための特注機を作ったのに対し、SergeはDIY文化と大学コミュニティに根ざし、**「回路図を公開し、誰でも作れる」**という精神を掲げた。  
このオープンソース的な姿勢は、後のEurorack普及に先駆けた概念的革命だった。

### 2-2. Sergeの哲学：Patch Programmability

Sergeの根本思想は、**“One module, many functions”**。  
つまり、単一の回路が接続方法次第で無数の動作モードを持つという考えだ。  
たとえばDual Universal Slope Generator（通称「DSG」）は、  
- エンベロープ  
- LFO  
- トリガーディレイ  
- クロックディバイダ  
- カオスモジュール  
と、パッチ構成次第で機能が変容する。

この思想は今日のMax/MSPパッチング、Reaktor Blocks、あるいはEurorackのMake Noise「Maths」へと直系で受け継がれている。

---

## 3. BuchlaとSergeの比較：構造と思想

| 要素 | Buchla | Serge |
|------|--------|--------|
| 出発点 | 芸術家向け実験楽器 | 教育・DIY文化 |
| 操作思想 | Performative（行為としての音） | Functional（構造としての音） |
| 機能設計 | 専用モジュール構成 | 汎用モジュールを組み合わせ |
| コントロール | 抽象的電圧動作 | 具体的信号操作 |
| 音響傾向 | 有機・動的・滑らか | 線形・明快・高速レスポンス |
| 文化的影響 | アートサウンド、インスタレーション | ノイズ、テクノ、DIY電子音楽 |

---

## 4. 技術年表

| 年 | 出来事 | 備考 |
|----|--------|------|
| 1963 | Buchla Series 100 開発開始 | Subotnick委託による最初のモジュラー |
| 1966 | Buchla Music Easel 原型登場 | ポータブル・シンセの始祖 |
| 1974 | Serge Modular 発表 | “People’s Synthesizer”のスローガン |
| 1980 | Serge Dual Slope Generator 登場 | パッチ哲学の完成形 |
| 1990s | Serge再評価期 | アナログリバイバルと再発 |
| 2004 | Eurorackブーム開始 | Doepfer, Make Noiseなどに継承 |
| 2020s | Buchla USA / Serge復刻 | オリジナル思想の再文脈化 |

---

## 5. モジュラー文化への影響

ブックラとサージの哲学は、**音響そのものを“社会的行為”として再定義**した。  
つまり、「楽器」から「環境」「インターフェース」へと視点を移したのだ。

Eurorackにおけるモジュラーの“無限の組み合わせ”は、単にパーツの自由ではなく、**意味の再構成**そのもの。  
Buchlaの「身体性」、Sergeの「構造性」が融合し、今日の電子音楽はますます“非中心的”になっている。

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

## 6. 現代への接続：アルゴリズムと身体のあいだで

Max/MSPやVCV Rack、さらにはAI生成音楽ツールにおいても、Buchla/Sergeの精神は生きている。  
それは単なる“モジュールの組み合わせ”ではなく、**時間・空間・身体・確率を接続するアート的フレーム**である。

モジュラーシンセは、音を作るための「道具」ではなく、  
音と人とのあいだに生まれる「出来事」を生成するメディアだ。  
BuchlaとSergeの設計思想は、まさにそのメディア哲学の萌芽であり続けている。

<iframe width="560" height="315" src="https://www.youtube.com/embed/GpCdodqTYtE?si=lIQMClxtxuqhBIvc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/QBVCa3RaR0c?si=VWdNaHjNBMK-r8Mj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
---

## 結語 — “Control Voltage” の詩学

Don Buchler is said to have said this before his death.  
> "Voltage is not a number — it"s a gesture."

Sarge also says.  
> "Every patch is a composition."

For them, voltage is not just a signal;
**It was ""a poetic language that connects the human will and machines.''**

Even now in 2025, we continue to listen to the poetry of that voltage.

---


