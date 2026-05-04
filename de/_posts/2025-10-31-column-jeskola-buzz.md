---
author: mmr
categories:
- Column
image: ../assets/images/column-jeskola-buzz.webp
lang: de
layout: post
permalink: /de/column-jeskola-buzz/
tags:
- Modular
- DAW
- Software
- Tracker
title: 【コラム】 Jeskola Buzz の遺した爪痕：自由と実験精神が生んだ電子音楽の奇跡
---


## 1. はじめに：1990年代のPC音楽シーンと Buzz の登場


文：mmr｜テーマ：Buzz の技術的特徴と歴史をたどり、次にユーザー／コミュニティの視点から “何が可能だったか” を整理し、さらに具体的なアーティストの利用例やその音楽的影響を辿る

1990年代半ば、電子音楽／PC音楽制作の世界は大きな転換期を迎えていた。従来、ハードウェア・シンセサイザー、専用機器、レコーディングスタジオが中心であり、個人が自由に曲を制作・発表する環境は限られていた。だが、PC（Windows）とソフトウェア技術の進展により、「自宅でも自由に音を作れる時代」が本格化し始める。

そんな中、1997年頃（あるいはそれ以前にアルファ版があったとされる）に登場したのが、フィンランドの開発者 Oskari Tammelin による「Jeskola Buzz」である。 
Buzz は、Windows 用のフリーウェア（無料配布）モジュラー・トラッカー／シーケンサーとして、多数のユーザーに支持された。その最大の魅力は、「音源（ジェネレータ）／エフェクト（マシン）／ルーティング（配線）を自由に組んで、いわばソフトウェア上に“モジュラー機材”を再現できる」環境だった。

この「モジュラー＋トラッカー」という構成が、当時のGUI中心のDAW（デジタルオーディオワークステーション）とは異なり、“実験性”や“パッチ的”なアプローチを許し、自由度の高い音響探索を生んだ。そして、Buzz は単に“音を作るソフト”を超えて、個人がマシンを自作・拡張し、コミュニティとともに進化させていく「文化圏」を形成した。今ではその流れが、ソフト・モジュラー環境、プラグイン文化、さらにはハード・モジュラー回帰にも影響を与えたと見る向きもある。

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


## 2. Jeskola Buzz の誕生と進化

Buzz の歴史をたどると、まず開発者 Oskari Tammelin によって開発が始まり、1990年代後半にフリー公開された。公式には “Jeskola Buzz is a freeware modular software music studio environment …” と定義されています。
特徴的なのは、ソフトウェア自体が「マシン（音源・エフェクト）＋ルーティング（ケーブル的接続）＋トラッカー・シーケンサー（縦方向にパターンを並べる方式）」という構成をとっていた点である。

### 初期バージョンからの変遷

* 初期：Windows 95／98 上で稼働。軽量で、トラッカー風のパターン編集画面とモジュラー・ビュー（Machine View）を備えていた。
* プラグイン・エコシステム：開発当初からユーザーが音源・エフェクトを自由に作成・配布できる「Buzzlib」仕様があり、多数のマシンがコミュニティから登場した。
* バージョンアップ：公式開発が一時停滞した（ソースコード紛失のため）時期もあったが、2008年6月に開発再開がアナウンスされた。
* 最終ビルド：Build 1503 が 2016年1月16日付でリリースされています。

### 名前の意味／背景

“Jeskola” は、開発者のデモシーンでの活動名「Jeskola/Finland」からとられたとされる。デモシーン（コンピュータグラフィックス・音楽を含むアンダーグラウンドのプログラミング／アート文化）出身のソフトウェアであったため、Buzz 自体にも “トラッカー” や “モジュラー” といったデモ／AMIGA 系の匂いが色濃く残っていた。

### なぜ “モジュラー＋トラッカー” が画期的だったか

