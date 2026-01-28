---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-music-easel.webp
lang: fr
layout: post
permalink: /fr/column-buchla-music-easel/
tags:
- Buchla
- Modular
- Ambient
title: '[Chronique] Buchla Music Easel et la philosophie de la « performance solitaire
  » : redéfinir l''improvisation avec les synthés analogiques'
---


## Introduction : Qu'est-ce que le chevalet musical Buchla ?

Texte : mmr｜Thème : Chevalet musical, qui, même à l'époque moderne, est salué par de nombreux artistes live comme le « plus petit orchestre pouvant être joué seul »


Le **Buchla Music Easel**, apparu en 1973, est une version portable de la célèbre **série Buchla 200** modulaire analogique.
Le concepteur **Don Buchla** a qualifié l'instrument d'« environnement de composition portable ».
Il ne s'agissait pas simplement d'un petit module, mais d'un « appareil personnel improvisé ».

> "Easel est une toile sonore. Vous ne pouvez pas enregistrer les lignes que le joueur dessine pour le moment."
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

## Chapitre 1 : Don Buchla et la philosophie « Anti-Moog »

Au début des années 1960, deux tendances majeures dans le développement des instruments de musique électroniques sont apparues en Amérique de l’Est et de l’Ouest.
Moog à l'est et Buchla à l'ouest.
Buchla visait à « générer » du son plutôt que de le « contrôler ».
Une plaque tactile a été utilisée à la place d'un clavier, et la performance était axée sur le **taux de changement et la contingence** plutôt que sur la hauteur.

Sa philosophie a été reprise dans le dernier Music Easel.
Le chevalet est un instrument permettant aux humains de jouer avec des circuits électroniques, et ce qui existe là-bas est l'attitude d'un « co-auteur » plutôt que d'un « interprète = contrôleur ».

### Analyse technique : relation entre la forme d'onde et la sensation tactile

Buchla pensait que « manipulation de la forme d'onde = expérience tactile ».
La figure ci-dessous est un modèle simplifié de la relation entre la FM (modulation de fréquence) et la sortie de forme d'onde dans Complex Oscillator.

<div class="mermaid">

graph TD
A[Modulation Oscillator] -->|FM Signal| B[Complex Oscillator]
B -->|Wavefolded Output| C[Audio Out]
B --> D[Harmonic Timbre CV]
D -->|Control Voltage| B

</div>

Grâce à cette interconnexion, une simple onde sinusoïdale a une structure harmonique et les moindres touches pendant la performance se reflètent immédiatement dans l'acoustique.

---

## Chapitre 2 : Structure et philosophie de Music Easel

Music Easel se compose de deux blocs principaux :

- **Source sonore du programme stocké Buchla 208**
- **Contrôleur de clavier tactile Buchla 218**

### Diagramme de flux de signal (Sirène)

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

Cette structure vous permet de compléter la génération d'horloge → la modulation → la sortie sonore** tout seul.
Easel lui-même fonctionne comme un « système musical complet » sans avoir besoin d'équipement externe.

### Caractéristiques techniques

* **Oscillateur complexe** : pliage de forme d'onde, FM, AM possible.
* **Pulser** : génère des impulsions périodiques, sert d'horloge.
* **Enveloppe** : contrôlée automatiquement, fermée, bouclable.
* **Reverb** : Réverbération naturelle avec réverbération à ressort.

L'idée qui les intègre n'est pas la « portabilité » mais « l'improvisation », et le centre de la production musicale est passé de la « pensée » à la « sensation tactile ».

---

## Chapitre 3 : Le chevalet comme instrument live

### Cas 1 : Suzanne Ciani « Séances de chevalet » (2016–)

La légendaire musicienne électronique **Suzanne Ciani** a commencé sa série solo live « Easel Sessions » à Easel dans les années 2010.
Elle supprime tous les ordinateurs portables et joue uniquement sur Easel.
Lors de la performance live, la hauteur change en douceur avec la pression des mains et la modulation FM fluctue de manière organique.
Ciani dit : « Buchla est un instrument respiratoire. »

Sur le plan sonore, la **modulation asynchrone** d'Easel crée un flux d'harmoniques qui semble flotter dans l'espace.
Le public a l'illusion que « l'air lui-même est diffusé ».

### Analyse de forme d'onde : Caractéristiques de la structure d'improvisation

