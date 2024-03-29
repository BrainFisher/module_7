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
            raise ValueError("Номер телефону має містити 10 цифр.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Неправильний формат дати. Використовуйте DD.MM.YYYY.")
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
            raise ValueError("Номер телефону не знайдено.")
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p.value
        raise ValueError("Номер телефону не знайдено.")

    def __str__(self):
        phones_str = '; '.join(str(p) for p in self.phones)
        return f"Ім'я: {self.name}, Телефони: {phones_str}, День народження: {self.birthday}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name not in self.data:
            raise KeyError("Контакт не знайдено.")
        return self.data[name]

    def delete(self, name):
        if name not in self.data:
            raise KeyError("Контакт не знайдено.")
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
            return f"Ім'я: {user.name}, Дата народження: {user.dob}, Телефон: {user.phone}"
        else:
            return "Контакт не знайдено."

    def list_all_users(self):
        if self.users:
            return "\n".join([f"Ім'я: {user.name}, Дата народження: {user.dob}, Телефон: {user.phone}" for user in self.users.values()])
        else:
            return "Немає доступних контактів."

    def add_birthday(self, name, dob):
        if name in self.users:
            self.users[name].dob = dob
            print(f"День народження додано/оновлено для {name}.")
        else:
            print("Контакт не знайдено.")

    def show_birthday(self, name):
        if name in self.users:
            return f"День народження {name} в {self.users[name].dob}."
        else:
            return "Контакт не знайдено."

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
            return "Немає наближених днів народження."

    def run(self):
        print("Ласкаво просимо до асистента!")
        while True:
            print("\nМеню:")
            print("1. Додати новий контакт")
            print("2. Показати інформацію про контакт")
            print("3. Показати всі контакти")
            print("4. Додати день народження")
            print("5. Показати день народження")
            print("6. Показати наближені дні народження")
            print("7. Вихід")
            choice = input("Введіть ваш вибір: ").strip()

            if choice == "1":
                name = input("Введіть ім'я: ")
                dob = input("Введіть дату народження (DD.MM.YYYY): ")
                phone = input("Введіть номер телефону: ")
                try:
                    self.add_user(name, dob, phone)
                    print("Контакт успішно додано.")
                except ValueError as e:
                    print(f"Помилка: {e}")

            elif choice == "2":
                name = input("Введіть ім'я для отримання інформації: ")
                print(self.get_user_info(name))

            elif choice == "3":
                print("Список контактів:")
                print(self.list_all_users())

            elif choice == "4":
                name = input("Введіть ім'я: ")
                dob = input("Введіть дату народження (DD.MM.YYYY): ")
                try:
                    self.add_birthday(name, dob)
                except ValueError as e:
                    print(f"Помилка: {e}")

            elif choice == "5":
                name = input("Введіть ім'я: ")
                print(self.show_birthday(name))

            elif choice == "6":
                print("Наближені дні народження:")
                print(self.birthdays())

            elif choice == "7":
                print("Виходимо...")
                return  # Завершуємо виконання функції, що призведе до виходу з циклу while та програми

            else:
                print("Неправильний вибір. Будь ласка, спробуйте знову.")


if __name__ == "__main__":
    bot = Bot()
    bot.run()
