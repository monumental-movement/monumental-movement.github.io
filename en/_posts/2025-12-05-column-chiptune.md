---
author: mmr
categories:
- Column
date: 2025-12-05 00:02:00 +0900
image: ../assets/images/column-chiptune.webp
lang: en
layout: post
tags:
- Chiptune
- 8bit
- Game
title: '[Column] Chiptune / 8-bit Music''s current location and future'
---


## 序章：8-bit音楽はなぜ現代に響くのか

文：mmr｜テーマ：ファミコン・ゲームボーイ音源を現代に再解釈する総合研究について

The sound known as Chiptune, or 8-bit music, has transcended the boundaries of simply being a nostalgic genre that evokes the sounds of retro games, and continues to have a unique power in modern music culture. There are many reasons for this, but the most fundamental one is **""universal musicality born from constraints''**.

The sounds of the Famicom/NES and Game Boy are both built with a limited number of channels, limited waveforms, and a limited range of tones. However, the melodies that were born from within these constraints are all unusually memorable. It has an extremely high melodiousness that anyone can memorize the melody within just a few seconds of listening.

Furthermore, in modern times, the ""digital purity'' that these tones provide is once again being valued. The overtones are well-balanced, the sound image is simple, and there is a high degree of freedom in arrangement. These qualities are very compatible with contemporary music, especially electronic, EDM, hyperpop, ambient, and techno.

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


## 第1章：8-bitの起源 ― ファミコンとゲームボーイの音源チップ

### 1-1. ファミコン（Famicom/NES）の音を決めた「Ricoh 2A03」

ファミコンのサウンドを決定したのは、CPUに統合された **Ricoh 2A03（日本）／2A07（海外NES）** という音源チップである。このチップは、いわゆる「PSG（Programmable Sound Generator）」に属する。

#### ファミコン音源の5チャンネル構成

- **矩形波（Pulse） ×2チャンネル**  
  デューティ比は 12.5% / 25% / 50% / 75% を選択でき、主旋律に向く。

- **三角波（Triangle） ×1チャンネル**  
It is often used for bass lines, but it was also used to simulate drums.

- **Noise ×1 channel**
  スネア・ハイハット・爆発音など、ゲーム演出的な音の大半を担当。

- **DPCM（サンプル再生） ×1チャンネル**  
Although the sound quality is low, close to 1 bit, it is possible to play drum samples and voice materials.

This structure later became the basic format of Chiptune, and modern musicians often keep this tone in mind when producing.

---

### 1-2. "LR35902" which created the tone of Game Boy (DMG-01)

ゲームボーイには **Sharp LR35902** というCPU＋PSG音源が搭載され、4チャンネルを持つ。

#### Game Boy音源の4チャンネル構成

- **矩形波（Pulse 1）**
- **矩形波（Pulse 2）**
- **Waveform memory (Wave channel)**
- Channel that allows you to freely draw 4-bit waveforms of 32 samples
- **Noise Channel**

Waveform memory is at the heart of creativity, and even in the modern Game Boy Chiptune, this wave channel is widely used for bass, lead, kick, and unique tone generation. The low-end thickness is particularly attractive, and it is loved as a ""Game Boy-like tone'' including the DAC noise peculiar to the hardware.

---

## Chapter 2: Musical individuality created by waveforms - Square waves, triangle waves, noise, and the structure of waveform memory

### 2-1. 矩形波（Square/Pulse）の魅力

矩形波は他の波形よりも倍音構造が明確で、ゲーム音楽らしい明瞭なメロディを作る。デューティ比を変えると音のキャラクターが大きく変化し、感情表現にも影響する。

- **12.5%**：細くて鋭い  
- **25%**：明るい  
- **50%**：標準的  
- **75%**: Thick and soft

Chiptuneの“歌心”は大部分がここに宿る。

### 2-2. 三角波（Triangle）の役割

The triangle wave is a waveform with few overtones, making it ideal for bass lines. Because the volume of the Famicom's triangular wave could not be changed, a technique was developed to create differences in volume by devising the expression of each note.

### 2-3. Magic of rhythm created by noise

Because noise contains random frequency components, it can generate many sound effects such as snares, hi-hats, wind, and explosions. This is why game music is called "percussion made of bits."

### 2-4. 波形メモリ（WAVE）の革命性

ゲームボーイのWAVEチャンネルは、固定波形ではなく任意の波形を作れるため、ベース、リード、パッド、キック、FXなど多彩な音色を生み出せる。

---

## Chapter 3: Tracker culture and Chipune production - LSDj / Nanoloop / Famitracker

### 3-1. What is Tracker?

Tracker is a sequencer that scrolls vertically.
**音階・音量・エフェクトを16進数で入力する** 手法を使う。

#### Modern typical Tracker

