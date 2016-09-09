import unittest

def hap(a,b):
    return a+b
def gop(a,b):
    return a*b


class My:
    def __init__(self,x,y):
        self.a=x
        self.b=y
        
class MyUnitTest1(unittest.TestCase):
        
    def test_a(self):
        obj = My(10,20)
        self.assertTrue(obj.a==10, 'a test')
        
    def test_b(self):
        obj = My(10,20)
        self.assertTrue(obj.b==20, 'b test')


def main():
    rst=hap(10,20)
    print(rst)
    
class MyUnitTest(unittest.TestCase):
#     def tearDown(self):
#         print("tear down")
#     
#     def setUp(self):
#         print("setup")
        
    def testHap(self):
        rst = hap(10,20)
        self.assertEqual(rst, 30, 'hap test')
        
    def testGop(self):
        rst = gop(10,20)
        self.assertEqual(rst, 200, 'gop test')
    
if __name__=='__main__':
    
    main()
    
#     suit = unittest.TestSuite()
#     suit.addTest(MyUnitTest('testHap'))
#     suit.addTest(MyUnitTest1('test_b'))
#     unittest.TextTestRunner(verbosity=2).run(suit)
    
#     suit = unittest.TestLoader().loadTestsFromTestCase(MyUnitTest)
#     unittest.TextTestRunner(verbosity=2).run(suit)

#     main()
#     unittest.main()