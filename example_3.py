from ctypes import c_char, pointer

st = pointer(c_char(b'A'))
index = 0

while True:
    st[index] = 1
    index += 1
