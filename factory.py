class Car:
    def drive(self):
        print("Driving a car.")

class Bike:
    def drive(self):
        print("Riding a bike.")

class Truck:
    def drive(self):
        print("Driving a truck.")


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Unknown vehicle type")


if __name__ == "__main__":
    factory = VehicleFactory()

    # Create a car
    car = factory.get_vehicle("car")
    car.drive()

    # Create a bike
    bike = factory.get_vehicle("bike")
    bike.drive()

    # Create a truck
    truck = factory.get_vehicle("truck")
    truck.drive()
