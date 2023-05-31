import subprocess
import re

# Listing all users of the Windows system
def list_users():

    list_users_command = "net users"
    result = subprocess.run(list_users_command, shell=True, capture_output=True, text=True).stdout
    print(result)

list_users()

