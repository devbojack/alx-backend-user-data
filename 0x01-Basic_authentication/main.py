#!/usr/bin/env python3

import base64

my_text = "Hello World"
my_text = my_text.encode("ascii")

my_text_base64 = base64.b64encode(my_text)

print(my_text_base64)


new_txt = base64.b64decode(my_text_base64)

print(new_txt)
