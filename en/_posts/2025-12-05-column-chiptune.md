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


## Introduction: Why does 8-bit music resonate today?

Text: mmr｜Theme: Comprehensive research on reinterpreting Famicom/Game Boy sound sources into modern times

The sound known as Chiptune, or 8-bit music, has transcended the confines of a nostalgic genre that simply evokes the sounds of retro games, and continues to have a unique power in modern music culture. There are many reasons, but the most fundamental one is ""universal musicality born from constraints''**.

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


## Chapter 1: The origins of 8-bit - Famicom and Game Boy sound source chips

### 1-1. "Ricoh 2A03" that determined the sound of Famicom/NES

What determined the Famicom's sound was a sound source chip called **Ricoh 2A03 (Japan)/2A07 (overseas NES)** integrated into the CPU. This chip belongs to the so-called "PSG (Programmable Sound Generator)".

#### 5-channel configuration of Famicom sound source

- **Square wave (Pulse) x 2 channels**
Duty ratio can be selected from 12.5% ​​/ 25% / 50% / 75%, suitable for main melody.

- **Triangle wave (Triangle) x 1 channel**
It is often used for bass lines, but it was also used to simulate drums.

- **Noise ×1 channel**
Responsible for most of the game production sounds, such as snares, hi-hats, and explosion sounds.

- **DPCM (sample playback) x 1 channel**
Although the sound quality is low, close to 1 bit, it is possible to play drum samples and voice materials.

This structure later became the basic format of Chiptune, and modern musicians often keep this tone in mind when producing.

---

### 1-2. "LR35902" which created the tone of Game Boy (DMG-01)

The Game Boy is equipped with a CPU + PSG sound source called **Sharp LR35902** and has 4 channels.

#### 4-channel configuration of Game Boy sound source

- **Square wave (Pulse 1)**
- **Square wave (Pulse 2)**
- **Waveform memory (Wave channel)**
- Channel that allows you to freely draw 4-bit waveforms of 32 samples
- **Noise Channel**

Waveform memory is at the heart of creativity, and even in the modern Game Boy Chiptune, the Wave channel is widely used to generate bass, lead, kick, and unique tones. The low-end thickness is particularly attractive, and it is loved as a ""Game Boy-like tone'' including the DAC noise peculiar to the hardware.

---

## Chapter 2: Musical individuality created by waveforms - Square waves, triangle waves, noise, and the structure of waveform memory

### 2-1. The appeal of square waves (Square/Pulse)

Square waves have a clearer overtone structure than other waveforms, creating clear melodies typical of game music. Changing the duty ratio will greatly change the character of the sound, and will also affect emotional expression.

- **12.5%**: Thin and sharp
- **25%**: Bright
- **50%**: Standard
- **75%**: Thick and soft

Most of Chiptune's "song spirit" resides here.

### 2-2. Role of triangle wave (Triangle)

The triangle wave is a waveform with few overtones, making it ideal for bass lines. Because the volume of the Famicom's triangular wave could not be changed, a technique was developed to create differences in volume by devising the expression of each note.

### 2-3. Magic of rhythm created by noise

Because noise contains random frequency components, it can generate many sound effects such as snares, hi-hats, wind, and explosions. This is why game music is called "percussion made of bits."

### 2-4. Revolutionary nature of waveform memory (WAVE)

The Game Boy's WAVE channel allows you to create arbitrary waveforms rather than fixed waveforms, allowing you to create a wide variety of tones such as bass, lead, pad, kick, and FX.

---

## Chapter 3: Tracker culture and Chiptune production - LSDj / Nanoloop / Famitracker

### 3-1. What is Tracker?

Tracker is a sequencer that scrolls vertically.
**Enter the scale, volume, and effects in hexadecimal numbers** Use the method.

#### Modern typical Tracker

- **LSDj (Little Sound DJ)**
- **Nanoloop**
- **Famitracker / 0CC-Famitracker**
- **Deflemask**

They are a core part of Chiptune culture and are used by artists around the world.

### 3-2. LSDj - King of Game Boy music

LSDj is a highly complete portable tracker that directly controls the sound source of the actual Game Boy. Bass sounds that skillfully use WAVE channels, rhythms created with noise, and unique fluctuations caused by clock fluctuations are popular.

### 3-3. Famitracker - Faithfully reproduces NES sound sources

Famitracker accurately reproduces the NES APU sound source and is used by composers around the world to arrange game music and create original Chiptunes.

### 3-4. Nanoloop - minimal aesthetics

Nanoloop produces minimal electronic music with a beautiful interface that has been stripped down to its bare minimum.

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

DAW allows you to freely process effects, making it ideal for fusing Chiptune with modern electronic music.

example:
- Add delay/reverb to 8-bit lead to create a synth lead
- Process the noise channel and apply it to Trap's snare
- Sidechain square wave bass to make it look like EDM

These "expanded chips" have become mainstream recently.

---

## Chapter 5: The intersection of game music remix culture and Chiptune

There are a huge number of game music arrangements on YouTube and social media.
Chiptune has a special role in this.

reason:

- Reconfiguring old game sound sources to sound like a different hardware
- Fusion with EDM/Lo-Fi/Trap
- 8-bit texture with strong iconic character
- Easy to arrange as it can be achieved with a small number of notes

Chiptune is by no means limited to a "reproduction of game music", but is actively interpreted within modern music culture.

---

## Chapter 6: Chiptune technical analysis and composition method

### 6-1. Build a lead melody

- Uses a square wave with a duty ratio of 25% / 50%
- Slide and vibrato retain the characteristics of the sound source chip
- Make an impression by repeating short phrases

### 6-2. How to create a baseline

- Famicom: Triangle wave
- Game Boy: WAVE Channel

### 6-3. How to create rhythm

- Adjust noise channel length and frequency
- Kick is reproduced by Pitch falling
- Snare combines a short noise with a square wave

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
The features are as follows.

- Live performance on actual Game Boy or NES
- Composition using Tracker is the world standard
- Highly compatible with illustrations, videos, and pixel art
- DIY spirit and open culture

It is considered not just a musical genre, but a comprehensive form of expression.

---

## Chapter 9: Modern production environment - actual equipment, software, and hardware

### 9-1. Production using actual equipment

- Game Boy DMG-01 modification
- EverDrive/Flash Cart
- Replacement of fragile parts
- Method of recording in stereo one channel at a time

### 9-2. DAW-based production

- Completely reproduce the original sound with Plogue chipsynth
- Sidechain/EQ correction
- Separate sound sources like a multi-mic
- Adjust the sound image with 32bit float recording

---

## Chapter 10: The future of Chiptune and the future of 8-bit aesthetics

8-bit music is no longer a symbol of retro;
**An existence that gives new ideas to the modern era as a "cluster of constrained aesthetics"**
It has become.

- Use in Hyperpop and EDM
- Lo-fi hiphop 8-bit textures
- Strengthening the worldview of video works
- Comprehensive production combined with pixel art

8-bit sound will continue to have an impact on both cultural and technological aspects.

---

## Conclusion: Chiptune is the musical language of the future

**Chiptune is not "music of the past" but "a musical language that will continue to be used by future creators." **

The square wave doesn't disappear.
The snare on the noise channel is still new.
The freedom of the Wave channel is the origin of digital music.

> 8-bit music will continue to resonate all over the world.

---

