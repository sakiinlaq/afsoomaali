---
layout: page
title: Afka hooyo
permalink: /afkahooyo/
---

## Af Soomaali
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="af Soomaali" %}
<div class="xogtaGuud">

<div class="label"> Cinwaan:</div> <div class="cinwaan"> {{ buug.cinwaan }}</div> <span> class="qoraa">	 {{ buug.qoraa }} </span>
<div class="label"> Sanad:</div> <div class="sanad"> {{ buug.sanad }} </div>
<div class="label"> Warbixin dheeri ah:</div> <div class="warbixin"> {{ buug.handle }} </div>
<div class="label"> link:</div> <div class="link"> {{ buug.pdf }} </div>
</div>

{% endif %}
{% endfor %}