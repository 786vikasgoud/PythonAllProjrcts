class Car:
    def __init__(self,type):
        self.type = type

    def typo(self,type):
        print(self.type)
    @staticmethod
    def start():
        print("car is started")

    @staticmethod
    def stop():
        print("car is stoped")


class Car_model(Car):
    def __init__(self, name, type):
        super().__init__(type)
        super().typo(type)
        self.name = name


car = Car_model("Fortuner","electric")
car.start()
car.typo("electric")
print(car.type)