- **LSDj (Little Sound DJ)**
- **Nanoloop**
- **Famitracker / 0CC-Famitracker**
- **Deflemask**

They are a core part of Chiptune culture and are used by artists around the world.

### 3-2. LSDj - King of Game Boy music

LSDjはポータブルTrackerとして完成度が高く、Game Boy実機の音源を直接制御する。WAVEチャンネルを巧みに使ったベースサウンド、ノイズで作るリズム、クロックの揺れによる独自の揺らぎなどが人気。

### 3-3. Famitracker - Faithfully reproduces NES sound sources

Famitracker accurately reproduces the NES APU sound source and is used by composers around the world to arrange game music and create original Chiptunes.

### 3-4. Nanoloop - minimal aesthetics

Nanoloopは機能を極限まで削ぎ落とした美しいインターフェースで、ミニマルな電子音楽を生む。

---

## Chapter 4: Create Chiptune with DAW - Modern plug-ins and sound source reproduction

### 4-1. Representative plugins

- **Plogue chipsynth 2A03**
- **Plogue chipsynth MD**
- **Plogue chipsynth C64**
- **YMCK Magical 8bit Plug**
- **NES VST / GameBoy VST**

Plogue reproduces the sound source chip from the circuit level, so it can produce almost the same sound as the actual device.

### 4-2. Production with Ableton / Logic / FL Studio

DAW allows you to freely process effects, making it perfect for fusing Chiptune with modern electronic music.

example:
- Add delay/reverb to 8-bit lead to create a synth lead
- ノイズチャンネルを加工しTrapのスネアへ応用  
- 矩形波ベースをサイドチェインでEDM風に  

These "expanded Chiptunes" have recently become mainstream.

---

## Chapter 5: The intersection of game music remix culture and Chiptune

There are a huge number of game music arrangements on YouTube and social media.
Chiptune has a special role in this.

reason:

- 昔のゲーム音源を“別ハード風”に再構成  
- Fusion with EDM/Lo-Fi/Trap
- 8-bitの質感が強いアイコン性を持つ  
- Easy to arrange as it can be achieved with a small number of notes

Chiptuneは決して“ゲーム音楽の復刻”に留まらず、現代の音楽文化の中で積極的に解釈されている。

---

## 第6章：Chiptuneの技術分析と作曲方法

### 6-1. リードメロディを構築する

- デューティ比25% / 50%の矩形波を使用  
- Slide and vibrato retain the characteristics of the sound source chip
- Make an impression by repeating short phrases

### 6-2. ベースラインの作り方

- ファミコン：三角波  
- Game Boy: WAVE Channel

### 6-3. How to create rhythm

- ノイズチャンネルの長さと周波数を調整  
- キックはPitch落下で再現  
- スネアは短いノイズと矩形波を合わせる

---

## Chapter 7: Chipune Genealogy

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

## Chapter 8: Global Chiptune Scene and Artist Culture

Chiptune has communities all over the world.
特徴は次の点にある。

- Live performance using actual Game Boy or NES
- Composition using Tracker is the world standard
- Highly compatible with illustrations, videos, and pixel art
- DIY精神とオープン文化  

It is considered not just a musical genre, but a comprehensive form of expression.

---

## Chapter 9: Modern production environment - actual equipment, software, and hardware

### 9-1. Production using actual equipment

- Game Boy DMG-01 modification
- EverDrive・Flash Cart
- 壊れやすいパーツの交換  
- Method of recording in stereo one channel at a time

### 9-2. DAWベースの制作

- Completely reproduce the original sound with Plogue chipsynth
- サイドチェイン・EQ補正  
- マルチマイクのように音源を分離  
- 32bit float録音で音像を調整

---

## 第10章：Chiptuneの将来と8-bit美学の行方

8-bit音楽はもはやレトロの象徴ではなく、  
**An entity that gives new ideas to the modern era as a "cluster of constrained aesthetics"**
It has become.

- HyperpopやEDMでの使用  
- Lo-fi hiphop 8-bit textures
- Strengthening the worldview of video works
- ピクセルアートと組み合わせた総合演出  

8-bitの音はこれからも、文化・技術の両側面で影響を与え続ける。

---

## 結語：Chiptuneは未来の音楽言語である

**Chiptuneは“過去の音楽”ではなく、“未来のクリエイターが使い続ける音楽言語”である。**

矩形波は消えない。  
ノイズチャンネルのスネアは今も新しい。  
Waveチャンネルの自由度はデジタル音楽の原点。  

> 8-bit音楽は、これからも世界中で鳴り続ける。

---


### YouTube Podcast

※このPodcastは英語ですが、自動字幕・翻訳で視聴できます

<iframe width="560" height="315" src="https://www.youtube.com/embed/aO1nwUlb9NY?si=UIFZl3C_-Ys-NfHH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
