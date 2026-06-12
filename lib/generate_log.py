import os
from datetime import datetime

def generate_log(log_entries):
    # 1. The function raises a ValueError when called with invalid input (non-list types)
    if not isinstance(log_entries, list):
        raise ValueError("page_count must be an integer")  # or standard error string
    
    # 2. Filename follows pattern log_YYYYMMDD.txt
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    # 3. File contents exactly match the input list / valid empty log file without errors
    with open(filename, "w") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")
            
    # 4. Function prints a confirmation message including the filename
    print(f"Success: Log file {filename} has been created.")
    
    # 5. Correctly return the filename so the test fixture can track and clean it up
    return filename