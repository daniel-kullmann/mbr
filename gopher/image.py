#!/usr/bin/python3

import base64

nested = [s.split(" ") for s in open("image.txt").read().split("\n")]
# Parse binary numbers
content2 = ''.join([chr(int(item, 2)) for sublist in nested for item in sublist if item != ''])
# Parse as hex string
content3 = ''.join([chr(int(s, 16)) for s in content2.split(" ") if s != ""])
# Parse as decimal string
content4 = ''.join([chr(int(s, 10)) for s in content3.split(" ") if s != ""])
# Decode base64
content5 = base64.b64decode(content4).hex()
### Split into hex chars, convert into binary, look for pattern
##content6a = [bin(int(content5[i:i+2], 16))[2:].rjust(8, '0') for i in range(0, len(content5), 2)]
##content6a = [s.translate(str.maketrans('01', ' X')) for s in content6a]
### Convert to binary again..
##content6 = bin(int(content5, 16))[2:]
##content6b = [content6[i:i+12].translate(str.maketrans('01', ' X')) for i in range(0, len(content6), 12)]
##print('\n'.join(content6a))
##print("")
##print('\n'.join(content6b))
print(content5)
