from objects import Object
import numpy as np
from input_sensor import InputSensor

class CombineModalities:
    def __init__(self):
        self.number_of_sensors = 0
        self.sensor_list = []
        self.number_of_objects = 0
        self.objects_detected = []
        self.objects = []

    def set_sensor_list(self,in_sensors):
        self.sensor_list = in_sensors

    def count_number_of_sensors(self, sensor_input):
        self.number_of_sensors = len(sensor_input)

        return self.number_of_sensors

    def detect_number_of_objects(self,sensor_inputs):

        return self.number_of_objects



if __name__ == "__main__":
    combined_modality = CombineModalities()

    sensor1 = InputSensor()
    sensor1.data = [("knife", 1, 99), ("scissor", 2, 65), ("spoon", 3, 33), ("spoon", 4, 80), ("keys", 5, 95)]

    sensor2 = InputSensor()
    sensor2.data = [("keys", 5, 95), ("spoon", 4, 99), ("fork", 3, 99), ("scissor", 2, 95), ("knife", 1, 55)]

    sensor_input = [sensor1,sensor2]

    combined_modality.set_sensor_list(sensor_input)

    result = combined_modality.count_number_of_sensors(sensor_input)
    print("Number of sensors:",result)
    print("\n")

