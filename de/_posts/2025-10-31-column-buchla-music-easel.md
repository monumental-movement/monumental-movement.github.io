---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-music-easel.webp
lang: de
layout: post
permalink: /de/column-buchla-music-easel/
tags:
- Buchla
- Modular
- Ambient
title: '[Kolumne] Buchla Music Easel und die Philosophie der „Solitary Performance“:
  Improvisation mit analogen Synthesizern neu definieren'
---


## Einführung: Was ist Buchla Music Easel?

Text: mmr｜Thema: Musikstaffelei, die auch in der Neuzeit von vielen Live-Künstlern als „kleinstes Orchester, das alleine gespielt werden kann“ gepriesen wird


Die **Buchla Music Easel**, die 1973 erschien, ist eine tragbare Version der berühmten analogen modularen **Buchla 200-Serie**.
Der Designer Don Buchla nannte das Instrument eine „tragbare Kompositionsumgebung“.
Es handelte sich nicht nur um ein kleines Modul, sondern um ein „persönliches improvisiertes Gerät“.

> „Easel ist eine Klangleinwand. Sie können die Linien, die der Spieler gerade zeichnet, nicht speichern.“
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

## Kapitel 1: Don Buchla und die „Anti-Moog“-Philosophie

In den frühen 1960er Jahren entstanden in Ost- und Westamerika zwei große Trends in der Entwicklung elektronischer Musikinstrumente.
Moog im Osten und Buchla im Westen.
Buchlas Ziel war es, Klang zu „erzeugen“, anstatt ihn zu „kontrollieren“.
Anstelle einer Tastatur wurde eine Touch-Plate verwendet, und der Schwerpunkt der Darbietung lag auf **Änderungsrate und Kontingenz** und nicht auf der Tonhöhe.

Seine Philosophie wurde in die spätere Musikstaffelei übernommen.
Staffelei ist ein Instrument, mit dem Menschen mit elektronischen Schaltkreisen agieren können, und dort herrscht eher die Einstellung eines „Co-Autors“ statt eines „Darstellers = Controllers“.

### Technische Analyse: Zusammenhang zwischen Wellenform und Tastempfindung

Buchla meinte, dass „Wellenformmanipulation = taktile Erfahrung“ sei.
Die folgende Abbildung ist ein vereinfachtes Modell der Beziehung zwischen FM (Frequenzmodulation) und der Wellenformausgabe im Complex Oscillator.

<div class="mermaid">

graph TD
A[Modulation Oscillator] -->|FM Signal| B[Complex Oscillator]
B -->|Wavefolded Output| C[Audio Out]
B --> D[Harmonic Timbre CV]
D -->|Control Voltage| B

</div>

Aufgrund dieser Verbindung hat eine einfache Sinuswelle eine harmonische Struktur und die kleinsten Berührungen während des Auftritts spiegeln sich sofort in der Akustik wider.

---

## Kapitel 2: Struktur und Philosophie von Music Easel

Music Easel besteht aus zwei Hauptblöcken:

- **Buchla 208 Stored Program Sound Source**
- **Buchla 218 Touch-Tastatur-Controller**

### Signalflussdiagramm (Meerjungfrau)

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

Diese Struktur ermöglicht es Ihnen, die Takterzeugung → Modulation → Tonausgabe** ganz von alleine abzuschließen.
Easel selbst fungiert als „komplettes Musiksystem“, ohne dass externe Geräte erforderlich sind.

### Technische Merkmale

* **Komplexer Oszillator**: Wellenformfaltung, FM, AM möglich.
* **Impulsgeber**: Erzeugt periodische Impulse, dient als Uhr.
* **Hüllkurve**: Automatisch gesteuert, getornt, schleifbar.
* **Reverb**: Natürlicher Nachhall mit Federhall.

Die Idee, die diese vereint, ist nicht „Portabilität“, sondern „Improvisation“, und das Zentrum der Musikproduktion hat sich vom „Denken“ zum „taktilen Empfinden“ verlagert.

---

## Kapitel 3: Staffelei als Live-Instrument

### Fall 1: Suzanne Ciani „Easel Sessions“ (2016–)

Die legendäre elektronische Musikerin **Suzanne Ciani** startete in den 2010er Jahren ihre Solo-Live-Serie „Easel Sessions“ bei Easel.
Sie verzichtet auf Laptops und tritt ausschließlich auf der Staffelei auf.
Bei der Live-Aufführung ändert sich die Tonhöhe sanft mit dem Druck der Hände und die FM-Modulation schwankt organisch.
Ciani sagt: „Buchla ist ein Ateminstrument.“

Klanglich erzeugt Easels **asynchrone Modulation** einen Fluss von Obertönen, der durch den Raum zu schweben scheint.
Beim Publikum entsteht die Illusion, dass „die Melodie selbst gespielt wird“.

### Wellenformanalyse: Merkmale der Improvisationsstruktur

