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
또한, Windows/Linux 커널 등 운영체제 의 코드에 취약점이 있는 경우 이를 악용하여 LPE (루팅 등) 를 하거나, Sandbox 와 같은 보안장치를 무력화 할 수 있습니다.
이러한 버그들은 주로 힙 메모리에서의 Overflow, Use-After-Free 와 같은 메모리 취약점, Race Condition 취약점 등으로 인해 발생할 수 있는데, 
이러한 버그를 RCE 까지 이끌어내는 과정에서는 상당한 Reverse Engineering (역공학) 이 필요합니다. 메모리 구조 이해, 어셈블리 분석, 디버거의 활용 등도 중요하지만 
무엇보다도 프로그래밍 및 소프트웨어 개발에 관한 다양한 경험이 필요합니다.
기본적으로 저희 연구실에서 수행하는 모든 Offensive Security 연구는 <U>프로그래밍과 소프트웨어 개발능력을 기반으로 합니다.</U> 
또한, 기존의 해킹/사이버보안 위협 등 대부분의 정보보안 이슈는 범용적인 PC 및 서버에서의
메모리 취약점 및 악성코드 유포 등에 집중되었으나, 최근 ICT 산업이 다양한 분야로 확대되면서
다양한 무인이동체 등 새로운 시스템에서도 해킹 문제들이 생겨나고 있습니다. 

<br>
<hr>
<br>

## Satellite System Security

스페이스X 의 등장이후의 인공위성 발사비용 절감, 국제적 우주 사이버보안 조약, 국내 우주항공청 설립 등
최근 저궤도 (LEO) 인공위성 시스템의 사이버 보안에 대한 중요성이 높아지고 있습니다. 
그러나 저전력, 방사선, 장거리통신, 빠른공전 등의 우주환경 특성상 강력한 암호화 및 시스템 보안기술의 
적용이 일반적인 지상 컴퓨터 시스템보다 어렵기 때문에 다양한 연구가 필요합니다.

![]({{ site.url }}{{ site.baseurl }}/images/respic/sat.png){: style="width: 90%; float: center; margin: 10px 0px 10px 10px"}

인공위성 시스템은 그림과 같이 지상국과의 교신 및 장거리 RF 통신등의 특수한 요소들을 포함하고 있으며
이러한 요소들에서 기존에 생각하기 어려웠던 사이버보안 및 해킹의 위협들이 등장하고 있습니다.
우리 연구실에서는 오픈소스 위성 지상국 구축부터 인공위성 탑제채 펌웨어의 역공학 및 위성 RF 통신 등
다양한 저궤도위성 운용에 관한 기술들에 대해서 해커/공격자적 관점의 연구를 수행합니다.

<br>
<hr>
<br>

## Drone System Security

저희 연구실에서는 인공위성 시스템과 더불어 UAV/UAM 등과 같은 드론 비행체 시스템에 대한 분석 및 취약성에 대한 연구를 수행합니다. 

![]({{ site.url }}{{ site.baseurl }}/images/respic/drone.png){: style="width: 90%; float: center; margin: 10px 0px 10px 10px"}

드론시스템은 RC 조종기, 무선통신, 모바일시스템 등 다양한 요소들이 융합적으로 상호작용하게 되는 복잡한
구조를 가집니다. 이러한 시스템을 대상으로 저희 연구실에서는 전통적 메모리 취약점 보다는 네트워크 프로토콜 상의 취약점
또는 인증 및 암호화의 취약점, 비행금지 (NFZ/Geofence) 우회 등에 관한 보안 문제를 연구합니다.
연구 수행을 위해서는 네트워크 기술, 펌웨어 리버싱, 암/복호화 분석, H/W 디버깅 인터페이스 연구
및 SDR 등을 통한 RF 신호분석 기술 등이 요구됩니다.

<br>
<hr>
<br>

## Web Application Security

최근의 웹 어플리케이션은 인터넷 홍보/게시판 등의 1차적 기능만을 수행하는 것이 아니라, 
클라우드, IoT, 및 무인이동체 시스템 등과 연계되어 REST API 등을 통해 복잡하게 구성됩니다. 

![]({{ site.url }}{{ site.baseurl }}/images/respic/web.png){: style="width: 90%; float: center; margin: 10px 0px 10px 10px"}

스캐너 등을 통해 비교적 쉽게 발견하고 고칠 수 있는 전통적인 웹 어플리케이션에서의 보안문제들 (SQLi, XSS, CSRF 등) 은
웹 개발 인프라의 발달로 인해 줄어드는 추세이나, 반면 REST API 보안문제, Deserialization, 타 시스템 연동에서의 인증문제 등 
시스템의 구성 자체가 복잡해짐에 따라 발생할 수 있는 논리적인 취약점들은 늘어날 것으로 예상되며, 이에 따라
선제적으로 취약성을 발견하여 공격을 방어하기 위한 연구가 필요합니다. 
저희 연구실에서는 Client 측 (브라우저 보안, JavaScript RCE, UXSS 등)
보다는 Server 측에 대한 보안문제들을 더 중점적으로 연구합니다.


<br>
<hr>
<br>

## Fuzzing

메모리 버그 기반의 보안 취약점들은 <i>Fuzzing</i> 이라는 방법으로 탐색을 자동화 할 수 있으며 이와 관련해서 수많은
연구들이 수행되고 있습니다. [Fuzzing@Home](http://fuzzcoin.gtisc.gatech.edu:8000) 은 저희 연구실에서 개발한 시스템으로
비신뢰 이기종 단말로 구성된 분산 컴퓨팅 네트워크에서 효율적으로 수행할 수 있는 인프라를 구축한 연구입니다. 아래의 그림은
Fuzzing@Home 시스템의 일부분으로, Google 의 libfuzzer 를 Web Assembly 바이너리로 포팅하여 웹 브라우저 엔진 내부에서
실행시킬 수 있도록 한 것을 나타냅니다.

![]({{ site.url }}{{ site.baseurl }}/images/respic/fuzzhome2.png){: style="width: 90%; float: center; margin: 10px 10px 10px 10px"}

다행히 (안타깝게도) 보안 기술의 발달로 인해 최신 소프트웨어에서는 단순 메모리 버그가 점점 사라지고 있습니다.
또한, 컴파일러 보안 기술의 발달로 인해 단순 메모리 버그들은 점점더 Unexploitable 해지고 있습니다. 
저희 연구실에서는 브라우저/커널과 같이 코드베이스가 큰 시스템을 대상으로는 계속해서 퍼징기반으로 메모리 취약점을 연구하고
인터페이스 및 구성이 복잡한 시스템을 대상으로는 다양한 분석을 통한 논리적인 취약점을 위주로 연구를 수행합니다.

