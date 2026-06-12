import os
from datetime import datetime

def generate_log(log_entries):
    # 1. Raise a ValueError when called with invalid input (non-list types)
    if not isinstance(log_entries, list):
        raise ValueError("Input must be a list of log entries.")
    
    # 2. Filename follows pattern log_YYYYMMDD.txt using current timestamp
    current_date = datetime.now().strftime("%Y%m%d")
    filename = f"log_{current_date}.txt"
    
    # 3. Create the log file (handles an empty list to create a valid empty file)
    with open(filename, "w") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")
            
    # 4. Print a confirmation message including the filename
    print(f"Success: Log file '{filename}' has been generated.")
    
    # CRITICAL: The test suite explicitly requires returning the filename string!
    return filename