---
author: mmr
categories:
- Column
date: 2026-04-11 00:00:05 +0900
image: ../assets/images/column-lunetta-cmos.webp
lang: en
layout: post
tags:
- CMOS
- Lunetta
- DIY
title: '[Column] The world of CMOS Synth and Lunetta: The aesthetics of primitive
  electronic music played by logic circuits'
---



## What is CMOS Synth?

Text: mmr｜Theme: The moment when logic circuits become music ─ The world of primitive electronic acoustics depicted by CMOS Synth and Lunetta

The so-called Lunetta Synth, a DIY synthesizer using CMOS logic ICs, is a culture that generates sounds from extremely simple and primitive circuits, in contrast to today's sophisticated electronic music environment. This article will discuss its origins, structure, acoustic characteristics, and modern re-evaluation based on historical facts and technical perspectives.

### The moment when logic IC becomes sound

CMOS Synth is a general term for synthesizers that generate sound using CMOS logic ICs originally designed as digital circuits. These ICs are originally intended for calculations and signal processing, but by devising a clock and feedback structure, they can oscillate and generate audible sounds.

Typical ICs include the following.

* 40106: Schmitt trigger inverter
*4040: Binary counter
* 4017: Decade counter
*4070: XOR gate

These can produce sounds on their own, but when combined, complex rhythms and patterns can be created.

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



### Definition of Lunetta Synth

Lunetta Synth is a name derived from the name of Italian DIY builder Stanley Lunetta, and specifically refers to a system with the following characteristics.

* Consisting only of CMOS logic ICs
*Basically do not use analog filters or VCA
*Free connection by patching
* Tone change due to power supply voltage

It is these constraints that have created a unique sound and culture.

> CMOS Synth is a field in which electronic circuits themselves become musical instruments, rather than musical equipment.

---

## Technical Basics: Why does sound come out?

### Mechanism of oscillation

CMOS inverters have the characteristic that the input and output are inverted. By combining this with a resistor and a capacitor, a self-oscillating circuit (oscillator) is constructed.

<div class="mermaid">
flowchart LR
A[input] --> B[inverter]
B --> C[output]
C --> D[RC circuit]
D --> A
</div>

This loop causes the voltage to change periodically, generating a square wave.

### Frequency division by counter

A counter IC divides the input clock and generates signals with multiple different periods. This provides the following effects.

* Generation of rhythm patterns
* Polyrhythm structure
* pseudo melody

<div class="mermaid">
flowchart TD
CLK[clock] --> C1[1/2]
CLK --> C2[1/4]
CLK --> C3[1/8]
CLK --> C4[1/16]
</div>

### Sound transformation using logic operations

Logical operations such as XOR and AND change the relationship between signals. This creates a complex spectrum even with a simple waveform.

*XOR: Increases overtones and becomes noisy
* AND: Gate-like intermittent sound
*OR: Density increase due to overlap

> Sound generation is based on logical operations rather than analog.

---

## Historical background

### The interface between digital circuits and music

In the 1970s, CMOS ICs became popular as low-power, inexpensive electronic components. Around the same time, experiments in electronic music gradually expanded from analog to digital.

However, the idea of ​​using CMOS as a sound source was not mainstream, and existed as an attempt by some experimentalists.

### Connection with DIY culture

In the early 2000s, CMOS sound creation was rediscovered through Internet forums and personal sites. The following factors are particularly important.

* Parts availability
*Circuit simplicity
*Low cost
* Can be manufactured by soldering only

In this vein, the concept of "Lunetta Synth" spread and became established in the DIY community.

### Relationship with modular synths

Lunetta has a different philosophy from modular synths, but they intersect in the following points.

* Structural changes due to patching
* Modular design
* Experimental sound generation

However, the decisive difference is that the focus is on logic signals rather than voltage control.

> Lunetta is not a modular simplification, but a completely different evolution.

---

## Acoustic characteristics

### Dominance of square waves

The basic waveform of CMOS Synth is a square wave. This results in the following characteristics:

* Strong harmonic components
* Digital hard texture
* Rhythmic discontinuity

### Instability and contingency

The behavior of CMOS circuits changes depending on the power supply voltage, temperature, and wiring.

* Clock fluctuation
* Aperiodic pattern
* Chaotic rhythm

This results in music with low reproducibility.

### Connection outside the audio range

By dividing the high frequency clock, the process of dropping it into the audible range itself becomes a musical structure.

<div class="mermaid">
flowchart LR
HF[high frequency] --> DIV[Frequency division]
DIV --> AUD[audible sound]
</div>

> Music is not generated, but extracted from a hierarchy of frequencies.

---

## Circuit design and practice

### Basic configuration

The simplest Lunetta has the following configuration.

*Oscillator (40106)
* Counter (4040)
* Output mixing

As a result, signals having multiple periods are output simultaneously.

### Patching culture

Lunetta's feature is not fixed wiring, but connection changes using jumpers and patch cables.

* Freely connect inputs and outputs
* Generating a feedback loop
* Unpredictable behavior

<div class="mermaid">
flowchart TD
A[OSC] --> B[COUNTER]
B --> C[LOGIC]
C --> A
</div>

### Importance of power supply voltage

CMOS ICs operate at around 3V to 15V, but the sound changes depending on the voltage.

* High voltage: high speed/treble range
* Low voltage: low speed/distortion

The voltage itself acts as a parameter.

> Breaking the stability of the circuit creates musicality.

---

## Chronology: Deployment of CMOS Synth and Lunetta

### 1970s-1990s

* 1970s: Popularization of CMOS ICs
* 1980s: Mainstreaming of digital sound sources
* 1990s: Fragmented practice of DIY electronic music

### 2000s

* Early circuit sharing on the Internet
* Popularization of the name Lunetta Synth
* Activation of individual production

### Since 2010s

* Re-evaluation in parallel with modular revival
* Workshops and community building
* Development as a work of art

<div class="mermaid">
flowchart LR
A[1970s CMOS spread] --> B[1990s experiment]
B --> C[2000s rediscovery]
C --> D[2010s culturalization]
</div>

> Circuits, which were a by-product of technology, became independent as a culture.

---

## Position in modern times

### Relationship with noise/experimental music

Lunetta has a high affinity with the following genres.

* Noise music
* Industrial
* Experimental electronic music

This is due to the emphasis on contingency rather than control.

### Educational value

CMOS Synth is also effective as an introduction to electronic engineering.

* Understanding logic circuits
* Experience the oscillation principle
* Visualization of the relationship between sound and electricity

### Circuits as art

The circuit itself becomes a visual object and is also used as an installation.

* Visualization with LED
* Synchronization of sound and light
* Physical layout aesthetics

> Lunetta sits at the interface of music, engineering, and art.

---

## Conclusion: Why CMOS Synth now?

In contrast to today's highly optimized music production environments, CMOS Synth is inefficient and uncontrollable. However, this very restriction creates unpredictable sounds and structures.

* Simple circuit
*Complicated results
* Non-reproducibility

These are elements that digital music tends to lose, and that"s where Lunetta"s value lies.

> Primitive circuits pose the most modern questions.

---
