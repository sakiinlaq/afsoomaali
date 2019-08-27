---
layout: page
title: Afka hooyo
permalink: /afkahooyo/
---

## Af Soomaali
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="af Soomaali" %}
<h2> {{ buug.cinwaan }}
	Qoraa: {{ buug.qoraa }}
	Sanad: {{ buug.sanad }}
	Warbixin dheeri ah: {{ buug.handle }}
	link: {{ pdf }}
{% endif %}
{% endfor %}