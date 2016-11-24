#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/01, "Basic 01")

It's hand-ray for Basic 01
I don't know Windows API very well so I may have error
If there are error in my pseudo-code please send email to me

---

~~~
#include <stdio.h>
int main(void)
{
    int var1=0;
    MessageBoxA(hwnd, "Make me think your HD is CD_Rom", "abex' 1st crackme", 0);
    var1 = GetDriveTypeA("c:\\");
    if (var1 == 5)
        MessageBoxA(hwnd, "Ok, I really think that your HD is a CD-ROM! :p", "YEAH!", 0);
    else
        MessageBoxA(hwnd, "Nah... This is not a CD_ROM Drive!", "Error", 0);
}
~~~