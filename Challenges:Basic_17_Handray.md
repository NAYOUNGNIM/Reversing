#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/17 "Basic 17")

It's hand-ray for Basic 17
I don't know Windows API very well so I may have error
If there are error in my pseudo-code please send email to me
This program is made with delphi instead of c
I can't find how to calculate medium(3rd) key ...
---

~~~
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char var1[100]={0}; //user input
    char var2[100]={0}; //user input
    char buf1[100]={0};
    char buf2[100]={0};
    char buf3[100]="I don't know";
    char buf4[100]={0};
    char buf5[100]={0};
    char res[100] = {0};
    unsigned int var3 = 0; //eax
    unsigned int var4 = 0; //ebx
    unsigned int var5 = 0; //ecx
    unsigned int var6 = 0; //edx
    unsigned int var7 = 0; //esi
    unsigned int var8 = 0; //edi
    unsigned int var9 = 0; //local.4
    unsigned int const1 = 0xa3557d07; //0x19f31c
    unsigned int const2 = 0x62fb12d3; //0x19f320
    unsigned int const3 = 0xefd945f6; //0x19f324
    unsigned int const4 = 0xe57ae29e; //0x19f328

    scanf("%s", var1);
    if(strlen(var1) <= 3)
        printf("Please Enter More Chars...");
    else if(strlen(var1) >= 30)
        printf("Please Enter Not More Then 30 Chars ...");

    scanf("%s", var2);
    for(int i=0; var1[i]; i++)
    {
        var7 = var1[i];
        var7 += var6;
        var7 *= 0x772;
        var6 = var7;
        var6 *= var7;
        var7 += var6;
        var7 *= 0x474;
        var7 += var7;
        var6 = var7;
    }

    for(int i=strlen(var1)-1; i>=0; i--)
    {
        var6 = var1[i];
        var6 += 0x11;
        var6 -= 5;
        var6 *= 0x92;
        var6 += var6;
        var6 *= 0x819;
        var9 += var6;
    }

    for(int i = strlen(var1)-1; i>=0; i--)
    {
        var5 = var1[i];
        var8 += var5;
        var8 += 0x929;
        var8 += 0x767;
        var8 += var3;
        var8 *= 0x8392;
        var3 = var8;
        var3 -= 0x33;
        var3 *= var8;
        var3 += var8;
    }
var6 = 0;
    for(int i = 0; var1[i]; i++)
    {
        var6 = var1[i];
        var4 += var6;
        var4 += var4;
        var6 = var4;
        var6 *= var4;
        var4 *= var6;
        var4 ^= 0x10;
        var4 |= 0x44;
        var6 = var4*0x373;
        var6 += 0x443;
        var4 = var6;
        var6 = var1[i];
        var4 += var6;
        var4 *= var4;
    }
    sprintf(buf1, "%X", var7);
    sprintf(buf2, "%X", var9);
    sprintf(buf4, "%X", var8);
    sprintf(buf5, "%X", var4);
    strncat(res, buf1, 4);
    strcat(res, "-");
    strncat(res, buf2, 4);
    strcat(res, "-");
    strncat(res, buf3, 20);
    strcat(res, "-");
    strncat(res, buf4, 4);
    strcat(res, "-");
    strncat(res, buf5, 4);

    if(!strcmp(res, var2))
    {
        MessageBoxA(hwnd, "Well done!", "Good Boy!!!", 0x40);
    }
}
~~~