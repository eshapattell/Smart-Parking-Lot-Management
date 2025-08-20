# 🅿️ Smart Parking Lot Management

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) 
[![Status](https://img.shields.io/badge/status-active-success.svg)]()  
---

# 📌 Project Overview
The *Smart Parking Lot Management System* is a Python-based simulation that manages the operations of a parking lot, including *car entry, exit, slot allocation, and overflow handling. It demonstrates how data structures like **linked lists* and *dynamic memory allocation* can be applied to solve a real-world problem.  

Unlike traditional fixed-slot approaches, this project dynamically assigns parking slots as vehicles enter and frees them upon exit. Cars currently parked are stored in a *linked list*, making insertion and deletion operations efficient. This allows the system to quickly update active parked cars without needing to shift data, which is common in array-based implementations.  

When the parking lot is full, the system gracefully handles *overflow* by preventing new entries until a slot is freed. This ensures proper resource management and simulates real-life constraints.  

The project also maintains a simple *log of parking history*, so that administrators or developers can analyze entry/exit events, available capacity, and peak usage times.  

This project is not only useful as a learning tool for understanding *self-referential structures* and *dynamic memory management, but it also mirrors the logic used in actual **smart parking solutions* deployed in malls, offices, and cities.  

In short:  
- 🅿️ Manages *entry and exit* of cars dynamically  
- 🧠 Reinforces *linked list concepts* in Python  
- 🚦 Handles *overflow scenarios* when the lot is full  
- 📊 Can be extended with features like pricing, slot categories, or time tracking  
- 🎓 Great project for students practicing *data structures + file handling* in real-world simulations
---

# ✨ Features

✔ *Dynamic Slot Allocation*  
Automatically assigns the next available parking slot when a car enters. Uses a *linked list* to keep track of active parked cars, making insertion and deletion fast and efficient.  

✔ *Car Exit Handling*  
When a car leaves, its slot is freed immediately and returned to the pool of available slots. The linked list updates dynamically without shifting or re-indexing data.  

✔ *Overflow Management*  
If the parking lot is full, new cars cannot enter until a slot becomes available. The system displays a clear "Parking Full" message to mimic real-world behavior.  

✔ *Linked List Implementation*  
Cars are stored as nodes in a linked list with details like car number and slot number. This demonstrates *self-referential structures* and *dynamic memory allocation* in Python.  

✔ *Parking History Log*  
Every car entry and exit is recorded, allowing administrators to review parking history and track usage patterns.  

✔ *Scalable Structure*  
The design makes it easy to add advanced features such as:  
- Time-based billing  
- VIP / reserved slots  
- Different zones for 2-wheelers, 4-wheelers, or EV charging spots  

✔ *Real-World Simulation*  
Mirrors how modern *smart parking systems* function in malls, offices, and cities, providing a solid foundation for more advanced IoT- or sensor-based extensions.  

✔ *Lightweight & Beginner-Friendly*  
Implemented entirely in *Python 3.9+* using only the standard library. No external dependencies, making it easy to run and understand.    

---

# 🧠 Data Structures
### **Linked List**
- Each node = one car currently in the parking lot  
- Contains: Car number, entry time, slot ID, next pointer  

### **Stack / Free List**
- For reusing freed slots dynamically  

### **Parking History**
- List of completed parking sessions  

---

# 🧮 Working Logic
1️⃣ **Car enters** → Assign next available slot  
2️⃣ **Track car** → Add node to linked list  
3️⃣ **Car exits** → Free slot, remove node from linked list  
4️⃣ **Overflow handling** → Reject entry if no free slot  
5️⃣ **Log history** → Keep entry/exit info  

---

# 📦 Project Layout


smart\_parking\_lot/
├── app.py          # Demo application
├── parking.py      # Core classes and parking logic
└── README.md       # Documentation

`

---

# 🚀 Quick Start
Run the demo locally:

bash
python3 app.py
`

This will:            
👉 Initialize parking lot with N slots          
👉 Allow cars to enter & exit                 
👉 Show parking status                 
👉 Maintain history of parked cars           

---

# 🧪 Example Output


Car KA-01-1234 entered Slot 1 at 10:30 AM 

Car KA-02-9876 entered Slot 2 at 10:32 AM 

Car KA-01-1234 exited Slot 1 at 11:00 AM 

Parking History:                
KA-01-1234 | Slot 1 | Entry: 10:30 | Exit: 11:00

KA-02-9876 | Slot 2 | Entry: 10:32 | Exit: Active


---

# 🧩 Extending the Simulator               

🔹 Add support for **different vehicle types** (car, bike, truck)        
🔹 Implement **pricing model** (per hour or per day)         
🔹 Add **search by car number**           
🔹 Support for **multi-floor parking**         
🔹 Database or file-based persistence       

---

# ⚙️ Requirements

* **Python 3.9+**
* Uses only standard library modules: `dataclasses`, `time`, `collections`

---

# 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).      
✔ Free to use, modify, and distribute with attribution.       
✔ No liability for issues arising from use.      

---

# 📊 Status

🟢 **Active** → This project is being maintained and improved.