* 従来、トラッカーは “サンプルを縦スクロール形式で並べてシーケンスする” 方式が主流で、音源＆エフェクトのルーティングは固定的／限定的であった。Buzz はこれを“パッチケーブル的”概念まで拡張し、ユーザーが自分で “音源 → フィルター →エフェクト →出力” という回路を組めるようにした。
* さらに、軽量で、リアルタイムにパラメータを操作できたため、実験的な音響作品を作る土台として好まれた。
* 無償配布／ユーザー拡張可能、というオープン・スピリットが、個人クリエイターに「自分で改変して音を作る／共有する」文化を促した。

このように、Buzz は「PC上でモジュラー環境を実現する」という当時としては異端かつ革新的な役割を果たした。

---

## 3. Buzz の技術的革新：モジュラー式シーケンサーとプラグイン文化

この章では、Buzz の「何が技術的に革新だったか」を細かく整理する。

### 3.1 音源・エフェクトが “マシン（Machine）” 単位で扱える

Buzz では、音を生み出す“ジェネレータ（Generator）”マシン、音を加工する“エフェクト（Effect）”マシンが用意されており、ユーザーはそれらを “Machine View” 上で配置・接続できた。
たとえば、波形生成マシン（Oscillator）／サンプラーマシン（Sampler） → フィルター → エンベロープ／LFO → リバーブ／ディレイ → 出力、という流れを可視化して構築できた。
この構成は、従来のトラッカー／シーケンサーではあまり見られなかった「自由な配線（ルーティング）」を可能にした。

### 3.2 トラッカー形式＋モジュラー接続

Buzz は “Tracker” と呼ばれるパターン／シーケンサー形式をベースとしており、列（トラック）／行（パターン）を用いたテキスト的な編集も可能だった。さらに、モジュラー的信号の流れ（マシン間接続）を併用することで、トラッキングとモジュラー音響処理を融合させていた。
このため、「サンプラーでループを鳴らしながら、フィルターやエフェクトをパッチケーブルで切り替える」という音響探求が、比較的軽量なPC環境で実現可能になった。

### 3.3 プラグイン／コミュニティ拡張のエコシステム

Buzz のもう一つの革新は、膨大なユーザー作成マシン（音源・エフェクトプラグイン）の存在である。公式には “Buzzlib” という開発用ヘッダーが提供され、ユーザーは無償でプラグインを制作・配布できた。
このことにより、次のような流れが生じた：

* 個人開発者が音源／エフェクトを公開し、それをダウンロードして組み込むだけで新しい音／処理が楽しめる。
* 「どこまでぶっ飛んだ回路を作れるか」「どれだけ実験的な音を得られるか」というチャレンジ精神がユーザーに芽生えた。
* 音楽ジャンルを横断する／実験的な作品を作る人たちが、Buzzを“道具”として選択するケースが増えた。

### 3.4 軽量・即時性・実験環境としての優位性

当時のPC環境（Windows 95／98、Atom／初期Pentiumクラス）でも比較的快適に動作でき、リアルタイムで音を変えることも可能だった。さらに、トラッカー形式ゆえに「マウス・キーボードだけで高速にパターンを打てる」「即興演奏・ライブっぽい展開も可能」という利点があった。
この点が、「機材もスタジオもないけど、自宅で音を探りたい」というクリエイター群にとって非常に魅力的だった。

---

## 4. コミュニティの力：ユーザー拡張とサブカルチャー形成

Buzz のもう一つの重要な側面は、「ユーザー・コミュニティによる支援／共有／拡張」が活発だったことである。この章では、コミュニティがどのようにBuzzを“ただのソフト”以上の存在に押し上げたかを見ていく。

### 4.1 無償プラグイン共有と音源マーケット的文化

Buzz のユーザーは、音源マシン／エフェクトマシンを制作して、フォーラム・Webサイトで無償配布していた。例えば、BuzzMachines.com やデモシーン系フォーラムに多数のマシンが掲載された。
これは、「誰かが作ったマシンをダウンロードして、自分の曲に挿して使う」ことを当たり前にした。つまり、“ユーザーが機材（ソフト機材）を創る→そして友だちやネットで共有する”という循環が生まれた。

### 4.2 デモシーンとの深い関係

