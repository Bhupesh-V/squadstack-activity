class Slot(dict):
    """Slot data"""

    vehicle_registration_number: str
    age_of_driver: int

class ParkingLot:

    def __init__(self, slots_count):
        self.slots_count = slots_count
        # slots are assigned in order from 0 to n -1
        self.slots = dict.fromkeys([n for n in range(self.slots_count)])

    def park_vehicle(vehicle_registration_number, driver_age):
        """A new vehicle enters the parking lot, create a new slot for them"""
        if len(self.slots) < self.slots_count:
            available_slot = self.__get_next_slot()
            self.slots[available_slot] = Slot(self.vehicle_registration_number, self.driver_age)
        else:
            print("Request to park rejected, No empty slots at the moment")

    def get_slot_numbers(driver_age: int) -> List[int]:
        slots_with_driver_age = []
        for slot in self.slots:
            if slot.driver_age == driver_age:
                slots_with_driver_age.append(slot)
        return slots_with_driver_age


    def get_slot(vehicle_registration_number: str):
        for slot in self.slots:
            if slot.vehicle_registration_number == vehicle_registration_number:
                return slot

    def get_vehicle_registration(driver_age: int) -> List[str]:
        vehicles = []
        for slot in self.slots:
            if slot.driver_age == driver_age:
                vehicles.append(slot.vehicle_registration_number)
        return vehicles

    def vacate_slot(slot_number: int):
        """A vehicle wants to leave the parking lot, vacate their slot"""
        if slot_number not in self.slots.keys():
            print("Invalid slot number")
        else:
            # make it None (i.e available to book again)
            self.slots[slot_number] = None

    def __get_next_slot() -> int:
        """Get next available free slot"""
        for slot in self.slots:
            if self.slots[slot] is None:
                # get the first available slot, assuming its nearest to entry
                return slot
