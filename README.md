# 🅿️ Smart Parking Lot Management

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) 
[![Status](https://img.shields.io/badge/status-active-success.svg)]()  
---

# 📌 Project Overview
The **Smart Parking Lot Management System** is a Python-based simulation that manages a parking lot in real time.  
It ensures smooth **entry and exit tracking** for cars, manages **dynamic slot allocation**, and gracefully handles cases when the parking lot is full.  

This project uses **linked lists** to track currently parked cars, making slot management efficient and flexible.  
It’s a great hands-on implementation for **data structures (linked list, dynamic memory)** and **real-world problem-solving**.  

---

# ✨ Features
✔ Track **car entry & exit** in real-time  
✔ **Linked list** to manage active parked cars  
✔ **Dynamic memory allocation** for flexible slot usage  
✔ Prevent overflow with **"Parking Full" handling**  
✔ Maintains **history of parked cars** (with entry/exit time)  
✔ Lightweight, dependency-free (pure Python)  

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
