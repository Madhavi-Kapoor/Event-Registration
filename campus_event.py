Event_name=input("Enter event name: ")

while True:
    try:
        Event_capacity = int(input("Enter event capacity: "))

        if Event_capacity > 0:
            break
        else:
            print("Capacity must be greater than zero.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")

participants = []



def register_participant():
    if len(participants) >= Event_capacity:
        print("Sorry, the event is full.")
    else:
        name = input("Enter participant name: ").strip()

        if name == "":
            print("Name cannot be empty.")
        elif any(char.isdigit() for char in name):
         print("Name cannot contain numbers.")
        elif name.lower() in [p.lower() for p in participants]:
            print("Participant already registered.")
        else:
            participants.append(name)
            print(name + " Registered Successfully!")



def remove_participant():
    name = input("Enter participant name to remove: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return
    elif name.lower() in [p.lower() for p in participants]:
        for participant in participants:
            if participant.lower() == name.lower():
                participants.remove(participant)
                print(f"{participant} removed successfully!")
                return
    else:
        print("Participant not found.")



def participants_in_event():
    if len(participants)==0:
        print("No participants registered yet")
    else:
        print(f"Total participants   are={len(participants)}")
        print(f"Remaining spaces are= {Event_capacity-len(participants)}")
        for name in participants:
               print(name)



def capacity_information():
    print(f"The maximum capacity of {Event_name} is {Event_capacity}")
    print(f"Total participants are={len(participants)}")
    print(f"Remaining spaces are= {Event_capacity-len(participants)}")
    if len(participants) >= Event_capacity:
     print("Event is full. No more participants can be registered.")




def save_data():
    try:
        file = open("registrations.txt", "w")
        file.write(Event_name + "\n")
        file.write(str(Event_capacity) + "\n")

        for name in participants:
            file.write(name + "\n")

        file.close()
        print("Data saved successfully!")

    except OSError:
        print("Error while saving the file.")





def load_data():
    global Event_name, Event_capacity, participants

    try:
        file = open("registrations.txt", "r")   
        lines = file.readlines()
        file.close()

        if len(lines) < 2:
            print("No saved data found.")
            return False

        Event_name = lines[0].strip()
        Event_capacity = int(lines[1].strip())

        participants = []

        for name in lines[2:]:
            participants.append(name.strip())

        print("Data loaded successfully!")
        return True

    except FileNotFoundError:
        print("No saved file found")
        return False

    except ValueError:
     print("Saved data is invalid.")
     return False

    except OSError:
     print("Error while reading the file.")
     return False



def terminal_menu():
    print("\n==== Campus Club Event sign up ====")
    print("1. Register participant")
    print("2. Remove participant")
    print("3. Show the list of the registered participants")
    print("4. Event participation capacity details")
    print("5. Save the data")
    print("6. Save data and Exit")

if load_data():
    print("Using saved event details.")


while True:      #loop to keep the menu running
 terminal_menu()
 choice = input("Enter the operation you want to perform between 1-6: ")
 if choice == "1":
        register_participant()

 elif choice == "2":
        remove_participant()

 elif choice == "3":
        participants_in_event()

 elif choice == "4":
        capacity_information()

 elif choice == "5":
        save_data()

 elif choice == "6":      #option to save data and exit
        save_data()
        print("Data saved. Goodbye!")
        break