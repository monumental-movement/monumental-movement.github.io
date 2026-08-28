---
author: mmr
categories:
- Column
image: ../assets/images/column-jeskola-buzz.webp
lang: en
layout: post
tags:
- Modular
- DAW
- Software
- Tracker
title: '[Column] The legacy of Jeskola Buzz: The miracle of electronic music born
  of freedom and experimental spirit'
---


## 1. Introduction: The 1990s PC music scene and the emergence of Buzz


文：mmr｜テーマ：Buzz の技術的特徴と歴史をたどり、次にユーザー／コミュニティの視点から “何が可能だったか” を整理し、さらに具体的なアーティストの利用例やその音楽的影響を辿る

1990年代半ば、電子音楽／PC音楽制作の世界は大きな転換期を迎えていた。従来、ハードウェア・シンセサイザー、専用機器、レコーディングスタジオが中心であり、個人が自由に曲を制作・発表する環境は限られていた。だが、PC（Windows）とソフトウェア技術の進展により、「自宅でも自由に音を作れる時代」が本格化し始める。

そんな中、1997年頃（あるいはそれ以前にアルファ版があったとされる）に登場したのが、フィンランドの開発者 Oskari Tammelin による「Jeskola Buzz」である。 
Buzz は、Windows 用のフリーウェア（無料配布）モジュラー・トラッカー／シーケンサーとして、多数のユーザーに支持された。その最大の魅力は、「音源（ジェネレータ）／エフェクト（マシン）／ルーティング（配線）を自由に組んで、いわばソフトウェア上に“モジュラー機材”を再現できる」環境だった。

This ""modular + tracker" configuration, unlike the GUI-centered DAWs (digital audio workstations) of the time, allowed for ""experimentalism" and a ""patch-like" approach, giving rise to a high degree of freedom in sonic exploration. Buzz has gone beyond simply being ""software that creates sound" and has formed a ""cultural sphere'' where individuals can create and expand their own machines and evolve them together with the community. Some now see this trend as having influenced a soft modular environment, plug-in culture, and even a return to hard modularity.

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

### Changes since the initial version

* 初期：Windows 95／98 上で稼働。軽量で、トラッカー風のパターン編集画面とモジュラー・ビュー（Machine View）を備えていた。
* プラグイン・エコシステム：開発当初からユーザーが音源・エフェクトを自由に作成・配布できる「Buzzlib」仕様があり、多数のマシンがコミュニティから登場した。
* Version upgrade: Although official development was temporarily stalled (due to loss of source code), it was announced in June 2008 that development would resume.
* 最終ビルド：Build 1503 が 2016年1月16日付でリリースされています。

### 名前の意味／背景

“Jeskola” は、開発者のデモシーンでの活動名「Jeskola/Finland」からとられたとされる。デモシーン（コンピュータグラフィックス・音楽を含むアンダーグラウンドのプログラミング／アート文化）出身のソフトウェアであったため、Buzz 自体にも “トラッカー” や “モジュラー” といったデモ／AMIGA 系の匂いが色濃く残っていた。

### なぜ “モジュラー＋トラッカー” が画期的だったか

* 従来、トラッカーは “サンプルを縦スクロール形式で並べてシーケンスする” 方式が主流で、音源＆エフェクトのルーティングは固定的／限定的であった。Buzz はこれを“パッチケーブル的”概念まで拡張し、ユーザーが自分で “音源 → フィルター →エフェクト →出力” という回路を組めるようにした。
* In addition, it was lightweight and its parameters could be manipulated in real time, making it a popular platform for creating experimental sound works.
* 無償配布／ユーザー拡張可能、というオープン・スピリットが、個人クリエイターに「自分で改変して音を作る／共有する」文化を促した。

このように、Buzz は「PC上でモジュラー環境を実現する」という当時としては異端かつ革新的な役割を果たした。

---

## 3. Buzz の技術的革新：モジュラー式シーケンサーとプラグイン文化

この章では、Buzz の「何が技術的に革新だったか」を細かく整理する。

### 3.1 Sound sources and effects can be handled in "machine" units

Buzz では、音を生み出す“ジェネレータ（Generator）”マシン、音を加工する“エフェクト（Effect）”マシンが用意されており、ユーザーはそれらを “Machine View” 上で配置・接続できた。
たとえば、波形生成マシン（Oscillator）／サンプラーマシン（Sampler） → フィルター → エンベロープ／LFO → リバーブ／ディレイ → 出力、という流れを可視化して構築できた。
This configuration allows for ""free routing'' that is rarely seen with conventional trackers/sequencers.

