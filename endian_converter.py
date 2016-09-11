#a변수 값에 바꾸고자하는 넣어주세요
#put value which you convert to a
a="hello"

res=[]
for i in range(len(a)/4+1):
    tmp=a[i*4:i*4+4]
    tmp=tmp[::-1]
    for j in tmp:
        print hex(ord(j))
        res.append(hex(ord(j))[2:])
print "\\x"+'\\x'.join(res)