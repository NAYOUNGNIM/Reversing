#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/15 "Basic 15")

It's hand-ray for Basic 15
I don't know Windows API very well so I may have error
If there are error in my pseudo-code please send email to me
---

~~~
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char var1[100]={0}; //user input(name)
    char var2[100]={0}; //user input(pw)
    int var3 = 0; //edx
    int var4 = 0; //eax
    int var5 = 0; //memory

    scanf("%s", var1);

    for(int i=0; var1[i]; i++)
    {
        var3 = var1[i];
        var3 *= 8;
        var5 += var3;
    }

    var4 = strlen(var1)*8;
    var5 += var4;
    var5 *= 4;

    scanf("%s", var2);

    if (var5 == atoi(var2))
        ShowMessage("You cracked the UBC CrackMe#1 ! Please send your solution to ubcrackers@hotmail.com!");
        SetText("CRACKED");
    else
        ShowMessage("Try Again !");
}
~~~