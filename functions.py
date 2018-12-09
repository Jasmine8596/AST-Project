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

        for number in range(self.number_of_sensors):
            reading = sensor_inputs[number]
            number_of_reading = len(reading)

            if number_of_reading > self.number_of_objects:
                self.number_of_objects = number_of_reading

        return self.number_of_objects

    def detect_objects(self,sensor_inputs):

        for sensor in sensor_inputs:
            for object in sensor:
                name = object[0]

                if name not in self.objects_detected:
                    self.objects_detected.append(name)
                else:
                    self.objects_detected = []
                    break

        return self.objects_detected

    def create_objects(self, sensor_inputs, sensors):

        for index, object_found in enumerate(sensor_inputs):
            created_object = Object(object_found, index + 1)
            self.objects.append(created_object)

        sensors = np.array(sensors)
        percentages = sensors[:, :, 2]
        percentages = percentages.T

        for index, percentage in enumerate(percentages):
            self.objects[index].percentage = max(percentage)

        return self.objects


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

