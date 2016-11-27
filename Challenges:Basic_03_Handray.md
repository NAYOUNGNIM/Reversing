#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/02 "Basic 02")

It's hand-ray for Basic 01
I don't know Windows API very well so I may have error
If there are error in my pseudo-code please send email to me
This program is made up with visual basic so I used VB Decompiler to decompile it.
It was really hard to find `msvbvm50.dll`.
---

~~~
#include <stdio.h>
#include <string.h>

int main(void)
{
    char var[100]={0};
    scanf("%s", var);

    if(!strcmp(var, "2G83G35Hs2"))
    {
        MessageBoxA(hwnd, "Gluckwunsch!", "Danke, das Passport ist richtig!", 0x31);
    }
    else
    {
        MessageBoxA(hwnd, "PASSWORT FALSCH", "Error! Das Passwort ist falsch!", 0x30);
    }
}
~~~