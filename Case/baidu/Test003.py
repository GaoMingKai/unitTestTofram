import unittest


class Test003(unittest.TestCase):


    def setUp(self):
        print("Test003")
    def tearDown(self):
        print("Test003behand")
    #测试单元测试
    def Test(self):
        print("Test003")
        self.assertEqual(2,2,"两个数据不同耶！")