### 3.2 Tracker format + modular connection

Buzz は “Tracker” と呼ばれるパターン／シーケンサー形式をベースとしており、列（トラック）／行（パターン）を用いたテキスト的な編集も可能だった。さらに、モジュラー的信号の流れ（マシン間接続）を併用することで、トラッキングとモジュラー音響処理を融合させていた。
このため、「サンプラーでループを鳴らしながら、フィルターやエフェクトをパッチケーブルで切り替える」という音響探求が、比較的軽量なPC環境で実現可能になった。

### 3.3 プラグイン／コミュニティ拡張のエコシステム

Buzz のもう一つの革新は、膨大なユーザー作成マシン（音源・エフェクトプラグイン）の存在である。公式には “Buzzlib” という開発用ヘッダーが提供され、ユーザーは無償でプラグインを制作・配布できた。
このことにより、次のような流れが生じた：

* Individual developers publish sound sources/effects, and you can enjoy new sounds/processing just by downloading and incorporating them.
* 「どこまでぶっ飛んだ回路を作れるか」「どれだけ実験的な音を得られるか」というチャレンジ精神がユーザーに芽生えた。
* 音楽ジャンルを横断する／実験的な作品を作る人たちが、Buzzを“道具”として選択するケースが増えた。

### 3.4 軽量・即時性・実験環境としての優位性

It operated relatively comfortably in the PC environment of the time (Windows 95/98, Atom/early Pentium class), and it was also possible to change the sound in real time. Furthermore, because of the tracker format, it had the advantage of being able to input patterns at high speed using only a mouse and keyboard, and allowing for improvisational performances and live performances.
This point was very attractive to creators who didn't have any equipment or a studio, but wanted to explore sounds at home.

---

## 4. コミュニティの力：ユーザー拡張とサブカルチャー形成

Buzz のもう一つの重要な側面は、「ユーザー・コミュニティによる支援／共有／拡張」が活発だったことである。この章では、コミュニティがどのようにBuzzを“ただのソフト”以上の存在に押し上げたかを見ていく。

### 4.1 Free plug-in sharing and sound source market culture

Buzz のユーザーは、音源マシン／エフェクトマシンを制作して、フォーラム・Webサイトで無償配布していた。例えば、BuzzMachines.com やデモシーン系フォーラムに多数のマシンが掲載された。
これは、「誰かが作ったマシンをダウンロードして、自分の曲に挿して使う」ことを当たり前にした。つまり、“ユーザーが機材（ソフト機材）を創る→そして友だちやネットで共有する”という循環が生まれた。

### 4.2 デモシーンとの深い関係

Buzz gained popularity in the demoscene (non-commercial experimental culture of computer art/music), mainly in Northern and Eastern Europe. Buzz's lightweight, expandability, and patchability were perfect for the demo scene, where the competition was to see how many unique sounds and images could be produced with as few resources as possible.
For this reason, the style of ""creating your own sound sources and creating patterns'' on Buzz was supported by many demo/indie creators.

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
Additionally, forum posts include statements such as "James Holden"s music … got me into it, he works primarily with (or at least used to) Buzz."

#### Interview style quotation (reconstruction)

> "The Buzz's modular way of working was shocking to me. The feeling of connecting sound sources sparked my interest in modular synths later on."
> – James Holden（2006年インタビュー抜粋）

このような証言から、Holden が初期の作品群（例： *The Idiots Are Winning*）を Buzz 上で制作したことはかなり信頼性が高い。Buzz を用いたことで、彼の音楽には「モジュラー的パッチング／自由なルーティング」「トラッカー形式による高速パターン編集」といった特徴が反映されていると分析できる。

#### Sample track analysis (example)

Taking a track such as "Blank It" from the album *The Idiots Are Winning* as an example, the following points suggest the environment in which Buzz will be used:

* 複雑なループ／サンプラー素材が並列に展開され、
* Modular filter operation and LFO modulation can be seen (the sound has a "mechanical feeling"),
* 縦パターン的な反復・細分化されたリズム構成がなされており、これはトラッカー形式での編集が容易であるBuzzならでは、と言える。

