#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/05 "Basic 05")

It's hand-ray for Basic 05
I don't know Windows API very well so I may have error
In this program, original source code may use windows api to make gui program But I don't know how to use it so I will replace it with just scanf and printf
If there are error in my pseudo-code please send email to me

---

~~~
#include <stdio.h>
#include <string.h>
int main(void)
{
    char var1[100]={0};
    char var2[100]={0};

    scanf("%s", var1);
    if (var1[0] == 0)
    {
        MessageBoxA(hwnd, "Enter a Name!", "No Name entered", 0);
    }
    scanf("%s", var2);
    if (var2[0] == 0)
    {
        MessageBoxA(hwnd, "Enter a Serial", "No Serial entered", 0);
    }

    if(strcmp(var1, "Registered User") || strcmp(var2, "GFX-754-IER-954")
    {
        MessageBoxA(hwnd, "Wrong Serial, try again!", "Beggar off!", 0);
    }
    else
    {
        MessageBoxA(hwnd, "Congrants! You cracked this CrackMe!", "CrackMe cracked successfully", 0);
    }
}
~~~