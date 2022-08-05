import unittest
import text_change


class TestTextChange(unittest.TestCase):

    def test_upper(self):
        word = "good day"
        result = text_change.everything(word)

        self.assertEqual(result,"GOOD DAY")


if __name__ == "__main__":
    unittest.main()