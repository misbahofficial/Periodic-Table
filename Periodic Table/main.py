import json


def increase_one_in_file():
    with open("stat.txt") as f:
        stat = int(f.read())
        stat += 1
    with open('stat.txt', 'w') as f2:
        f2.write(str(stat))


def show_stat():
    with open('stat.txt') as f:
        data = f.read()
        print(f"Total Elements: {data}")


# defining function for adding elements
def add_element():
    element_no = int(input("Enter element number: "))

    # taking dictionary as input
    element = {
        'name': input("Enter element's name: "),
        'atomic number': int(input("Enter atomic number: ")),
        'ram': float(input("Enter relative atomic mass: ")),
        'chemical formulae': input("Enter chemical formula: ")
    }

    data = {}  # Initialize data dictionary here

    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'element' not in data:
        data['element'] = {}

    data['element'][element_no] = element

    try:
        with open("data.json", 'w') as f:
            json.dump(data, f, indent=4)
            increase_one_in_file()
            print("Element added successfully.")
    except FileNotFoundError:
        raise FileNotFoundError


# defining function for viewing data from the list
def check_element_info():
    element_no = input("Enter element number: ")
    data = {}

    try:
        with open("data.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if "element" in data and element_no in data['element']:
        print(f"""
 ======== Showing Data ========
 Name:                  {data['element'][element_no]['name']}
 Atomic Number:         {data['element'][element_no]['atomic number']}
 Relative Atomic Mass:  {data['element'][element_no]['ram']}
 Chemical Formula:      {data['element'][element_no]['chemical formulae']}
""")
    else:
        print("Data not found!")


def main():
    try:
        while True:
            user_choice = int(input(f"""
        ********** Welcome **********

1. Add Element
2. Specific Element Info
3. Statistics
4. Exit
>>> Hit Input >>> 
        """))
            if user_choice == 1:
                add_element()
                choice = input("Type 'y' to continue or 'n' to exit: ").lower()
                if choice == 'y':
                    continue
                elif choice == 'n':
                    break
                else:
                    print("Wrong choice!")
                    # break
            elif user_choice == 2:
                check_element_info()
                choice = input("Type 'y' to continue or 'n' to exit: ").lower()
                if choice == 'y':
                    continue
                elif choice == 'n':
                    break
                else:
                    print("Wrong choice!")
                    # break
            elif user_choice == 3:
                show_stat()
                choice = input("Type 'y' to continue or 'n' to exit: ").lower()
                if choice == 'y':
                    continue
                elif choice == 'n':
                    break
                else:
                    print("Wrong choice!")
                    # break
            elif user_choice == 4:
                break
            else:
                print("Invalid Command!")
                choice = input("Type 'y' to continue or 'n' to exit: ").lower()
                if choice == 'y':
                    continue
                elif choice == 'n':
                    break
                else:
                    print("Wrong choice!")
                    # break
    except ValueError:
        print("Invalid Command")


# intended to be run
if __name__ == "__main__":
    main()
