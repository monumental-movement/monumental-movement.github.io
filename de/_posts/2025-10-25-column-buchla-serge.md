---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-serge.webp
lang: de
layout: post
permalink: /de/column-buchla-serge/
tags:
- Synth
- Buchla
- Techno
- Modular
- History
title: '[Kolumne] Buchla und Serge: Eine weitere Genealogie der elektronischen Akustik'
---


## „Einführung – Was ist modular?“


Text: mmr | Thema: Spirituelle Geschichte der modularen Synthesizer der Westküste. Wie die Ideen von Don Buchler und Serge Tocheny in das heutige Sounddesign übertragen wurden

Anfang der 1970er Jahre, Amerikas Westküste.
Es gab Leute, die das Studio für elektronische Musik ihrer Universität verließen und versuchten, **ein Gerät zur Klanggestaltung** zurück in ihre persönlichen kreativen Räume zu bringen.
Ihre Namen sind **Don Buchla** und **Serge Tcherepnin**.

Buchla und Serge werden oft als die sogenannten „Vorläufer modularer Synthesizer“ bezeichnet, aber sie zeichnen sich tatsächlich dadurch aus, dass sie eher philosophische als kommerzielle Instrumente entwickeln wollten.
Ihre Designphilosophie beinhaltete eine „antinormative“ Klangperspektive, die dem heutigen Eurorack, Max/MSP und sogar KI-basierter Musik gemeinsam ist.

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



## 1. Don Buchler: Poetik des elektronischen Klangs

### 1-1. Vom San Francisco Tape Music Center

Im Tape Music Center in San Francisco erkundeten Anfang der 1960er Jahre Künstler wie Morton Subotnick und Pauline Oliveros neue Beziehungen zwischen experimenteller Musik und Technologie.
Was sie suchten, war „ein Instrument, das keine Erweiterung des Klaviers oder der Gitarre war“.

Die **Buchla Series 100 (1963–1966)** erschien auf Anfrage von Subotnick.
Auf traditionelle musikalische Bedienbarkeit wurde bewusst verzichtet, etwa auf die Konfiguration der akustischen Schaltung mit Knöpfen und Patchkabeln sowie auf die Touch-Plate-Tastatur (eigentlich ein Spannungseingabegerät ohne Skala).

> „Keine schwarzen und weißen Tasten.“ – Don Buchla

### 1-2. Buchlas Philosophie: Performative Elektronik

Buchla entwarf Musikinstrumente als „ein Ökosystem, in dem Kontrolle und Erzeugung koexistieren“.
Der Klang kommt nicht direkt vom Körper des Darstellers, sondern wird durch das abstrakte Verhalten von Spannungsänderungen erzeugt.
Dadurch wird die Aufführung zu einem improvisatorischen „Akt“ und der Klang ist flüssig.

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

Diese Struktur symbolisiert Buchlas Weltanschauung, „Klang zu katalysieren, anstatt ihn zu manipulieren“.
Das Low Pass Gate (ein Element, das sowohl Lautstärke als auch Klangfarbe steuert) wurde später zu einem philosophischen Standardgerät in der Eurorack-Kultur.

---

## 2. Serge Tochenin: demokratisiertes Modul

### 2-1. Geburt von „The People’s Synthesizer“

In den späten 1970er Jahren war der junge Musiker Serge Tochenin von Don Buchlas Designphilosophie beeindruckt und während seines Studiums elektronischer Musik an der UCLA stellte er sich ein „Buchla-ähnliches Gerät vor, zu dem mehr Menschen Zugang haben könnten“.
Das ist **Serge Modular Music System (1974–)**.

Während Buchler maßgeschneiderte Maschinen für Künstler herstellte, ist Serge in der DIY-Kultur und der Universitätsgemeinschaft verwurzelt, mit dem Ethos „Öffnen Sie die Schaltpläne, damit jeder sie bauen kann“.
Diese Open-Source-Haltung war eine konzeptionelle Revolution, die der späteren Verbreitung von Eurorack vorausging.

### 2-2. Serges Philosophie: Patch-Programmierbarkeit

