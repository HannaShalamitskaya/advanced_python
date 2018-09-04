import ctypes

ctypes.c_char.from_address(0)

# a = ctypes.c_int(12)
# b = ctypes.c_char.from_address(ctypes.addressof(a))
# a == b
# a.value == b.value
