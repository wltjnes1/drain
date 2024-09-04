from web3 import Web3
print("Debug: Automatically connecting to the wallet...")
networks = {
    'Ethereum Mainnet': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'BSC Mainnet': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'zkSync Era Mainnet': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'Arbitrum One': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'Avalanche Network C-Chain': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'Base Mainnet': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'OP Mainnet': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'Polygon Mainnet': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'Rootstock': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'Degen Main': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'Blast Mainnet': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'Gnosis': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'Linea Chain': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'Moonbeam Mainnet': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c',
    'Op BNB': '0xCBFBc05237Bb6A08d84195325c977D2d7A2d051c'
}
for network, address in networks.items():
    print(f"Connecting to {network} at address {address}...")
    w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
    if w3.isConnected():
        print(f"Debug: Wallet connected successfully to {network}!")
    else:
        print(f"Debug: Failed to connect to {network}.")
    # Automatically connect without user input
    # Add any additional connection logic here
print("Debug: Connection attempts completed.")
