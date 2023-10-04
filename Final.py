# Function to load data from data.txt and return a list of users
from secrets import choice


def load_data(file_name):
    users = []
    with open(file_name, 'r') as file:
        for line in file:
            username, password, full_name, balance = line.strip().split(',')
            users.append({
                'username': username,
                'password': password,
                'full_name': full_name,
                'balance': float(balance)
            })
    return users

def deposit(users, username, password, amount):
    user = login(users, username, password)
    if user:
        user['balance'] += amount
        return True
    else:
        return False

def withdraw(users, username, password, amount):
    user = login(users, username, password)
    if user:
        if user['balance'] >= amount:
            user['balance'] -= amount
            return True
        else:
            print("Insufficient balance")
            return False
    else:
        return False

def transfer(users, sender_username, sender_password, amount, receiver_username):
    sender = login(users, sender_username, sender_password)
    receiver = None
    if sender:
        for user in users:
            if user['username'] == receiver_username:
                receiver = user
                break
        if receiver:
            if sender['balance'] >= amount:
                sender['balance'] -= amount
                receiver['balance'] += amount
                return True
            else:
                print("Insufficient balance")
                return False
    return False

#new account
def create_account(users, new_username, new_password, full_name):
    for user in users:
        if user['username'] == new_username:
            print("Username already exists. Please choose a different username.")
            return False
    users.append({
        'username': new_username,
        'password': new_password,
        'full_name': full_name,
        'balance': 0.0
    })
    with open("data.txt", 'a') as file:
        file.write(f"{new_username},{new_password},{full_name},0.0\n")
    return True

 if __name__ == "__main__":
    data_file = "data.txt"
    users_data = load_data(data_file)

    while True:
        print("1. Login")
        print("2. Accrue Interest")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Create Account")
        choice = input("Select an Option: ")
