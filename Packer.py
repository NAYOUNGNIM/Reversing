#-*- coding:utf-8 -*-
import sys
import binascii
reload(sys)
sys.setdefaultencoding('utf-8')

#Little Endian 방식을 Big Endian 방식으로 바꿔준다.
def rever(tar):
    out=[]
    i=0
    while i <len(tar):
        out.append(tar[i:i+2])
        i+=2
    out.reverse()
    return (''.join(out)).upper()

#IMAGE_NT_HEADER를 찾아가는 함수
def Image_NT_Header(f):
    return rever(binascii.hexlify(f[60:64]))

#Section의 개수를 찾는 함수
def Num_Sections(f, start):
    idx=int(start, 16)+6
    return rever(binascii.hexlify(f[idx:idx+2])), rever(binascii.hexlify(f[idx+14:idx+16]))

#명령어를 암호화하는 부분
def encrypt(f, pointer, size):
    start=int(rever(binascii.hexlify(pointer)), 16)
    end=int(rever(binascii.hexlify(size)), 16)+start
    for i in range(start, end):
        f[i]=hex(int(f[i], 16)+11)

#Section을 추가하는 부분
def inc(f, start):
    f=f[:start+6]+chr(int(binascii.hexlify(f[start+6]), 16)+1)+f[start+7:]
    return f

#main 함수
def main():
    file_name=raw_input()
    with open(file_name, 'rb') as f:
        content=f.read()
    print type(content[0])
    start=Image_NT_Header(content)
    num, size=Num_Sections(content, start)
    section=int(start, 16)+24+int(size, 16)

    """for i in range(int(num, 16)):
        tar=content[section+(i*40):section+(i*40)+8]
        if 'CODE' in tar or 'text' in tar:
            encrypt(content, content[section+(i*40)+20:section+(i*40)+24], content[section+(i*40)+16:section+(i*40)+20])
            break"""

    content=inc(content, int(start, 16))
    with open(file_name, 'wb') as f:
        f.write(content)


if __name__ == '__main__':
    main()
