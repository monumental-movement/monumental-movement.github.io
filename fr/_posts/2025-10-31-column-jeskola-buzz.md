---
author: mmr
categories:
- Column
image: ../assets/images/column-jeskola-buzz.webp
lang: fr
layout: post
permalink: /fr/column-jeskola-buzz/
tags:
- Modular
- DAW
- Software
- Tracker
title: '[Chronique] L''héritage de Jeskola Buzz : Le miracle de la musique électronique
  née de la liberté et de l''esprit expérimental'
---


## 1. Introduction : La scène musicale PC des années 1990 et l'émergence de Buzz


Texte : mmr｜Thème : Retracez les caractéristiques techniques et l'histoire de Buzz, puis organisez ce qui était possible du point de vue de l'utilisateur/de la communauté, et tracez des exemples spécifiques d'utilisation par les artistes et de son influence musicale.

Au milieu des années 1990, le monde de la production de musique électronique/musique sur PC se trouvait à un tournant majeur. Traditionnellement, les synthétiseurs matériels, les équipements dédiés et les studios d'enregistrement étaient au centre de l'attention, limitant l'environnement dans lequel les individus pouvaient librement produire et présenter des chansons. Cependant, les progrès de la technologie des PC (Windows) et des logiciels ont marqué le début d’une ère dans laquelle les gens peuvent créer librement des sons à la maison.

Pendant ce temps, "Jeskola Buzz" du développeur finlandais Oskari Tammelin est apparu vers 1997 (ou aurait eu une version alpha avant cette date).
Buzz est un tracker/séquenceur modulaire gratuit (distribution gratuite) pour Windows qui a été pris en charge par de nombreux utilisateurs. Le plus grand attrait était l'environnement dans lequel « les sources sonores (générateurs), les effets (machines) et le routage (câblage) pouvaient être librement assemblés pour recréer un « équipement modulaire » sur logiciel. »

Cette configuration « modulaire + tracker », contrairement aux DAW (stations de travail audio numériques) centrées sur l'interface graphique de l'époque, permettait un « expérimentalisme » et une approche « patch-like », donnant lieu à un haut degré de liberté dans l'exploration sonore. Buzz est allé au-delà du simple « logiciel qui crée du son » et a formé une « sphère culturelle » où les individus peuvent créer et développer leurs propres machines et les faire évoluer avec la communauté. Certains considèrent désormais que cette tendance a influencé un environnement modulaire souple, une culture du plug-in et même un retour à une modularité matérielle.

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


## 2. Naissance et évolution de Jeskola Buzz

Retraçant l'histoire de Buzz, il a été développé pour la première fois par le développeur Oskari Tammelin et publié gratuitement à la fin des années 1990. Officiellement défini comme « Jeskola Buzz est un environnement de studio de musique logiciel modulaire gratuit… »
Ce qui était distinctif, c'est que le logiciel lui-même se composait d'une machine (source sonore/effets) + routage (connexion par câble) + tracker/séquenceur (une méthode d'arrangement vertical des motifs).

### Modifications depuis la version initiale

* Initiale : fonctionne sous Windows 95/98. Il était léger et disposait d'un écran d'édition de motifs de type tracker et d'une vue modulaire (Machine View).
* Écosystème de plug-ins : Depuis le début du développement, il existe une spécification « Buzzlib » qui permet aux utilisateurs de créer et de distribuer librement des sources sonores et des effets, et de nombreuses machines sont apparues au sein de la communauté.
* Mise à niveau de la version : le développement officiel a été temporairement bloqué (en raison de la perte du code source), mais il a été annoncé en juin 2008 que le développement reprendrait.
*Dernière build : Build 1503 publiée le 16 janvier 2016.

### Signification/arrière-plan du nom

« Jeskola » proviendrait du nom de la scène démo du développeur, « Jeskola/Finland ». Parce qu'il s'agissait d'un logiciel issu de la démoscène (programmation underground/culture artistique comprenant l'infographie et la musique), Buzz lui-même avait une forte saveur démo/AMIGA, comme « tracker » et « modulaire ».

