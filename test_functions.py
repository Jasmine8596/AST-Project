from functions import CombineModalities
import unittest
from input_sensor import InputSensor


class TestCodes(unittest.TestCase):

    test = CombineModalities()
    sensor1 = InputSensor()
    sensor1.data = [("knife", 1, 99), ("scissor", 2, 65), ("spoon", 3, 33), ("spoon", 4, 80), ("keys", 5, 95)]

    sensor2 = InputSensor()
    sensor2.data = [("keys", 5, 95), ("spoon", 4, 99), ("fork", 3, 99), ("scissor", 2, 95), ("knife", 1, 55)]

    objects_detected = []
    percentage_required = []
    objects = []

    def test_count_number_of_sensors(self):

        result = TestCodes.test.count_number_of_sensors([TestCodes.sensor1,TestCodes.sensor2])
        self.assertEqual(2,result)

    def test_detect_number_of_objects(self):

        pass

    def test_detect_objects(self):

        pass

    def test_create_objects(self):

        pass


if __name__ == "__main__":
    unittest.main(exit=False)