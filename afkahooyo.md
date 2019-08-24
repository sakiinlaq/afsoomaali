---
layout: page
title: Afka hooyo
permalink: /afkahooyo/
---


{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="af Soomaali" %}
<h2> {{ buug.cinwaan }}
{% endif %}
{% endfor %}