---
layout: page
title: Podcast
permalink: /podcast/
lang: en
---

## Monumental Movement Podcast

An audio archive exploring sound, ideology, and cultural movements.  
All episodes are published in **English**.

---

### 🎧 Listen on
- [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-monumentalmovementrecordss-podcast/id1862890079)
- [Spotify](https://open.spotify.com/show/2u98RYjxz8Y8VwsS258Nto)
- [Amazon Music](https://music.amazon.co.jp/podcasts/fa167ede-5eec-4d5f-8134-ee6fe193f324/the-monumentalmovementrecords’s-podcast)
- [RSS Feed](https://feed.podbean.com/monumentalmovementrecords/feed.xml)

---

## Latest Episodes
<ul class="podcast-list">
  {% for post in site.episodes limit:12 %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a><br>
      <small>{{ post.date | date: "%Y.%m.%d" }}</small>
    </li>
  {% endfor %}
</ul>