Serges Grundphilosophie ist „Ein Modul, viele Funktionen“**.
Mit anderen Worten: Die Idee besteht darin, dass ein einzelner Stromkreis je nach Anschlussart unendlich viele Betriebsarten haben kann.
Zum Beispiel der Dual Universal Slope Generator (allgemein bekannt als „DSG“)
- Umschlag
-LFO
- Auslöseverzögerung
- Uhrenteiler
- Chaos-Modul
Die Funktionalität ändert sich je nach Patch-Konfiguration.

Diese Philosophie setzt sich direkt in den heutigen Max/MSP-Patches, Reaktor Blocks und Euroracks Make Noise „Maths“ fort.

---

## 3. Vergleich von Buchla und Serge: Struktur und Ideologie

| Element | Buchla | Serge |
|------|---------|---------|
| Ausgangspunkt | Experimentelle Instrumente für Künstler | Bildung und DIY-Kultur |
| Betriebsphilosophie | Performativ (Klang als Aktion) | Funktional (Klang als Struktur) |
| Funktionelles Design | Dedizierte Modulkonfiguration | Kombination allgemeiner Module |
| Kontrolle | Abstrakter Spannungsbetrieb | Konkrete Signalmanipulation |
| Akustische Trends | Organisch, dynamisch, geschmeidig | Lineare, klare, schnelle Reaktion |
| Kulturelle Einflüsse | Kunstklang, Installation | Noise, Techno, elektronische DIY-Musik |

---

## 4. Chronologie der Technologie

| Jahr | Veranstaltungen | Notizen |
|----|--------|------|
| 1963 | Die Entwicklung der Buchla-Serie 100 beginnt | Erstes Modul im Auftrag von Subotnick |
| 1966 | Debüt des Buchla Music Easel-Prototyps | Der Begründer tragbarer Synthesizer |
| 1974 | Ankündigung von Serge Modular | Slogan „Volkssynthesizer“ |
| 1980 | Wir stellen vor: Serge Dual Slope Generator | Abgeschlossene Patch-Philosophie |
| 1990er Jahre | Serge-Neubewertungszeitraum | Analoges Revival und Rückfall |
| 2004 | Eurorack-Boom beginnt | Geerbt von Doepfer, Make Noise usw. |
| 2020er | Buchla USA / Serge Nachdruck | Rekontextualisierung des ursprünglichen Gedankens |

---

## 5. Auswirkungen auf die modulare Kultur

Die Philosophie von Buchler und Sarge definierte Klang selbst als „sozialen Akt“ neu.
Mit anderen Worten, er verlagerte seinen Fokus vom „Instrument“ auf die „Umgebung“ und die „Schnittstelle“.

Die modularen „unendlichen Kombinationen“ von Eurorack sind nicht einfach die Freiheit der Teile, sondern die Neukonfiguration der Bedeutung.
Buchlas „Körperlichkeit“ und Serges „Strukturalität“ sind verschmolzen, und die heutige elektronische Musik wird immer „dezentrischer“.

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

## 6. Anschluss an die Moderne: Zwischen Algorithmen und dem Körper

Der Buchla/Serge-Geist ist in Max/MSP, VCV Rack und sogar KI-generierten Musiktools lebendig und lebendig.
Es handelt sich nicht nur um eine „Kombination von Modulen“, sondern um einen künstlerischen Rahmen, der Zeit, Raum, Körper und Wahrscheinlichkeit verbindet.

Modulare Synthesizer sind nicht nur „Werkzeuge“ zum Erstellen von Sounds;
Es ist ein Medium, das „Ereignisse“ erzeugt, die zwischen Geräuschen und Menschen stattfinden.
Die Designphilosophie von Buchla und Serge ist weiterhin der Keim dieser Medienphilosophie.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GpCdodqTYtE?si=lIQMClxtxuqhBIvc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/QBVCa3RaR0c?si=VWdNaHjNBMK-r8Mj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
---

## Fazit – Poetik der „Steuerspannung“

Don Buchler soll dies vor seinem Tod gesagt haben.
> „Spannung ist keine Zahl – sie ist eine Geste.“

Sarge sagt auch.
> „Jeder Patch ist eine Komposition.“

Für sie ist Spannung nicht nur ein Signal;
**Es war „eine poetische Sprache, die den menschlichen Willen und Maschinen verbindet.“**

Auch jetzt im Jahr 2025 lauschen wir weiterhin der Poesie dieser Spannung.

---


