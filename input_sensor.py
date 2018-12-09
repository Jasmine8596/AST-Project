import pprint 

class InputSensor:

    def __init__(self):
        self.data = []
        self.algorithm = ""

    def set_algorithm(self):
        pass

    def get_data(self):
        return self.data


if __name__ == "__main__":

    sensor_1 = InputSensor()
    sensor_1.data = [("knife", 1, 99), ("scissor", 2, 65), ("spoon", 3, 33), ("spoon", 4, 80), ("keys", 5, 95)]
    print(sensor_1.get_data())
