---
layout: page
title: Afka hooyo
permalink: /afkahooyo/
---

### Af Soomaali
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="af Soomaali" %}
<div class="buugiiba" >

<div class="cinwaan"> {{ buug.cinwaan }} <span class="sanad"> ({{ buug.sanad }}) </span> <a href="{{ buug.pdf }}">pdf </a>  </div>

<div class="qoraWarbixin">
<span class="qoraa">{{ buug.qoraa }} </span> <span class="warbixin"> <a href="{{ buug.handle }}"> handle </a> </span> </div>
</div>

{% endif %}
{% endfor %}



### Murti iyo Sheekooyin
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="sheeko" %}
<div class="buugiiba" >
<div class="cinwaan"> {{ buug.cinwaan }} <span class="sanad"> ({{ buug.sanad }}) </span><a href="{{ buug.pdf }}"> pdf </a> </div>

<div class="qoraWarbixin">
<span class="qoraa">{{ buug.qoraa }} </span> <span class="warbixin"> <a href="{{ buug.handle }}"> handle </a> </span> </div>
 </div>

{% endif %}
{% endfor %}



###  Xisaab
{% for buug in site.data.buugaag-manhaj %}
{% if buug.maado=="xisaab" %}
<div class="buugiiba" >
<div class="cinwaan"> {{ buug.cinwaan }} <span class="sanad"> ({{ buug.sanad }}) </span> <a href="{{ buug.pdf }}">pdf</a> </div>

<div class="qoraWarbixin">
<span class="qoraa">{{ buug.qoraa }} </span> <span class="warbixin"> <a href="{{ buug.handle }}"> handle </a> </span> </div>
 </div>

{% endif %}
{% endfor %}