| Elemente | Technische Punkte | Höreindrücke |
| ------------ | ------------- | ------------ |
| Änderung des FM-Anteils des Modulationsoszillators | Die Wellenform schwankt im Laufe der Zeit nichtlinear | Organische Fluktuation |
| Pulser + Umschlagverbindung | Erzeugung von Zyklen ohne Taktgefühl | Zeitgefühl wie „Atmen“ |
| Selbstinterferenz des Hall-Nachhalls | Gegenphasige Erzeugung von Obertönen | Schwebendes Gefühl/hallende Ausbreitung |

---

## Kapitel 4: Möglichkeit des Soloauftritts und Konstruktion des akustischen Raums

Der Reiz von Easel besteht darin, dass die Klangskulptur ohne äußere Einflüsse fertiggestellt werden kann.
Durch die Verknüpfung mehrerer Modulationen mit Pulser als Trigger,
Es ist möglich, „generierte Minimalmuster“ und „zufällige Rhythmusstrukturen“ zu erstellen.

### Fall 2: Charles Cohen „Live at the Rotunda“ (2014)

Der legendäre Philadelphia-Improvisator **Charles Cohen** nutzte die Buchla Music Easel über 40 Jahre lang.
Bei seinen Live-Shows bricht das Konzept des Tempos zusammen und Pulser dehnt sich aus und zieht sich zusammen wie beim Atmen.
Cohen sagte: „Staffelei ist ein Werkzeug zur Gestaltung der Zeit.“

In seiner Performance führt die Wellenformfaltung des Komplexen Oszillators dazu, dass Obertöne zusammenbrechen und sich kontinuierlich reproduzieren.
Es erzeugt einen Klang, der so ist, als würde sich ein akustisches Instrument selbst rekonstruieren.

### Klangtechnologieanalyse: Cohens Improvisationsstruktur

<div class="mermaid">

graph TD
A[Pulser] -->|Irregular Trigger| B[Envelope]
B -->|CV Modulation| C[Complex Oscillator]
C -->|Audio| D[Wavefolder]
D -->|Audio| E[Reverb]
E -->|Stereo Out| F[Audience Space]

</div>

Diese asynchrone Triggerstruktur ermöglicht es dem Easel, selbst einen „nicht gemessenen Groove“ zu erzeugen.
Cohen sagt, dass Musik einfach dadurch entsteht, dass man sich dem Fluss des Stroms „hingibt“.

---

## Kapitel 5: Zeitgenössische Künstler und Staffelei-Erbe

### Suzanne Ciani

→ Die Verkörperung des Klangfeminismus. Ich vertraue meine Körperlichkeit Buchlas sanftem elektrischem Strom an.

### Todd Barton

→ Als Pädagoge erklärt er Easel als „den Kontaktpunkt zwischen Bewusstsein und Maschinen“.
„Spiel es nicht – hör zu, wie es dich spielt.“

###Charles Cohen

→ Der äußerste Norden der Improvisation. Bei einem Live-Auftritt geht es nicht um Musik, sondern darum, einen Ort zu schaffen.
Auch nach seinem Tod druckte Buchla seinen Patch als „Cohen Program Card“ nach.

### Kaitlyn Aurelia Smith

→ Integration der Easel-Philosophie mit digitaler Technologie. Erweiterung natürlicher Klangschwankungen auf moderne Ambient-Musik.

---

## Kapitel 6: Technologie und Körperlichkeit – der Akt des „Spielens von elektrischem Strom“

Beim Spielen von Music Easel geht es nicht darum, einen Schalter umzulegen;
**Es ist der Vorgang, sich auf die Reaktionsgeschwindigkeit eines Stromkreises zu verlassen**.
Der Druck, die Luftfeuchtigkeit und die Temperatur Ihrer Fingerspitzen beeinflussen den CV-Wert und verändern den Klang.

Mit anderen Worten: Staffelei ist ein Instrument, bei dem die menschliche Haut zum Schaltkreis wird.
Die dort existierenden Geräusche sind Phänomene, keine Daten.

Bei neueren Live-Auftritten werden analoge Easel-Bedienungen nicht in MIDI konvertiert,
Der Trend, es als reine aktuelle Reaktion zu betrachten, erregt erneut Aufmerksamkeit.
Dieser „antidigitale“ Trend ist auch ein Zeichen dafür, die physische Realität in die elektronische Musik zurückzubringen.

---

## Fazit: Die Zukunft als Orchester

Die Staffelei ist funktional klein und der Ausdruckskraft grenzenlos.
Der im Inneren flackernde elektrische Strom erzeugt einen „lebendigen Klang“ im Takt der Atmung des Künstlers.

Wie Charles Cohen sagte: „Staffelei ist ein einsamer Gesprächspartner.“
Wie Suzanne Ciani gezeigt hat, „ist es das Organ, das menschliche Emotionen in elektronische Form übersetzt.“

In der heutigen, von Laptops dominierten Live-Umgebung
Buchla Music Easel bleibt ein „Einzelorchester“.
Es birgt die Zukunft der Improvisation verborgen in der kleinsten Schaltkreiseinheit.

---

## Anhang: Buchla Music Easel Chronologie

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
