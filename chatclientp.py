import socket
import json
import os
import sys

HOST = 'gckmytm2fvqpf47ddifmd6umoilmnwxueevgraqdgvj4zykgwc5ntvqd.onion'  # Server IP address
PORT = 12345  # Server port


def profile():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Post to your profile")
    post = input("Enter your post: ")

    data = {
        "action": "post",
        "post": post
    }

    response = send_request(data)
    print(response["message"])


def search():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Search")
        print("1. Username")
        print("2. Item")
        print("3. Back")

        choice = input()

        if choice == "1":
            print("no")
        elif choice == "2":
            print("no")
        elif choice == "3":
            shop()
        else:
            print("Invalid option")


def shop():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to the Flea Market")
        print("1. Search")
        print("2. Browse")
        print("3. Purchases")
        print("4. Back")

        choice = input()

        if choice == "1":
            search()
        elif choice == "2":
            print("no")
        elif choice == "3":
            print("no")
        elif choice == "4":
            visit_shops()
        else:
            print("Invalid option.")


def visit_shops():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to the Flea Market")
        print("1. Shop")
        print("2. Sell")
        print("3. Back")

        choice = input()

        if choice == "1":
            shop()
        elif choice == "2":
            print("no")
        elif choice == "3":
            welcome_page()
        else:
            print("Invalid option.")


def welcome_page():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to Term-O-Market")
        print("1. Post to your Profile")
        print("2. Visit Shops")
        print("3. View Messages")
        print("4. Chat")
        print("5. Account")
        print("6. Logout")
        print("7. Exit")

        choice = input()

        if choice == "1":
            profile()
        elif choice == "2":
            visit_shops()
        elif choice == "3":
            print("no")
        elif choice == "4":
            print("no")
        elif choice == "5":
            print("no")
        elif choice == "6":
            main()
        elif choice == "7":
            sys.exit()
        else:
            print("Invalid option.")


def send_request(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.send(json.dumps(data).encode())

    response = client_socket.recv(1024).decode()
    response = json.loads(response)

    client_socket.close()

    return response


def login():
    print("Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    data = {
        "action": "login",
        "username": username,
        "password": password
    }

    response = send_request(data)
    print(response["message"])
    if response["message"] == "Login successful.":
        welcome_page()


def register():
    print("Registration")
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    data = {
        "action": "register",
        "username": username,
        "password": password
    }

    response = send_request(data)
    print(response["message"])


def main():
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Quit")

        choice = input()

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
