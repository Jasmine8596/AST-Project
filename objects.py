class Object:

    def __init__(self,object_name=None,object_num=0,object_percentage=0):
        self.name = object_name
        self.number = object_num
        self.percentage = object_percentage

    def __str__(self):
        string = self.name + " , " + str(self.number) + " , " + str(self.percentage)
        return string
