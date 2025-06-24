import sys
from modules.port_scanner import PortScanner
from modules.brute_forcer import BruteForcer

def main():
    print("Welcome to the Penetration Testing Toolkit")
    print("Select an option:")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        target = input("Enter the target IP address or hostname: ")
        scanner = PortScanner()
        results = scanner.scan_ports(target)
        scanner.display_results(results)
    elif choice == '2':
        target = input("Enter the target IP address or hostname: ")
        username = input("Enter the username: ")
        password_list = input("Enter the path to the password list file: ")
        with open(password_list, 'r') as file:
            passwords = file.read().splitlines()
        for password in passwords:
            success = BruteForcer.attempt_login(target, username, password)
            BruteForcer.report_success(success)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()