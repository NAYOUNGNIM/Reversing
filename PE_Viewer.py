#-*- coding:utf-8 -*-

#소스코드의 기본 인코딩을 utf-8로 고정한다.
import sys
import binascii
reload(sys)
sys.setdefaultencoding('utf-8')

#출력을 위한 포멧
fmt='%08X %-30s: %s'

#인텔 계열 CPU에서 사용하는 Little Endian 방식을 Big Endian 방식으로 바꿔준다
def rever(tar):
    out=[]
    i=0
    while i <len(tar):
        out.append(tar[i:i+2])
        i+=2
    out.reverse()
    return (''.join(out)).upper()

#PE 파일의 각 부분을 구분해주는 함수
def carriage(Name):
    print '-'*70
    print ' '*15, Name, '\n'
    print 'Address', ' '*7, 'Description', ' '*12, 'Data'
    print '-'*70

#PE 파일의 가장 첫 부분인 DOS_HEADER를 출력하고 NT_HEADERS의 시작 주소를 반환한다.
def DOS_HEADER(content, curpos):
    #DOS_HEADER에 있는 멤버의 DESCRIPTION들
    Description=['Signature', 'Bytes on Last Page of File', 'Pages in File', 'Relocations', 'Size of Header in Paragraphs',
                 'Minimum Extra Paragraphs', 'Maximum Extra Paragraphs', 'Initial (relative) SS', 'Initial SP', 'Checksum',
                 'Initial IP', 'Initial (relative) CS', 'Offset to Relocation Table', 'Overlay Number', 'Reserved', 'Reserved',
                 'Reserved', 'Reserved', 'OEM Identifier', 'OEM Information', 'Reserved', 'Reserved', 'Reserved', 'Reserved',
                 'Reserved', 'Reserved', 'Reserved', 'Reserved', 'Reserved', 'Reserved', 'Offset to New EXE Header']
    for i in range(30):
        print fmt %(curpos+i*2, Description[curpos+i], rever(binascii.hexlify(content[curpos+i*2:curpos+i*2+2])))
    curpos=60
    print fmt %(curpos, Description[-1], rever(binascii.hexlify(content[curpos:curpos+4])))
    curpos=int(rever(binascii.hexlify(content[curpos:curpos+4])), 16)
    return curpos

#MS_DOS Stub Program부분을 나타내주는 함수
def DOS_STUB(content, curpos):
    pass

#NT_HEADER중 SIGNATURE를 보여주는 함수로써 FILE_HEADER의 시작 주소를 반환한다.
def Signature(content, curpos):
    print fmt %(curpos, 'Signature', rever(binascii.hexlify(content[curpos:curpos+4])))
    curpos+=4
    return curpos

#NT_HEADER중 IMAGE_FILE_HEADER를 보여주는 함수로써 OPTIONAL_HEADER의 시작주소와 크기, 그리고 Section Header의 개수를 반환한다.
def FILE_HEADER(content, curpos):
    print fmt %(curpos, 'Machine', rever(binascii.hexlify(content[curpos:curpos+2])))
    print fmt %(curpos+2, 'Number of Sections', rever(binascii.hexlify(content[curpos+2:curpos+4])))
    print fmt %(curpos+4, 'Time Date Stamp', rever(binascii.hexlify(content[curpos+4:curpos+8])))
    print fmt %(curpos+8, 'Pointer to Symbol Table', rever(binascii.hexlify(content[curpos+8:curpos+12])))
    print fmt %(curpos+12, 'Number of Symbols', rever(binascii.hexlify(content[curpos+12:curpos+16])))
    print fmt %(curpos+16, 'Size of Optional Header', rever(binascii.hexlify(content[curpos+16:curpos+18])))
    print fmt %(curpos+18, 'Characteristics', rever(binascii.hexlify(content[curpos+18:curpos+20])))
    return (curpos+20, int(rever(binascii.hexlify(content[curpos+16:curpos+18])), 16), int(rever(binascii.hexlify(content[curpos+2:curpos+4])), 16))

