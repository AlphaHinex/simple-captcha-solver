import unittest
from captcha_decoder import decoder


class TestStringMethods(unittest.TestCase):

    def test_images(self):
        # Duplicated numbers
        # self.assertEqual(decoder('imageRandeCode.jpg'), '6263')
        # self.assertEqual(decoder('raw-material/3.jpg'), '3200')
        self.assertEqual(decoder('raw-material/6.jpg'), '6698')
        # self.assertEqual(decoder('raw-material/7.jpg'), '0797')
        # self.assertEqual(decoder('raw-material/9.jpg'), '4393')

        # Right
        # self.assertEqual(decoder('raw-material/0.jpg'), '0619')
        # self.assertEqual(decoder('raw-material/1.jpg'), '1683')
        # self.assertEqual(decoder('raw-material/2.jpg'), '2983')
        # self.assertEqual(decoder('raw-material/4.jpg'), '4186')
        # self.assertEqual(decoder('raw-material/5.jpg'), '9501')
        # self.assertEqual(decoder('raw-material/8.jpg'), '8194')

if __name__ == '__main__':
    unittest.main()