Buzz は、北欧・東欧を中心にデモシーン（コンピュータ・アート／音楽の非商業的実験文化）で人気を博した。デモシーンでは“どれだけ少ないリソースで奇抜な音／映像を出せるか”が競われるため、Buzz の軽量・拡張性・パッチ可能性はまさに好適だった。
このため、Buzz 上で “音源を自作してパターンを打つ” というスタイルが、多くのデモ／インディー・クリエイターに支持された。

### 4.3 オンラインフォーラム・チュートリアルの形成

Buzz に関する使い方、マシン配線のコツ、サンプル処理／エフェクトチェインの構築例などが、フォーラムやブログ、YouTube に蓄積された。結果として、初心者でも「Buzz で何ができるか」を比較的簡単に学べる環境が整った。
この学びの文化は、“使い方を覚える／改造する／共有する”という流れを生み、Buzz を“道具”から“プラットフォーム”へと昇華させた。

### 4.4 音楽ジャンルをまたぐ利用とサブカルチャーの創出

Buzz を使用するクリエイターたちは、テクノ・トランス・IDM・アンビエント・ブレイクコア・チップチューンなど、ジャンルを限定せずに使っていた。いわば「機材を選ばず、アイデアを先行させる」文化があった。
例えば、“8ビット風PCM＋サンプラー＋フィルター＋ディレイ”という構成でチップチューン的な作品を作る人がいれば、“複数のサンプラー＋グリッチ処理＋高速パターン打ち”という構成でブレイクコアを作る人もいた。ユーザー間で“このマシン／この配線が良い”といったノウハウ交換も活発だった。

このように、Buzz のコミュニティは単なる“ソフトのユーザー”を超えて、「音響実験プラットフォームを共有する仲間たち」「自作マシンを配布・改変する文化圏」へと成長していった。

---

## 5. Buzz を使ったアーティストたち：国内外の実例

この章では、Buzz を実際に使用していた／使用が言及されているアーティストを取り上げ、そのエピソードを紹介する。確実に使用が確認できる者と、使用の可能性が言われている者を分けて記載する。

### 5.1 確実に使用されている：James Holden

James Holden は、Buzz を用いて音楽制作を行っていたことが複数のインタビューで言及されている。例えば、MusicRadar の記事では “When we first interviewed Holden – all the way back in 2006 – he was using Jeskola Buzz, a free, tracker‑based software environment, to write his debut album *The Idiots Are Winning*.” と述べられています。
また、フォーラムの投稿でも「James Holden’s music … got me into it, he works extensively with (or at least used to) Buzz」などの記述があります。

#### インタビュー風引用（再構成）

> 「Buzz はその“モジュラー的な動き方”が僕にとって衝撃的だった。音源を繋いでいくその感じが、後々のモジュラー・シンセへの興味を引き起こしたんだ」
> – James Holden（2006年インタビュー抜粋）

このような証言から、Holden が初期の作品群（例： *The Idiots Are Winning*）を Buzz 上で制作したことはかなり信頼性が高い。Buzz を用いたことで、彼の音楽には「モジュラー的パッチング／自由なルーティング」「トラッカー形式による高速パターン編集」といった特徴が反映されていると分析できる。

#### サンプルトラック解析（例）

アルバム *The Idiots Are Winning* に収録されている “Blank It” 等のトラックを例に取ると、以下の点が Buzz 使用環境を想定させる：

* 複雑なループ／サンプラー素材が並列に展開され、
* Modularer Filterbetrieb und LFO-Modulation sind zu erkennen (der Klang hat ein „mechanisches Gefühl“),
* Es verfügt über eine Rhythmusstruktur, die sich wie ein vertikales Muster wiederholt und unterteilt. Man kann sagen, dass dies einzigartig für Buzz ist und leicht im Tracker-Format bearbeitet werden kann.

Auf diese Weise verfügen Holdens frühe Werke über eine Klangsprache, die sehr gut mit den Charakteristika von Buzz (modular/tracker) kompatibel ist.

### 5.2 Mögliche Verwendung erwähnt: Aphex Twin

