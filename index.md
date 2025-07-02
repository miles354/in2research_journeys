---
layout: default
title: In2research Journeys
---


{% comment %}
To inspect a variable you can do:
{{this_year | inspect}}

Note that this_year is a string, but is converted as number adding 0
{% endcomment %}

{% assign authors_year = 0 | plus: 0 %}
{% assign authors_names = "" | split: "," %}
{% assign this_year = site.time | date: '%Y' | plus: 0 %}

{% for author in site.authors %}
  {% if author.year == this_year %}
	{% assign authors_year = authors_year | plus: 1 %}
	{% assign authors_names = authors_names | push: author.name %}
  {% endif %}
{% endfor %}

Welcome to this [In2research](https://in2scienceuk.org/our-programmes/in2research/) Journeys at ARC blog where ARC's placement students post a weekly summary of their experience while they learn. This year {{this_year}} we've got {{authors_year}} students: {{authors_names | short_natural | join: ", "}}.
	
You can subscribe to our [RSS feed]({{"feed.xml" | prepend: baseurl}}) if you'd like to get them on your favourite reader.
	
  <p>
{% if site.posts.size > 0 %}
  <h2>Latests Blog Posts</h2>
  <ul class="posts">
    {% assign count = 0 %}
    {% for post in site.posts %}
      {% assign count = count | plus: 1 %}
      {% if count <= 5 %}
        {% for author in site.authors %}
          {% if author.short_name == post.author %}
            {% assign author_url = author.url | prepend:site.baseurl %}
            {% assign post_url = post.url | prepend:site.baseurl %}
            <!-- TODO: add photo of the author -->
            <li><span>{{ post.date | date_to_string }}</span> &raquo; <span><a href="{{ author_url }}.html">{{ post.author }}</a></span> &raquo;  <a href="{{ post_url }}">{{ post.title }}</a>
            <p class="entry">{{ post.content | strip_html | truncate:250 }}
              <a href="{{ post_url }}">Read more...</a>
            </p>
            </li>
          {% endif %}
        {% endfor %}
      {% endif %}
    {% endfor %}
  </ul>
{% endif %}

{% if site.categories.size > 0 %}
<h2> categories </h2>
<ul class="tags">
  <!-- From http://vvv.tobiassjosten.net/jekyll/jekyll-tag-cloud/ -->
{% for category in site.categories %}
<li style="font-size: {{category | last | size | times: 100 | divided_by: site.categories.size | plus: 70 }}%">
<a href="{{site.baseurl}}/categories.html#{{ category | first | slugize }}">
  {{ category | first }}
</a>
</li>
{% endfor %}
</ul>

{% endif %}
