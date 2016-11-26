#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/15 "Basic 15")

It's hand-ray for Basic 15
I don't know Windows API very well so I may have error
If there are error in my pseudo-code please send email to me
This program is made with c++ instead of c
---

~~~
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char var1[100]={0};
    char var2[100]={0};
    unsigned int var3 = 0; //eax
    unsigned int var4 = 0; //edx
    unsigned int var5 = 0; //memory

    system("Title ReWrit's Crackme #5");
    system("mode con: Cols=32 Lines=16");
    printf("ReWrit's Crackme#5\n");
    printf("******************************\n");
    printf("* This is my 5th crackme,    *\n");
    printf("* i hope you will enjoy it.  *\n");
    printf("******************************\n");
    printf("\n\n");
    printf("Enter your Name: ");
    scanf("%s", var1);

    var3 = strlen(var1);
    var4 = var3;
    var3 = var4;
    var3 += var3;
    var3 += var4;
    var3 *= 4;
    var5 = var3;
    var3 *= var5;
    var3 *= var5;
    var3 += 0x17;
    var5 = var3;

    printf("Enter your Password: ");
    scanf("%s", var2);

    var3 = var5;
    var4 = var3 * 0xace80;
    var4 += var5;

    if(var4 == atoi(var2))
    {
        printf("Good Job!\n");
        printf("=> ");
        system("pause > null");
        system("del null");
    }

    else
    {
        printf("Wrong password!\n");
        printf("=/ ");
        system("pause > null");
        system("del null");
    }
}
~~~