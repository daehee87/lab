---
title: "PwnLab - Research"
layout: textlay
excerpt: "PwnLab -- Research"
sitemap: false
permalink: /research/
---

![]({{ site.url }}{{ site.baseurl }}/images/respic/pwn.gif){: style="width: 50%; float: left; margin: 10px 10px"}  저희 연구실에서는 다양한 시스템에 대한 Offensive Security 연구를 수행하고 있습니다. 왼쪽은 [CVE-2018-5200](https://www.boho.or.kr/krcert/secNoticeView.do?bulletin_writing_sequence=30113) RCE 취약점의 Exploit (pwn) 데모 영상입니다. 이러한 RCE 취약점을 공격하는 과정에서 여러가지 시스템 지식 및 익스플로잇 기술을 터득 할 수 있습니다. 예를들어 KMPlayer CVE-2018-5200 의 취약점을 통해 최종 RCE 까지의 Exploit 흐름을 이끌어내는 과정에서 힙 레이아웃 제어 및 힙 스프레이 등에 관한 다양한 연구를 동반하게 됩니다.

**힙 레이아웃 조작:** KMPlayer 가 사용하는 커스텀 힙 할당자는 2가지 size 를 기준으로 bin 을 관리하여 메모리를 할당하는 dl-malloc 스타일의 할당자 입니다. 이 경우 Windows 의 표준 LFH 와는 다르기 때문에, 힙 메모리를 제어함에 있어서 연구가 필요합니다. 예를들어 메모리의 Temporal Locality, Spatial Locality 를 이용하여 메모리 de-fragmentation 을 유발하고, 원하는 객체를 원하는 상대적 위치에 할당되게 유도하는 등과 관련한 연구가 필요합니다.

![]({{ site.url }}{{ site.baseurl }}/images/respic/defrag.png){: style="width: 50%; float: left; margin: 10px 10px"}

**힙 스프레이 방법론:** 힙 스프레이는 Application 및 OS 와 기타 상황에따라 그 전략이 매우 상이할 수 있습니다. 파일 파서와 같은 어플리케이션의 경우 JavaScript 엔진등과 힙스프레이 방법론이 차이나게 되며, 파일내부의 데이터들중 경우에 따라 힙 할당자 대신 MapViewOfFile 등과 같은 형태로 매핑이 되는 이슈, 64bit 운영체제에서 32bit Application 을 실행할때의 가상메모리 공간 레이아웃, 메모리 할당에 관한 입상도 (Alignment) 등 다양한 연구들이 취약점 분석 및 Exploit 개발을 위해서 필요합니다.


<br>


![]({{ site.url }}{{ site.baseurl }}/images/respic/pwn2.gif){: style="width: 50%; float: right; margin: 10px  10px"}
오른쪽은 한컴오피스 문서파싱 프로그램의 RCE 취약점 Exploit 데모 영상입니다. 해당 버그는 힙 메모리에서의 Use-After-Free 와 같은
취약점으로 인해 발생하게 되며, 이러한 버그를 RCE 까지 이끌어내는 과정에서는 Reverse Engineering (역공학) 이 필요하고, 효과적인
역공학을 수행하기 위해서는 메모리 분석, 어셈블리 코드 분석, 디버거의 사용법 등도 중요하지만 무엇보다도 풍부한 소프트웨어 개발에 관한 심도있는 경험 및 지식이 필요합니다.
예를 들어, 메모리 레이아웃과 어셈블리코드를 디버거를 통해서 열심히 분석한다고 해도 소프트웨어에 대한 개발경험이 부족하다면
분석대상 바이너리가 어떠한 개발환경을 통해서 제작된 것인지 알기 어려우며, 이것은 역공학을 통한 프로그램의 로직을
이해하는데 어려움을 주게 됩니다.

또한 역공학을 통해서 Exploit 을 개발하기 위해서는 기본적인 프로그래밍 능력이 요구됩니다. 왼쪽의 코드는 데모영상에서 사용된 RCE 를 수행하게 해주는 조작된 문서파일을
생성하기 위한 파이썬 코드의 일부분 예시를 보여줍니다. 이러한 <U>Exploit 코드개발을 통해서 소프트웨어의 내부 동작 과정 및 프로그래밍의 원리등을
심도있게 연구 할 수 있습니다.</U> 

![]({{ site.url }}{{ site.baseurl }}/images/respic/code.png){: style="width: 50%; float: left; margin: 10px 10px"}

<br>


위와 같은 메모리 버그로 인한 보안 취약점들은 Fuzzing 이라는 방법으로 탐색을 자동화 할 수 있으며 이와 관련해서 수많은
연구들이 수행되고 있습니다. [Fuzzing@Home](http://fuzzcoin.gtisc.gatech.edu:8000) 은 이러한 Fuzzing 프로그램을
비신뢰 이기종 단말로 구성된 분산 컴퓨팅 네트워크에서 효율적으로 수행할 수 있는 인프라를 구축한 연구입니다. 아래의 그림은
Fuzzing@Home 시스템의 일부분으로, Google 의 libfuzzer 를 Web Assembly 바이너리로 포팅하여 웹 브라우저 엔진 내부에서
실행시킬 수 있도록 한 것을 나타냅니다.

![]({{ site.url }}{{ site.baseurl }}/images/respic/fuzzhome2.png){: style="width: 95%; float: center; margin: 10px 10px"}

<br>

현재 퍼징을 통해 Google 에서는 수많은 메모리 버그들을 자동적으로 발견하고 패치하고 있습니다. 또한, 컴파일러 보안 기술의 발달로 인해
대다수의 메모리 버그들은 점점더 RCE Exploit 단계까지 가는데에 어려움이 있습니다. 저희 연구실에서는 전통적인 메모리 버그에 관한
연구 뿐 만 아니라, 앞으로 IT 시장에서 클라우드 서버 기반의 서비스 비중이 커질 것을 예상하여 <U>가상화 및 Container, SandBox 에 관한 보안문제, 임베디드 시스템
및 드론시스템 등 여러가지 시스템에서 구성요소들 간의 상호작용에서 발생 할 수 있는 로직버그를 효과적으로 발견하기 위한 연구들</U> 또한 중점적으로 수행합니다.




