---
layout: page
title: Afka hooyo
permalink: /afkahooyo/
---

## Af Soomaali
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="af Soomaali" %}

<div class="cinwaan"> <a href="{{ buug.pdf }}"> {{ buug.cinwaan }} </a> </div><span class="sanad"> ({{ buug.sanad }}) </span><span class="qoraa">{{ buug.qoraa }} </span> 
 
 <div class="warbixin"> {{ buug.handle }} </div>

{% endif %}
{% endfor %}