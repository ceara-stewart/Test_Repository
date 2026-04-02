# package_loader.py
# A simple script to import and load common Python packages

import os
import sys
import json
import math
import random
import datetime

def main():
    print("=== Package Loader ===\n")

    # os - Operating System interface
    print(f"[os]       Current directory: {os.getcwd()}")

    # sys - System-specific parameters
    print(f"[sys]      Python version: {sys.version}")

    # json - JSON encoder/decoder
    sample = {"name": "Test_Repository", "owner": "ceara-stewart", "active": True}
    print(f"[json]     Serialized: {json.dumps(sample)}")

    # math - Mathematical functions
    print(f"[math]     Pi = {math.pi:.4f}, sqrt(144) = {math.sqrt(144)}")

    # random - Generate random numbers
    print(f"[random]   Random number (1-100): {random.randint(1, 100)}")

    # datetime - Date and time
    print(f"[datetime] Current timestamp: {datetime.datetime.now()}")

    print("\nAll packages loaded successfully!")

if __name__ == "__main__":
    main()