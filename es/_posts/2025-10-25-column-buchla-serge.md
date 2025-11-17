---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-serge.webp
lang: es
layout: post
permalink: /es/column-buchla-serge/
tags:
- Synth
- Techno
- History
title: '[Columna] Buchla y Serge: Otra genealogía de la acústica electrónica'
---


## “Introducción: ¿Qué es modular?”


Texto: mmr | Tema: Historia espiritual de los sintetizadores modulares de la costa oeste. Cómo las ideas de Don Buchler y Serge Tocheny se han trasladado al diseño de sonido actual

Principios de la década de 1970, costa oeste de Estados Unidos.
Hubo personas que abandonaron el estudio de música electrónica de su universidad e intentaron llevar **un dispositivo para diseñar sonido** a sus espacios creativos personales.
Sus nombres son **Don Buchla** y **Serge Tcherepnin**.

A menudo se habla de Buchla y Serge como los llamados "progenitores de los sintetizadores modulares", pero en realidad se destacan porque buscaron crear herramientas filosóficas en lugar de instrumentos comerciales.
Su filosofía de diseño contenía una perspectiva sonora "antinormativa" que es común al Eurorack, Max/MSP e incluso a la música generada con inteligencia artificial de hoy en día.

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



## 1. Don Buchler: Poética del sonido electrónico

### 1-1. Desde el Centro de Música Tape de San Francisco

En el Tape Music Center de San Francisco, a principios de la década de 1960, artistas como **Morton Subotnick** y **Pauline Oliveros** exploraban nuevas relaciones entre la música experimental y la tecnología.
Lo que buscaban era "un instrumento que no fuera una extensión del piano o la guitarra".

La **Buchla Serie 100 (1963-1966)** apareció en respuesta a la petición de Subotnick.
Se evitó intencionalmente la operatividad musical tradicional, como la configuración del circuito acústico mediante perillas y cables de conexión, y el teclado con placa táctil (en realidad, un dispositivo de entrada de voltaje sin escala).

> “Sin teclas blancas y negras”. —Don Buchla

### 1-2. La filosofía de Buchla: la electrónica performativa

Buchla diseñó instrumentos musicales como "un ecosistema en el que coexisten control y generación".
El sonido no proviene directamente del cuerpo del intérprete, sino que se genera mediante el comportamiento abstracto de los cambios de voltaje.
Por tanto, la interpretación se convierte en un "acto" de improvisación y el sonido es fluido.

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

Esta estructura simboliza la visión del mundo de Buchla de "catalizar el sonido en lugar de manipularlo".
El Low Pass Gate (un elemento que controla tanto el volumen como el timbre) se convirtió más tarde en un dispositivo filosófico estándar en la cultura Eurorack.

---

## 2. Serge Tochenin: módulo democratizado

### 2-1. Nacimiento del “Sintetizador del Pueblo”

A finales de la década de 1970, el joven músico Serge Tochenin quedó impresionado por la filosofía de diseño de Don Buchla y, mientras estudiaba música electrónica en UCLA, imaginó un "dispositivo similar a Buchla al que más personas pudieran tener acceso".
Ese es **Serge Modular Music System (1974–)**.

Mientras Buchler creaba máquinas personalizadas para artistas, Serge está arraigado en la cultura del bricolaje y en la comunidad universitaria, con el espíritu de "abrir los esquemas para que cualquiera pueda construirlos".
Esta actitud de código abierto fue una revolución conceptual que precedió a la posterior difusión de Eurorack.

### 2-2. La filosofía de Serge: programabilidad de parches

La filosofía fundamental de Serge es **“Un módulo, muchas funciones”**.
Es decir, la idea es que un único circuito pueda tener una infinidad de modos de funcionamiento dependiendo de cómo esté conectado.
Por ejemplo, el generador de pendiente universal dual (comúnmente conocido como "DSG")
- sobre
-LFO
- retardo de disparo
- divisor de reloj
- Módulo Caos
La funcionalidad cambia según la configuración del parche.

