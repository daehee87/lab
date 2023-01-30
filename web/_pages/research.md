---
title: "PwnLab - Research"
layout: textlay
excerpt: "PwnLab -- Research"
sitemap: false
permalink: /research/
---

## Pwnable and Exploitation

![]({{ site.url }}{{ site.baseurl }}/images/respic/pwn.gif){: style="width: 400px; float: left; margin: 10px 10px 10px 0px"}  저희 연구실에서는 다양한 시스템에 대한 Offensive Security 연구를 수행하고 있습니다. 다음은 [CVE-2018-5200](https://www.boho.or.kr/krcert/secNoticeView.do?bulletin_writing_sequence=30113) RCE 취약점의 Exploitation (pwn) Proof-of-Concept 데모 영상입니다. 이러한 RCE 취약점을 공격하는 과정에서 여러가지 시스템 지식 및 익스플로잇 기술을 터득 할 수 있습니다. 예를들어 KMPlayer CVE-2018-5200 의 취약점을 통해 최종 RCE 까지의 Exploit 흐름을 이끌어내는 과정은 
메모리 취약점에 대한 이해 뿐만 아니라 파일 및 프로세스의 메모리 구조, 힙 레이아웃 제어방법 및 힙 스프레이 방법론, 운영체제/아키텍쳐별 쉘코드 작성방법 등에 관한 다양한 연구를 동반하게 됩니다.

<br>

**힙 레이아웃 조작:** KMPlayer 가 사용하는 커스텀 힙 할당자는 2가지 size 를 기준으로 bin 을 관리하여 메모리를 할당하는 dl-malloc 스타일의 할당자 입니다. 이 경우 Windows 의 표준 LFH 와는 메모리 할당 순서 등이 다르기 때문에, 힙 메모리를 원하는 형태로 제어하기 위해서 추가적인 알고리즘 분석 및 연구가 필요합니다. 예를들어 다음 그림에서 묘사하는 것과 같이 메모리의 Temporal Locality, Spatial Locality 를 이용하여 메모리 de-fragmentation 을 유발하고, 원하는 객체를 원하는 상대 위치에 할당되도록 유도하는 등, 다양한 연구가 필요합니다.

![]({{ site.url }}{{ site.baseurl }}/images/respic/defrag.png){: style="width: 400px; float: right; margin: 10px 0px 10px 10px"}

**힙 스프레이 방법론:** 힙 스프레이는 메모리 버그를 통한 Exploit 을 개발할때 필요한 기술중 하나이며, Application/OS 특성과 기타 시스템 상황에따라 그 방법론이 매우 상이할 수 있습니다. 예를 들어 파일 파서는 직접적으로 명령어를 실행하여 메모리 할당을 유도할 수 없고, 파일의 내용을 통해 간접적으로 힙 할당을 유도해야 하는 반면와 JavaScript 엔진과 같은 구문해석기는 직접적으로 메모리 사용을 유발하는 관련함수를 호출하여 힙 할당 및 해제를 유도할 수 있습니다. 힙 스프레이 분석 과정에서 다양한 메모리 할당 알고리즘, Garbage Collection, 메모리 할당 입상도 (Granularity/Alignment) 문제 등 시스템 심화 내용들에 대한 연구가 요구됩니다. 이러한 연구들 중 일반화 할 수 있는 내용들의 경우 논문화 할 수 있습니다. 이와같은 방향의 연구를 시작하기에 가장 좋은 출발점은 재미있는 Wargame 을 찾아서 경쟁적으로 점수를 얻기위해 노력하는 것입니다.

<br>

![]({{ site.url }}{{ site.baseurl }}/images/respic/pwn2.gif){: style="width: 400px; float: left; margin: 10px 10px 10px 0px"}
다음 영상은 한컴오피스 문서파싱 프로그램의 RCE 취약점 Exploit 데모 영상입니다. 해당 버그는 힙 메모리에서의 Use-After-Free 와 같은
취약점으로 인해 발생하게 되며, 이러한 버그를 RCE 까지 이끌어내는 과정에서는 Reverse Engineering (역공학) 이 필요합니다. 효과적인
역공학을 수행하기 위해서는 메모리 분석, 어셈블리 코드 분석, 디버거의 사용법 등도 중요하지만 무엇보다도 프로그래밍 및 소프트웨어 개발에 관한 다양한 경험이 필요합니다.
예를 들어, 메모리 레이아웃과 어셈블리코드를 디버거를 통해서 열심히 분석한다고 해도 소프트웨어에 대한 개발경험이 부족하다면
분석대상 바이너리가 어떠한 개발환경을 통해서 제작된 것인지 알기 어려우며, 이것은 역공학을 통한 프로그램의 로직을
이해하는데 어려움을 주게 됩니다.

![]({{ site.url }}{{ site.baseurl }}/images/respic/code.png){: style="width: 400px; float: right; margin: 10px 0px 10px 10px"}

뿐만 아니라 취약점의 발견, Exploit 개발등을 위해서도 프로그래밍 능력과 소프트웨어 개발능력이 중요하게 요구됩니다. 
다음 코드는 데모영상의 Exploit에 사용된 문서파일을 생성하는 파이썬 코드의 일부분 예시를 보여줍니다. 
예시 코드를 보면, 기계어 Hex 코드로부터 쉘코드를 준비하는 부분부터, 메모리상의 데이터를 여러가지 형태로 변환하고 다루기위한 
라이브러리 사용, 취약점을 발현시키는 데이터 생성을 위한 자료구조 파악 및 디버깅 정보 생성 등 
다양한 종류의 프로그래밍이 요구 됩니다.
저희 연구실에서 수행하는 Offensive Security 연구는 <U>프로그래밍과 소프트웨어 개발능력을 기반으로 합니다.</U> 

<br>
<hr>
<br>

## Fuzzing

위 예시들과 같은 메모리 버그 기반의 보안 취약점들은 <i>Fuzzing</i> 이라는 방법으로 탐색을 자동화 할 수 있으며 이와 관련해서 수많은
연구들이 수행되고 있습니다. [Fuzzing@Home](http://fuzzcoin.gtisc.gatech.edu:8000) 은 이러한 Fuzzing 프로그램을
비신뢰 이기종 단말로 구성된 분산 컴퓨팅 네트워크에서 효율적으로 수행할 수 있는 인프라를 구축한 연구입니다. 아래의 그림은
Fuzzing@Home 시스템의 일부분으로, Google 의 libfuzzer 를 Web Assembly 바이너리로 포팅하여 웹 브라우저 엔진 내부에서
실행시킬 수 있도록 한 것을 나타냅니다.

![]({{ site.url }}{{ site.baseurl }}/images/respic/fuzzhome2.png){: style="width: 95%; float: center; margin: 10px 10px 10px 10px"}


현재 Google 에서는 퍼징을 통해 수많은 메모리 버그들을 자동적으로 발견하여 패치하고 있습니다, 이에 최신 소프트웨어에서는
단순한 메모리 버그를 발견하기가 어려워 지고 있습니다. 또한, 컴파일러 보안 기술의 발달로 인해 대다수의 메모리 버그들은 점점더
Unexploitable 해지고 있습니다. 그 대신, 클라우드 기반의 서비스들이 많고 다양해지면서 새로운 종류의 시스템 보안 취약점들이
앞으로 더 많아질 것으로 보입니다. 저희 연구실에서는 이러한 트렌드를 고려하여 전통적인 메모리 버그에 관한 연구 뿐 만 아니라
복잡한 시스템의 구성 및 상호작용에서 발생할 수 있는 <U>로직버그를 효과적으로 발견하기 위한 연구도 중점적으로 수행</u>합니다.
특히, 다음의 시스템들을 대상으로 보안취약점 연구를 수행합니다.
* 운영체제 커널 (Linux, Windows, FreeBSD, ...)
* 컨테이너 (Docker, Kubernetes, Podman, ...)
* 서버 (DBMS, Apache/Nginx, PHP, Flask, ...)
* 드론 (PX4, Ardupilot, DJI, ...)







