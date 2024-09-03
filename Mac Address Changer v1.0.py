import os
import subprocess
import random

# Stores generated MAC addresses
generatedMACs = ""

# Main menu display
main_menu = """
************************************************************************
** MAC Address Changer Tool **
************************************************************************

Please select an option:

1. Print Current MAC Address
2. Change MAC Address

"""

# Change MAC address menu display
change_mac_menu = """
************************************************************************
** Change MAC Address **
************************************************************************

Please select an option:

1. Generate New MAC Address
2. Enter Custom MAC Address

"""

# Display for generated MAC addresses
generated_macs_menu1 = """
************************************************************************
** Generated MAC Addresses **
************************************************************************

"""

# Additional options after generating MAC addresses
generated_macs_menu2 = """
\nPlease select an option:

0. Regenerate MAC Addresses
1. Option 1
2. Option 2
3. Option 3
4. Option 4
5. Option 5

"""

# Function to generate a random MAC address
def generate_random_mac():
    mac = ['0' + random.choice('2468ACE')]  # Ensure the first character is even

    for i in range(5):
        mac.append(random.choice('0123456789ABCDEF') + random.choice('0123456789ABCDEF'))
    return ':'.join(mac)

# Function to generate multiple MAC addresses and save them to a file
def generate_mac():
    clearScreen()
    mac_addresses = []

    for i in range(5):
        mac_address = generate_random_mac()
        mac_addresses.append(mac_address)
        print(f"MAC_{i + 1}: {mac_address}")

    # Save generated MAC addresses to a file
    with open('/home/kali/codes/MAC_changer/generatedMACaddresses.txt', 'w') as file1:
        for mac_address in mac_addresses:
            file1.write(mac_address + '\n')

# Function to display the current MAC address
def get_MAC():
    clearScreen()
    subprocess.call(['ifconfig', 'eth0', 'up'])  # Bring the network interface up
    result = subprocess.run(['ifconfig'], capture_output=True, text=True)

    # Save the output of `ifconfig` to a file
    with open('/home/kali/codes/MAC_changer/terminal_output.txt', 'w') as file1:
        file1.write(result.stdout)

    # Read the file and extract the MAC address
    with open('/home/kali/codes/MAC_changer/terminal_output.txt', 'r') as file2:
        for line in file2:
            line = line.lstrip()
            if line.startswith('ether'):
                parts = line.split()
                if len(parts) >= 2:
                    print(f"\nYour Current MAC Address is: {parts[1]}")

# Function to clear the terminal screen
def clearScreen():
    os.system('clear')

# Main function to display the main menu
def main():
    clearScreen()
    mainMenu()

# Function to display the main menu and handle user input
def mainMenu():
    clearScreen()
    print(main_menu)
    choice1 = input("\nEnter your choice:").strip()

    if choice1 == '1':
        get_MAC()
        input("\nPlease press ENTER to proceed.")
        mainMenu()

    elif choice1 == '2':
        clearScreen()
        print(change_mac_menu)
        choice2 = input("\nEnter your choice:").strip()

        if choice2 == '1':
            while True:
                generate_mac()
                clearScreen()
                print(generated_macs_menu1)
                with open('/home/kali/codes/MAC_changer/generatedMACaddresses.txt', 'r') as file3:
                    generatedMACs = file3.read()
                    print(generatedMACs)
                    print(generated_macs_menu2)

                choice3 = input("\nEnter your choice:").strip()

                if choice3 == '0':
                    continue

                elif choice3 in ['1', '2', '3', '4', '5']:
                    index = int(choice3) - 1
                    with open('/home/kali/codes/MAC_changer/generatedMACaddresses.txt', 'r') as file3:
                        mac_list = file3.readlines()
                        newMAC = mac_list[index].strip()
                        changeMAC(newMAC)

                else:
                    input("ERROR: Invalid input.\nPlease press ENTER to proceed.")
                    continue

        elif choice2 == '2':
            clearScreen()
            print("Please note that the MAC address must be entered in the following format:\nxx:xx:xx:xx:xx:xx")
            print("The first character must be '0' and the second character must be one of '0,2,4,6,8,A,C,E'")
            newMAC = input("\nPlease enter a MAC address:").strip()
            newMAC = str(newMAC)
            changeMAC(newMAC)

        else:
            input("ERROR: Invalid input.\nPlease press ENTER to proceed.")
            mainMenu()

    else:
        input("ERROR: Invalid input.\nPlease press ENTER to continue.")
        mainMenu()

# Function to change the MAC address
def changeMAC(newMAC):
    clearScreen()
    try:
        subprocess.check_call(['ifconfig', 'eth0', 'down'])
        subprocess.check_call(['ifconfig', 'eth0', 'hw', 'ether', newMAC])
        subprocess.check_call(['ifconfig', 'eth0', 'up'])

    except subprocess.CalledProcessError:
        print("\n\nERROR: Cannot assign requested address. Please check the MAC address format or your network interface.")

    except Exception as e:
        print(f"\n\nERROR: {e}")

    else:
        print("\nMAC Address successfully changed.")

    finally:
        input("\nPlease press ENTER to return to the Main Menu.")
        mainMenu()

if __name__ == "__main__":
    main()
