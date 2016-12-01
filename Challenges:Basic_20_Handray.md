#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/20 "Basic 20")

It's hand-ray for Basic 20
I don't know Windows API very well so I may have error
If there are error in my pseudo-code please send email to me
---

~~~
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp = NULL;
    char var1[20] = {0};
    fp = fopen("CRACKME3.KEY", "r");
    fscanf(fp, "%s", var1);

    if(strlen(var1) != 0x12)
    {
        return 0;
    }

    if(!strcmp(var1, "\x40\x43\x42\x45\x44\x5\x28\x2c\x2c\xf\x25\x2b\x23\x6f\x51\x55\x34\x12"))
    {
        MessageBoxA(hwnd, "Success", "Success", 0);
    }
}
~~~