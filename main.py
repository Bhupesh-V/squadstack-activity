from parkinglot.parkinglot import ParkingLot

def readInstructions():
    with open("input.txt", "r") as file:
        for line in file:
            instruction = line.rstrip().split(" ")

            if instruction[0] == "Create_parking_lot":
                print("Create lot")
                p = ParkingLot()
                print(p)
            elif instruction[0] == "Park":
                print("Park car with number", instruction[1])
            elif instruction[0] == "Slot_numbers_for_driver_of_age":
                print("get slot numbers")
            elif instruction[0] == "Slot_number_for_car_with_number":
                print("get slot number for car")
            elif instruction[0] == "Leave":
                print("vacate slot")
            elif instruction[0] == "Vehicle_registration_number_for_driver_of_age":
                print("get reg number for driver age,", instruction[1])
            else:
                print("Unrecognised instruction, skipping")

if __name__ == "__main__":
    readInstructions()