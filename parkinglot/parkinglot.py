from typing import List
from collections import OrderedDict


class Slot:
    """Slot data"""

    def __init__(self, vehicle_registration_number: str, age_of_driver: int):
        self.vehicle_registration_number = vehicle_registration_number
        self.age_of_driver = age_of_driver


class ParkingLot:
    def __init__(self, slots_count):
        self.slots_count = slots_count
        self.is_lot_full = False
        # slots are assigned in order from 1 to N
        self.slots = OrderedDict.fromkeys([n for n in range(1, self.slots_count + 1)])

    def park_vehicle(self, vehicle_registration_number, driver_age) -> int:
        """A new vehicle enters the parking lot, create a new slot for them"""
        if not self.is_lot_full:
            available_slot = self.__get_next_slot()
            slot = Slot(
                vehicle_registration_number=vehicle_registration_number,
                age_of_driver=driver_age,
            )
            self.slots[available_slot] = slot
            return available_slot
        else:
            self.is_lot_full = True
            print("Request to park rejected, No empty slots at the moment")

    def get_slot_numbers(self, driver_age: int) -> List[int]:
        slots_with_driver_age = []
        for slot in self.slots:
            if (
                self.slots[slot] is not None
                and self.slots[slot].age_of_driver == driver_age
            ):
                slots_with_driver_age.append(slot)
        return slots_with_driver_age

    def get_slot(self, vehicle_registration_number: str):
        for slot in self.slots:
            if (
                self.slots[slot].vehicle_registration_number
                == vehicle_registration_number
            ):
                return slot

    def get_vehicle_registration(self, driver_age: int) -> List[str]:
        vehicles = []
        for slot in self.slots:
            if (
                self.slots[slot] is not None
                and self.slots[slot].age_of_driver == driver_age
            ):
                vehicles.append(slot.vehicle_registration_number)
        return vehicles

    def vacate_slot(self, slot_number: int) -> Slot:
        """A vehicle wants to leave the parking lot, vacate their slot"""
        if slot_number not in self.slots.keys():
            print("Invalid slot number")
            return
        else:
            deleted_data = self.slots[slot_number]
            # make it None (i.e available to book again)
            self.slots[slot_number] = None
        return deleted_data

    def __get_next_slot(self) -> int:
        """Get next available free slot"""
        for slot in self.slots:
            if self.slots[slot] is None:
                # get the first available slot, assuming its nearest to entry
                return slot
        return None
