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
title_en: '[Column] Buchla Music Easel and the philosophy of “solitary performance”:
  Redefining improvisation with analog synths'
---


## Introduction: What is Buchla Music Easel?

Text: mmr｜Theme: Music Easel, which even in modern times is praised by many live artists as the “smallest orchestra that can be played alone”

The **Buchla Music Easel**, which appeared in 1973, is a portable version of the famous analog modular **Buchla 200 series**.
Designer **Don Buchla** called the instrument a "portable composition environment."
It was not just a small modular, but was conceived as a ``personal improvised device.''

> "Easel is a sonic canvas. You can't save the lines the player draws at the moment."
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

## Chapter 1: Don Buchla and the “Anti-Moog” Philosophy

In the early 1960s, two major trends in the development of electronic musical instruments arose in East and West America.
Moog in the east and Buchla in the west.
Buchla aimed to "generate" sound rather than "control" it.
A touch plate was used instead of a keyboard, and the focus of performance was on **rate of change and contingency** rather than pitch.

His philosophy was carried over into the later Music Easel.
Easel is an instrument for humans to perform with electronic circuits, and what exists there is the attitude of a ``co-author'' rather than a ``performer = controller.''

### Technical analysis: Relationship between waveform and tactile sensation

Buchla thought that "waveform manipulation = tactile experience."
The figure below is a simplified model of the relationship between FM (frequency modulation) and waveform output in Complex Oscillator.

<div class="mermaid">

graph TD
A[Modulation Oscillator] -->|FM Signal| B[Complex Oscillator]
B -->|Wavefolded Output| C[Audio Out]
B --> D[Harmonic Timbre CV]
D -->|Control Voltage| B

</div>

Due to this interconnection, a simple sine wave has a harmonic structure, and the minute touches during performance are immediately reflected in the acoustics.

---

## Chapter 2: Structure and philosophy of Music Easel

Music Easel consists of two main blocks:

- **Buchla 208 Stored Program Sound Source**
- **Buchla 218 Touch Keyboard Controller**

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
Easel itself functions as a "complete music system" without the need for external equipment.

### Technical features

* **Complex Oscillator**: Waveform folding, FM, AM possible.
* **Pulser**: Generates periodic pulses, serves as a clock.
* **Envelope**: Automatically controlled, gated, loopable.
* **Reverb**: Natural reverberation with spring reverb.

The idea that integrates these is not "portability" but "improvisation", and the center of music production has shifted from "thinking" to "tactile sensation".

---

## Chapter 3: Easel as a live instrument

### Case 1: Suzanne Ciani “Easel Sessions” (2016–)

Legendary female electronic musician **Suzanne Ciani** started her solo live series “Easel Sessions” at Easel in the 2010s.
She does away with any laptops and performs solely on Easel.
At the live performance, the pitch changes smoothly with the pressure of the hands, and the FM modulation organically fluctuates.
Ciani says, ``Buchla is a breathing instrument.''

Sonically, Easel's **asynchronous modulation** creates a flow of overtones that seems to float through space.
The audience gets the illusion that ``the air itself is being played.''

### Waveform analysis: Characteristics of improvisational structure

| Elements | Technical Points | Auditory Impressions |
| --------------------------- | ------------- | ------------ |
| Change in FM amount of Modulation Oscillator | Waveform fluctuates nonlinearly over time | Organic fluctuation |
| Pulser + Envelope connection | Generation of cycles without a sense of beat | Sense of time like “breathing” |
| Self-interference of Reverb reverberation | Opposite phase generation of overtones | Floating feeling/reverberant spread |

---

## Chapter 4: Possibility of solo performance and construction of acoustic space

The appeal of Easel is that the sound sculpture can be completed without any external effects.
By linking multiple modulations using Pulser as a trigger,
It is possible to create "generated minimal patterns" and "random rhythm structures."

### Case 2: Charles Cohen “Live at the Rotunda” (2014)

Legendary Philadelphia improviser **Charles Cohen** used the Buchla Music Easel for over 40 years.
At his live shows, the concept of tempo collapses, and Pulser expands and contracts like breathing.
Cohen said, ``Easel is a tool for sculpting time.''

In his performance, the waveform folding of the Complex Oscillator causes overtones to collapse and reproduce continuously,
It produces a sound that is as if an acoustic instrument were reconstructing itself.

### Sound technology analysis: Cohen's improvisational structure

<div class="mermaid">

graph TD
A[Pulser] -->|Irregular Trigger| B[Envelope]
B -->|CV Modulation| C[Complex Oscillator]
C -->|Audio| D[Wavefolder]
D -->|Audio| E[Reverb]
E -->|Stereo Out| F[Audience Space]

</div>

This asynchronous trigger structure allows the Easel to generate a "non-metered groove" on its own.
Cohen says that music arises just by "surrendering" yourself to the flow of current.

---

## Chapter 5: Contemporary Artists and Easel Inheritance

### Suzanne Ciani

→ The embodiment of sonic feminism.I entrust my physicality to Buchla's soft electric current.

### Todd Barton

→ As an educator, he explains Easel as "the point of contact between consciousness and machines."
“Don’t play it—listen to it playing you.”

### Charles Cohen

→ The extreme north of improvisation.A live performance is not about music, but about creating a place.
Even after his death, Buchla reprinted his patch as the "Cohen Program Card."

### Kaitlyn Aurelia Smith

→ Integrating Easel's philosophy with digital technology.Extending natural sound fluctuations to modern ambient music.

---

## Chapter 6: Technology and physicality - the act of “playing electric current”

Playing Music Easel isn't about flipping a switch;
**It is the act of relying on the reaction speed of an electric circuit**.
The pressure, humidity, and temperature of your fingertips affect the CV value and change the sound.

In other words, Easel is an instrument in which the human skin becomes the circuit.
The sounds that exist there are phenomena, not data.

In recent live performances, analog Easel operations are not converted to MIDI,
The movement to treat it as a pure current response is once again attracting attention.
This "anti-digital" trend is also a sign of bringing back physical reality to electronic music.

---

## Conclusion: The future as an orchestra

Easel is functionally small and expressively limitless.
The electric current flickering inside creates a "living sound" in synchronization with the performer's breathing.

As Charles Cohen said, "Easel is a lonely conversation partner"
As Suzanne Ciani has shown, "it is the organ that translates human emotions into electronic form."

In today's laptop-dominated live environment,
Buchla Music Easel remains a "solitary orchestra".
It holds the future of improvisation hidden within the smallest unit of circuitry.

---

## Appendix: Buchla Music Easel Chronology

<div class="mermaid">

timeline
title Buchla Music Easel Chronology
1963: Don Buchla begins development of the Buchla 100 series (same time as Moog)
1966 : Collaborative research with experimental musicians at San Francisco Tape Music Center
1973 : Music Easel (Model 208/218) introduced
1975 : First live performance by Suzanne Ciani and Buchla
1980: Charles Cohen starts improvised live performances using Easel
1990 : Easel re-evaluates in the underground experimental music scene
2013 : Easel reprint edition (BEMI) released
2014 : Charles Cohen “Live at the Rotunda” announced
2018 : Easel Command (208c) released
2022: Expansion of Buchla live movement by new generation artists

</div>

---