### Pourquoi « modulaire + tracker » était révolutionnaire

* Conventionnellement, la méthode traditionnelle des trackers consistait à séquencer les échantillons dans un format de défilement vertical, et le routage des sources sonores et des effets était fixe/limité. Buzz a élargi ce concept pour inclure un concept de « câble de brassage », permettant aux utilisateurs de créer leurs propres circuits tels que « source sonore -> filtre -> effet -> sortie ».
* De plus, il était léger et ses paramètres pouvaient être manipulés en temps réel, ce qui en faisait une base populaire pour créer des œuvres sonores expérimentales.
* L'esprit ouvert de la distribution gratuite et de l'extensibilité des utilisateurs a encouragé les créateurs individuels à créer une culture de « modification de leurs propres sons pour les créer/partager ».

De cette manière, Buzz a joué à l’époque un rôle hérétique et novateur en « réalisant un environnement modulaire sur PC ».

---

## 3. Innovation Buzz : séquenceur modulaire et culture plug-in

Dans ce chapitre, nous analyserons en détail « ce qui était technologiquement innovant » chez Buzz.

### 3.1 Les sources sonores et les effets peuvent être gérés dans des unités « machine »

Buzz dispose d'une machine « Générateur » qui produit du son et d'une machine « Effet » qui traite le son, et les utilisateurs peuvent les organiser et les connecter sur la « Vue Machine ».
Par exemple, j'ai pu visualiser et construire un flux machine de génération de forme d'onde (Oscillateur)/machine d'échantillonnage (Sampler) → filtre → enveloppe/LFO → réverbération/délai → sortie.
Cette configuration permet un « routage libre » rarement vu dans les trackers/séquenceurs conventionnels.

### 3.2 Format Tracker + connexion modulaire

Buzz était basé sur un format de motif/séquenceur appelé « Tracker », et l'édition de type texte était également possible à l'aide de colonnes (pistes) et de lignes (motifs). De plus, en utilisant un flux de signal modulaire (connexions machine à machine), le suivi et le traitement modulaire du son ont été combinés.
En conséquence, l'exploration sonore consistant à « jouer une boucle avec un échantillonneur et changer de filtres et d'effets à l'aide d'un câble de raccordement » est devenue possible dans un environnement PC relativement léger.

### 3.3 Écosystème de plugins/extensions communautaires

