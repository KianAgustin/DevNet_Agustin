"""
Midterm Practical Exam — Network Device Inventory Tool
Student: Agustin, Kian Gabriel P.
"""
devices = []  # starts empty — the user adds devices as the program runs


def add_device():       # ask for name, IP, status — build the string, add to the list
    dev_name = input("\nDevice Name : ")
    dev_ip = input("\nDevice IP Address : ")
    dev_status = input("\nDevice Status : ")
    dev_details = dev_name + " - "+ dev_ip  +" - "+ dev_status
    if dev_details:
        devices.append(dev_details)
        print(f"'{dev_details}' added successfully!")
    else:
        print("Task cannot be empty.")

def view_device():    # loop through and print every device — handle empty list
    if not devices:
        print("\nNo device yet!")
        return False

    print("\n----- YOUR DEVICE-----")
    for i, dev in enumerate(devices, start=1):
        print(f"{i}. {dev}")
    print("-----------------------")
    return True


def main():
    running = True
    while running:
            print("===== Network Device Inventory =====")
            print("1. Add a device")
            print("2. View all devices")
            print("3. Count active vs inactive devices")
            print("4. Find a device by name")
            print("5. Remove a device")
            print("6. Exit")

            choice = input("Choose an option (1-5): ").strip()

            if choice == '1':
                add_device()
            elif choice == '2':
                view_device()
            elif choice == '6':
                print("Thank You!")
                break
            else:
                print("!!!Invalid Choice, Choose 1 - 5 only!!!")



main()
