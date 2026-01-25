import sys
import socket
import shutil
import os

print("DISCLAIMER:")
print("This tool is intended for educational purposes only.")
print("Use it only on systems you own or have explicit permission to test.")
print("The author is not responsible for any misuse of this tool.\n")

permission = input("Do you have explicit authorization to scan this target? (yes/no): ")

if permission.lower() != "yes":
    print("Authorization not confirmed. Exiting the tool.")
    sys.exit()

target = input("Enter the domain or IP to scan: ")

if len(target) == 0:
    print("No target provided. Exiting the tool.")
    sys.exit()

try:
    socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid or unreachable target. DNS resolution failed.")
    sys.exit()

if shutil.which("nmap") is None:
    print("Nmap is not installed or not found in PATH.")
    print("Please install Nmap before running this tool.")
    sys.exit()
while True:
    print("\nChoose scan type:")
    print("1. Fast scan (-F)")
    print("2. Service version detection (-sV)")
    print("3. TCP connect scan (-sT)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        scan_flag = "-F"
        break
    elif choice == "2":
        scan_flag = "-sV"
        break
    elif choice == "3":
        scan_flag = "-sT"
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
while True:
    print("\nChoose output format:")
    print("1. Normal output (-oN)")
    print("2. XML output (-oX)")
    print("3. All formats (-oA)")

    out_choice = input("Enter your choice (1/2/3): ")

    if out_choice == "1":
        output_flag = "-oN"
        break
    elif out_choice == "2":
        output_flag = "-oX"
        break
    elif out_choice == "3":
        output_flag = "-oA"
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

use_pn = input("\nHost discovery may fail if ICMP is blocked. Use -Pn (assume host is up)? (yes/no): ")

if use_pn.lower() == "yes":
    pn_flag = "-Pn"
else:
    pn_flag = ""


output_file = f"{target}_scan"

print(f"\nStarting Nmap scan on {target}...")
print(f"Saving results to {output_file}\n")

os.system(f"nmap {scan_flag} {target} {output_flag} {output_file}")

print("Scan completed successfully.")
print("Exiting the tool.")

