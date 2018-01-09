import unittest


class Test004(unittest.TestCase):


    def setUp(self):
        print("Test004")
    def tearDown(self):
        print("Test004behand")
    def Test(self):
        print("Test003")
        self.assertEqual(1,2,"两个数据不同耶！")