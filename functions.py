

class combine_modalities:
    def __init__ (self):
        self.number_of_sensors = 0
        self.number_of_objects = 0
        self.objects_detected = []

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


if __name__ == "__main__":
    obj = combine_modalities()

    sensor1 = [('knife', 1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
    sensor2 = [('knife', 1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95)]
    sensor_input = [sensor1,sensor2]

    result = obj.count_number_of_sensors(sensor_input)
    print("Number of sensors:",result)

    result = obj.detect_number_of_objects(sensor_input)
    print("Number of objects detected:",result)

    result = obj.detect_objects(sensor_input)
    print("Objects detected:",result)
