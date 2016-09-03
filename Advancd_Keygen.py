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


req='Please type name: '
number=raw_input('What number you need to generate key: ')
if number == '4':
    print keygen4(raw_input(req))