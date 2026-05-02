---
author: mmr
categories:
- Column
date: 2026-04-11 00:00:05 +0900
image: ../assets/images/column-lunetta-cmos.webp
lang: fr
layout: post
permalink: /fr/column-lunetta-cmos/
tags:
- CMOS
- Lunetta
- DIY
title: '[Chronique] Le monde du synthétiseur CMOS et Lunetta : l''esthétique de la
  musique électronique primitive jouée par des circuits logiques'
---



## Qu'est-ce que le synthétiseur CMOS ?

Texte : mmr｜Thème : Le moment où les circuits logiques deviennent musique ─ Le monde de l'acoustique électronique primitive représenté par CMOS Synth et Lunetta

Le soi-disant Lunetta Synth, un synthétiseur DIY utilisant des circuits intégrés logiques CMOS, est une culture qui génère des sons à partir de circuits extrêmement simples et primitifs, contrairement à l'environnement musical électronique sophistiqué d'aujourd'hui. Cet article discutera de ses origines, de sa structure, de ses caractéristiques acoustiques et de sa réévaluation moderne basée sur des faits historiques et des perspectives techniques.

### Le moment où le circuit intégré logique devient sonore

CMOS Synth est un terme général désignant les synthétiseurs qui génèrent du son à l'aide de circuits intégrés logiques CMOS conçus à l'origine comme des circuits numériques. Ces circuits intégrés sont initialement destinés aux calculs et au traitement du signal, mais en concevant une structure d'horloge et de rétroaction, ils peuvent osciller et générer des sons audibles.

Les circuits intégrés typiques sont les suivants.

* 40106 : Onduleur à déclenchement Schmitt
*4040 : Compteur binaire
* 4017 : Compteur décennal
*4070 : porte XOR

Ceux-ci peuvent produire des sons seuls, mais lorsqu’ils sont combinés, des rythmes et des motifs complexes peuvent être créés.

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



### Définition du synthétiseur Lunetta

Lunetta Synth est un nom dérivé du nom du constructeur de bricolage italien Stanley Lunetta et fait spécifiquement référence à un système présentant les caractéristiques suivantes.

* Composé uniquement de circuits intégrés logiques CMOS
*En principe, n'utilisez pas de filtres analogiques ou de VCA
*Connexion gratuite par patch
* Changement de tonalité dû à la tension d'alimentation

Ce sont ces contraintes qui ont créé un son et une culture uniques.

> Le synthétiseur CMOS est un domaine dans lequel les circuits électroniques deviennent eux-mêmes des instruments de musique plutôt que des équipements musicaux.

---

## Bases techniques : Pourquoi le son sort-il ?

### Mécanisme d'oscillation

Les inverseurs CMOS ont la caractéristique que l'entrée et la sortie sont inversées. En combinant cela avec une résistance et un condensateur, un circuit auto-oscillant (oscillateur) est construit.

<div class="mermaid">
flowchart LR
A[入力] --> B[インバータ]
B --> C[出力]
C --> D[RC回路]
D --> A
</div>

Cette boucle fait changer périodiquement la tension, générant une onde carrée.

### Division de fréquence par compteur

Un compteur IC divise l'horloge d'entrée et génère des signaux avec plusieurs périodes différentes. Cela produit les effets suivants.

* Génération de motifs rythmiques
* Structure polyrythmique
* pseudo mélodie

<div class="mermaid">
flowchart TD
CLK[クロック] --> C1[1/2]
CLK --> C2[1/4]
CLK --> C3[1/8]
CLK --> C4[1/16]
</div>

### Transformation du son à l'aide d'opérations logiques

Les opérations logiques telles que XOR et AND modifient la relation entre les signaux. Cela crée un spectre complexe même avec une forme d'onde simple.

*XOR : augmente les harmoniques et devient bruyant
* ET : son intermittent semblable à celui d'une porte
*OR : augmentation de la densité due au chevauchement

> La génération sonore est basée sur des opérations logiques plutôt que analogiques.

---

## Contexte historique

### L'interface entre les circuits numériques et la musique

Dans les années 1970, les circuits intégrés CMOS sont devenus populaires en tant que composants électroniques peu coûteux et à faible consommation. À peu près à la même époque, les expériences en matière de musique électronique se sont progressivement étendues de l’analogique au numérique.

Cependant, l'idée d'utiliser le CMOS comme source sonore n'était pas courante et existait comme une tentative de certains expérimentateurs.

### Connexion avec la culture du bricolage

Au début des années 2000, la création sonore CMOS a été redécouverte grâce aux forums Internet et aux sites personnels. Les facteurs suivants sont particulièrement importants.

* Disponibilité des pièces
*Simplicité des circuits
*Faible coût
* Peut être fabriqué par soudure uniquement

