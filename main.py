# module
import mymodule as mm
import goodbye as gb
import Greeting as g
import hello as hl

print("\n== Module Menu ==")
print("1. Hello module")
print("2. Greeting module")
print("3. Good bye module")
print("4. My module")
print("E. Exit")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n[ Hello module ]")
        hl.hello()
    elif choice == '2':
        print("\n[ Greeting module ]")
        g.greet()
    elif choice == '3':
        print("\n[ Good bye module ]")
        gb.goodbye()
    elif choice == '4':
        print("\n[ My module ]")
        mm.hello()
        mm.me()
    else:
        print("\n[ Invalid input ]")

    print("\n== Module Menu ==")
    print("1. Hello module")
    print("2. Greeting module")
    print("3. Good bye module")
    print("4. My module")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")
