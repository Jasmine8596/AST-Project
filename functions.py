

class combine_modalities:
    def __init__ (self):
        return None

    def count_number_of_sensors(self, sensor_input):
        number_of_sensors = len(sensor_input)

        return number_of_sensors


if __name__ == "__main__":
    obj = combine_modalities()

    sensor1 = [('knife', 1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
    sensor2 = [('knife', 1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95)]

    result = obj.count_number_of_sensors([sensor1,sensor2])
    print("Number of sensors:",result)