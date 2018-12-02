from objects import Object
import numpy as np


class combine_modalities:
    def __init__(self):
        self.number_of_sensors = 0
        self.number_of_objects = 0
        self.objects_detected = []
        self.objects = []

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
    obj = combine_modalities()

    sensor1 = [('knife', 1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
    sensor2 = [('knife', 1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95)]
    sensor_input = [sensor1,sensor2]
    objects_found = ["knife", "scissor", "fork", "spoon", "keys"]

    result = obj.count_number_of_sensors(sensor_input)
    print("Number of sensors:",result)
    print("\n")

    result = obj.detect_number_of_objects(sensor_input)
    print("Number of objects detected:",result)
    print("\n")

    result = obj.detect_objects(sensor_input)
    print("Objects detected:",result)
    print("\n")

    result = obj.create_objects(objects_found, sensor_input)
    print("Objects created:")
    for param in result:
        print(param)
    print("\n")
