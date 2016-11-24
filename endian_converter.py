def change_endian(shellcode):
    shellcode=shellcode[2:]
    print shellcode
    res=''
    for i in range(len(shellcode), -1, -2):
        res+=shellcode[i:i+2]
    return '0x'+res