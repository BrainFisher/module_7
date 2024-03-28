class User:
    def __init__(self, name, dob, phone):
        self.name = name
        self.dob = dob
        self.phone = phone


class Bot:
    def __init__(self):
        self.users = {}

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

    def run(self):
        while True:
            command = input(
                "Enter a command (add, info, list, exit): ").strip().lower()

            if command == "add":
                name = input("Enter name: ")
                dob = input("Enter date of birth: ")
                phone = input("Enter phone number: ")
                self.add_user(name, dob, phone)
                print("User added successfully.")

            elif command == "info":
                name = input("Enter name to get info: ")
                print(self.get_user_info(name))

            elif command == "list":
                print("List of users:")
                print(self.list_all_users())

            elif command == "exit":
                print("Exiting...")
                break

            else:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    bot = Bot()
    bot.run()
