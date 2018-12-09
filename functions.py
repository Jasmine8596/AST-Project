from objects import Object
import numpy as np
from input_sensor import InputSensor

class CombineModalities:
    def __init__(self):
        self.number_of_sensors = 0
        self.sensor_list = []
        self.number_of_objects = 0
        self.merged_sensor_data = []
        self.objects = []

    def set_sensor_list(self,in_sensors):
        self.sensor_list = in_sensors

    def count_number_of_sensors(self, sensor_input):
        self.number_of_sensors = len(sensor_input)

        return self.number_of_sensors

    def detect_number_of_objects(self,sensor_inputs):

        for sensor in sensor_inputs:
            for recognised_object in sensor.data:
                if recognised_object[1] > self.number_of_objects:
                    self.number_of_objects = recognised_object[1]

        return self.number_of_objects

    def merge_sensor_data(self,sensor_inputs):

        for sensor in sensor_inputs:
            for recognised_object in sensor.data:
                self.merged_sensor_data.append(recognised_object)

        return self.merged_sensor_data




if __name__ == "__main__":
    combined_modality = CombineModalities()

    sensor1 = InputSensor()
    sensor1.data = [("knife", 1, 99), ("scissor", 2, 65), ("spoon", 3, 33), ("spoon", 4, 80), ("keys", 5, 95)]

    sensor2 = InputSensor()
    sensor2.data = [("keys", 5, 95), ("spoon", 4, 99), ("fork", 3, 99), ("scissor", 2, 95), ("knife", 1, 55)]

    sensor_input = [sensor1,sensor2]

    combined_modality.set_sensor_list(sensor_input)

    number_of_sensors = combined_modality.count_number_of_sensors(sensor_input)
    print("Number of sensors:",number_of_sensors)
    print("\n")

    number_of_objects = combined_modality.detect_number_of_objects(sensor_input)
    print("Number of objects detected:",number_of_objects)
    print("\n")

    merged_list = combined_modality.merge_sensor_data(sensor_input)
    for i in merged_list:
        print(i)