Une autre innovation de Buzz est l'existence d'un grand nombre de machines créées par les utilisateurs (générateurs de sons et plug-ins d'effets). Officiellement, un en-tête de développement appelé « Buzzlib » a été fourni, permettant aux utilisateurs de créer et de distribuer des plug-ins gratuitement.
Cela a conduit aux tendances suivantes :

* Les développeurs individuels publient des sources/effets sonores, et vous pouvez profiter de nouveaux sons/traitements simplement en les téléchargeant et en les incorporant.
* Les utilisateurs ont commencé à relever le défi de « jusqu'où ils pouvaient créer des circuits » et « jusqu'où ils pouvaient obtenir du son expérimental ».
* Les personnes qui créent des œuvres expérimentales qui traversent les genres musicaux choisissent de plus en plus Buzz comme « outil ».

### 3.4 Léger, immédiat et supérieur en tant qu'environnement expérimental

Il fonctionnait relativement confortablement dans l'environnement PC de l'époque (Windows 95/98, Atom/ancienne classe Pentium), et il était également possible de modifier le son en temps réel. De plus, grâce au format tracker, il avait l'avantage de pouvoir saisir des motifs à grande vitesse en utilisant uniquement une souris et un clavier, et de permettre des performances improvisées et de type live.
Ce point était très attractif pour les créateurs qui ne disposaient ni de matériel ni de studio, mais souhaitaient explorer les sons chez eux.

---

## 4. Le pouvoir de la communauté : expansion des utilisateurs et formation d'une sous-culture

Un autre aspect important de Buzz était qu'il était activement soutenu, partagé et développé par la communauté des utilisateurs. Dans ce chapitre, nous verrons comment la communauté a contribué à faire de Buzz plus qu'un simple logiciel.

### 4.1 Partage de plug-ins gratuits et culture du marché des sources sonores

Les utilisateurs de Buzz créaient des machines à sources sonores/machines à effets et les distribuaient gratuitement sur des forums et des sites Web. Par exemple, de nombreuses machines ont été publiées sur BuzzMachines.com et sur les forums demoscene.
Cela a rendu courant le téléchargement de la machine de quelqu'un d'autre et l'insertion dans vos propres chansons. En d'autres termes, un cycle est né dans lequel « les utilisateurs créent des équipements (équipements logiciels) puis les partagent avec des amis et sur Internet ».

### 4.2 Relation profonde avec la démoscène

Buzz a gagné en popularité dans la démoscène (culture expérimentale non commerciale de l'art informatique/de la musique), principalement en Europe du Nord et de l'Est. La légèreté, l'évolutivité et la possibilité de patch de Buzz étaient parfaites pour la scène de démonstration, où la compétition consistait à voir combien de sons et d'images uniques pouvaient être produits en utilisant le moins de ressources possible.
Pour cette raison, le style de « création de vos propres sources sonores et création de motifs » sur Buzz a été soutenu par de nombreux créateurs de démos/indépendants.

### 4.3 Création d'un forum/tutoriel en ligne

Des informations sur l'utilisation de Buzz, des conseils de câblage de la machine, des exemples de traitement d'échantillons/de construction de chaînes d'effets, etc. ont été accumulées sur des forums, des blogs et YouTube. En conséquence, nous avons créé un environnement dans lequel même les débutants peuvent apprendre relativement facilement « ce que Buzz peut faire ».
Cette culture de l'apprentissage a créé une tendance à « apprendre à utiliser/modifier/partager » et a élevé Buzz du statut d'« outil » à celui de « plateforme ».

### 4.4 Utilisation dans tous les genres musicaux et création d'une sous-culture

Les créateurs utilisant Buzz n'étaient limités à aucun genre, notamment la techno, la transe, l'IDM, l'ambient, le breakcore et le chiptune. Il existait, pour ainsi dire, une culture qui consistait à « donner la priorité aux idées, quel que soit l'équipement ».
Par exemple, certaines personnes ont créé des morceaux de type chiptune avec une configuration de « PCM de style 8 bits + échantillonneur + filtre + délai », tandis que d'autres ont créé du breakcore avec une configuration de « plusieurs échantillonneurs + traitement des problèmes + modélisation à grande vitesse ». Il y a également eu un échange animé de savoir-faire entre les utilisateurs, du type « cette machine/ce câblage est bon ».

De cette manière, la communauté Buzz s'est développée au-delà des simples « utilisateurs de logiciels » pour devenir « des amis partageant une plateforme d'expérimentation acoustique » et « une communauté culturelle qui distribue et modifie des machines fabriquées par ses soins ».

---

## 5. Artistes utilisant Buzz : exemples du Japon et de l'étranger

Dans ce chapitre, nous mettrons en lumière les artistes qui ont réellement utilisé Buzz ou qui ont été mentionnés comme l'utilisant, et présenterons leurs histoires. Énumérez séparément ceux dont il est confirmé qu'ils ont utilisé le médicament et ceux qui auraient la possibilité de l'utiliser.

### 5.1 Certainement utilisé : James Holden

James Holden a mentionné dans plusieurs interviews qu'il avait utilisé Buzz pour produire de la musique. Par exemple, un article de MusicRadar déclare : « Lorsque nous avons interviewé Holden pour la première fois – en 2006 – il utilisait Jeskola Buzz, un environnement logiciel gratuit basé sur des trackers, pour écrire son premier album *The Idiots Are Winning*.
De plus, les messages du forum incluent des déclarations telles que "La musique de James Holden… m'a poussé à le faire, il travaille principalement avec (ou du moins avait l'habitude de) Buzz."

#### Citation de style d'entretien (reconstruction)

> "Le Buzz m'a choqué en raison de son fonctionnement modulaire. C'est la sensation de connecter des sources sonores qui a suscité mon intérêt pour les synthés modulaires plus tard."
> – James Holden (extrait d'entretien de 2006)

D'après ces récits, il est hautement fiable que Holden a produit certaines de ses premières œuvres (par exemple *The Idiots Are Winning*) sur Buzz. En utilisant Buzz, on peut analyser que sa musique reflète des caractéristiques telles que le « patching modulaire/routage libre » et « l'édition de motifs à grande vitesse utilisant le format tracker ».

#### Exemple d'analyse de piste (exemple)

En prenant comme exemple un morceau tel que « Blank It » de l’album *The Idiots Are Winning*, les points suivants suggèrent l’environnement dans lequel Buzz sera utilisé :

* Le matériel complexe de boucle/échantillonneur est développé en parallèle,
* Le fonctionnement du filtre modulaire et la modulation du LFO sont visibles (le son a une "sensation mécanique"),
* Il a une structure rythmique qui se répète et se subdivise comme un motif vertical, et cela peut être considéré comme unique à Buzz, qui peut être facilement édité au format tracker.

Ainsi, les premières œuvres de Holden ont un langage sonore hautement compatible avec les caractéristiques de Buzz (modulaire/tracker).

### 5.2 Utilisation possible mentionnée : Aphex Twin

Concernant Aphex Twin (de son vrai nom Richard D. James), aucun document primaire solide (interviews officielles, etc.) n'a été trouvé indiquant qu'il "a utilisé Buzz", et il n'y a que des mentions de "il a utilisé/pourrait utiliser Buzz" dans les messages du forum et les témoignages d'utilisateurs. Par exemple, sur le forum KVR, un utilisateur a déclaré : "...mon tracker préféré est Jeskola Buzz...", suggérant qu'AFX (Aphex Twin) utilise peut-être un logiciel de tracker.
Également indiqué dans le fil HackerNews :

> "Le flux de travail productif rapide de Jeskola Buzz de l'époque me manque toujours. Synthé logiciel modulaire + tracker avec séquençage de motifs. "


### 5.3 Autres artistes/créateurs nationaux

L'article Wikipédia correspondant répertorie les artistes qui ont pu utiliser Buzz, notamment Andreas Tilliander, The Field et Simon Viklund, et les présente comme les « candidats utilisateurs notables » de Buzz.

---

## 6. L'influence musicale de Buzz : expansion du genre et de l'expression

Dans ce chapitre, nous résumerons la manière dont Buzz a influencé les genres musicaux et les méthodes d’expression.

### 6.1 Buzz comme outil multi-genres

Buzz est plus qu'un simple DAW pour la techno et la house, il a joué un rôle important dans les genres et applications suivants :

* **Breakcore/IDM (Intellectual Dance Music)** : un genre qui utilise des rythmes complexes, un traitement des glitchs et des chaînes d'effets profondes, et les connexions modulaires et le format de suivi de Buzz étaient idéaux pour ce genre.
* **Système Chiptune/8 bits** : En tant qu'environnement léger et hautement improvisé, Buzz est devenu un outil permettant d'essayer rapidement la configuration « échantillonneur + génération de forme d'onde + filtre ».
* **Musique ambiante/expérimentale** : au-delà des signatures rythmiques et des structures fixes, la possibilité de patch de Buzz a été utilisée pour explorer les espaces acoustiques, les textures et la conception sonore.
* **Performance/Improvisation Live** : Comme mentionné ci-dessus, il était également utilisé comme outil d'improvisation sur ordinateur portable et de sets live car il était léger et très réactif.

### 6.2 Élargir l'expression acoustique : diffuser la pensée modulaire

La « pensée modulaire » encouragée par Buzz (connecter les sons de manière linéaire, câbler les signaux librement et improviser des sons pour changer les sons) allait au-delà du style traditionnel « piste + mixeur + chaîne d'effets » et permettait une exploration sonore plus « organique et dynamique ».
Dans « Dreaming Of Wires » publié dans cet article, James Holden dit :

> "Buzz était assez modulaire dans son fonctionnement... cette façon de visualiser ma chaîne audio restait bloquée. J'ai pris l'habitude de travailler uniquement avec des dégâts bancaux et peu fiables." ([Magazine d'attaque][8])

De cette façon, Buzz a donné naissance à l'idée de « profiter intentionnellement de circuits instables/atypiques (patchs bancaux) », ce qui a conduit au retour modulaire ultérieur (à la fois matériel et logiciel).

### 6.3 Impact pour aujourd'hui : pontage souple/dur

Même après l'arrêt du développement officiel de Buzz, « l'héritage » suivant a été dérivé :

* Projets d'imitation/dérivés sans licence (par exemple BuzzTrak/Buzz clone), environnement de module Tracker fonctionnant sous Linux, etc.
* Maturation de la culture logicielle modulaire/plugin. Le style selon lequel « les utilisateurs ajoutent des extensions et les partagent en ligne » est devenu monnaie courante.
* L'esprit « modulaire + improvisation » de Buzz est référencé dans la renaissance de la modularité matérielle (par exemple Eurorack). Dans l'article précédent « Dreaming Of Wires », Holden a déclaré que « la pensée du câblage qu'il a apprise de Buzz » est devenue le point de départ de sa transition vers le modulaire dur.

### 6.4 Contribuer à la production musicale/à l'éducation/à la culture du bricolage

Buzz a encouragé « les individus à créer/expérimenter de la musique sans avoir besoin d'un équipement de studio coûteux ». Par conséquent, il servait d’« entrée » aux créateurs indépendants, aux étudiants et aux amateurs.
De plus, comme présenté dans la section précédente, les débutants utilisaient Buzz pour modifier des sources sonores et construire des machines, et partageaient les résultats en ligne, donnant ainsi naissance à une culture « d'apprendre à créer des sons ensemble ». Cela va de pair avec « l'éducation musicale DIY » que nous voyons aujourd'hui sur YouTube, les blogs et les forums de production musicale en ligne, dont Buzz est un pionnier.

---

## 7. La fin de Buzz et son héritage

Buzz a atteint son apogée au début des années 2000 et est entré dans une phase de « stagnation du développement officiel », mais son influence est restée.

### 7.1 Contexte de stagnation

Selon l'explication officielle, les développeurs de Buzz ont perdu le code source et le développement a été interrompu le 5 octobre 2000. Cependant, un redémarrage a été annoncé en juin 2008 et des mises à jour/correctifs communautaires pilotés par les utilisateurs ont été effectués depuis lors.
Cette structure de stagnation/reprise a également été influencée par des facteurs externes tels que les limitations du logiciel, l'évolution de l'environnement PC et la diversification des environnements utilisateurs (DAW plus sophistiqués).

### 7.2 On ne peut pas dire que c'est fini : Suite et récupération

* La version Build1503 du 16 janvier 2016 a été publiée et existe en tant que dernière version.
* En outre, des logiciels/environnements héritant de la philosophie de Buzz sont apparus, tels que l'environnement de module Tracker pour Linux et un renouveau en tant que système « modulaire doux ».
*De plus, avec la renaissance du matériel modulaire (Eurorack, etc.), l'idée de « construire et câbler vos propres circuits » a été réévaluée, et la sensation/idée de fonctionnement de type Buzz est présentée comme une « expérience originale ».

### 7.3 Traces laissées : Résumé

L'héritage de Buzz peut être globalement classé en trois éléments :

- 1. **Diffusion de la pensée modulaire** : L'idée d'assembler des correctifs sur des logiciels est devenue populaire et l'image selon laquelle « créer du son = connecter des câbles » s'est imposée.
- 2. **Culture d'expansion des utilisateurs/plugins** : Une culture d'utilisateurs créant et partageant des équipements a pris racine et peut être considérée comme le prototype de la communauté VST/plugin d'aujourd'hui.
- 3. **Promotion des créateurs individuels/DIY music** : La production de musique électronique indie/underground a été revitalisée grâce à la disponibilité d'un environnement acoustique sophistiqué à bas prix ou gratuitement.

Ce ne sont pas seulement des reliques des « outils rétro » du passé, mais ils influencent également l'environnement de production musicale actuel et même le contexte des équipements live/modulaires.

---

## 8. Résumé : Connecter l'esprit freeware et la musique moderne

Buzz était bien plus qu’un simple logiciel. Il s'agissait d'un « outil qui encourage la création sonore libre », d'une « plate-forme qui permet aux individus d'expérimenter, de partager et de développer » et d'une « culture audio/tracker modulaire publiée sur PC ».

Aujourd’hui, nous vivons à l’ère des DAW hautes performances, du partage dans le cloud et de l’intégration logiciel/matériel, mais à la base de tout cela se trouve l’idée « légère, gratuite et évolutive » que Buzz a encouragée, et dans une certaine mesure, nous avons hérité des mêmes gènes.

En d’autres termes, l’existence de Buzz a brisé le stéréotype selon lequel « on ne peut pas commencer à jouer de la musique parce qu’on n’a pas l’équipement » et a ouvert la porte à « tant qu’on a une idée et une curiosité, on peut explorer les sons avec juste un PC à la maison ». Cette porte continue d’être l’une des « entrées » pour de nombreux créateurs.

---

## 9. Chronologie

Vous trouverez ci-dessous une chronologie de l'histoire et des événements majeurs de Buzz.

| Année | Événements |
| ------------ | ------------------------------------------------------------------- |
| Vers 1997 | Jeskola Buzz publié. Introduit comme un tracker modulaire pour Windows.                                |
| 1998 | La version initiale active la communauté des utilisateurs. De nombreux plugins/machines sont apparus.                                    |
| 1999 | Utilisation répandue parmi les scènes de démonstration et la musique électronique indépendante.                                                 |
| 2000 (5 octobre) | Le développeur a perdu le code source et a annoncé la suspension officielle du développement.                                |
| 2002 | Les extensions non officielles et la distribution de plug-ins par la communauté ont atteint leur apogée.                                              |
| 2008 (juin) | Annonce de redémarrage du développement. Les mises à jour centrées sur l'utilisateur se poursuivent. ) |
| Vers 2012 | La Build 1400 est sortie et des témoignages tels que "James Holden l'a utilisé" se répandent sur les forums. |
| 2016 (16 janvier) | Build 1503 publié. Enregistré comme la « dernière » version officielle.                           |
| Années 2020 | Avec le renouveau de la modularité matériel/logiciel, la philosophie de Buzz sera réévaluée.                                     |

---

## 10. Illustration : exemple de flux de signal Buzz

Vous trouverez ci-dessous un schéma d'une connexion de machine typique (flux de signal) dans Buzz.

<div class="mermaid">

flowchart LR
    A[Oscillator／Sampler] --> B[Filter]
    B --> C[Envelope／LFO]
    C --> D[Delay]
    D --> E[Reverb]
    E --> F[Output]
    G[LFO／Modulator] --> B

</div>

**Explication**:

* A : Source sonore (génération de forme d'onde ou échantillonneur)
* B : Filtre (passe-haut/passe-bas)
* C : Enveloppe/LFO (changement d'heure/changement de période)
* D : Retard (traitement spatial/temporel)
* E : Reverb (espace de réverbération)
*F : Sortie (mixeur → stéréo)
* G : Ajoute une modulation en appliquant un modulateur (LFO, etc.) à un filtre, etc.

De cette manière, avec Buzz, les machines peuvent être librement connectées, ce qui permet de créer des structures sonores « de type circuit », « de type patch » et « exploratoires » qui ne peuvent pas être obtenues avec le flux fixe conventionnel de « source sonore → mixeur → effet ».

---

