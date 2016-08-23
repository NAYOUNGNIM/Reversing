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

number=raw_input('What number you need to generate key: ')
if number == '14':
    print keygen14(raw_input())
else:
    print 'I did not make it'
