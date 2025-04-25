class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[len(self.old_passwords) - 1]
        return None

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False

    def is_correct(self, password):
        return password == self.get_password()

pm = Password_manager() #object of Password_manager class

while True:
    new_password = input("Enter a new password: ")
    if pm.set_password(new_password):
        print("Password set successfully.")
    else:
        print("Password has been used before. Try a different password.")

    # Ask the user if they want to continue or exit
    continue_input = input("Do you want to add another password? (yes/no): ")
    if continue_input.lower() != 'yes':
        break

current_password = pm.get_password()
print(f"The current password is: {current_password}")

password_to_check = input("Enter the password to verify: ")
if pm.is_correct(password_to_check):
    print("The password is correct.")
else:
    print("The password is incorrect.")
