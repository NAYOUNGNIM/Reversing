#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/06 "Basic 06")

It's hand-ray for Basic 06
I don't know Windows API very well so I may have error
In this program, original source code may use windows api to make gui program But I don't know how to use it so I will replace it with just scanf and printf
If there are error in my pseudo-code please send email to me
This program is packed with upx, before start debugging you should unpack this one

---

~~~
#include <stdio.h>
#include <string.h>

void DialogFunc(int argv1)
{
    //Other Procedure is omitted
    char var1[100]={0};
    char var2[100]={0};
    char var3[100]="L2C-5781";
    scanf("%s", var1);
    var2 = GetVolumeInformation(); //I omit it's parameter, In real source code parameter will be located
    var2[0]+=2;
    var2[1]+=2;
    var2[2]+=2;
    var2[3]+=2;
    strcat(var2, "4562-ABEX");
    strcat(var3, var2);
    if (!strcmp(var1, var3))
        MessageBoxA(hwnd, "The serial you entered is not correct!", "Error!", 0);
    else
        MessageBoxA(hwnd, "Yep, you entered a correct serial!", "Well Done!", 0);
}

int main(void)
{
    char var1[100]={0};
    int hInstance = 0;
    hInstance = GetModuleHandleA(0);
    DialogBoxParamA(hInstance, 1, 0, DialogFunc, 0);
    ExitProcess(0);
}
~~~