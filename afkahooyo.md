---
layout: page
title: Afka hooyo
permalink: /afkahooyo/
---

## Af Soomaali
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="af Soomaali" %}
<ul type="disc">
<div class="cinwaan"><a href="{{ buug.pdf }}"> {{ buug.cinwaan }} </a> <span class="sanad"> ({{ buug.sanad }}) </span> </div> <span class="qoraa">{{ buug.qoraa }} </span> <span class="warbixin"> <a href="{{ buug.handle }}"> Warbixin dheeri ah </a> </span> 
 </ul>

{% endif %}
{% endfor %}



## Murti iyo Sheekooyin
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="sheeko" %}
<ul type="disc">
<div class="cinwaan"><a href="{{ buug.pdf }}"> {{ buug.cinwaan }} </a> <span class="sanad"> ({{ buug.sanad }}) </span></div><span class="qoraa">{{ buug.qoraa }} </span> <span class="warbixin"> <a href="{{ buug.handle }}"> Warbixin dheeri ah </a> </span> 
 </ul>

{% endif %}
{% endfor %}



##  Xisaab
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="xisaab" %}
<ul type="disc">
<div class="cinwaan"><a href="{{ buug.pdf }}"> {{ buug.cinwaan }} </a> <span class="sanad"> ({{ buug.sanad }}) </span></div><span class="qoraa">{{ buug.qoraa }} </span> <span class="warbixin"> <a href="{{ buug.handle }}"> Warbixin dheeri ah </a> </span> 
 </ul>

{% endif %}
{% endfor %}

