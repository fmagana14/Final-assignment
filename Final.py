# Function to load data from data.txt and return a list of users
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

