# Randx
Secure text generator using Python. This script follows uppercase, lowercase, special symbols and numerical characters to make your password more strong. 

# Usage
### Without Downloading Script
```bash
curl -s https://raw.githubusercontent.com/FlareXes/randx/master/randx.py | python -
```
With Specific Length Like Here Is 32
```bash
curl -s https://raw.githubusercontent.com/FlareXes/randx/master/randx.py | python - 32
```
Also Remove Ambiguous Chars
```bash
curl -s https://raw.githubusercontent.com/FlareXes/randx/master/randx.py | python - 11 --safe
```

### Usual Method After Downloading
```bash
python randx.py
```
With Specific Length Like Here Is 32
```bash
python randx.py 32
```
Also Remove Ambiguous Chars
```bash
python randx.py 11 --safe
```

### Randx Executable
If you don't like using `python` everytime. Then, much better option is to use complied binaries available in `bin` directory.
```
randx_unix: For Linux and Macos
randx_win: For Windows
```

Now, we can use it from anywhere in terminal
```bash
randx_unix 16 --safe
```

You can even create yourself if you want to. Follow the below steps.
```bash
pip install pyinstaller
git clone https://github.com/flarexes/randx
cd randx && pyinstaller --onefile randx.py
```
Read this for more info [.py to .exe](https://towardsdatascience.com/how-to-easily-convert-a-python-script-to-an-executable-file-exe-4966e253c7e9)

# License

Licensed under **The Unlicense**

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
