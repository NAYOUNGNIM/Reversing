#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/04 "Basic 04")

It's hand-ray for Basic 04
I don't know Windows API very well so I may have error
If there are error in my pseudo-code please send email to me

---

~~~
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int var1=0;

    while(1)
    {
        Sleep(0x3e8); (Not sleep!!!)
        #chkesp();
        var1 = IsDebuggerPresent();
        if(var1 == 0)
            printf("정상\n");
        else
            printf("디버깅 당함\n");
    }
}
~~~