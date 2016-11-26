#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/14 "Basic 14")

It's hand-ray for Basic 14
I don't know Windows API very well so I may have error
If there are error in my pseudo-code please send email to me
---

~~~
#include <stdio.h>
#include <string.h>

int main(void)
{
    char var1[100]={0};
    char var2[100]={0};
    int var3 = 0; //edx
    int var4 = 0; //ebx
    int var5 = 0; //esi
    int var6 = 0; //eax
    if(!scanf("%s", var1))
        MessageBoxA(hwnd, "Please Fill in 1 more Char!!", "Key/Crackme #2", 0);
    if(!scanf("%s", var2))
        MessageBoxA(hwnd, "Please Fill in 1 more Char!!", "Key/Crackme #2", 0);
    for(int i=0; var1[i]; i++)
    {
        var3 = var1[i];
        var4 = var1[i];
        var4 *= var3;
        var5 += var4;
        var4 = var3;
        var4 /= 2;
        var5 += var4;
        var5 -= var3;
    }

    for(int i=0; var2[i]; i++)
    {
        var6=var2[i]-0x30;
        for(int j=0; strlen(var2)-i-j-1; j++)
            var6 *= 0x0a;
    }

    if (var5 == var6)
        MessageBoxA(hwnd, "Good Job, I Wish You the Very Best", "Key/CrackMe #2", 0);
    else
        MessageBoxA(hwnd, "You Have Enter A Wrong Serial, Please Try Again", "Key/CrackMe #2", 0);
}
~~~