import schedule
import subprocess
import time
import pyautogui

def open_zoom_and_join_meeting():
    try:
        # Replace "C:\path\to\join_button.png" 
        # with the full path to the image file on your system
        image_path = r"C:\path\to\join_button.png"
        
        # Replace "C:\path\to\Zoom.exe" 
        # with the actual path to the Zoom app executable on your system
        zoom_app_path = r"C:\path\to\Zoom.exe"
        
        # Open the Zoom app
        subprocess.Popen(zoom_app_path)
        
        # Wait for the Zoom app to open
        time.sleep(1)  # Adjust the delay if needed
        
        # Click on the "Join" button
        join_button_location = pyautogui.locateCenterOnScreen(image_path)
        if join_button_location is None:
            raise Exception("Join button not found")
        pyautogui.click(join_button_location)
        
        # Wait for the "Join Meeting" window to appear
        time.sleep(1)  # Adjust the delay if needed
        
        # Enter the Zoom room ID
        zoom_room_id = "place.zoom.id.here"  # Replace with your Zoom room ID
        pyautogui.write(zoom_room_id)
        pyautogui.press('enter')
        
        # Wait for the meeting ID to be entered before typing the password
        time.sleep(1)  # Adjust the delay if needed
        
        # Enter the meeting password
        meeting_password = "place.password.here"  # Replace with your meeting password
        pyautogui.typewrite(meeting_password, interval=0.1)  # Adjust the interval if needed
        pyautogui.press('enter')
        
    except Exception as e:
        print("An error occurred:", e)

# Call the function directly to join the meeting when the script is run
open_zoom_and_join_meeting()

