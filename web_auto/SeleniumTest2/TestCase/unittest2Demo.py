import unittest2
class unittest2_Demo(unittest2.TestCase):
    def test_cogin(self):
        print(1)
    def test_add(self):
        print("4")
    def setUp(self):
        print("2")
    def tearDown(self):
        print("3")
    @classmethod
    def setUpClass(cls):
        print("5")
    @classmethod
    def tearDownClass(cls):
        print("6")
if __name__ == '__main__':
    unittest2.main()