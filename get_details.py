import time
from datetime import datetime
import win32gui

# Initialize variables
w = win32gui
window_name = str(w.GetWindowText(w.GetForegroundWindow()))
start_time = datetime.now().replace(microsecond=0)

print("Tracking started... Press Ctrl+C to stop.")

try:
    while True:
        # Prevent 100% CPU usage
        time.sleep(0.5)
        
        # Get current active window
        new_window_name = str(w.GetWindowText(w.GetForegroundWindow()))
        
        # Check for window change
        if window_name != new_window_name:
            stop_time = datetime.now().replace(microsecond=0)
            time_spent = stop_time - start_time
            
            # Print result if the window had a title
            if window_name.strip():
                print(f"{window_name} | Time Spent: {time_spent}")
            
            # Reset trackers
            window_name = new_window_name
            start_time = datetime.now().replace(microsecond=0)

except KeyboardInterrupt:
    print("\nTracking stopped.")