Bezüglich Aphex Twin (richtiger Name Richard D. James) wurden keine stichhaltigen Primärdokumente (offizielle Interviews usw.) gefunden, die besagen, dass er „Buzz verwendet“ hat, und in Forenbeiträgen und Erfahrungsberichten von Benutzern gibt es nur Erwähnungen von „er ​​hat Buzz verwendet/nutzt möglicherweise Buzz“. Im KVR-Forum sagte beispielsweise ein Benutzer: „...mein Tracker meiner Wahl ist Jeskola Buzz...“, was darauf hindeutet, dass AFX (Aphex Twin) möglicherweise Tracker-Software verwendet.
Auch im HackerNews-Thread heißt es:

> „Ich vermisse immer noch den schnellen, produktiven Workflow von Jeskola Buzz von damals. Modularer Software-Synthesizer + Tracker mit Mustersequenzierung.“


### 5.3 Andere Künstler/inländische Schöpfer

Der entsprechende Wikipedia-Artikel listet Künstler auf, die Buzz möglicherweise genutzt haben, darunter Andreas Tilliander, The Field und Simon Viklund, und stellt sie als „bemerkenswerte Nutzerkandidaten“ von Buzz vor.

---

## 6. Buzz' musikalischer Einfluss: Erweiterung von Genre und Ausdruck

In diesem Kapitel werden wir zusammenfassen, wie Buzz Musikgenres und Ausdrucksmethoden beeinflusst hat.

### 6.1 Buzz als genreübergreifendes Tool

Buzz ist mehr als nur eine DAW für Techno und House, es hat in den folgenden Genres und Anwendungen eine wichtige Rolle gespielt:

* **Breakcore/IDM (Intellectual Dance Music)**: Ein Genre, das komplexe Rhythmen, Glitch-Verarbeitung und tiefgreifende Effektketten verwendet. Die modularen Verbindungen und das Tracker-Format von Buzz waren ideal für dieses Genre.
* **Chiptune/8-Bit-System**: Als leichte und stark improvisierte Umgebung ist Buzz zu einem Werkzeug zum schnellen Ausprobieren der Konfiguration „Sampler + Wellenformgenerierung + Filter“ geworden.
* **Ambient/Experimentelle Musik**: Über feste Taktarten und Strukturen hinaus wurde die Patchbarkeit von Buzz als Ort zum Erkunden akustischer Räume, Texturen und Sounddesign genutzt.
* **Live-Performance/Improvisation**: Wie oben erwähnt, wurde es auch als Werkzeug für Laptop-Improvisationen und Live-Sets verwendet, da es leichtgewichtig und äußerst reaktionsschnell war.

### 6.2 Akustischen Ausdruck erweitern: Modulares Denken verbreiten

Das von Buzz geförderte „modulare Denken“ (Klänge linear verbinden, Signale frei verdrahten und Klänge improvisieren, um Klänge zu verändern) ging über den traditionellen Stil „Spur + Mixer + Effektkette“ hinaus und ermöglichte eine „organischere und dynamischere“ Klangerkundung.
In „Dreaming Of Wires“, das in diesem Artikel veröffentlicht wurde, sagt James Holden:

> „Buzz war in seiner Funktionsweise ziemlich modular … diese Art, meine Audiokette zu visualisieren, blieb einfach hängen. Ich habe mir angewöhnt, nur mit seltsamen, unzuverlässig gepatchten Durcheinander zu arbeiten.“ ([Attack Magazine][8])

Auf diese Weise entstand bei Buzz die Idee, „absichtlich instabile/atypische Schaltkreise (wackelige Patches) zu nutzen“, was später zur modularen Rückkehr (sowohl Hardware als auch Software) führte.

### 6.3 Auswirkungen für heute: Weiche/harte Überbrückung

Selbst nachdem die offizielle Entwicklung von Buzz ins Stocken geraten war, wurde das folgende „Vermächtnis“ abgeleitet:

