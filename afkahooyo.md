---
layout: page
title: Afka hooyo
permalink: /afkahooyo/
---

## Af Soomaali
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="af Soomaali" %}
<div class="xogtaGuud">

<div class="cinwaan"> {{ buug.cinwaan }}<span class="qoraa">{{ buug.qoraa }} </span></div> 
 <div class="sanad"> ({{ buug.sanad }}) </div>
 <div class="warbixin"> {{ buug.handle }} </div>
 <div class="link"> {{ buug.pdf }} </div>
</div>

{% endif %}
{% endfor %}