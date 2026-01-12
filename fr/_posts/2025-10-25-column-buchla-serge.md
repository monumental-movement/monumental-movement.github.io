---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-serge.webp
lang: fr
layout: post
permalink: /fr/column-buchla-serge/
tags:
- Synth
- Buchla
- Techno
- Modular
- History
title: '[Chronique] Buchla et Serge : Une autre généalogie de l''acoustique électronique'
---


## « Introduction – Qu'est-ce que le modulaire ? »


Texte : mmr | Thème : Histoire spirituelle des synthés modulaires de la côte Ouest. Comment les idées de Don Buchler et Serge Tocheny ont été transposées dans la conception sonore d'aujourd'hui

Début des années 1970, côte ouest américaine.
Il y a des gens qui ont quitté le studio de musique électronique de leur université et ont essayé de réintégrer **un appareil de conception sonore** dans leurs espaces de création personnels.
Leurs noms sont **Don Buchla** et **Serge Tcherepnin**.

Buchla et Serge sont souvent considérés comme les « ancêtres des synthés modulaires », mais ils se distinguent en réalité par le fait qu'ils ont cherché à créer des outils philosophiques plutôt que des instruments commerciaux.
Leur philosophie de conception contenait une perspective sonore « anti-normative » qui est commune à la musique générée aujourd'hui par Eurorack, Max/MSP et même par l'IA.

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



## 1. Don Buchler : Poétique du son électronique

### 1-1. De San Francisco Tape Music Center

Au Tape Music Center de San Francisco, au début des années 1960, des artistes comme **Morton Subotnick** et **Pauline Oliveros** exploraient de nouvelles relations entre la musique expérimentale et la technologie.
Ce qu'ils recherchaient, c'était «un instrument qui ne soit pas une extension du piano ou de la guitare».

La **Série Buchla 100 (1963-1966)** est apparue en réponse à la demande de Subotnick.
L'opérabilité musicale traditionnelle a été intentionnellement évitée, comme la configuration du circuit acoustique utilisant des boutons et des câbles de raccordement, et le clavier à plaque tactile (en fait un dispositif d'entrée de tension sans échelle).

> "Pas de touches noires et blanches." -Don Buchla

### 1-2. La philosophie de Buchla : l'électronique performative

Buchla a conçu les instruments de musique comme « un écosystème dans lequel coexistent contrôle et génération ».
Le son ne provient pas directement du corps de l'interprète, mais est généré par le comportement abstrait des changements de tension.
La performance devient alors un « acte » d’improvisation et le son est fluide.

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

Cette structure symbolise la vision du monde de Buchla consistant à « catalyser le son plutôt que de le manipuler ».
Le Low Pass Gate (un élément qui contrôle à la fois le volume et le timbre) est devenu plus tard un dispositif philosophique standard dans la culture Eurorack.

---

## 2. Serge Tochenin : module démocratisé

### 2-1. Naissance du « Synthétiseur du peuple »

À la fin des années 1970, le jeune musicien Serge Tochenin a été impressionné par la philosophie de conception de Don Buchla et, alors qu'il étudiait la musique électronique à l'UCLA, il a imaginé un « appareil de type Buchla auquel davantage de gens pourraient avoir accès ».
Il s'agit du **Serge Modular Music System (1974–)**.

Alors que Buchler créait des machines personnalisées pour les artistes, Serge est enraciné dans la culture du bricolage et dans la communauté universitaire, avec une philosophie consistant à « ouvrir les schémas pour que tout le monde puisse les construire ».
Cette attitude open source était une révolution conceptuelle qui a précédé la diffusion ultérieure d'Eurorack.

### 2-2. La philosophie de Serge : Programmabilité des Patchs

La philosophie fondamentale de Serge est **« Un module, plusieurs fonctions »**.
Autrement dit, l’idée est qu’un seul circuit peut avoir une infinité de modes de fonctionnement selon la manière dont il est connecté.
Par exemple, le Dual Universal Slope Generator (communément appelé « DSG »)
- enveloppe
-LFO
- délai de déclenchement
- diviseur d'horloge
-Module Chaos
La fonctionnalité change en fonction de la configuration du correctif.

Cette philosophie se poursuit directement dans les correctifs Max/MSP actuels, les Reaktor Blocks et les « Maths » Make Noise d'Eurorack.

---

## 3. Comparaison de Buchla et Serge : structure et idéologie

| Élément | Bouchla | Serge |
|------|---------|---------|
| Point de départ | Instruments expérimentaux pour artistes | Éducation et culture du bricolage |
| Philosophie opérationnelle | Performatif (le son comme action) | Fonctionnel (le son comme structure) |
| Conception fonctionnelle | Configuration du module dédié | Combinaison de modules à usage général |
| Contrôle | Fonctionnement en tension abstraite | Manipulation concrète du signal |
| Tendances acoustiques | Organique, dynamique, fluide | Réponse linéaire, claire et rapide |
| Influences culturelles | Art sonore, installation | Noise, techno, musique électronique DIY |

---

## 4. Chronologie technologique

| Année | Événements | Remarques |
|----|--------|------|
| 1963 | Début du développement de la Buchla Series 100 | Premier modulaire commandé par Subotnick |
| 1966 | Début du prototype du Buchla Music Easel | Le fondateur des synthés portables |
| 1974 | Annonce modulaire Serge | Slogan « Synthétiseur populaire » |
| 1980 | Présentation du générateur à double pente Serge | Philosophie du patch terminé |
| années 1990 | Serge Période de réévaluation | Reprise analogique et rechute |
| 2004 | Le boom de l'Eurorack commence | Hérité de Doepfer, Make Noise, etc. |
| Années 2020 | Buchla USA / Serge réimpression | Recontextualisation de la pensée originale |

---

## 5. Impact sur la culture modulaire

La philosophie de Buchler et Sarge a redéfini le son comme un « acte social ».
En d’autres termes, il a déplacé son attention de « l’instrument » vers « l’environnement » et « l’interface ».

Les « combinaisons infinies » modulaires d'Eurorack ne sont pas simplement la liberté des pièces, mais la reconfiguration même du sens.
La « physicalité » de Buchla et la « structuralité » de Serge ont fusionné, et la musique électronique d'aujourd'hui devient de plus en plus « décentrique ».

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

## 6. Se connecter à l'ère moderne : entre algorithmes et corps

L’esprit Buchla/Serge est bien vivant dans Max/MSP, VCV Rack et même dans les outils musicaux générés par l’IA.
Il ne s'agit pas simplement d'une « combinaison de modules », mais d'un cadre artistique qui relie le temps, l'espace, le corps et les probabilités.

Les synthés modulaires ne sont pas de simples « outils » pour créer des sons ;
C'est un médium qui génère des « événements » qui se produisent entre les sons et les personnes.
La philosophie du design de Buchla et Serge continue d'être le germe de cette philosophie médiatique.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GpCdodqTYtE?si=lIQMClxtxuqhBIvc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/QBVCa3RaR0c?si=VWdNaHjNBMK-r8Mj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
---

## Conclusion — Poétique de la « tension de contrôle »

Don Buchler aurait dit cela avant sa mort.
> "La tension n'est pas un nombre, c'est un geste."

Sarge dit également.
> « Chaque patch est une composition. »

Pour eux, la tension n’est pas seulement un signal ;
**C'était « un langage poétique qui relie la volonté humaine et les machines. »**

Même aujourd’hui, en 2025, nous continuons d’écouter la poésie de cette tension.

---


