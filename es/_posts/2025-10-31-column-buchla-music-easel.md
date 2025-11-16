---
author: mmr
categories:
- Column
image: ../assets/images/column-buchla-music-easel.webp
lang: es
layout: post
permalink: /es/column-buchla-music-easel/
tags:
- Buchla
- Modular
- Ambient
title: '[Columna] Buchla Music Easel y la filosofía de la “interpretación solitaria”:
  Redefiniendo la improvisación con sintetizadores analógicos'
---


## Introducción: ¿Qué es el caballete musical Buchla?

Texto: mmr｜Tema: Music Easel, que incluso en los tiempos modernos es elogiado por muchos artistas en vivo como la “orquesta más pequeña que se puede tocar sola”


El **Buchla Music Easel**, que apareció en 1973, es una versión portátil de la famosa **serie Buchla 200** modular analógica.
El diseñador **Don Buchla** llamó al instrumento un "entorno de composición portátil".
No era sólo un pequeño módulo modular, sino que fue concebido como un "dispositivo personal improvisado".

> "Easel es un lienzo sónico. No puedes guardar las líneas que el jugador dibuja en ese momento".
> — Don Buchla

---

<style type="text/css">

mesa, td, th {
borde: 2px #111 sólido;
ancho: automático;
relleno: 10px;
}
th {
color de fondo: #111;
color: #fff;
}
</style>


---

## Capítulo 1: Don Buchla y la Filosofía “Anti-Moog”

A principios de la década de 1960, surgieron dos tendencias importantes en el desarrollo de instrumentos musicales electrónicos en el este y el oeste de América.
Moog al este y Buchla al oeste.
Buchla pretendía "generar" sonido en lugar de "controlarlo".
Se utilizó una placa táctil en lugar de un teclado, y la interpretación se centró en **la tasa de cambio y la contingencia** en lugar del tono.

Su filosofía se trasladó al posterior Music Easel.
El caballete es un instrumento para que los humanos actúen con circuitos electrónicos, y lo que existe allí es la actitud de un "coautor" en lugar de un "intérprete = controlador".

### Análisis técnico: Relación entre forma de onda y sensación táctil.

Buchla pensaba que "manipulación de formas de onda = experiencia táctil".
La siguiente figura es un modelo simplificado de la relación entre FM (modulación de frecuencia) y la salida de forma de onda en Complex Oscillator.

<div class="mermaid">

gráfico TD
A[Oscilador de modulación] -->|Señal FM| B[Oscilador complejo]
B -->|Salida plegada en onda| C[Salida de audio]
B --> D [Timbre armónico CV]
D -->|Voltaje de control| B

</div>

Gracias a esta interconexión, una onda sinusoidal simple tiene una estructura armónica y los pequeños toques durante la interpretación se reflejan inmediatamente en la acústica.

---

## Capítulo 2: Estructura y filosofía de Music Easel

Music Easel consta de dos bloques principales:

- **Fuente de sonido del programa almacenado Buchla 208**
- **Controlador de teclado táctil Buchla 218**

### Diagrama de flujo de señal (sirena)

<div class="mermaid">

gráfico LR
A[Teclado táctil 218] -->|CV/Puerta| B[Oscilador complejo]
B -->|Audio| C[Mezclador y salida]
A -->|Presión CV| D[Oscilador de modulación]
D -->|FM| B
E[Pulsador] -->|Disparador| F[Generador de sobres]
F -->|CV| B
B --> G[Unidad de reverberación]
G --> H [Salida principal]

</div>

Esta estructura le permite completar la generación de reloj → modulación → salida de sonido** por sí solo.
El propio Easel funciona como un "sistema de música completo" sin necesidad de equipos externos.

### Características técnicas

* **Oscilador complejo**: Plegado de formas de onda, FM, AM posible.
* **Pulser**: Genera pulsos periódicos, sirve como reloj.
* **Envelope**: Controlado automáticamente, cerrado, en bucle.
* **Reverberación**: Reverberación natural con reverberación de resorte.

La idea que los integra no es la "portabilidad" sino la "improvisación", y el centro de la producción musical ha pasado del "pensamiento" a la "sensación táctil".

---

## Capítulo 3: El caballete como instrumento en vivo

### Caso 1: Suzanne Ciani “Sesiones de caballete” (2016–)

La legendaria música electrónica **Suzanne Ciani** comenzó su serie en vivo en solitario “Easel Sessions” en Easel en la década de 2010.
Ella elimina las computadoras portátiles y actúa únicamente en Easel.
En la actuación en directo, el tono cambia suavemente con la presión de las manos y la modulación FM fluctúa orgánicamente.
Ciani dice: "Buchla es un instrumento para respirar".

Sónicamente, la **modulación asincrónica** de Easel crea un flujo de armónicos que parece flotar en el espacio.
El público tiene la ilusión de que "se está tocando el aire mismo".

### Análisis de forma de onda: características de la estructura de improvisación

