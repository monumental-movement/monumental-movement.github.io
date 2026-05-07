---
author: mmr
categories:
- Column
date: 2026-04-11 00:00:05 +0900
image: ../assets/images/column-lunetta-cmos.webp
lang: de
layout: post
permalink: /de/column-lunetta-cmos/
tags:
- CMOS
- Lunetta
- DIY
title: '[Kolumne] Die Welt von CMOS Synth und Lunetta: Die Ästhetik primitiver elektronischer
  Musik, gespielt von Logikschaltungen'
---



## Was ist CMOS Synth?

Text: mmr｜Thema: Der Moment, in dem Logikschaltungen zu Musik werden – Die Welt der primitiven elektronischen Akustik, dargestellt von CMOS Synth und Lunetta

Der sogenannte Lunetta Synth, ein DIY-Synthesizer mit CMOS-Logik-ICs, ist eine Kultur, die im Gegensatz zur heutigen anspruchsvollen elektronischen Musikumgebung Klänge aus extrem einfachen und primitiven Schaltkreisen erzeugt. In diesem Artikel werden seine Ursprünge, seine Struktur, seine akustischen Eigenschaften und seine moderne Neubewertung auf der Grundlage historischer Fakten und technischer Perspektiven erörtert.

### Der Moment, in dem der Logik-IC zum Klang wird

CMOS Synth ist ein allgemeiner Begriff für Synthesizer, die mithilfe von CMOS-Logik-ICs, die ursprünglich als digitale Schaltkreise konzipiert waren, Klang erzeugen. Diese ICs sind ursprünglich für Berechnungen und Signalverarbeitung gedacht, aber durch die Entwicklung einer Takt- und Rückkopplungsstruktur können sie oszillieren und hörbare Töne erzeugen.

Zu den typischen ICs gehören die folgenden.

* 40106: Schmitt-Trigger-Inverter
*4040: Binärzähler
* 4017: Dekadenzähler
*4070: XOR-Gatter

Diese können einzeln Klänge erzeugen, in Kombination können jedoch komplexe Rhythmen und Muster erzeugt werden.

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



### Definition von Lunetta Synth

Lunetta Synth ist ein Name, der vom Namen des italienischen Heimwerkerherstellers Stanley Lunetta abgeleitet ist und sich speziell auf ein System mit den folgenden Eigenschaften bezieht.

* Besteht nur aus CMOS-Logik-ICs
*Grundsätzlich keine analogen Filter oder VCA verwenden
*Kostenlose Verbindung durch Patchen
* Tonänderung aufgrund der Versorgungsspannung

Es sind diese Zwänge, die einen einzigartigen Sound und eine einzigartige Kultur geschaffen haben.

> CMOS Synth ist ein Bereich, in dem elektronische Schaltkreise selbst zu Musikinstrumenten und nicht zu Musikgeräten werden.

---

## Technische Grundlagen: Warum kommt Ton heraus?

### Mechanismus der Schwingung

CMOS-Inverter haben die Eigenschaft, dass Ein- und Ausgang invertiert sind. Durch die Kombination mit einem Widerstand und einem Kondensator entsteht ein selbstschwingender Schaltkreis (Oszillator).

<div class="mermaid">
flowchart LR
A[入力] --> B[インバータ]
B --> C[出力]
C --> D[RC回路]
D --> A
</div>

Diese Schleife bewirkt, dass sich die Spannung periodisch ändert und eine Rechteckwelle erzeugt.

### Frequenzteilung durch Zähler

Ein Zähler-IC teilt den Eingangstakt und erzeugt Signale mit mehreren unterschiedlichen Perioden. Dies führt zu folgenden Effekten.

* Generierung von Rhythmusmustern
* Polyrhythmische Struktur
* Pseudomelodie

<div class="mermaid">
flowchart TD
CLK[クロック] --> C1[1/2]
CLK --> C2[1/4]
CLK --> C3[1/8]
CLK --> C4[1/16]
</div>

### Klangtransformation mittels logischer Operationen

Logische Operationen wie XOR und AND verändern die Beziehung zwischen Signalen. Dadurch entsteht selbst bei einer einfachen Wellenform ein komplexes Spektrum.

*XOR: Erhöht die Obertöne und macht Rauschen
* UND: Torartiges intermittierendes Geräusch
*ODER: Dichteerhöhung aufgrund von Überlappung

> Die Tonerzeugung basiert eher auf logischen als auf analogen Operationen.

---

## Historischer Hintergrund

### Die Schnittstelle zwischen digitalen Schaltkreisen und Musik

In den 1970er Jahren wurden CMOS-ICs als kostengünstige elektronische Komponenten mit geringem Stromverbrauch populär. Etwa zur gleichen Zeit weiteten sich die Experimente in der elektronischen Musik schrittweise von analog auf digital aus.

Die Idee, CMOS als Schallquelle zu verwenden, war jedoch nicht weit verbreitet und existierte nur als Versuch einiger Experimentatoren.

### Verbindung zur DIY-Kultur

In den frühen 2000er Jahren wurde die CMOS-Klangerzeugung durch Internetforen und persönliche Websites wiederentdeckt. Folgende Faktoren sind besonders wichtig.

* Teileverfügbarkeit
*Einfachheit der Schaltung
*Niedrige Kosten
* Kann nur durch Löten hergestellt werden

In diesem Sinne verbreitete sich das Konzept von „Lunetta Synth“ und etablierte sich in der DIY-Community.

