from web3 import Web3

# Replace with the RPC endpoint of the EVM chain
rpc_endpoint = 'https://rpc.example.com'

# Replace with your private key
private_key = '0xYourPrivateKey'

# Connect to the EVM chain
web3 = Web3(Web3.HTTPProvider(rpc_endpoint))

# Check if connected
if web3.isConnected():
    print(f"Connected to {rpc_endpoint}")
else:
    print("Connection failed. Check RPC endpoint.")

# Replace with the contract address and ABI of the smart contract you want to interact with
contract_address = '0xContractAddress'
contract_abi = [...]
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Replace with the recipient address and amount
recipient_address = '0xRecipientAddress'
amount = web3.toWei(1, 'ether')

# Build transaction
transaction = contract.functions.yourContractFunction().buildTransaction({
    'from': web3.toChecksumAddress(web3.eth.account.privateKeyToAccount(private_key).address),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'nonce': web3.eth.getTransactionCount(web3.toChecksumAddress(web3.eth.account.privateKeyToAccount(private_key).address)),
})

# Sign transaction
signed_transaction = web3.eth.account.sign_transaction(transaction, private_key)

# Send transaction
transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

print(f"Transaction sent: {transaction_hash}")
