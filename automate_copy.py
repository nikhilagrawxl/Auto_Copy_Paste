import pyautogui
import time

def copy_description_to_destination(description):
    # Set the coordinates or identifiers of the destination
    # Adjust these values based on the specific application or website you're targeting
    
    time.sleep(3)
    
    text_coordinates = (628, 35)  
    pyautogui.click(text_coordinates)
    
    t_coordinates=(628,125)
    pyautogui.click(t_coordinates)
    
    # time.sleep(1)

    # Paste the description
    pyautogui.typewrite(description)
    a_coordinates=(628,215)
    pyautogui.click(a_coordinates)
    
    p_coordinates=(1200,35)
    pyautogui.click(p_coordinates)
    
    pu_coordinates=(1200,365)
    pyautogui.click(pu_coordinates)

    # Press Enter key to submit (optional)
    # pyautogui.press('enter')

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
