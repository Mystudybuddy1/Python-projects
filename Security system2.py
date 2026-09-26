
import msvcrt


def get_password():
    password = ""

    while True:
        char = msvcrt.getch()

        if char == b'\r':
            print()
            break

        elif char == b'\x08':
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)

        else:
            password += char.decode()
            print("*", end="", flush=True)

    return password


def check_password(password):
    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    return True


class SecuritySystem:
    def __init__(self, password):
        self.__password = password
        self.__status = "Locked"

    def unlock(self):
        print("Enter your password: ", end="")
        password = get_password()

        if password == self.__password:
            self.__status = "Unlocked"
            print("Access Granted!")
        else:
            print("Wrong Password! Access Denied.")

    def lock(self):
        self.__status = "Locked"
        print("System Locked.")

    def show_status(self):
        print("System Status:", self.__status)


while True:
    print("Set your password: ", end="")
    password = get_password()

    if check_password(password):
        print("Strong password!")
        break

    else:
        print("Weak password!")
        print("Password must have:")
        print("- At least 8 characters")
        print("- At least one number")
        print("- At least one uppercase letter")
        print("- At least one lowercase letter")


security = SecuritySystem(password)
security.show_status()

while True:
    print(1, "Unlock your account")
    print(2, "Lock your account")
    print(3, "Show status of the account")
    print(4, "Exit")

    x = int(input("Select your choice: "))

    if x == 1:
        security.unlock()

    elif x == 2:
        security.lock()

    elif x == 3:
        security.show_status()

    elif x == 4:
        print("Thanks for visiting! ")
        break

    else:
        print("Invalid choice!!!!")