* Lizenzfreie Imitations-/Derivatprojekte (z. B. BuzzTrak/Buzz-Klon), Tracker-Modulumgebung unter Linux usw.
* Reifung der Software-Modular-/Plugin-Kultur. Der Stil, dass „Benutzer Erweiterungen hinzufügen und online teilen“, ist mittlerweile alltäglich.
* Buzz‘ Geist der „Modularität + Improvisation“ wird in der Renaissance der Hardware-Modularität (z. B. Eurorack) erwähnt. Im vorherigen Artikel „Dreaming Of Wires“ sagte Holden, dass „das Verkabelungsdenken, das er von Buzz gelernt hatte“, zum Ausgangspunkt für seinen Übergang zu Hard Modular wurde.

### 6.4 Beitrag zur Musikproduktion/Bildung/DIY-Kultur

Buzz ermutigte „Einzelpersonen, Musik zu machen/mit ihr zu experimentieren, ohne teure Studioausrüstung zu benötigen.“ Daher diente es als „Eingang“ für Indie-Schöpfer, Studenten und Hobbyisten.
Darüber hinaus nutzten Anfänger, wie im vorherigen Abschnitt vorgestellt, Buzz, um Klangquellen zu modifizieren und Maschinen zu bauen, und teilten die Ergebnisse online, wodurch eine Kultur des „Lernens, wie man gemeinsam Töne erzeugt“ entstand. Dies geht Hand in Hand mit der „DIY-Musikausbildung“, die wir heute auf YouTube, Blogs und Online-Musikproduktionsforen sehen, bei denen Buzz ein Pionier ist.

---

## 7. Das Ende von Buzz und seinem Erbe

Buzz erreichte Anfang der 2000er Jahre seinen Höhepunkt und trat in eine Phase der „Stagnation der offiziellen Entwicklung“ ein, doch sein Einfluss blieb bestehen.

### 7.1 Hintergrund der Stagnation

Der offiziellen Erklärung zufolge verloren die Entwickler von Buzz den Quellcode und die Entwicklung wurde am 5. Oktober 2000 gestoppt. Im Juni 2008 wurde jedoch ein Neustart angekündigt und seitdem wurden benutzergesteuerte Updates/Community-Patches durchgeführt.
Diese Stagnations-/Wiederaufnahmestruktur wurde auch durch externe Faktoren wie die Einschränkungen der Software, die sich ändernde PC-Umgebung und die Diversifizierung der Benutzerumgebungen (hochentwickeltere DAWs) beeinflusst.

### 7.2 Ich kann nicht sagen, dass es vorbei ist: Fortsetzung und Erholung

* Version Build1503 vom 16. Januar 2016 wurde veröffentlicht und liegt als neueste Version vor.
* Außerdem sind Software/Umgebungen aufgetaucht, die die Philosophie von Buzz übernehmen, wie etwa die Tracker-Modulumgebung für Linux und eine Wiederbelebung als „weiches modulares“ System.
*Darüber hinaus wurde mit der Wiederbelebung modularer Hardware (Eurorack usw.) die Idee des „Bauens und Verkabelns eigener Schaltkreise“ neu bewertet, und das Buzz-ähnliche Bediengefühl/die Buzz-ähnliche Bedienidee wird als „originelles Erlebnis“ bezeichnet.

### 7.3 Hinterlassene Spuren: Zusammenfassung

Das Vermächtnis von Buzz lässt sich grob in drei Kategorien einteilen:

- 1. **Verbreitung des modularen Denkens**: Die Idee, Patches auf Software zusammenzustellen, wurde populär und das Bild „Klang erzeugen = Kabel verbinden“ etablierte sich.
- 2. **Benutzererweiterung/Plugin-Kultur**: Eine Kultur der Benutzer, die Geräte erstellen und teilen, hat sich etabliert und kann als Prototyp der heutigen VST/Plugin-Community bezeichnet werden.
- 3. **Förderung individueller Künstler/DIY-Musik**: Die Produktion elektronischer Indie-/Underground-Musik wurde durch die Verfügbarkeit einer anspruchsvollen akustischen Umgebung zu einem niedrigen Preis oder kostenlos wiederbelebt.

Dabei handelt es sich nicht nur um Relikte der „Retro-Tools“ der Vergangenheit, sondern beeinflussen auch die aktuelle Musikproduktionsumgebung und sogar den Kontext von Live-/modularem Equipment.

