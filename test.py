import unittest
from captcha_decoder import decoder


class TestStringMethods(unittest.TestCase):

    def test_images(self):
        # self.assertEqual(decoder('test.jpg'), '1bda2')
        # self.assertEqual(decoder('test2.jpg'), '7f4ca')
        self.assertEqual(decoder('imageRandeCode.jpg'), '1234')

if __name__ == '__main__':
    unittest.main()
