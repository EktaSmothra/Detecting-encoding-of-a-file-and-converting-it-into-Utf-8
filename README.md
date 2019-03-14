# Detecting-encoding-of-a-file-and-converting-it-into-Utf-8
For manipulating text in computers, we should have mapping between the character set ( it is the finite list of characters that the system recognizes) and numbers. Text is ordered sequences of characters and encoding is the process of converting characters to numbers. To understand this concept more, let's take an example of following string :
 
    Hello

In unicode, this "Hello" would represent as:

    U+0048 U+0065 U+006C U+006C U+006F.

We can see that it is just a bunch of code points or numbers. Now the point is how we will store this code point in memory of computer. This is where encoding comes in play. The earliest idea was to store these numbers in two bytes each. So, "Hello" would become :

    00 48 00 65 00 6C 00 6C 00 6F

Well, technically, it can also be written as following.

    48 00 65 00 6C 00 6C 00 6F 00 ?

Early implementors wanted to be able to store their Unicode code points in high-endian or low-endian mode, whichever their particular CPU was fastest at, meaning, there were already two ways to store Unicode. There were already some doggone documents out there using various ANSI and DBCS character sets and who’s going to convert them all? Moi? For this reason alone most people decided to ignore Unicode for several years and in the meantime things got worse. Then came the concept of Utf-8. In this, every code point from 0-127 is stored in a single byte. Only code points 128 and above are stored using 2, 3, in fact, up to 6 bytes. Now "Hello" can be stored as:

    48 65 6C 6C 6F

If you want to study more about encodings and history about it, i would recommend you to go through the second reference. Now, moving on to my program and understanding how encoding detection can be done in python.

## Chardet
Chardet is a universal character encoding detector. This library is a port of the auto-detection code in Mozilla. The easiest way to use chardet library is with the detect function. This function takes one argument and returns a dictionary containing auto-detected encoding including confidence level from 0 to 1. You can study more about it on https://chardet.readthedocs.io/en/latest/usage.html#basic-usage

## urllib.request
This module defines various functions and classes that can be used for opening url in web browser. It means you can access your websites via your program. You can download data, parse data, access website, perform GET and POST requests, modify headers etc. Read more about this module in the official guide at https://docs.python.org/3/library/urllib.request.html and https://pythonprogramming.net/urllib-tutorial-python-3/

## codecs
This module defines base classes for standard Python codecs (encoders and decoders) and provides access to the internal Python codec registry which manages the codec and error handling lookup process. We can also execute the code of this repository without using codecs. To learn more about codecs, you can follow the official documentation at https://docs.python.org/2/library/codecs.html

These libraries and having basic knowledge of file operations in python are enough to understand the code and its working. 

# References
* http://www.wellformedness.com/blog/understanding-text-encoding-in-python-2-and-python-3/   
* https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/

