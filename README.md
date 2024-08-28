This code implements a simple banking system with user authentication, allowing users to check their balance, deposit, withdraw, and send money. If the user has a "CEO" rank, they can also set, deduct, and add to other users' balances. Data is loaded from a backup file at the start and updated when a user logs out. The program uses Python's gc module to manage and interact with user objects dynamically.




![image](https://github.com/user-attachments/assets/1403dd9b-0777-49a3-a860-37f394205683)


to use this program, ensure all the py script as well as the txt files are saved in the same directory.
ensure the following modules are imported before use:
-import gc
-import time
-import sys
-import fileinput
