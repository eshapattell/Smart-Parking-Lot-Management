from dataclasses import dataclass, field
import time


@dataclass
class Car:
    number: str
    entry_time: float = field(default_factory=time.time)
    slot_id: int = None
    next: "Car" = None  # linked list pointer


@dataclass
class ParkingRecord:
    car_number: str
    slot_id: int
    entry_time: float
    exit_time: float


class ParkingLot:
    def _init_(self, capacity: int):
        self.capacity = capacity
        self.head: Car = None  # linked list head
        self.available_slots = list(range(1, capacity + 1))  # free slots pool
        self.history: list[ParkingRecord] = []

    def is_full(self) -> bool:
        return len(self.available_slots) == 0

    def park_car(self, car_number: str):
        if self.is_full():
            print(f"❌ Parking Full! Car {car_number} cannot be parked.")
            return None

        slot_id = self.available_slots.pop(0)
        new_car = Car(number=car_number, slot_id=slot_id)

        # Add to linked list (at head for O(1))
        new_car.next = self.head
        self.head = new_car

        print(f"✅ Car {car_number} entered Slot {slot_id} at {time.ctime(new_car.entry_time)}")
        return new_car

    def remove_car(self, car_number: str):
        prev, curr = None, self.head
        while curr:
            if curr.number == car_number:
                # Remove from linked list
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next

                exit_time = time.time()
                record = ParkingRecord(
                    car_number=curr.number,
                    slot_id=curr.slot_id,
                    entry_time=curr.entry_time,
                    exit_time=exit_time
                )
                self.history.append(record)

                # Free slot
                self.available_slots.append(curr.slot_id)
                self.available_slots.sort()

                print(f"🚗 Car {car_number} exited Slot {curr.slot_id} at {time.ctime(exit_time)}")
                return record

            prev, curr = curr, curr.next

        print(f"⚠️ Car {car_number} not found in parking lot.")
        return None

    def show_active_parking(self):
        print("\n🅿️ Active Parking:")
        curr = self.head
        if not curr:
            print("No cars currently parked.")
            return
        while curr:
            print(f"- Car {curr.number} in Slot {curr.slot_id} (since {time.ctime(curr.entry_time)})")
            curr = curr.next

    def show_history(self):
        print("\n📜 Parking History:")
        if not self.history:
            print("No records yet.")
            return
        for record in self.history:
            entry = time.ctime(record.entry_time)
            exit_t = time.ctime(record.exit_time)
            print(f"- {record.car_number} | Slot {record.slot_id} | Entry: {entry} | Exit: {exit_t}")
