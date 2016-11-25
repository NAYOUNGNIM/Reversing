#This is pseudo-code for [Codeengn](http://codeengn.com/challenges/basic/13 "Basic 13")

It's hand-ray for Basic 13
I don't know Windows API very well so I may have error
If there are error in my pseudo-code please send email to me
This program is packed with upx, before start debugging you should unpack this one
This program is made with microsoft .net, I used [ILSpy](http://ilspy.net "ILSpy .net decompiler")
I don't know any sementics of .net so I just almost copy source from ILSpy's result
In this question it was more hard to find answer than handray. I just made same C# programs to get key.
---

~~~
using System;

public class RijndaelSimple
{
    public static string Encrypt(string plainText, string passPhrase, string saltValue, string hashAlgorithm, int passwordIterations, string initVector, int keySize)
    {
        byte[] bytes = Encoding.ASCII.GetBytes(initVector);
        byte[] bytes2 = Encoding.ASCII.GetBytes(saltValue);
        byte[] bytes3 = Encoding.UTF8.GetBytes(plainText);
        PasswordDeriveBytes passwordDeriveBytes = new PasswordDeriveBytes(passPhrase, bytes2, hashAlgorithm, passwordIterations);
        ICryptoTransform transform = new RijndaelManaged(Mode = CipherMode.CBC).CreateEncryptor(bytes4, bytes);
        MemoryStream memoryStream = new MemoryStream();
        CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write);
        cryptoStream.Write(bytes3, 0, bytes3.Length);
        byte[] inArray = memoryStream.ToArray();
        memoryStream.Close();
        cryptoStream.Close();
        return Convert.ToBase64String(inArray);
    }

    public static string Encrypt(string cipherText, string passPhrase, string saltValue, string hashAlgorithm, int passwordIterations, string initVector, int keySize)
    {
        byte[] bytes = Encoding.ASCII.GetBytes(initVector);
        byte[] bytes2 = Encoding.ASCII.GetBytes(saltValue);
        byte[] array = Convert.FromBase64String(cipherText);
        PasswordDeriveBytes passwordDeriveBytes = new PasswordDeriveBytes(passPhrase, bytes2, hashAlgorithm, passwordIterations);
        byte[] bytes3 = passwordDeriveBytes.GetBytes(keySize/8);
        ICryptoTransform transform = new RijndaelManaged(Mode = CipherMode.CBC).CreateEncryptor(bytes4, bytes);
        MemoryStream memoryStream = new MemoryStream(array);
        CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Read);
        byte[] array2 = new byte[array.Length);
        int count = cryptoStream.Read(array2, 0, array2.Length);
        memoryStream.Close();
        cryptoStream.Close();
        return Encoding.UTF8.GetString(array2, 0, count);
    }
}

public class RijndaelSimpleTest
{
    private static void Main(string[] args)
    {
        string text="";
        string cipherText="BnCxGiN4a3DE+qUe2yIm8Q;
        string passPhrase="^F79ejk56$£";
        string saltValue="DHj47&*)$h";
        string hashAlgorithm="MD5";
        int passwordIterations=1024;
        string initVector="&!£%^&*()CvHgE!";
        int keySize=256;
        RijndaelSimple.Encrypt(text, passPhrase, saltValue, hashAlgorithm, passwordIterations, initVector, keySize);
        text=RijndaelSimple.Decrypt(cipherText, passPhrase, saltValue, hashAlgorithm, passwordIterations, initVector, keySize);
        while(true)
        {
            Console.WriteLine("Please enter the password: ");
            string a = Console.ReadLine();
            if(a==text)
            {
                break;
            }
            Console.WriteLine("Bad Luck! Try again!");
        }
        Console.WriteLine("Well Done! You cracked it!");
        Console.ReadLine();
    }
}
~~~