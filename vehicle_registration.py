class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def update_owner(self, new_owner):
            self.owner = new_owner

vehicles = {}

def new_car(reg_num, type, owner):
    vehicles[reg_num] = Vehicle(reg_num, type, owner)
    print(f"Car {reg_num} of type {type} has been added to Vehicles")

def update_owner(reg_num, new_owner):
     if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Owner of car {reg_num} has been changed to {new_owner}")

new_car(123, "Sedan", "Jeff")
new_car(456, "Truck", "Bill")
update_owner(456, "Frank")
