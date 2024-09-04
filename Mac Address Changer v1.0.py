import os
import subprocess
import random

#Screens:
generatedMACs = ""
#___________________________________________


main_menu = """
************************************************************************
** MAC Address Changer Tool **
************************************************************************

Please select an option:

1. Print Current MAC Address
2. Change MAC Address
3. Exit
 
"""
#___________________________________________


change_mac_menu = """
************************************************************************
** Change MAC Address **
************************************************************************

Please select an option:

1. Generate New MAC Address
2. Enter Custom MAC Address
3. Return to main menu

"""
#___________________________________________


generated_macs_menu1 = """
************************************************************************
** Generated MAC Addresses **
************************************************************************

"""
#___________________________________________


generated_macs_menu2 = """
\nPlease select an option:

0. Regenerate MAC Addresses
1. Option 1
2. Option 2
3. Option 3
4. Option 4
5. Option 5

"""
#___________________________________________


#Functions:

def generate_random_mac():
    mac = ['0' + random.choice('2468ACE')]

    for i in range(5):
        mac.append(random.choice('0123456789ABCDEF') + random.choice('0123456789ABCDEF'))
    return ':'.join(mac)
#___________________________________________

def generate_mac():
    clearScreen()
    mac_addresses = []

    for i in range(5):
        mac_address = generate_random_mac()
        mac_addresses.append(mac_address) 
        print(f"MAC_{i + 1}: {mac_address}") 

    with open ('generatedMACaddresses.txt','w') as file1:
        for mac_address in mac_addresses:
            file1.write(mac_address + '\n')
#___________________________________________

def get_MAC():
    clearScreen()
    subprocess.call(['ifconfig','eth0','up'])
    result = subprocess.run(['ifconfig'], capture_output=True, text=True)

    with open('terminal_output.txt', 'w+') as file:
        # Write the output of `ifconfig` to the file
        file.write(result.stdout)
        file.seek(0)  # Move the file pointer back to the beginning of the file

        # Read the file and extract the MAC address
        for line in file:
            line = line.lstrip()
            if line.startswith('ether'):
                parts = line.split()
                if len(parts) >= 2:
                    print(f"\nYour Current MAC Address is: {parts[1]}")            
#___________________________________________                  

def clearScreen():
    os.system('clear')
#___________________________________________

def main():
    clearScreen()
    mainMenu()
#___________________________________________

def mainMenu():
    clearScreen()
    print(main_menu)
    choice1 = input("\n Enter your choice:")

    match choice1:
        case '1':
            get_MAC()
            input("\n Please press ENTER to proceed.")
            mainMenu()
        case '2':
            clearScreen()
            print(change_mac_menu)
            choice2 = input("\n Enter your choice:")

            match choice2:
                case '1':
                    while True:
                        generate_mac()
                        clearScreen()
                        print(generated_macs_menu1)
                        with open ('generatedMACaddresses.txt','r') as file3:
                            generatedMACs = file3.read()
                            print(generatedMACs)
                            print(generated_macs_menu2)

                        choice3 = input("\n Enter your choice:")

                        if choice3 == '0':
                            continue

                        elif choice3 in ['1', '2', '3', '4', '5']:
                            index = int(choice3) - 1  
                            with open('generatedMACaddresses.txt', 'r') as file3:
                                mac_list = file3.readlines()
                                newMAC = mac_list[index].strip() 
                                changeMAC(newMAC)

                        else:
                            input("ERROR, Invalid input.\n Please press ENTER to proceed.")
                            continue

                case '2':
                    clearScreen()
                    print("(Please note that the MAC address must be entered in a similar format to this:\nxx:xx:xx:xx:xx:xx)")
                    print("\nPlease also note that the first character must be 0 and the second must be one of \"0,2,4,6,8,A,C,E\"")
                    newMAC = input("\nPlease enter a MAC address:").strip()
                    newMAC = str(newMAC)
                    changeMAC(newMAC)

                case _:
                    if choice2 != '3':
                        input("ERROR, Invalid input. Please press ENTER to proceed.")
                    mainMenu()
        case '3':
            exit()
        case _:
            input("ERROR, Invalid input.\n Please press ENTER to continue.")
            mainMenu()
#___________________________________________

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
        input("\nPlease press ENTER to return to Main Menu.")
        mainMenu()
#___________________________________________

if __name__ == "__main__":
    main()
