# MAC Address Changer Tool

## Overview

The MAC Address Changer Tool allows users to view and modify the MAC address of their network interface. This tool provides options to either generate random MAC addresses or enter a custom MAC address. It is designed to work on Linux-based systems and requires `ifconfig` for network interface management.

## Features

- **Print Current MAC Address**: Display the current MAC address of the `eth0` network interface.
- **Change MAC Address**: Change the MAC address using either generated or custom MAC addresses.

## Prerequisites

- Linux-based operating system (e.g., Kali Linux, Ubuntu).
- `ifconfig` utility installed (typically part of the `net-tools` package).

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AbdullahZeynel/python-MAC-changer.git
   ```

2. **Navigate to the Directory**

   ```bash
   cd python-MAC-changer
   ```

3. **Ensure `ifconfig` is Installed**

   Install `ifconfig` if it's not already available on your system:

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

   - **Print Current MAC Address**: Shows the current MAC address of `eth0`.
   - **Change MAC Address**:
     - **Generate New MAC Address**: Generates and displays five random MAC addresses.
     - **Enter Custom MAC Address**: Allows you to manually enter a MAC address to change.

3. **Generated MAC Addresses Menu**

   After generating MAC addresses, you can:
   - **Regenerate MAC Addresses**: Generate a new set of MAC addresses.
   - **Select and Apply a MAC Address**: Choose one of the generated MAC addresses to apply.

## Example

```bash
************************************************************************
** MAC Address Changer Tool **
************************************************************************

Please select an option:

1. Print Current MAC Address
2. Change MAC Address

```

### Changing MAC Address

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

- The MAC address must be entered in the format `xx:xx:xx:xx:xx:xx`.
- The first character of the MAC address must be `0` and the second must be one of `0,2,4,6,8,A,C,E`.

## Troubleshooting

- **Error: Cannot assign requested address**: Check the format of the MAC address and ensure that the `eth0` interface is correctly specified.
- **Error: Invalid input**: Ensure that the options you enter are valid and follow the specified format.

## Contributing

Feel free to submit issues or pull requests to improve the tool. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

