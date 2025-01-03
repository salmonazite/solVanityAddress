# solVanityAddress

Vanity Address Generator
This project is a Python script that generates Solana vanity addresses. A vanity address is a cryptocurrency address that contains a specific pattern of characters, either at the beginning (prefix) or the end (suffix) of the address.

Features
Generates Solana keypairs.
Checks if the generated address matches the desired prefixes and suffixes.
Uses multithreading to speed up the generation process.
Stops after finding 10 matching addresses.
Prints the generated keypairs and addresses along with the time taken.
Requirements
Python 3.6 or higher
pynacl library
base58 library
Installation
Clone the repository:

Install the required libraries:

Usage
Run the script:

Enter the desired Solana address prefixes and suffixes when prompted. Separate multiple prefixes or suffixes with a comma.

Example
The script will then generate Solana addresses and print the ones that match the specified prefixes and suffixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Acknowledgements
PyNaCl for cryptographic functions.
base58 for Base58 encoding.
Author
GitHub Copilot
For any questions or issues, please open an issue on the GitHub repository.