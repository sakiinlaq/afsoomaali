---
layout: page
title: Afka hooyo
permalink: /afkahooyo/
---

## Af Soomaali
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="af Soomaali" %}
<a href="{{ buug.pdf }}">
<div class="cinwaan"> {{ buug.cinwaan }}</div> </a>  <span class="qoraa">{{ buug.qoraa }} </span> 
 <div class="sanad"> ({{ buug.sanad }}) </div>
 <div class="warbixin"> {{ buug.handle }} </div>
 <div class="link"> {{ buug.pdf }} </div>

{% endif %}
{% endfor %}