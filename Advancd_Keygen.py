def keygen4(name):
    edx=0xa
    ecx=0
    esi=0
    edi=1
    for i in name:
        eax=ord(i)+1
        eax=(eax+edx)&0xffffffff
        esi=(esi+eax)&0xffffffff
        ecx+=1
        edx=(edx*ecx)&0xffffffff
        edi=edx
        edi=(edi*esi)&0xffffffff
    return ('LOD-%lu-%lx' %(esi, edi)).upper()

def tohex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))

def bswap(num, len=4):
    if num>=0:
        tmp='%08x' %num
    else:
        tmp=("%s" %tohex(num, 32))[2:]
    res=''
    for i in range(len-1, -1, -1):
        res+=tmp[i*2:i*2+2]
    return int(res, 16)

def func_4013ab(eax, ecx, mem):
    ecx=bswap(ecx)
    edx=ecx&0x0000ffff
    mem[4+edx]=eax
    ecx+=4
    ecx=bswap(ecx)
    return ecx

def func_4013bf(eax, ecx, mem):
    ecx=bswap(ecx)
    cx=ecx&0x0000ffff
    cx-=4
    ecx=ecx&0xffff0000
    print hex(ecx)
    ecx=ecx|cx
    print hex(ecx)
    if cx == -4:
        ecx=ecx&0xffff0000
        ecx=bswap(ecx)
        eax=0
        return eax, ecx
    else:
        edx=cx
        eax=mem[edx+4]
        mem[edx+4]=0
        ecx=bswap(ecx)
        return eax, ecx

def func_40138a(ebx, ecx):
    tl=(ebx&0x000000ff)+(ecx&0x000000ff)
    th=(ebx&0x0000ff00)+(ecx&0x0000ff00)
    if tl == 0xff:
        tl=0x13
    if th == 0xff:
        th=3
    if tl == 0x14:
        tl=0
    if th == 4:
        th=0
    ebx=ebx&0xffff0000
    ebx=(ebx+th+tl)&0xffffffff
    return ebx

def init(mem):
    for i in range(0xfffff):
        mem.append(0)

def ROL(data, shift, size=32):
    shift %= size
    remains = data >> (size - shift)
    body = (data << shift) - (remains << size )
    return (body + remains)


