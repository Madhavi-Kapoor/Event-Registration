
Event_name = input("Enter event name: ").strip()


while True:
    try:
        Event_capacity = int(input("Enter event participant capacity: "))

        if Event_capacity > 0:
            break
        else:
            print("Capacity must be greater than zero.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


while True:
    try:
        Attendee_capacity = int(input("Enter event attendee capacity: "))

        if Attendee_capacity > 0:
            break
        else:
            print("Capacity must be greater than zero.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


participants = []
attendees = []


# PARTICIPANT FUNCTIONS

def register_participant():
    if len(participants) >= Event_capacity:
        print("Participant capacity is full.")
        return

    name = input("Enter participant name: ").strip()

    if name == "":
        print("Name cannot be empty.")
    elif any(char.isdigit() for char in name):
        print("Name cannot contain numbers.")
    elif name.lower() in [p.lower() for p in participants]:
        print("Participant already registered.")
    else:
        participants.append(name)
        print(name, "registered successfully!")


def remove_participant():
    name = input("Enter participant name to remove: ").strip()

    for participant in participants:
        if participant.lower() == name.lower():
            participants.remove(participant)
            print(participant, "removed successfully!")
            return

    print("Participant not found.")


def participants_in_event():
    print("\n==== Registered Participants ====")
    print("Total participants:", len(participants))
    print("Remaining spaces:", Event_capacity - len(participants))

    for name in participants:
        print(name)


def capacity_information():
    print("\nEvent:", Event_name)
    print("Participant capacity:", Event_capacity)
    print("Registered participants:", len(participants))
    print("Remaining spaces:", Event_capacity - len(participants))


# ATTENDEE FUNCTIONS

def attendee_registration():
    if len(attendees) >= Attendee_capacity:
        print("Attendee capacity is full.")
        return

    name = input("Enter attendee name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return
    elif any(char.isdigit() for char in name):
        print("Name cannot contain numbers.")
        return

    student_id = input("Enter student ID: ").strip()

    if student_id == "":
        print("Student ID cannot be empty.")
        return

    for attendee in attendees:
        if attendee[1].lower() == student_id.lower():
            print("Attendee already registered.")
            return

    attendees.append([name, student_id])
    print(name, "registered successfully!")


def remove_attendee():
    student_id = input("Enter student ID to remove: ").strip()

    for attendee in attendees:
        if attendee[1].lower() == student_id.lower():
            attendees.remove(attendee)
            print(attendee[0], "removed successfully!")
            return

    print("Attendee not found.")


def show_attendees():
    print("\n==== Registered Attendees ====")
    print("Total attendees:", len(attendees))
    print("Remaining spaces:", Attendee_capacity - len(attendees))

    for attendee in attendees:
        print("Name:", attendee[0], "| Student ID:", attendee[1])


def attendee_capacity_information():
    print("\nEvent:", Event_name)
    print("Attendee capacity:", Attendee_capacity)
    print("Registered attendees:", len(attendees))
    print("Remaining spaces:", Attendee_capacity - len(attendees))


# SAVE DATA

def save_data():
    try:
        with open("participants.txt", "w") as file:
            for name in participants:
                file.write(name + "\n")

        with open("attendees.txt", "w") as file:
            for attendee in attendees:
                file.write(attendee[0] + "|" + attendee[1] + "\n")

        print("All registration data saved successfully!")

    except OSError:
        print("Error while saving data.")


# LOAD DATA

def load_data():
    global participants, attendees

    try:
        with open("participants.txt", "r") as file:
            participants = [name.strip() for name in file if name.strip()]

    except FileNotFoundError:
        participants = []

    except OSError:
        print("Error loading participant data.")

    try:
        with open("attendees.txt", "r") as file:
            attendees = []

            for line in file:
                details = line.strip().split("|", 1)

                if len(details) == 2:
                    attendees.append(details)

    except FileNotFoundError:
        attendees = []

    except OSError:
        print("Error loading attendee data.")


# ONE COMMON MENU

def terminal_menu():
    print("\n===== CAMPUS CLUB EVENT REGISTRATION =====")
    print("Event:", Event_name)
    print("1. Register participant")
    print("2. Remove participant")
    print("3. Show registered participants")
    print("4. Participant capacity details")
    print("5. Register attendee")
    print("6. Remove attendee")
    print("7. Show registered attendees")
    print("8. Attendee capacity details")
    print("9. Save all data")
    print("10. Save data and Exit")


# MAIN PROGRAM

load_data()

while True:
    terminal_menu()
    choice = input("Enter your choice (1-10): ").strip()

    if choice == "1":
        register_participant()

    elif choice == "2":
        remove_participant()

    elif choice == "3":
        participants_in_event()

    elif choice == "4":
        capacity_information()

    elif choice == "5":
        attendee_registration()

    elif choice == "6":
        remove_attendee()

    elif choice == "7":
        show_attendees()

    elif choice == "8":
        attendee_capacity_information()

    elif choice == "9":
        save_data()

    elif choice == "10":
        save_data()
        print("Data saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 10.")
