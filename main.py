from nacl.signing import SigningKey
import base58
import secrets
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import os

class VanityAddressGenerator:
    def __init__(self, prefixes, suffixes):
        self.prefixes = [prefix.lower() for prefix in prefixes]
        self.suffixes = [suffix.lower() for suffix in suffixes]
        self.counter = 0
        self.stop_event = threading.Event()
        self.results = []
        self.start_time = time.time()

    def generate_keypair(self):
        """Create a new keypair"""
        seed = secrets.token_bytes(32)
        private_key = SigningKey(seed)
        public_key = private_key.verify_key
        address = base58.b58encode(public_key.encode()).decode('utf-8')
        private_key_64 = private_key.encode() + public_key.encode()
        return private_key_64, address

    def is_vanity_address(self, address):
        """Check if the address matches the desired prefixes and suffixes"""
        return any(address.startswith(prefix) for prefix in self.prefixes) and \
               any(address.endswith(suffix) for suffix in self.suffixes)

    def generate_vanity_keypair(self):
        while not self.stop_event.is_set():
            private_key_64, address = self.generate_keypair()
            self.counter += 1

            if self.is_vanity_address(address.lower()):
                self.results.append((private_key_64, address))
                self.print_result(private_key_64, address)

                if len(self.results) >= 10:
                    self.stop_event.set()

    def print_result(self, private_key_64, address):
        """Print the generated keypair and address"""
        print("Private key: ", base58.b58encode(private_key_64).decode('utf-8'))
        print("Solana address: ", address)
        elapsed_time = time.time() - self.start_time
        print("Generated addresses: ", self.counter)
        print("Time taken: ", elapsed_time, "seconds")

    def run(self):
        self.start_time = time.time()
        with ThreadPoolExecutor(max_workers=os.cpu_count() * 2) as executor:
            futures = [executor.submit(self.generate_vanity_keypair) for _ in range(os.cpu_count() * 2)]
            for future in futures:
                future.result()

        elapsed_time = time.time() - self.start_time
        for private_key_64, address in self.results:
            self.print_result(private_key_64, address)
        print("Total generated addresses: ", self.counter)
        print("Total time taken: ", elapsed_time, "seconds")

def main():
    prefixes = input("Please enter the Solana address prefixes (separated by ,): ").split(',')
    suffixes = input("Please enter the Solana address suffixes (separated by ,): ").split(',')
    generator = VanityAddressGenerator(prefixes, suffixes)
    generator.run()

if __name__ == "__main__":
    main()