#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/06 "Basic 06")

It's hand-ray for Basic 06
I don't know Windows API very well so I may have error
In this program, original source code may use windows api to make gui program But I don't know how to use it so I will replace it with just scanf and printf
If there are error in my pseudo-code please send email to me
This program is packed with upx, before start debugging you should unpack this one

---

~~~
#include <stdio.h>
int main(void)
{
    char var1[100]={0};
    scanf("%s", var1);
    if(strcmp(var1, "AD46DFS547"))
    {
        MessageBoxA(hwnd, "Wrong serial!!!", "ERROR", 0x10);
    }
    else
    {
        MessageBoxA(hwnd, "You got it ;>", "Good Job!", 0x40);
    }
}
~~~