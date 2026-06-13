import datetime

def generate_log(data_list):
    # Requirement: Raise ValueError for non-list types
    if not isinstance(data_list, list):
        raise ValueError("Input must be a list")

    # Requirement: Filename pattern log_YYYYMMDD.txt
    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    filename = f"log_{timestamp}.txt"

    # Requirement: Create file and write contents
    with open(filename, "w") as f:
        for item in data_list:
            f.write(f"{item}\n")

    # Requirement: Print confirmation message
    print(f"Log created successfully: {filename}")