import unittest


class TestDemo(unittest.TestCase):

    def fun_1(self) -> str:
        x = None
        return x

    def fun_2(self):
        x = None
        return x

    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")

    def setUp(self) -> None:
        print("setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")

    def tearDown(self) -> None:
        print("teardown")

    def test_sum(self):
        x = 1 + 2
        print(x)
        self.assertEqual(3, x, f'x={x} exception=3')

    def test_demo(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