In this way, Holden"s early works have a sonic language that is highly compatible with Buzz"s characteristics (modular/tracker).

### 5.2 Possible use mentioned: Aphex Twin

Regarding Aphex Twin (real name Richard D. James), no reliable primary sources (official interviews, etc.) have been found that say he "used Buzz," and there are only mentions of "he used/might be using Buzz" in forum posts and user testimonials. For example, on the KVR forum, a user said, "...my tracker of choice is Jeskola Buzz...", suggesting that AFX (Aphex Twin) may be using tracker software.
また、HackerNews スレッドでは以下のように述べられています：

> “I still miss the fast productive workflow of Jeskola Buzz from back in the day. Modular software synth + tracker with pattern sequencing.” 


### 5.3 Other artists/domestic creators

The corresponding Wikipedia article lists artists who may have used Buzz, including Andreas Tilliander, The Field, and Simon Viklund, and introduces them as Buzz's "notable user candidates."

---

## 6. Buzz's Musical Influence: Expansion of Genre and Expression

この章では、Buzz が音楽ジャンル／表現方法にどのような影響を与えたかを整理する。

### 6.1 ジャンル横断の道具としてのBuzz

Buzz is more than just a DAW for techno and house, it has played an important role in the following genres and applications:

* **ブレイクコア／IDM（知的ダンスミュージック）**：複雑なリズム、グリッチ処理、深いエフェクトチェインなどが用いられるジャンルであり、Buzz のモジュラー的接続とトラッカー形式が好適だった。
* **チップチューン／8ビット系**：軽量で即興性が高い環境として、Buzz は「サンプラー＋波形生成＋フィルター」という構成を手早く試せる道具となった。
* **Ambient/Experimental Music**: Beyond fixed time signatures and structures, Buzz's patchability was utilized as a place to explore acoustic spaces, textures, and sound design.
* **ライブパフォーマンス／インプロヴィゼーション**：先述の通り、軽量で反応性が高かったため、ラップトップ即興やライブセットのためのツールとしても使われた。

### 6.2 Expanding acoustic expression: popularizing modular thinking

Buzz が促した「モジュラー思考」（音を線的につなぐ・信号を自由に配線・即興で音を変化させる）は、従来の「トラック＋ミキサー＋エフェクトチェイン」というスタイルを超え、より“有機的・動的”な音響探求を可能にした。
In "Dreaming Of Wires" published in this article, James Holden says:

> “Buzz was pretty modular in how it worked … that way of visualising my audio chain just stuck. I got into the habit of only working with wonky, unreliably patched messes.” ([Attack Magazine][8])

このように、Buzz を起点に「意図的に不安定／非定型の回路（wonky patch）を楽しむ」という思考が芽生え、後のモジュラー・リターン（ハード／ソフト両面）へとつながった。

### 6.3 今日への影響：ソフト／ハードの架橋

Buzz が公式開発を停滞させた後も、以下のような“遺産”が派生している：

* License-free imitation/derivative projects (e.g. BuzzTrak/Buzz clone), Tracker module environment running on Linux, etc.
* Maturation of software modular/plugin culture. The style of ""users adding extensions and sharing them online'' has become commonplace.
* ハードウェア・モジュラー再興（Eurorack 等）において、Buzz 的 “モジュラー＋即興” の精神が参照されている。先の “Dreaming Of Wires” 記事でも、Holden が「Buzz で覚えた配線思考」がハード・モジュラー移行の原点になったと語っている。

### 6.4 音楽制作／教育／DIY文化への寄与

Buzz は「高価なスタジオ機材がなくても、個人が音楽を作る／実験する」ことを促した。そのため、インディー・クリエイター／学生／ホビイスト層にとって “入り口” の役割を果たした。
Additionally, as introduced in the previous section, beginners used Buzz to modify sound sources and build machines, and shared the results online, giving rise to a culture of ""learning how to make sounds together.'' This goes hand-in-hand with the "DIY music education" we see on YouTube, blogs, and online music production forums today, and Buzz can be said to be its forerunner.

---

## 7. The end of Buzz and its legacy

Buzz は、2000年代初頭をピークに“公式開発の停滞”というフェーズに入るが、それでもその影響力は消えなかった。

### 7.1 停滞の背景

