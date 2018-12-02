from functions import combine_modalities
import unittest


class TestCodes(unittest.TestCase):

    test = combine_modalities()
    sensor1 = [('knife', 1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
    sensor2 = [('knife', 1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95)]
    objects_detected = ["knife", "scissor", "fork", "spoon", "keys"]
    percentage_required = [99, 95, 99, 99, 95]
    objects = []

    def test_count_number_of_sensors(self):

        result = TestCodes.test.count_number_of_sensors([TestCodes.sensor1,TestCodes.sensor2])
        self.assertEqual(2,result)

    def test_detect_number_of_objects(self):

        result = TestCodes.test.detect_number_of_objects([TestCodes.sensor1,TestCodes.sensor2])
        self.assertEqual(5,result)

    def test_detect_objects(self):

        result = TestCodes.test.detect_objects([TestCodes.sensor1,TestCodes.sensor2])
        self.assertEqual(TestCodes.objects_detected,result)

    def test_create_objects(self):

        TestCodes.objects = TestCodes.test.create_objects(TestCodes.objects_detected, [TestCodes.sensor1, TestCodes.sensor2])
        self.assertEqual(TestCodes.objects_detected[0], TestCodes.objects[0].name)
        self.assertEqual(TestCodes.objects_detected[1], TestCodes.objects[1].name)
        self.assertEqual(TestCodes.objects_detected[2], TestCodes.objects[2].name)
        self.assertEqual(TestCodes.objects_detected[3], TestCodes.objects[3].name)
        self.assertEqual(TestCodes.objects_detected[4], TestCodes.objects[4].name)

        self.assertEqual(TestCodes.percentage_required[0], int(TestCodes.objects[0].percentage))
        self.assertEqual(TestCodes.percentage_required[1], int(TestCodes.objects[1].percentage))
        self.assertEqual(TestCodes.percentage_required[2], int(TestCodes.objects[2].percentage))
        self.assertEqual(TestCodes.percentage_required[3], int(TestCodes.objects[3].percentage))
        self.assertEqual(TestCodes.percentage_required[4], int(TestCodes.objects[4].percentage))


if __name__ == "__main__":
    unittest.main(exit=False)