def keygen11(name):
    mem_40217b='24 35 25 24 23 77 76 23 5F 22 61 73 22 2A 33 24 24 76 2B 38 76 2A 22 7E 78 22 3C 5C 5E 60 5C 22 39 22 3A 3C 3B 78 22 2D 3E 7E 3A 21 34 23 76 24 5F 22 6D 64 38 22 47 2B 2A 25 2A 2B 6C 3A 21 23 40 5F 3E 38 37 2B 2F 5C 22 30 22 5E 76 3E 2C 2B 50 69 6E 65 77 61 72 65 5F 30 30 31 20 2D 20 4B 65 79 67 65 6E 6D 65 0D 0A 42 79 20 4A 6F 65 6C 20 43 6F 78 0D 0A 0D 0A 68 74 74 70 3A 2F 2F 70 69 6E 65 77 61 72 65 2E 66 72 65 65 68 6F 73 74 69 61 2E 63 6F 6D 2F'.split(' ')
    mem_402534=[]
    res=''
    ebx=0
    ecx=1
    idx=0
    init(mem_402534)

    while True:
        eax=ebx&0x0000ff00
        edx=ebx&0x000000ff
        eax=(eax*0x14)&0xffffffff
        eax=int(mem_40217b[eax+edx], 16)
        print hex(eax), hex(ecx), hex(edx), hex(ebx)
        raw_input()
        if eax&0x000000ff == 0x22:
            ebx=bswap(ebx)
            tmp=ebx&0x000000ff
            tmp^=0x1
            ebx&=0xffffff00
            ebx|=tmp
            ebx=bswap(ebx)
            ebx=func_40138a(ebx, ecx)
            continue
        edx=ebx
        edx=bswap(edx)
        if edx&0x000000ff != 0:
            ecx=func_4013ab(eax, ecx, mem_402534)
            tmp=ebx&0x000000ff
            tmp^=0x1
            ebx&=0xffffff00
            ebx|=tmp
            ebx=bswap(ebx)
            ebx=func_40138a(ebx, ecx)
            continue
        if (eax&0x000000ff) > 0x30 and (eax&0x000000ff <0x39):
            tmp=eax&0x000000ff
            tmp-=0x30
            eax=eax&0xffffff00
            eax|=tmp
            ecx=func_4013ab(eax, ecx, mem_402534)
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x7e:
            eax=ord(name[idx])
            idx+=1
            ecx=func_4013ab(eax, ecx, mem_402534)
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x2c:
            ecx=bswap(ecx)
            eax=eax&0xffff0000
            eax|=ecx&0x0000ffff
            ecx=bswap(ecx)
            res+=chr(int(mem_402534[eax]),16)
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            print mem_402534[4:13], "Hello"
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x3e:
            ecx=ecx&0xffff0001
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x3c:
            ecx=ecx&0xffff00ff
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x76:
            ecx=ecx&0xffff0100
            print hex(ecx)
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x5e:
            ecx=ecx&0xffffff00
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x2b:
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            edx=eax
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            eax=(eax+edx)&0xffffffff
            ecx=func_4013ab(eax, ecx, mem_402534)
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x2d:
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            edx=eax
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            eax, edx = edx, eax
            eax=(eax-edx)&0xffffffff
            ecx=func_4013ab(eax, ecx, mem_402534)
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x2a:
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            tmp=eax
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            edx=tmp
            eax=(eax*edx)&0xffffffff
            ecx=func_4013ab(eax, ecx, mem_402534)
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x2f:
            tmp1=ecx
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            tmp2=eax
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            ecx=tmp2
            if ecx == 0:
                eax=0
                ecx=0
            else:
                tmp=edx<<32+eax
                eax=tmp/ecx
                edx=tmp%ecx
            tmp=eax
            eax=edx
            ecx=func_4013ab(eax, ecx, mem_402534)
            eax=tmp
            ecx=func_4013ab(eax, ecx, mem_402534)
            ecx=tmp1
            ebx=func_40138a(ebx, ecx)
            continue

        if eax&0x000000ff == 0x5c:
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            edx=eax
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            eax, edx=edx, eax
            ecx=func_4013ab(eax, ecx, mem_402534)
            eax=edx
            ecx=func_4013ab(eax, ecx, mem_402534)
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x5f:
            edx=0x4011f2
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            if eax == 0:
                ecx=ecx&0xffff0001
            else:
                ecx=ecx&0xffff00ff
        if eax&0x000000ff == 0x23:
            ebx=func_40138a(ebx, ecx)
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x3a:
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            ecx=func_4013ab(eax, ecx, mem_402534)
            ecx=func_4013ab(eax, ecx, mem_402534)
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x21:
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            edx=eax
            eax=0
            if edx == 0:
                eax=1
            ecx=func_4013ab(eax, ecx, mem_402534)
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x6c:
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            eax=ROL(eax, 1)
            ecx=func_4013ab(eax, ecx, mem_402534)
        if eax&0x000000ff == 0x60:
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            tmp=eax
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            edi=tmp
            edx=0
            if edi>eax:
                edx=1
            eax=edx
            ecx=func_4013ab(eax, ecx, mem_402534)
        if eax&0x000000ff == 0x24:
            eax, ecx=func_4013bf(eax, ecx, mem_402534)
            ebx=func_40138a(ebx, ecx)
            continue
        if eax&0x000000ff == 0x40:
            break
        else:
            ebx=func_40138a(ebx, ecx)




req='Please type name: '
number=raw_input('What number you need to generate key: ')
if number == '4':
    print keygen4(raw_input(req))
if number == '11':
    print keygen11(raw_input(req))