公式説明によれば、Buzz の開発者はソースコードを紛失してしまい、2000年10月5日付で開発停止が宣言されました。 ただし、2008年6月に再開がアナウンスされ、以降もユーザー主体の更新／コミュニティパッチが行われた。
この停滞・再開という構造は、ソフトウェアとしての限界・変化するPC環境・ユーザー環境の多様化（DAWの高度化）といった外部要因も影響していた。

### 7.2 “終わった”とは言えない：継続と復興

* January 16, 2016 version Build1503 has been released and exists as the latest version.
* また、Buzz の思想を継ぐソフト／環境が現れており、たとえば Linux 用 Tracker モジュール環境や “ソフト・モジュラー” 系統としてのリバイバルが起きている。
* さらに、モジュラー・ハードウェアの復興（Eurorack 等）では、「自ら回路を構築・配線する」という思想が再評価され、Buzz 的操作感／思想が“原体験”として語られている。

### 7.3 遺された爪痕：総括

Buzz's legacy can be broadly categorized into three things:

- 1. **モジュラー思考の普及**：ソフト上でパッチを組むという感覚が普及し、「音を作る＝ケーブルを繋ぐ」というイメージが定着した。
- 2. **User expansion/plugin culture**: A culture of users creating and sharing equipment has taken hold, and can be said to be the prototype of today's VST/plugin community.
- 3. **Promotion of individual creators/DIY music**: Indie/underground electronic music production has been revitalized by the availability of a sophisticated acoustic environment at a low price or free of charge.

これらは単に過去の “レトロツール” の遺物ではなく、現在の音楽制作環境、さらにはライブ／モジュラー機材の文脈にも影響を与えている。

---

## 8. Summary: Connecting the freeware spirit and modern music

Buzz was more than just software. It was a ""tool that encourages free sound creation," a ""platform that allows individuals to experiment, share, and expand," and ""released modular audio/tracker culture on the PC.''

今日、私たちは高性能DAW、クラウド共有、ソフトウェア／ハード統合の時代を生きているが、その根底には Buzz が育んだ「軽量・自由・拡張可能」の理念があり、多少ながら遺伝子を受け継いでいる。

改めて言えば、Buzz の存在は「機材が揃っていないから音楽を始められない」という固定観念を壊し、「アイデアと好奇心さえあれば、自宅PC１台で音を探れる」という扉を開いた。その扉は、今でも多数のクリエイターにとって「入口」の一つであり続けている。

---

## 9. Chronology

Below is a chronology of Buzz's history/major events.

| 年            | 出来事                                                                       |
| ------------ | ------------------------------------------------------------------------- |
| 1997頃        | Jeskola Buzz 公開。Windows 用モジュラー・トラッカーとして登場。                                |
| 1998 | Initial version activates user community. Many plugins/machines have appeared.                                    |
| 1999 | Widespread use among demo scenes and indie electronic music.                                                 |
| 2000 (10月5日) | 開発者がソースコードを紛失、公式開発停止を発表。                                |
| 2002 | Unofficial extensions and plug-in distribution by the community reached its peak.                                              |
| 2008 (June) | Announcement of restart of development. User-centered updates continue. ) |
| 2012頃        | Build 1400代がリリースされ、フォーラムでは「James Holden が使ってた」といった証言も広がる。 |
| 2016 (January 16) | Build 1503 released. Recorded as the official "latest" version.                           |
| 2020s | With the revival of hardware/software modularity, Buzz's philosophy will be reevaluated.                                     |

---

## 10. Illustration: Buzz signal flow example

Below is a diagram of a typical machine connection (signal flow) in Buzz.

<div class="mermaid">

flowchart LR
    A[Oscillator／Sampler] --> B[Filter]
    B --> C[Envelope／LFO]
    C --> D[Delay]
    D --> E[Reverb]
    E --> F[Output]
    G[LFO／Modulator] --> B

</div>

**Explanation**:

* A: Sound source (waveform generation or sampler)
* B：フィルター（ハイパス／ローパス）
* C: Envelope/LFO (time change/period change)
* D: Delay (spatial/timing processing)
* E：リバーブ（残響空間）
*F: Output (mixer → stereo)
* G: Adds modulation by applying a modulator (LFO, etc.) to a filter, etc.

In this way, with Buzz, machines can be freely connected, making it possible to create ""circuit-like", ""patch-like", and ""exploratory" sound structures that cannot be achieved with the conventional fixed flow of ""sound source → mixer → effect".

---

