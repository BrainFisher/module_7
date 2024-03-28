from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        if old_phone not in [str(p) for p in self.phones]:
            raise ValueError("Phone number not found.")
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p.value
        raise ValueError("Phone number not found.")

    def __str__(self):
        phones_str = '; '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}, birthday: {self.birthday}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name not in self.data:
            raise KeyError("Contact not found.")
        return self.data[name]

    def delete(self, name):
        if name not in self.data:
            raise KeyError("Contact not found.")
        del self.data[name]


class User:
    def __init__(self, name, dob, phone):
        self.name = name
        self.dob = dob
        self.phone = phone


class Bot:
    def __init__(self):
        self.users = {}
        self.address_book = AddressBook()

    def add_user(self, name, dob, phone):
        self.users[name] = User(name, dob, phone)

    def get_user_info(self, name):
        if name in self.users:
            user = self.users[name]
            return f"Name: {user.name}, DOB: {user.dob}, Phone: {user.phone}"
        else:
            return "User not found."

    def list_all_users(self):
        if self.users:
            return "\n".join([user.name for user in self.users.values()])
        else:
            return "No users available."

    def add_birthday(self, name, dob):
        if name in self.users:
            self.users[name].dob = dob
            print(f"Birthday added/updated for {name}.")
        else:
            print("User not found.")

    def show_birthday(self, name):
        if name in self.users:
            return f"{name}'s birthday is on {self.users[name].dob}."
        else:
            return "User not found."

    def birthdays(self):
        upcoming_birthdays = []
        today = datetime.now()
        for name, user in self.users.items():
            dob = datetime.strptime(user.dob, "%d.%m.%Y")
            if dob.month == today.month and dob.day >= today.day:
                upcoming_birthdays.append((name, dob.strftime("%d.%m")))
        if upcoming_birthdays:
            return "\n".join([f"{name}: {dob}" for name, dob in upcoming_birthdays])
        else:
            return "No upcoming birthdays."

    def run(self):
        print("Welcome to the assistant bot!")
        while True:
            print("\nMenu:")
            print("1. Add a new contact")
            print("2. Show contact info")
            print("3. List all contacts")
            print("4. Add birthday")
            print("5. Show birthday")
            print("6. Show upcoming birthdays")
            print("7. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                name = input("Enter name: ")
                dob = input("Enter date of birth (DD.MM.YYYY): ")
                phone = input("Enter phone number: ")
                self.add_user(name, dob, phone)
                print("User added successfully.")

            elif choice == "2":
                name = input("Enter name to get info: ")
                print(self.get_user_info(name))

            elif choice == "3":
                print("List of users:")
                print(self.list_all_users())

            elif choice == "4":
                name = input("Enter name: ")
                dob = input("Enter date of birth (DD.MM.YYYY): ")
                self.add_birthday(name, dob)

            elif choice == "5":
                name = input("Enter name: ")
                print(self.show_birthday(name))

            elif choice == "6":
                print("Upcoming birthdays:")
                print(self.birthdays())

            elif choice == "7":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    bot = Bot()
    bot.run()
