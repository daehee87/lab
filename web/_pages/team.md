---
title: "PwnLab - People"
layout: gridlay
excerpt: "PwnLab: members"
sitemap: false
permalink: /team/
---

## Professor
{% assign number_printed = 0 %}
{% for member in site.data.prof %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix" style="width: 100%;">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i> {{ member.email }}<br></i>
  <i> <a href='/downloads/cv.pdf'>[Download CV]</a><br></i>
  <ul style="overflow: hidden">
  <li> IT플랫폼안전성연구회 부회장 </li>
  <li> 경희대 융합보안대학원 사업단장 </li>
  <li> 한국우주안보학회 종신회원 </li>
  <li> 한국정보처리학회 이사 </li>
  <li> 세종시핵테온 해킹대회 자문위원 </li>
  <li> 한국디지털포렌식학회 이사 </li>
  <li> 육군본부 정보화분과 자문의원 </li>
  <li> 2023.3 ~ 현재 경희대 컴퓨터공학과 조교수 </li>
  <li> 2021.3 ~ 2023.2 성신여대 융합보안공학과 조교수 </li>
  <li> 2019.5 ~ 2020.12 <a href="https://gts3.org">Georgia Tech</a> 박사후연구원 (Advisor: Prof. Taesoo Kim) </li>
  <li> 2014.3 ~ 2019.2 KAIST 정보보호대학원 석,박사 (Advisor: Prof. Byunghoon Kang) </li>
  <li> 2005.3 ~ 2012.2 한양대학교 컴퓨터공학과 학사 (Cum Laude) </li>
  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


## Research Professor
<div class="row">

<div class="col-sm-6 clearfix" style="width: 100%;">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/kya.jpg" class="img-responsive" width="17%" style="float: left" />
  <h4> Yeongan Kim (김영안) </h4>
  <i> roundsun@khu.ac.kr <br></i>
  <ul style="overflow: hidden">
  <li> 국방전산정보원 과업심의위원 </li>
  <li> ADD, 방위사업청 C4I분야 자문위원 </li>
  <li> 한국정보과학회(종신회원) </li>
  <li> 2019.3~현재 경희대 컴퓨터공학과 학술연구교수 </li>
  <li> 2014.11~2019.2 경희대 컴퓨터공학과 산학협력중점교수 </li>
  <li> 2009.2~2014.10 국방대학교 국방과학학과 교수 </li>
  <li> 1988.3~2014.10 국방부 육군 정보통신 중령 </li>
  <li> 2000.9~2008.2 경희대 컴퓨터공학과 박사(Advisor:Prof. Choonsun Hong) </li>
  <li> 1994.3~1996.3 KEIO University, JAPAN 석사(Advisor:Prof. Masao NAKAGAWA) </li>
  <li> 1984.3~1988.2 국립 금오공과대학교 학사 </li>
  </ul>
</div>
</div>


<!-- **Position open for M.S./Ph.D. Candidates.** [(more info)]({{ site.url }}{{ site.baseurl }}/vacancies) **!** -->

## Researcher/Student
{% assign number_printed = 0 %}
{% for member in site.data.researchers %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>
    {% if member.link %}
      <a href="{{ member.link }}" target="_blank">{{ member.name }}</a>
    {% else %}
      {{ member.name }}
    {% endif %}
  </h4>
  
  <i>{{ member.info }}</i>
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}








## Alumni
{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.duration }} <br>
   역할: {{ member.info }} <br>
   진로: {{ member.result }}
   </i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Staff
<div class="row">
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/joo.png" class="img-responsive" width="25%" style="float: left" />
  <h4>주수민 (산학협력단)</h4>
  <i>email: jj00@khu.ac.kr</i><br>
   역할: 행정지원 <br>
   사무실 번호: 031-201-5345 
  <ul style="overflow: hidden">
  </ul>
</div>
</div>