#NT_HEADER중 IMAGE_OPTIONAL_HEADER를 출력하는 부분, Image_Section_Header가 시작되는 주소를 반환한다.
def OPTIONAL_HEADER(content, curpos, size):

    Descriptions=['Size of Stack Reverse', 'Size of Stack Commit', 'Size of Heap Reverse', 'Size of Heap Commit',
                  'Loader Flags', 'Number of Data Directories', 'EXPORT Table RVA', 'EXPORT Table Size',
                  'IMPORT Table RVA', 'IMPORT Table Size', 'Resource Table RVA', 'Resource Table Size',
                  'Exception Table RVA', 'Exception Table Size', 'Certificate Table RVA', 'Certificate Table Size',
                  'Base Relocation Table RVA', 'Base Relocation Table Size', 'Debug Directory RVA', 'Debug Directory Size',
                  'Architecture Specific Data RVA', 'Architecture Specific Data Size', 'Global Pointer Register RVA',
                  'Global Pointer Register Size', 'TLS Table RVA', 'TLS Table Size', 'Load Configuration Table RVA',
                  'Load Configuration Table Size', 'Bound Import Table RVA', 'Bound Import Table Size', 'Import Address Table RVA',
                  'Import Address Table Size', 'Delay Import Descriptors RVA', 'Delay Import Descriptors Size',
                  'CLI Header RVA', 'CLI Header Size']

    if curpos+224<size:
        print '이 프로그램은 이상합니다.'
        exit(1)
    else:
        print fmt %(curpos, 'Magic', rever(binascii.hexlify(content[curpos:curpos+2])))
        print fmt %(curpos+2, 'Major Linker Version', rever(binascii.hexlify(content[curpos+2:curpos+3])))
        print fmt %(curpos+3, 'Minor Linker Version', rever(binascii.hexlify(content[curpos+3:curpos+4])))
        print fmt %(curpos+4, 'Size of Code', rever(binascii.hexlify(content[curpos+4:curpos+8])))
        print fmt %(curpos+8, 'Size of Initialized Data', rever(binascii.hexlify(content[curpos+8:curpos+12])))
        print fmt %(curpos+12, 'Size of Uninitialized Data', rever(binascii.hexlify(content[curpos+12:curpos+16])))
        print fmt %(curpos+16, 'Address of Entry Point', rever(binascii.hexlify(content[curpos+16:curpos+20])))
        print fmt %(curpos+20, 'Base of Code', rever(binascii.hexlify(content[curpos+20:curpos+24])))
        print fmt %(curpos+24, 'Base of Data', rever(binascii.hexlify(content[curpos+24:curpos+28])))
        print fmt %(curpos+28, 'Image Base', rever(binascii.hexlify(content[curpos+28:curpos+32])))
        print fmt %(curpos+32, 'Section Alignment', rever(binascii.hexlify(content[curpos+32:curpos+36])))
        print fmt %(curpos+36, 'File Alignment', rever(binascii.hexlify(content[curpos+36:curpos+40])))
        print fmt %(curpos+40, 'Major O/S Version', rever(binascii.hexlify(content[curpos+40:curpos+42])))
        print fmt %(curpos+42, 'Minor O/S Version', rever(binascii.hexlify(content[curpos+42:curpos+44])))
        print fmt %(curpos+44, 'Major Image Version', rever(binascii.hexlify(content[curpos+44:curpos+46])))
        print fmt %(curpos+46, 'Minor Image Version', rever(binascii.hexlify(content[curpos+46:curpos+48])))
        print fmt %(curpos+48, 'Major Subsystem Version', rever(binascii.hexlify(content[curpos+48:curpos+50])))
        print fmt %(curpos+50, 'Minor Subsystem Version', rever(binascii.hexlify(content[curpos+50:curpos+52])))
        print fmt %(curpos+52, 'Win32 Version Value', rever(binascii.hexlify(content[curpos+52:curpos+56])))
        print fmt %(curpos+56, 'Size of Image', rever(binascii.hexlify(content[curpos+56:curpos+60])))
        print fmt %(curpos+60, 'Size of Headers', rever(binascii.hexlify(content[curpos+60:curpos+64])))
        print fmt %(curpos+64, 'Checksum', rever(binascii.hexlify(content[curpos+64:curpos+68])))
        print fmt %(curpos+68, 'Subsystem', rever(binascii.hexlify(content[curpos+68:curpos+70])))
        print fmt %(curpos+70, 'DLL Characteristics', rever(binascii.hexlify(content[curpos+70:curpos+72])))

        for i in range(36):
            print fmt %(curpos+72+i*4, Descriptions[i], rever(binascii.hexlify(content[curpos+72+i*4:curpos+76+i*4])))

        return curpos+size

