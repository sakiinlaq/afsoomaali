---
layout: page
title: Afka hooyo
permalink: /afkahooyo/
---

## Af Soomaali
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="af Soomaali" %}

<div class="cinwaan"><a href="{{ buug.pdf }}"> {{ buug.cinwaan }} </a> <span class="sanad"> ({{ buug.sanad }}) </span><span class="qoraa">{{ buug.qoraa }} </span> <span class="warbixin"> <a href="{{ buug.handle }}"> Warbixin dheeri </a>> </span> </div>
 
 <div class="warbixin">  </div>

[//]:<div class="cinwaan"> 

{% endif %}
{% endfor %}