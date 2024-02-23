import requests
from eth_account import Account
import time
Account.enable_unaudited_hdwallet_features()

def get_wallet_balance(address, etherscan_api_key):
    try:
        url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={etherscan_api_key}"
        response = requests.get(url)
        data = response.json()
        balance_in_wei = int(data['result'])
        balance_in_eth = balance_in_wei / 1e18  # Convert Wei to Ether
        return balance_in_eth
    except Exception as e:
        print(f"Error fetching balance for address {address}: {e}")
        return None

def check_balances(file_path, etherscan_api_key, output_file):
    with open(file_path, 'r') as file:
        seed_phrases = set(file.readlines())  # Using a set to remove duplicates

    print("Starting balance check...")
    with open(output_file, 'a') as out_file:  # Change to append mode
        for seed in seed_phrases:
            seed = seed.strip()
            if seed:
                try:
                    wallet = Account.from_mnemonic(seed)
                    print(f"Checking wallet: {wallet.address}")
                    balance = get_wallet_balance(wallet.address, etherscan_api_key)
                    if balance is not None and balance > 0:
                        print(f"Success: Address {wallet.address} has a balance of {balance:.18f} ETH.")
                        out_file.write(f"Seed: {seed}\nAddress: {wallet.address}\nBalance: {balance:.18f} ETH\n\n")
                    elif balance is not None:
                        print(f"Address {wallet.address} has zero balance.")
                    time.sleep(0.2)  # Delay to avoid hitting the rate limit
                except Exception as e:
                    print(f"Error with seed phrase '{seed}': {e}")
    print("Balance check completed.")

# Replace these paths with your actual file paths
seed_file_path = 'seedd.txt'
output_file_path = 'good.txt'
etherscan_api_key = "YOUR_ETHER_API_KEY"

check_balances(seed_file_path, etherscan_api_key, output_file_path)

