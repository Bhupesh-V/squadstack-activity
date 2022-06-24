from parkinglot.parkinglot import ParkingLot


def readInstructions():
    with open("input.txt", "r") as file:
        for line in file:
            instruction = line.rstrip().split(" ")

            if instruction[0] == "Create_parking_lot":
                p = ParkingLot(int(instruction[1]))
                print(f"Created parking of {instruction[1]} slots")

            elif instruction[0] == "Park":
                slot = p.park_vehicle(instruction[1], int(instruction[3]))
                print(
                    f'Car with vehicle registration number "{instruction[1]}" has been parked at slot number {slot}'
                )

            elif instruction[0] == "Slot_numbers_for_driver_of_age":
                slot_nos = p.get_slot_numbers(int(instruction[1]))
                print(",".join(str(slot) for slot in slot_nos))

            elif instruction[0] == "Slot_number_for_car_with_number":
                print(p.get_slot(instruction[1]))

            elif instruction[0] == "Leave":
                slot_data = p.vacate_slot(int(instruction[1]))
                print(
                    f'Slot number {instruction[1]} vacated, the car with vehicle registration number "{slot_data.vehicle_registration_number}" left the space, the driver of the car was of age {slot_data.age_of_driver}'
                )

            elif instruction[0] == "Vehicle_registration_number_for_driver_of_age":
                vehicles = p.get_vehicle_registration(int(instruction[1]))
                if len(vehicles) != 0:
                    print(",".join(vehicles))
                else:
                    print(f"No vehicle found with age of driver", instruction[1])

            else:
                print("Unrecognised instruction, skipping")


if __name__ == "__main__":
    readInstructions()
