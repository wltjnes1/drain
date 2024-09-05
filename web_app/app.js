// app.js
document.getElementById('connectWallet').addEventListener('click', async () => {
    if (typeof window.ethereum !== 'undefined') {
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Wallet connected');
        } catch (error) {
            console.error('User denied account access');
        }
    } else {
        console.log('Please install MetaMask!');
    }
});

document.getElementById('drainFunds').addEventListener('click', async () => {
    // Call the function to drain funds here
    console.log('Draining funds...');
});