Esta filosofía continúa directamente en los parches Max/MSP actuales, los bloques Reaktor y los "Maths" de Make Noise de Eurorack.

---

## 3. Comparación de Buchla y Serge: estructura e ideología

| Elemento | Buchla | Serguéi |
|------|---------|---------|
| Punto de partida | Instrumentos experimentales para artistas | Educación y cultura del bricolaje |
| Filosofía operativa | Performativo (sonido como acción) | Funcional (el sonido como estructura) |
| Diseño funcional | Configuración del módulo dedicado | Combinando módulos de uso general |
| Controlar | Operación de voltaje abstracto | Manipulación de señales concretas |
| Tendencias acústicas | Orgánico, dinámico, suave | Respuesta lineal, clara y rápida |
| Influencias culturales | Sonido artístico, instalación | Ruido, techno, música electrónica DIY |

---

## 4. Cronología tecnológica

| Año | Eventos | Notas |
|----|--------|------|
| 1963 | Comienza el desarrollo de Buchla Serie 100 | Primer modular encargado por Subotnick |
| 1966 | Debut del prototipo Buchla Music Easel | El fundador de los sintetizadores portátiles |
| 1974 | Anuncio modular de Serge | Lema “El sintetizador del pueblo” |
| 1980 | Presentamos el generador de doble pendiente Serge | Filosofía de parche completada |
| Década de 1990 | Período de reevaluación de Serge | Renacimiento analógico y recaída |
| 2004 | Comienza el boom del Eurorack | Heredado por Doepfer, Make Noise, etc. |
| Años 2020 | Buchla EE.UU. / Serge reimpresión | Recontextualización del pensamiento original |

---

## 5. Impacto en la cultura modular

La filosofía de Buchler y Sarge redefinió el sonido como un "acto social".
En otras palabras, cambió su enfoque de los "instrumentos" a los "entornos" y las "interfaces".

Las "infinitas combinaciones" modulares de Eurorack no son simplemente la libertad de las piezas, sino la reconfiguración misma del significado.
La "física" de Buchla y la "estructuralidad" de Serge se han fusionado, y la música electrónica actual se está volviendo cada vez más "decéntrica".

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

## 6. Conectándonos con la Era Moderna: Entre los Algoritmos y el Cuerpo

El espíritu de Buchla/Serge está vivo y coleando en Max/MSP, VCV Rack e incluso en herramientas musicales generadas por IA.
No es sólo una "combinación de módulos", sino un marco artístico que conecta el tiempo, el espacio, el cuerpo y la probabilidad.

Los sintetizadores modulares no son sólo "herramientas" para crear sonidos;
Es un medio que genera "eventos" que ocurren entre sonidos y personas.
La filosofía de diseño de Buchla y Serge sigue siendo el germen de esa filosofía mediática.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GpCdodqTYtE?si=lIQMClxtxuqhBIvc" title="Reproductor de vídeo de YouTube" frameborder="0" permitir="acelerómetro; reproducción automática; escritura en portapapeles; medios cifrados; giroscopio; imagen en imagen; compartir web" referrerpolicy="origen-estricto-cuando-origen-cruzado" enablefullscreen></iframe>

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/QBVCa3RaR0c?si=VWdNaHjNBMK-r8Mj" title="Reproductor de vídeo de YouTube" frameborder="0" permitir="acelerómetro; reproducción automática; escritura en portapapeles; medios cifrados; giroscopio; imagen en imagen; compartir web" referrerpolicy="origen-estricto-cuando-origen-cruzado" enablefullscreen></iframe>
---

## Conclusión: poética del “voltaje de control”

Se dice que Don Buchler dijo esto antes de su muerte.
> “El voltaje no es un número, es un gesto”.

Sarge también dice.
> “Cada parche es una composición”.

Para ellos, el voltaje no es sólo una señal;
**Era "un lenguaje poético que conecta la voluntad humana y las máquinas".**

Incluso ahora, en 2025, seguimos escuchando la poesía de ese voltaje.

---