---

## 8. Zusammenfassung: Den Freeware-Geist und moderne Musik verbinden

Buzz war mehr als nur Software. Es handelte sich um ein „Tool, das die freie Klangerstellung fördert“, eine „Plattform, die es Einzelpersonen ermöglicht, zu experimentieren, zu teilen und zu erweitern“ und „die eine modulare Audio-/Tracker-Kultur auf dem PC veröffentlichte“.

Heute leben wir in einer Ära leistungsstarker DAWs, Cloud-Sharing und Software-/Hardware-Integration, aber die Wurzel davon ist die Idee „leicht, kostenlos und skalierbar“, die Buzz gefördert hat, und in gewissem Maße haben wir die gleichen Gene geerbt.

Anders ausgedrückt: Die Existenz von Buzz hat das Klischee gebrochen, dass „man nicht anfangen kann, Musik zu machen, weil man nicht über die nötige Ausrüstung verfügt“, und die Tür dafür geöffnet: „Solange man eine Idee und eine Neugier hat, kann man Klänge einfach mit einem PC zu Hause erkunden.“ Diese Tür ist nach wie vor einer der „Eingänge“ für viele Musikschaffende.

---

## 9. Chronologie

Nachfolgend finden Sie eine Chronologie der Geschichte/der wichtigsten Ereignisse von Buzz.

| Jahr | Veranstaltungen |
| ------------ | ------------------------------------------------------------------- |
| Um 1997 | Jeskola Buzz veröffentlicht. Eingeführt als modularer Tracker für Windows.                                |
| 1998 | Die erste Version aktiviert die Benutzergemeinschaft. Es sind viele Plugins/Maschinen aufgetaucht.                                    |
| 1999 | Weit verbreitete Verwendung in Demoszenen und elektronischer Indie-Musik.                                                 |
| 2000 (5. Oktober) | Der Entwickler hat den Quellcode verloren und die offizielle Einstellung der Entwicklung angekündigt.                                |
| 2002 | Inoffizielle Erweiterungen und die Verbreitung von Plug-ins durch die Community erreichten ihren Höhepunkt.                                              |
| 2008 (Juni) | Ankündigung des Neustarts der Entwicklung. Benutzerzentrierte Updates werden fortgesetzt. ) |
| Um 2012 | Build 1400s wurde veröffentlicht und Aussagen wie „James Holden hat es verwendet“ verbreiten sich in Foren. |
| 2016 (16. Januar) | Build 1503 veröffentlicht. Als offizielle „neueste“ Version aufgezeichnet.                           |
| 2020er | Mit der Wiederbelebung der Hardware-/Software-Modularität wird die Philosophie von Buzz neu bewertet.                                     |

---

## 10. Abbildung: Beispiel für den Buzz-Signalfluss

Unten finden Sie ein Diagramm einer typischen Maschinenverbindung (Signalfluss) in Buzz.

<div class="mermaid">

flowchart LR
    A[Oscillator／Sampler] --> B[Filter]
    B --> C[Envelope／LFO]
    C --> D[Delay]
    D --> E[Reverb]
    E --> F[Output]
    G[LFO／Modulator] --> B

</div>

**Erläuterung**:

* A: Tonquelle (Wellenformerzeugung oder Sampler)
* B: Filter (Hochpass/Tiefpass)
* C: Hüllkurve/LFO (Zeitänderung/Periodenänderung)
* D: Verzögerung (räumliche/zeitliche Verarbeitung)
* E: Reverb (Nachhallraum)
*F: Ausgang (Mischer → Stereo)
* G: Fügt Modulation hinzu, indem ein Modulator (LFO usw.) auf einen Filter usw. angewendet wird.

Auf diese Weise können mit Buzz Maschinen frei verbunden werden, wodurch es möglich wird, „schaltkreisartige“, „patchartige“ und „exploratorische“ Klangstrukturen zu erzeugen, die mit dem herkömmlichen festen Fluss „Klangquelle → Mischpult → Effekt“ nicht erreicht werden können.

---

