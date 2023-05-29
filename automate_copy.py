import pyautogui
import time

def copy_description_to_destination(description):
    # Set the coordinates or identifiers of the destination
    # Adjust these values based on the specific application or website you're targeting
    destination_coordinates = (26, 26)  # Example: (x, y) coordinates of the destination

    # Click on the destination to focus on it
    pyautogui.click(destination_coordinates)
    
    time.sleep(1)

    # Paste the description
    pyautogui.typewrite(description)

    # Press Enter key to submit (optional)
    pyautogui.press('enter')

# Provide the path to the source document
source_file_path = 'test.txt'

# Read the source document and extract the description
with open(source_file_path, 'r') as file:
    content = file.read()

    # Extract the description (example: assuming description starts with "Description:")
    start_keyword = "Description:"
    end_keyword = "\n"
    start_index = content.find(start_keyword) + len(start_keyword)
    end_index = content.find(end_keyword, start_index)
    description = content[start_index:end_index].strip()

    # Call the function to copy the description to the destination
    copy_description_to_destination(description)