| Éléments | Points techniques | Impressions auditives |
| -------------------------------- | ------------- | ------------ |
| Changement de la quantité FM de l'oscillateur de modulation | La forme d'onde fluctue de manière non linéaire dans le temps | Fluctuation organique |
| Connexion Pulseur + Enveloppe | Génération de cycles sans sensation de rythme | Sens du temps comme « respiration » |
| Auto-interférence de la réverbération de réverbération | Génération de phases opposées d'harmoniques | Sensation de flottement/diffusion réverbérante |

---

## Chapitre 4 : Possibilité de performance solo et construction d'espace acoustique

L’attrait d’Easel réside dans le fait que la sculpture sonore peut être réalisée sans aucun effet extérieur.
En reliant plusieurs modulations en utilisant Pulser comme déclencheur,
Il est possible de créer des « motifs minimaux générés » et des « structures rythmiques aléatoires ».

### Cas 2 : Charles Cohen « Live at the Rotunda » (2014)

L'improvisateur légendaire de Philadelphie **Charles Cohen** a utilisé le chevalet musical Buchla pendant plus de 40 ans.
Lors de ses concerts, le concept de tempo s'effondre et Pulser se dilate et se contracte comme une respiration.
Cohen a déclaré : « Le chevalet est un outil pour sculpter le temps. »

Dans sa performance, le repliement de la forme d'onde de l'oscillateur complexe provoque l'effondrement et la reproduction continue des harmoniques,
Il produit un son qui ressemble à celui d’un instrument acoustique en train de se reconstruire.

### Analyse de la technologie sonore : la structure d'improvisation de Cohen

<div class="mermaid">

graph TD
A[Pulser] -->|Irregular Trigger| B[Envelope]
B -->|CV Modulation| C[Complex Oscillator]
C -->|Audio| D[Wavefolder]
D -->|Audio| E[Reverb]
E -->|Stereo Out| F[Audience Space]

</div>

Cette structure de déclenchement asynchrone permet au chevalet de générer lui-même un « groove non mesuré ».
Cohen dit que la musique naît simplement en « s'abandonnant » au flux du courant.

---

## Chapitre 5 : Artistes contemporains et héritage du chevalet

### Suzanne Ciani

→ L'incarnation du féminisme sonique. Je confie ma physicalité au doux courant électrique de Buchla.

###Todd Barton

→ En tant qu'éducateur, il explique Easel comme « le point de contact entre la conscience et les machines ».
"Ne le joue pas, écoute-le en train de te jouer."

###Charles Cohen

→ L'extrême nord de l'improvisation. Un spectacle live n’est pas une question de musique, mais de création d’un lieu.
Même après sa mort, Buchla a réimprimé son patch sous le nom de « Cohen Program Card ».

### Kaitlyn Aurélia Smith

→ Intégrer la philosophie d'Easel au numérique. Extension des fluctuations sonores naturelles à la musique ambiante moderne.

---

## Chapitre 6 : Technologie et physicalité - l'acte de « jouer du courant électrique »

Jouer à Music Easel ne consiste pas à appuyer sur un interrupteur ;
**C'est l'acte de s'appuyer sur la vitesse de réaction d'un circuit électrique**.
La pression, l'humidité et la température du bout de vos doigts affectent la valeur CV et modifient le son.

En d’autres termes, Easel est un instrument dont la peau humaine devient le circuit.
Les sons qui y existent sont des phénomènes, pas des données.

Lors des performances live récentes, les opérations analogiques du chevalet ne sont pas converties en MIDI,
Le mouvement visant à le traiter comme une pure réponse actuelle attire à nouveau l’attention.
Cette tendance « anti-numérique » est aussi le signe d’un retour de la réalité physique dans la musique électronique.

---

## Conclusion : L'avenir en tant qu'orchestre

Le chevalet est fonctionnellement petit et expressivement illimité.
Le courant électrique vacillant à l’intérieur crée un « son vivant » en synchronisation avec la respiration de l’interprète.

Comme le disait Charles Cohen : « Le chevalet est un interlocuteur solitaire »
Comme l'a montré Suzanne Ciani, « c'est l'organe qui traduit les émotions humaines sous forme électronique ».

Dans l'environnement live d'aujourd'hui, dominé par les ordinateurs portables,
Buchla Music Easel reste un « orchestre solitaire ».
Il cache l’avenir de l’improvisation dans la plus petite unité de circuit.

---

## Annexe : Chronologie du chevalet de musique Buchla

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
