def keygen14 (name) :
    res=0
    for i in name:
        tmp=ord(i)
        ebx=tmp
        edx=tmp
        ebx*=ebx
        res+=ebx
        ebx=edx
        ebx=ebx>>1
        res+=ebx
        res-=edx
    return res

def keygen15(name):
    res=0
    for i in name:
        tmp=ord(i)
        tmp=tmp<<3
        res+=tmp
    res+=(len(name)*8)
    res*=4
    return res

def keygen16(name):
    res=0
    tmp=len(name)
    tmp*=3
    tmp*=4
    res=tmp*tmp
    res*=tmp
    res+=23
    res+=((res*int('ace80', 16))&0xffffffff)
    return res

def keygen17(name):
    mem1=0
    mem2=[]
    ebx=0
    edx=0
    edi=0
    eax=0
    e_esi=0
    e_edi=0
    e_edx=0
    e_ecx=0
    e_ebx=0
    e_eax=0
    for i in name:
        esi=ord(i)
        esi=(esi+edx)&0xffffffff
        esi=(esi*0x772)&0xffffffff
        edx=esi
        edx=(edx*esi)&0xffffffff
        esi=(esi+edx)&0xffffffff
        esi=esi|esi
        esi=(esi*0x474)&0xffffffff
        esi=(esi+esi)&0xffffffff
        edx=esi
        e_edx=edx
        e_esi=esi
    for i in name[::-1]:
        edx=ord(i)
        edx=(edx+0x11)&0xffffffff
        edx=(edx-5)&0xffffffff
        edx=(edx*0x92)&0xffffffff
        edx=(edx+edx)&0xffffffff
        edx=(edx*0x819)&0xffffffff
        e_edx=edx
        mem1+=edx
    for i in name[::-1]:
        ecx=ord(i)
        edi=(edi+ecx)&0xffffffff
        edi=(edi+0x929)&0xffffffff
        edi=(edi+0x767)&0xffffffff
        edi=(edi+e_eax)&0xffffffff
        edi=(edi*0x8392)&0xffffffff
        e_eax=edi
        e_eax=(e_eax-0x33)&0xffffffff
        e_eax=(e_eax*edi)&0xffffffff
        e_eax=(e_eax+edi)&0xffffffff
        e_ecx=ecx
        e_edi=edi

    for i in name:
        edx=ord(i)
        ebx=(ebx+edx)&0xffffffff
        ebx=(ebx+ebx)&0xffffffff
        edx=ebx
        edx=(edx*ebx)&0xffffffff
        ebx=(edx*ebx)&0xffffffff
        ebx^=0x10
        ebx|=0x44
        edx=(ebx*0x373)&0xffffffff
        edx=(edx+0x443)&0xffffffff
        ebx=edx
        ebx=(ebx+ord(i))&0xffffffff
        ebx=(ebx*ebx)&0xffffffff
        e_edx=edx
        e_ebx=ebx

    eax=e_esi
    while(eax):
        edx=eax%0x10
        eax=eax/0x10
        print hex(eax), hex(edx)
        edx+=0x30
        if edx > 0x3a:
            edx+=0x7
        mem2.append(hex(edx))

    print hex(e_eax), hex(e_ecx), hex(e_edx), hex(e_ebx), hex(e_esi), hex(e_edi), mem2, hex(mem1)

req='Please type name: '
number=raw_input('What number you need to generate key: ')
if number == '14':
    print keygen14(raw_input(req))
elif number == '15':
    print keygen15(raw_input(req))
elif number == '16':
    print keygen16(raw_input(req))
elif number == '17':
    keygen17(raw_input(req))
else:
    print 'I did not make it'