#각각 SECTION_HEADER의 이름을 구하는 함수
def name(content, curpos):
    names=content[curpos:curpos+8]
    return names.strip('\0')

#SECTION_HEADER의 정보를 출력해주는 함수, 각각의 SECTION이 시작하는 주소와 크기를 딕셔너리 형태로 반환
def SECTION_HEADER(content, curpos, cnt):
    dicts={}
    for i in range(cnt):
        carriage(name(content, curpos))
        print fmt %(curpos, 'Name', name(content, curpos))
        print fmt %(curpos+8, 'Virtual Size', rever(binascii.hexlify(content[curpos+8:curpos+12])))
        print fmt %(curpos+12, 'RVA', rever(binascii.hexlify(content[curpos+12:curpos+16])))
        print fmt %(curpos+16, 'Size of Raw Data', rever(binascii.hexlify(content[curpos+16:curpos+20])))
        print fmt %(curpos+20, 'Pointer to Raw Data', rever(binascii.hexlify(content[curpos+20:curpos+24])))
        print fmt %(curpos+24, 'Pointer to Relocations', rever(binascii.hexlify(content[curpos+24:curpos+28])))
        print fmt %(curpos+28, 'Pointer to Line Numbers', rever(binascii.hexlify(content[curpos+28:curpos+32])))
        print fmt %(curpos+32, 'Number of Relocations', rever(binascii.hexlify(content[curpos+32:curpos+34])))
        print fmt %(curpos+34, 'Number of Line Numbers', rever(binascii.hexlify(content[curpos+34:curpos+36])))
        print fmt %(curpos+36, 'Characteristics', rever(binascii.hexlify(content[curpos+36:curpos+40])))
        dicts[name(content, curpos)]=(int(rever(binascii.hexlify(content[curpos+16:curpos+20])), 16), int(rever(binascii.hexlify(content[curpos+20:curpos+24])), 16))
        curpos+=40

    return dicts

def SECTION_BODY(content, sections):
    for i in sections.keys():
        carriage(i)
        size, start=sections[i]
        #print size, start
        for i in range(size/16+1):
            print fmt %(start+i*16, 'None', content[start+i*16:start+i*16+16])


#프로그램의 중심이 되는 메인 함수.
#파일을 읽어들이고 적절한 함수를 출력한다.
#모든 출력은 main이 호출한 함수 내에서 이루어 진다.
def main():

    cur_pos=0

    #파일을 읽어 들여서 문자의 리스트로 바꾼다.
    file_name=raw_input()
    with open(file_name, 'rb') as f:
        content=f.read()

    carriage('IMAGE_DOS_HEADER')
    cur_pos=DOS_HEADER(content, cur_pos)

    carriage('SIGNATURE')
    cur_pos=Signature(content, cur_pos)

    carriage('IMAGE_FILE_HEADER')
    cur_pos, size, cnt=FILE_HEADER(content, cur_pos)

    carriage('IMAGE_OPTIONAL_HEADER')
    cur_pos=OPTIONAL_HEADER(content, cur_pos, size)

    sections=SECTION_HEADER(content, cur_pos, cnt)
    SECTION_BODY(content, sections)

if __name__ == '__main__':
    main()
