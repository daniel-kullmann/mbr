#!/usr/bin/python3

import re, base64

base64_chars = re.compile("[A-Za-z0-9/+=]")
content = "".join(open("welcome.enc").read().split("\n"))
for c in content:
    if not base64_chars.match(c):
        print(c)
print("==========")
fh = open("welcome.enc.png", "wb")
fh.write(base64.b64decode(content))
fh.close()
