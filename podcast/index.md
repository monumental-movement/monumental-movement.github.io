---
layout: podcast
title: Podcast
image: ../assets/images/podcast-top.webp
permalink: /podcast/
lang: en
comments: false
---

## Monumental Movement Podcast

An audio archive exploring sound, ideology, and cultural movements.  
All episodes are published in **English**.
Subtitles and translation are available on YouTube for global listeners.

---

### 🎧 Listen on
- [YouTube Podcasts](https://www.youtube.com/@MonumentalMovementRecords)
- [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-monumentalmovementrecordss-podcast/id1862890079)
- [Spotify](https://open.spotify.com/show/2u98RYjxz8Y8VwsS258Nto)
- [Amazon Music](https://music.amazon.co.jp/podcasts/fa167ede-5eec-4d5f-8134-ee6fe193f324/the-monumentalmovementrecords’s-podcast)
- [RSS Feed](https://feed.podbean.com/monumentalmovementrecords/feed.xml)

---

## Latest Episodes
<div class="episode-grid">
  {% assign episodes = site.episodes | sort: "date" | reverse %}
  {% for post in episodes limit:999 %}
    {% if post.lang == "en" %}
    <article class="episode-card">
      <a class="episode-link" href="{{ post.url }}">
        <div class="episode-meta">
          <time datetime="{{ post.date | date_to_xmlschema }}">
            {{ post.date | date: "%Y.%m.%d" }}
          </time>
        </div>
        <h3 class="episode-title">{{ post.title }}</h3>

        {% if post.description %}
        <p class="episode-desc">
          {{ post.description | truncate: 140 }}
        </p>
        {% endif %}
      </a>
    </article>
    {% endif %}
  {% endfor %}
</div>

