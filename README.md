# Campus Club Event Sign-Up

A simple command-line program written in Python to manage participant registrations for a campus club event. You can register people, remove them, view the list, check how many spots are left, and save everything to a file so your data is still there the next time you run the program.

## Features

- Set an event name and a maximum capacity
- Register participants (until the event is full)
- Remove participants (name matching is not case-sensitive)
- View the list of registered participants
- See capacity details: total capacity, number registered, and remaining spaces
- Save data to a file and load it automatically on the next run

## Requirements

- Python 3.6 or higher (uses f-strings)
- No external libraries needed. Only Python's built-in features are used.

## How to Run

1. Download or clone this project.
2. Open a terminal in the project folder.
3. Run:

   ```
   python campus_event.py
   ```

   (On some systems you may need to use `python3 campus_event.py`.)

## How to Use

When the program starts, it asks for:

1. **Event name**: for example, `Coding Workshop`
2. **Event capacity**: a whole number greater than zero, for example, `30`

If a saved file (`registrations.txt`) already exists from a previous session, the program loads the saved event name, capacity, and participants, and these replace what you just typed.

Then the main menu appears:

```
==== Campus Club Event sign up ====
1. Register participant
2. Remove participant
3. Show the list of the registered participants
4. Event participation capacity details
5. Save the data
6. Save data and Exit
```

Type a number from 1 to 6 and press Enter.

| Option | What it does |
|--------|--------------|
| 1 | Registers a new participant by name |
| 2 | Removes a participant by name |
| 3 | Shows the total number of participants, remaining spaces, and all names |
| 4 | Shows the event's maximum capacity, total participants, and remaining spaces |
| 5 | Saves the current data to `registrations.txt` |
| 6 | Saves the data and exits the program |

## Input Rules

- **Capacity** must be a whole number greater than zero.
- **Participant names** cannot be empty, cannot contain numbers, and cannot be duplicates (`Ali` and `ali` count as the same person).
- Registration is blocked once the event reaches full capacity.

## Saved Data Format

Data is stored in a plain text file called `registrations.txt` in the same folder as the program:

```
Coding Workshop
30
Ali
Sara
John
```

- Line 1: event name
- Line 2: event capacity
- Line 3 onward: one participant name per line

> **Tip:** Choose option 5 or 6 to save. If you close the program without saving, any new registrations or removals will be lost.

## Project Structure

```
.
├── campus_event.py      # Main program
├── registrations.txt    # Created automatically when you save
└── README.md            # This file
```

## Code Overview

| Function | Purpose |
|----------|---------|
| `register_participant()` | Validates and adds a participant |
| `remove_participant()` | Finds and removes a participant |
| `participants_in_event()` | Displays the participant list and counts |
| `capacity_information()` | Displays capacity details |
| `save_data()` | Writes event data to `registrations.txt` |
| `load_data()` | Reads saved data from `registrations.txt` |
| `terminal_menu()` | Prints the main menu |

## Error Handling

The program handles common problems without crashing:

- Non-numeric or invalid capacity input
- Missing or corrupted save file
- File read/write errors

## Possible Future Improvements

- Show a message when an invalid menu option is entered
- Allow editing the event name and capacity after startup
- Use a `with open(...)` block for safer file handling
- Add a search feature for participants

## Author

Madhavi Kapoor
