from functions import combine_modalities
import unittest


class TestCodes(unittest.TestCase):

    def test_count_number_of_sensors(self):
        test = combine_modalities()

        sensor1 = [('knife', 1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
        sensor2 = [('knife', 1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95)]

        result = test.count_number_of_sensors([sensor1,sensor2])
        self.assertEqual(2,result)

    def test_detect_number_of_objects(self):
        test = combine_modalities()

        sensor1 = [('knife', 1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
        sensor2 = [('knife', 1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95)]

        result = test.detect_number_of_objects([sensor1,sensor2])
        self.assertEqual(5,result)


if __name__ == "__main__":
    unittest.main(exit=False)