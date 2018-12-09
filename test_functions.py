from functions import CombineModalities
import unittest
from input_sensor import InputSensor


class TestCodes(unittest.TestCase):

    test = CombineModalities()
    sensor1 = InputSensor()
    sensor1.data = [("knife", 1, 99), ("scissor", 2, 65), ("spoon", 3, 33), ("spoon", 4, 80), ("keys", 5, 95)]

    sensor2 = InputSensor()
    sensor2.data = [("keys", 5, 95), ("spoon", 4, 99), ("fork", 3, 99), ("scissor", 2, 95), ("knife", 1, 55)]

    sensor_input = [sensor1,sensor2]

    objects_detected = ["knife","scissor","fork","spoon","keys"]

    def test_count_number_of_sensors(self):

        result = TestCodes.test.count_number_of_sensors(TestCodes.sensor_input)
        self.assertEqual(2,result)

    def test_detect_number_of_objects(self):

        number_of_objects_actual = TestCodes.test.detect_number_of_objects(TestCodes.sensor_input)
        self.assertEqual(5,number_of_objects_actual)


    def test_merge_sensor_data(self):

        merged_list = TestCodes.test.merge_sensor_data(TestCodes.sensor_input)
        self.assertEqual(10,len(merged_list))

    def test_create_final_objects(self):

        created_objects = TestCodes.test.create_final_objects(TestCodes.sensor_input)
        self.assertEqual(TestCodes.objects_detected[0],created_objects[0].name)


if __name__ == "__main__":
    unittest.main(exit=False)