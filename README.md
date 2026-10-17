<div align="center">

# 🎓 Campus Club Event Registration System

**A clean, menu-driven Python app for managing event participants and attendees, right from your terminal.**

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-CLI-lightgrey)
![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen)
![Storage](https://img.shields.io/badge/Storage-Text%20Files-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📑 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Requirements](#-requirements)
- [Getting Started](#-getting-started)
- [Menu Options](#-menu-options)
- [Example Session](#-example-session)
- [How It Works](#-how-it-works)
- [Data Storage](#-data-storage)
- [Validation Rules](#-validation-rules)
- [Code Structure](#-code-structure)
- [Troubleshooting](#-troubleshooting)
- [Known Limitations](#-known-limitations)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 📖 About the Project

Running a campus club event means keeping track of who is taking part and who is coming to watch. This program handles both groups in one place:

- **Participants**: people actively taking part in the event, tracked by name.
- **Attendees**: students attending the event, tracked by name and **student ID**.

Each group has its own capacity limit, set when the program starts. Registrations are blocked once a group is full, duplicates are rejected, and everything can be saved to text files and reloaded the next time you run the program.

---

## ✨ Features

| | Feature | Details |
|---|---------|---------|
| 🎯 | **Event setup** | Enter the event name and separate capacities for participants and attendees |
| 👤 | **Participant management** | Register, remove, list, and view capacity details |
| 🎟️ | **Attendee management** | Register with a student ID, remove by ID, list, and view capacity details |
| 🛡️ | **Input validation** | No empty names, no digits in names, no duplicates, positive whole-number capacities only |
| 🔠 | **Case-insensitive matching** | `alice` and `Alice` are treated as the same person |
| 💾 | **Persistent storage** | Data is saved to and loaded from plain text files |
| ⚙️ | **Error handling** | Handles invalid input and file read/write problems without crashing |

---

## 📋 Requirements

- **Python 3.6 or newer**
- No external libraries (standard library only)

Check your version with:

```bash
python --version
```

---

## 🚀 Getting Started

**1. Save the code** as `event_registration.py`.

**2. Run it** from a terminal in the same folder:

```bash
python event_registration.py
```

> On some systems you may need to use `python3 event_registration.py`.

**3. Answer the setup prompts:**

```text
Enter event name: Tech Talk 2026
Enter event participant capacity: 20
Enter event attendee capacity: 50
```

**4. Use the menu** to register people, view lists, and save your data.

---

## 🧭 Menu Options

### Participants

| # | Action | What it does |
|:-:|--------|--------------|
| 1 | Register participant | Adds a participant by name |
| 2 | Remove participant | Removes a participant by name |
| 3 | Show registered participants | Lists everyone with totals and remaining spaces |
| 4 | Participant capacity details | Shows capacity, registered count, and spaces left |

### Attendees

| # | Action | What it does |
|:-:|--------|--------------|
| 5 | Register attendee | Adds an attendee with a name and student ID |
| 6 | Remove attendee | Removes an attendee by student ID |
| 7 | Show registered attendees | Lists everyone with totals and remaining spaces |
| 8 | Attendee capacity details | Shows capacity, registered count, and spaces left |

### Data

| # | Action | What it does |
|:-:|--------|--------------|
| 9 | Save all data | Writes data to files and keeps the program running |
| 10 | Save data and exit | Writes data to files and quits |

---

## 🖥️ Example Session

```text
===== CAMPUS CLUB EVENT REGISTRATION =====
Event: Tech Talk 2026
1. Register participant
2. Remove participant
3. Show registered participants
4. Participant capacity details
5. Register attendee
6. Remove attendee
7. Show registered attendees
8. Attendee capacity details
9. Save all data
10. Save data and Exit
Enter your choice (1-10): 1
Enter participant name: Alice Johnson
Alice Johnson registered successfully!

Enter your choice (1-10): 5
Enter attendee name: Bob Smith
Enter student ID: S12345
Bob Smith registered successfully!

Enter your choice (1-10): 7

==== Registered Attendees ====
Total attendees: 1
Remaining spaces: 49
Name: Bob Smith | Student ID: S12345

Enter your choice (1-10): 10
All registration data saved successfully!
Data saved. Goodbye!
```

---

## 🔄 How It Works

```text
        ┌──────────────────────┐
        │  Start program       │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │  Enter event name &  │
        │  both capacities     │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │  Load saved data     │
        │  (if files exist)    │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
   ┌───▶│  Show menu           │
   │    └──────────┬───────────┘
   │               ▼
   │    ┌──────────────────────┐
   │    │  Run chosen action   │
   │    └──────────┬───────────┘
   │               ▼
   │         Option 10?
   │          │       │
   │         No      Yes
   └──────────┘       ▼
                ┌──────────────┐
                │ Save & exit  │
                └──────────────┘
```

---

## 💾 Data Storage

Two plain text files are created in the folder where you run the program:

| File | Format | Example line |
|------|--------|--------------|
| `participants.txt` | One name per line | `Alice Johnson` |
| `attendees.txt` | `name\|student_id` per line | `Bob Smith\|S12345` |

Saved data is loaded automatically at startup. If the files don't exist yet, the program starts with empty lists.

> ⚠️ **Don't forget to save.** Changes are written to disk only when you choose option **9** or **10**. Closing the window or pressing `Ctrl + C` will lose any unsaved changes.

---

## ✅ Validation Rules

| Field | Rules |
|-------|-------|
| **Capacity** | Must be a whole number greater than zero |
| **Participant name** | Not empty, no digits, not already registered (case-insensitive) |
| **Attendee name** | Not empty, no digits |
| **Student ID** | Not empty, must be unique (case-insensitive) |
| **Registration** | Blocked once the relevant capacity is full |
| **Menu choice** | Must be a number from 1 to 10 |

---

## 🗂️ Code Structure

```text
event_registration.py
├── Setup                    → event name and capacity input
├── Participant functions    → register, remove, list, capacity info
├── Attendee functions       → register, remove, list, capacity info
├── save_data()              → writes participants.txt and attendees.txt
├── load_data()              → reads saved data back at startup
├── terminal_menu()          → prints the menu
└── Main loop                → handles user choices until exit
```

---

## 🩺 Troubleshooting

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| `python` is not recognized | Python isn't installed or isn't on your PATH | Install Python and tick **Add to PATH**, or try `python3` |
| Old data didn't appear | Program was run from a different folder | Run it from the folder containing the `.txt` files |
| Changes disappeared | Program was closed without saving | Use option **9** regularly, and exit with option **10** |
| "Capacity is full" right away | Entered capacity is lower than the loaded records | Restart and enter a larger capacity |
| "Error while saving data" | No write permission in the folder | Run from a folder you can write to |

---

## ⚠️ Known Limitations

- **Capacities and event name are not saved**, so you are asked for them every run.
- **Names containing digits are rejected**, which may exclude some valid names.
- **A `|` character in an attendee name** could corrupt the attendee file, since it's used as the separator.
- Storage is plain text rather than a database, so it suits small to medium events.

---

## 💡 Future Improvements

- [ ] Save and load the event name and capacities
- [ ] Search for a participant or attendee
- [ ] Export registrations to CSV
- [ ] Block the `|` character in names
- [ ] Add a simple GUI or web interface

---

## 📄 License

This project is free to use for learning and personal projects. Add a license of your choice if you plan to share it publicly.

---

## 👩‍💻 Author

**Madhavi Kapoor**

*Built as a campus club event management project.*

---

<div align="center">

⭐ If you found this project helpful, consider giving it a star!

</div>
