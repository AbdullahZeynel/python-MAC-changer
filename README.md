# MAC Address Changer Tool

## Overview

The **MAC Address Changer Tool** is a Python-based utility designed to view and modify the MAC address of your network interface. This tool supports generating random MAC addresses or entering a custom MAC address. It operates on Linux-based systems and utilizes the `ifconfig` command for network interface management.

## Features

- **Print Current MAC Address**: Display the current MAC address of the `eth0` network interface.
- **Change MAC Address**: Modify the MAC address using either randomly generated or custom MAC addresses.

## Prerequisites

- **Operating System**: Linux-based (e.g., Kali Linux, Ubuntu).
- **Utilities**: `ifconfig` from the `net-tools` package.

## Installation

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/AbdullahZeynel/python-MAC-changer.git
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd python-MAC-changer
   ```

3. **Install Dependencies**

   Ensure that `ifconfig` is installed on your system. You can install it by running:

   ```bash
   sudo apt-get update
   sudo apt-get install net-tools
   ```

## Usage

1. **Run the Tool**

   Execute the script using Python:

   ```bash
   python3 mac_changer.py
   ```

2. **Main Menu Options**

   The tool will present a menu with the following options:

   - **Print Current MAC Address**: Displays the current MAC address of `eth0`.
   - **Change MAC Address**:
     - **Generate New MAC Address**: Creates and displays five random MAC addresses.
     - **Enter Custom MAC Address**: Prompts you to manually enter a MAC address to apply.

3. **Generated MAC Addresses Menu**

   After generating MAC addresses, you can:

   - **Regenerate MAC Addresses**: Produce a new set of MAC addresses.
   - **Select and Apply a MAC Address**: Choose one of the displayed MAC addresses to apply.

## Example Usage

### Main Menu

```bash
************************************************************************
** MAC Address Changer Tool **
************************************************************************

Please select an option:

1. Print Current MAC Address
2. Change MAC Address
3. Exit
```

### Change MAC Address

```bash
************************************************************************
** Change MAC Address **
************************************************************************

Please select an option:

1. Generate New MAC Address
2. Enter Custom MAC Address
```

### Generated MAC Addresses

```bash
************************************************************************
** Generated MAC Addresses **
************************************************************************

MAC_1: 00:1A:2B:3C:4D:5E
MAC_2: 00:2B:3C:4D:5E:6F
...
```

## Notes

- **MAC Address Format**: The MAC address should be entered in the format `xx:xx:xx:xx:xx:xx`, where the first character must be `0` and the second character must be one of `0,2,4,6,8,A,C,E`.
- **Network Interface**: This tool currently assumes the network interface is named `eth0`. If your interface is different, you will need to modify the script accordingly.

## Troubleshooting

- **Error: Cannot assign requested address**: Ensure that the MAC address format is correct and that the network interface `eth0` is correctly specified.
- **Error: Invalid input**: Verify that you are entering valid options and that any MAC addresses follow the required format.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. For major changes, open an issue to discuss the proposed modifications first.