Dans cette veine, le concept de « Lunetta Synth » s'est répandu et s'est imposé dans la communauté DIY.

### Relation avec les synthés modulaires

Lunetta a une philosophie différente des synthés modulaires, mais ils se croisent sur les points suivants.

* Modifications structurelles dues aux correctifs
* Conception modulaire
* Génération sonore expérimentale

Cependant, la différence décisive est que l’accent est mis sur les signaux logiques plutôt que sur le contrôle de tension.

> Lunetta n'est pas une simplification modulaire, mais une évolution complètement différente.

---

## Caractéristiques acoustiques

### Dominance des ondes carrées

La forme d'onde de base du CMOS Synth est une onde carrée. Il en résulte les caractéristiques suivantes :

* Fortes composantes harmoniques
* Texture dure numérique
* Discontinuité rythmique

### Instabilité et contingence

Le comportement des circuits CMOS change en fonction de la tension d'alimentation, de la température et du câblage.

* Fluctuation de l'horloge
* Modèle apériodique
* Rythme chaotique

Il en résulte une musique avec une faible reproductibilité.

### Connexion hors de la plage audio

En divisant l'horloge haute fréquence, le processus de chute dans la plage audible devient lui-même une structure musicale.

<div class="mermaid">
flowchart LR
HF[高周波] --> DIV[分周]
DIV --> AUD[可聴音]
</div>

> La musique n'est pas générée, mais extraite d'une hiérarchie de fréquences.

---

## Conception et pratique des circuits

###Configuration de base

La Lunetta la plus simple a la configuration suivante.

*Oscillateur (40106)
* Compteur (4040)
* Mixage de sortie

En conséquence, des signaux ayant plusieurs périodes sont émis simultanément.

### Culture des correctifs

La fonctionnalité de Lunetta n'est pas un câblage fixe, mais des changements de connexion à l'aide de cavaliers et de câbles de brassage.

* Connectez librement les entrées et les sorties
* Générer une boucle de rétroaction
* Comportement imprévisible

<div class="mermaid">
flowchart TD
A[OSC] --> B[COUNTER]
B --> C[LOGIC]
C --> A
</div>

### Importance de la tension d'alimentation

Les circuits intégrés CMOS fonctionnent entre 3 V et 15 V environ, mais le son change en fonction de la tension.

* Haute tension : plage de vitesse/aigus élevée
* Basse tension : faible vitesse/distorsion

La tension elle-même fait office de paramètre.

> Briser la stabilité du circuit crée de la musicalité.

---

## Chronologie : Déploiement de CMOS Synth et Lunetta

### Années 1970-1990

* Années 1970 : Vulgarisation des circuits intégrés CMOS
* Années 1980 : Généralisation des sources sonores numériques
* Années 1990 : Pratique fragmentée de la musique électronique DIY

### Années 2000

* Premier partage de circuits sur Internet
* Vulgarisation du nom Lunetta Synth
* Activation de la production individuelle

### Depuis les années 2010

* Réévaluation en parallèle de la relance modulaire
* Ateliers et développement communautaire
* Le développement en tant qu'œuvre d'art

<div class="mermaid">
flowchart LR
A[1970s CMOS普及] --> B[1990s 実験]
B --> C[2000s 再発見]
C --> D[2010s 文化化]
</div>

> Les circuits, qui étaient un sous-produit de la technologie, sont devenus indépendants en tant que culture.

---

## Position dans les temps modernes

### Relation avec la musique noise/expérimentale

Lunetta a une grande affinité avec les genres suivants.

* Musique bruyante
* Industriel
* Musique électronique expérimentale

Cela est dû à l’accent mis sur la contingence plutôt que sur le contrôle.

### Valeur éducative

CMOS Synth est également efficace comme introduction à l’ingénierie électronique.

* Comprendre les circuits logiques
* Découvrez le principe d'oscillation
* Visualisation de la relation entre le son et l'électricité

### Les circuits comme art

Le circuit lui-même devient un objet visuel et est également utilisé comme installation.

* Visualisation avec LED
* Synchronisation du son et de la lumière
* Esthétique de l'aménagement physique

> Lunetta se situe à l'interface de la musique, de l'ingénierie et de l'art.

---

## Conclusion : Pourquoi un synthétiseur CMOS maintenant ?

Contrairement aux environnements de production musicale hautement optimisés d'aujourd'hui, le synthétiseur CMOS est inefficace et incontrôlable. Cependant, cette restriction même crée des sons et des structures imprévisibles.

*Circuit simple
*Résultats compliqués
* Non-reproductibilité

Ce sont des éléments que la musique numérique a tendance à perdre, et c'est là que réside la valeur de Lunetta.

> Les circuits primitifs posent les questions les plus modernes.

---
