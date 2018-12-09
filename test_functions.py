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
    percentage_required = [99,95,99,99,95]

    sensor1 = []
    sensor2 = []
    objects_detected = []
    percentage_required = []
    objects = []


    def test_count_number_of_sensors(self):

        self.test.number_of_sensors = self.test.count_number_of_sensors(self.sensor_input)
        self.assertEqual(2,self.test.number_of_sensors)

    def test_detect_number_of_objects(self):


        self.test.number_of_objects = self.test.detect_number_of_objects(self.sensor_input)
        self.assertEqual(5,self.test.number_of_objects)


        result = TestCodes.test.detect_number_of_objects([TestCodes.sensor1,TestCodes.sensor2])
        self.assertEqual(0,result)


    def test_merge_sensor_data(self):

        self.test.number_of_objects = self.test.detect_number_of_objects(self.sensor_input)
        self.test.merged_sensor_data = self.test.merge_sensor_data(self.sensor_input)
        self.assertEqual(10,len(self.test.merged_sensor_data))

    def test_create_final_objects(self):

        self.test.number_of_objects = self.test.detect_number_of_objects(self.sensor_input)
        self.test.merged_sensor_data = self.test.merge_sensor_data(self.sensor_input)
        self.test.objects = self.test.create_final_objects(self.test.merged_sensor_data)

        for det_obj,test_obj in zip(self.objects_detected,self.test.objects):
            self.assertEqual(det_obj, test_obj.name)

        for percent_req,test_obj in zip(self.percentage_required,self.test.objects):
            self.assertEqual(percent_req, test_obj.percentage)

if __name__ == "__main__":
    unittest.main(exit=False)