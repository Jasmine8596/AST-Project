from functions import combine_modalities
import unittest


class TestCodes(unittest.TestCase):

    test = combine_modalities()
    sensor1 = [('knife', 1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
    sensor2 = [('knife', 1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95)]
    objects = ["knife", "scissor", "fork", "spoon", "keys"]

    def test_count_number_of_sensors(self):

        result = TestCodes.test.count_number_of_sensors([TestCodes.sensor1,TestCodes.sensor2])
        self.assertEqual(2,result)

    def test_detect_number_of_objects(self):

        result = TestCodes.test.detect_number_of_objects([TestCodes.sensor1,TestCodes.sensor2])
        self.assertEqual(5,result)

    def test_detect_objects(self):

        result = TestCodes.test.detect_objects([TestCodes.sensor1,TestCodes.sensor2])
        self.assertEqual(TestCodes.objects,result)

    def test_create_objects(self):

        result = TestCodes.test.create_objects(TestCodes.objects)
        self.assertEqual(TestCodes.objects[0], result[0].name)
        self.assertEqual(TestCodes.objects[1], result[1].name)
        self.assertEqual(TestCodes.objects[2], result[2].name)
        self.assertEqual(TestCodes.objects[3], result[3].name)
        self.assertEqual(TestCodes.objects[4], result[4].name)


if __name__ == "__main__":
    unittest.main(exit=False)