### Beziehung zu modularen Synthesizern

Lunetta hat eine andere Philosophie als modulare Synthesizer, sie überschneiden sich jedoch in den folgenden Punkten.

* Strukturelle Veränderungen durch Patching
* Modularer Aufbau
* Experimentelle Klangerzeugung

Der entscheidende Unterschied besteht jedoch darin, dass der Fokus auf logischen Signalen und nicht auf der Spannungssteuerung liegt.

> Lunetta ist keine modulare Vereinfachung, sondern eine völlig andere Weiterentwicklung.

---

## Akustische Eigenschaften

### Dominanz von Rechteckwellen

Die Grundwellenform von CMOS Synth ist eine Rechteckwelle. Daraus ergeben sich folgende Eigenschaften:

* Starke harmonische Komponenten
* Digitale harte Textur
* Rhythmische Diskontinuität

### Instabilität und Kontingenz

Das Verhalten von CMOS-Schaltkreisen ändert sich je nach Versorgungsspannung, Temperatur und Verkabelung.

* Uhrschwankung
* Aperiodisches Muster
* Chaotischer Rhythmus

Dies führt zu Musik mit geringer Reproduzierbarkeit.

### Verbindung außerhalb der Audioreichweite

Durch die Teilung des Hochfrequenztaktes wird der Vorgang des Absinkens in den hörbaren Bereich selbst zu einer musikalischen Struktur.

<div class="mermaid">
flowchart LR
HF[高周波] --> DIV[分周]
DIV --> AUD[可聴音]
</div>

> Musik wird nicht generiert, sondern aus einer Frequenzhierarchie extrahiert.

---

## Schaltungsdesign und -praxis

### Grundkonfiguration

Die einfachste Lunetta hat die folgende Konfiguration.

*Oszillator (40106)
* Zähler (4040)
* Ausgangsmischung

Dadurch werden Signale mit mehreren Perioden gleichzeitig ausgegeben.

### Kultur patchen

Die Besonderheit von Lunetta liegt nicht in der festen Verkabelung, sondern in der Verbindungsänderung mithilfe von Jumpern und Patchkabeln.

* Ein- und Ausgänge frei verbinden
* Erzeugen einer Feedbackschleife
* Unvorhersehbares Verhalten

<div class="mermaid">
flowchart TD
A[OSC] --> B[COUNTER]
B --> C[LOGIC]
C --> A
</div>

### Bedeutung der Versorgungsspannung

CMOS-ICs arbeiten bei etwa 3 V bis 15 V, aber der Klang ändert sich je nach Spannung.

* Hochspannung: hoher Geschwindigkeits-/Höhenbereich
* Niederspannung: niedrige Geschwindigkeit/Verzerrung

Als Parameter fungiert die Spannung selbst.

> Durch das Brechen der Stabilität der Schaltung entsteht Musikalität.

---

## Zeitleiste: Bereitstellung von CMOS Synth und Lunetta

### 1970er-1990er Jahre

* 1970er Jahre: Popularisierung von CMOS-ICs
* 1980er Jahre: Mainstreaming digitaler Tonquellen
* 1990er Jahre: Fragmentierte Praxis elektronischer DIY-Musik

### 2000er Jahre

* Frühzeitige gemeinsame Nutzung von Schaltkreisen im Internet
* Popularisierung des Namens Lunetta Synth
* Aktivierung der Einzelproduktion

### Seit 2010

* Neubewertung parallel zur Wiederbelebung des Moduls
* Workshops und Gemeinschaftsaufbau
* Entwicklung als Kunstwerk

<div class="mermaid">
flowchart LR
A[1970s CMOS普及] --> B[1990s 実験]
B --> C[2000s 再発見]
C --> D[2010s 文化化]
</div>

> Schaltkreise, die ein Nebenprodukt der Technik waren, verselbstständigten sich als Kultur.

---

## Position in der Neuzeit

### Beziehung zu Lärm/experimenteller Musik

Lunetta hat eine hohe Affinität zu den folgenden Genres.

* Lärmmusik
* Industriell
* Experimentelle elektronische Musik

Dies liegt an der Betonung der Kontingenz statt der Kontrolle.

### Pädagogischer Wert

CMOS Synth eignet sich auch als Einstieg in die Elektrotechnik.

* Logikschaltungen verstehen
* Erleben Sie das Schwingungsprinzip
* Visualisierung der Beziehung zwischen Schall und Elektrizität

### Schaltungen als Kunst

Der Rundgang selbst wird zum visuellen Objekt und wird gleichzeitig als Installation genutzt.

* Visualisierung mit LED
* Synchronisation von Ton und Licht
* Ästhetik des physischen Layouts

> Lunetta liegt an der Schnittstelle von Musik, Technik und Kunst.

---

## Fazit: Warum jetzt CMOS Synth?

Im Gegensatz zu den heutigen hochoptimierten Musikproduktionsumgebungen ist CMOS Synth ineffizient und unkontrollierbar. Allerdings führt gerade diese Einschränkung zu unvorhersehbaren Klängen und Strukturen.

* Einfache Schaltung
*Komplizierte Ergebnisse
* Nichtreproduzierbarkeit

Dies sind Elemente, die digitale Musik tendenziell verliert, und darin liegt der Wert von Lunetta.

> Primitive Schaltkreise werfen modernste Fragen auf.

---