| 要素                          | 技術的要点         | 聴覚印象         |
| --------------------------- | ------------- | ------------ |
| Modulation OscillatorのFM量変化 | 波形が時間的に非線形に変動 | 有機的揺らぎ       |
| Pulser＋Envelope連結           | 拍感を持たない周期の生成  | “呼吸”のような時間感覚 |
| Reverb残響の自己干渉               | 倍音の逆相生成       | 浮遊感・残響的広がり   |

---

## Capítulo 4: Posibilidad de actuación solista y construcción de espacio acústico.

El atractivo de Easel es que la escultura sonora se puede completar sin ningún efecto externo.
Al vincular múltiples modulaciones usando Pulser como disparador,
Es posible crear "patrones mínimos generados" y "estructuras rítmicas aleatorias".

### Caso 2: Charles Cohen “Live at the Rotunda” (2014)

El legendario improvisador de Filadelfia **Charles Cohen** utilizó el caballete musical Buchla durante más de 40 años.
En sus shows en vivo, el concepto de tempo colapsa y Pulser se expande y contrae como si respirara.
Cohen dijo: "El caballete es una herramienta para esculpir el tiempo".

En su interpretación, el plegado de la forma de onda del oscilador complejo hace que los armónicos colapsen y se reproduzcan continuamente.
Produce un sonido que es como si un instrumento acústico se estuviera reconstruyendo.

### Análisis de la tecnología del sonido: la estructura de improvisación de Cohen

<div class="mermaid">

gráfico TD
A[Pulsador] -->|Disparador irregular| B[Sobre]
B -->|Modulación CV| C[Oscilador complejo]
C -->|Audio| D[carpeta de ondas]
D -->|Audio| mi[reverberación]
E -->|Salida estéreo| F[Espacio de audiencia]

</div>

Esta estructura de disparo asíncrona permite que el caballete genere un "surco no medido" por sí solo.
Cohen dice que la música surge simplemente "entregándose" al flujo de la corriente.

---

## Capítulo 5: Artistas contemporáneos y herencia de caballete

### Suzanne Ciani

→ La encarnación del feminismo sonoro. Confío mi físico a la suave corriente eléctrica de Buchla.

### Todd Barton

→ Como educador, explica Easel como "el punto de contacto entre la conciencia y las máquinas".
"No lo reproduzcas, escúchalo interpretándote a ti".

### Charles Cohen

→ El extremo norte de la improvisación. Una actuación en vivo no se trata de música, sino de crear un lugar.
Incluso después de su muerte, Buchla reimprimió su parche como la "Tarjeta del Programa Cohen".

### Kaitlyn Aurelia Smith

→ Integrando la filosofía de Easel con la tecnología digital. Extendiendo las fluctuaciones del sonido natural a la música ambiental moderna.

---

## Capítulo 6: Tecnología y fisicalidad: el acto de “reproducir corriente eléctrica”

Tocar Music Easel no se trata de accionar un interruptor;
**Es el acto de confiar en la velocidad de reacción de un circuito eléctrico**.
La presión, la humedad y la temperatura de las yemas de los dedos afectan el valor CV y ​​cambian el sonido.

En otras palabras, Easel es un instrumento en el que la piel humana se convierte en el circuito.
Los sonidos que existen allí son fenómenos, no datos.

En presentaciones en vivo recientes, las operaciones analógicas de Easel no se convierten a MIDI,
El movimiento para tratarlo como una respuesta puramente actual vuelve a llamar la atención.
Esta tendencia "antidigital" es también una señal de devolver la realidad física a la música electrónica.

---

## Conclusión: El futuro como orquesta

Easel es funcionalmente pequeño y expresivamente ilimitado.
La corriente eléctrica que parpadea en el interior crea un "sonido vivo" en sincronización con la respiración del artista.

Como dijo Charles Cohen, "Easel es un compañero de conversación solitario"
Como ha demostrado Suzanne Ciani, "es el órgano que traduce las emociones humanas en forma electrónica".

En el entorno actual dominado por los portátiles,
Buchla Music Easel sigue siendo una "orquesta solitaria".
Mantiene el futuro de la improvisación escondido dentro de la unidad más pequeña de circuito.

---

## Apéndice: Cronología del caballete musical de Buchla

<div class="mermaid">

línea de tiempo
título Buchla Music Easel Cronología
1963: Don Buchla comienza el desarrollo de la serie Buchla 100 (al mismo tiempo que Moog)
1966: Investigación colaborativa con músicos experimentales en el San Francisco Tape Music Center.
1973: Se presenta el caballete musical (modelo 208/218)
1975 : Primera actuación en directo de Suzanne Ciani y Buchla
1980: Charles Cohen comienza presentaciones improvisadas en vivo usando Easel.
1990: Easel se revaloriza en la escena musical experimental underground.
2013: Lanzamiento de la edición de reimpresión de caballete (BEMI)
2014: Se anuncia Charles Cohen “Live at the Rotunda”
2018: Lanzamiento de Easel Command (208c)
2022: Ampliación del movimiento en vivo Buchla por parte de artistas de nueva generación

</div>

---
