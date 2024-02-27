# checkBalanceSeedPhrases
All you have to do is
1. Register an account on etherscan.io , activate it by email, log in to your etherscan account, go to API Keys, generate your key and replace "YOUR_ETHER_API_KEY" with your actual key
2. Place your seeds into seedd.txt where the seedchecker.py is located, create good.txt or simply replace path and name of your seed and result files at the end of the checkseed.py
3. Run: python checkseed.py

When script will finish checking, results will be saved in good.txt ( or w/e file you specify for output. )

Don't forget to install requirements with pip
pip install requests
pip install eth-account
