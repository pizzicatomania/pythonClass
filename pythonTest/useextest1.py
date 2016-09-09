from ctypes import *
import extest

class Test(Structure):
    _fields_=[("aa", c_int), ("bb", c_int), ("cc", c_char_p)]
    
obj = Test(10, 20, b'abc')
print(obj.aa, obj.bb, obj.cc)

result = extest.sfn(addressof(obj))
print(result)