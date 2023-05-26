import requests
from mnemonic import Mnemonic
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
import asyncio

# Define the desired number of iterations per minute
iterations_per_minute = 7

# Calculate the delay duration in seconds between each iteration
delay_seconds = 60 / iterations_per_minute

# Infinite loop for generating mnemonic phrases and fetching data from the API
async def main():
    while True:
        # Generate a new mnemonic phrase offline
        mnemonic = Mnemonic("english").generate(strength=256)  # 256 bits is commonly used for Bitcoin

        # Derive the private key from the mnemonic phrase
        private_key = CBitcoinSecret.from_secret_bytes(Mnemonic("english").to_seed(mnemonic))

        # Get the corresponding public key
        public_key = private_key.pub

        # Derive the address from the public key
        address = str(P2PKHBitcoinAddress.from_pubkey(public_key))

        # Construct the API URL for fetching balance
        url = f"https://blockchain.info/balance?active={address}"

        # Send GET request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            try:
                data = response.json()
                balance = data[address]["final_balance"] / 100000000  # Convert satoshis to BTC
                print("Mnemonic:", mnemonic)
                print("Address:", address)
                print("Balance (BTC):", balance)

                # Save winners and losers to plain text databases
                if balance > 0:
                    with open('winners.txt', 'a') as winners_file:
                        winners_file.write(f"Mnemonic: {mnemonic}\n")
                        winners_file.write(f"Address: {address}\n")
                        winners_file.write(f"Balance (BTC): {balance}\n")
                        winners_file.write('\n')
                else:
                    with open('losers.txt', 'a') as losers_file:
                        losers_file.write(f"Mnemonic: {mnemonic}\n")
                        losers_file.write(f"Address: {address}\n")
                        losers_file.write(f"Balance (BTC): {balance}\n")
                        losers_file.write('\n')

            except ValueError:
                print("Error occurred while decoding JSON response.")

        else:
            print("Error occurred while fetching data from the API.")

        # Delay between iterations
        await asyncio.sleep(delay_seconds)

# Run the main function in an event loop
asyncio.run(main())
