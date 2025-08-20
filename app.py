from parking import ParkingLot
import time

# Initialize parking lot with 3 slots
lot = ParkingLot(capacity=3)

# Cars enter
lot.park_car("KA-01-1234")
time.sleep(1)
lot.park_car("KA-02-9876")
time.sleep(1)
lot.park_car("KA-03-2222")

# Try overflow
lot.park_car("KA-04-3333")

# Show current parking
lot.show_active_parking()

time.sleep(2)

# Cars exit
lot.remove_car("KA-01-1234")
lot.remove_car("KA-02-9876")

# Show active parking again
lot.show_active_parking()

# Show history
lot.show_history()
