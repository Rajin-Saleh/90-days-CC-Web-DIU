import tkinter as tk
from tkinter import messagebox
from plyer import notification
import datetime

# Function to set a reminder
def set_reminder():
    reminder_text = entry.get()
    reminder_time = time_entry.get()

    try:
        # Parse the time string to a datetime object
        reminder_datetime = datetime.datetime.strptime(reminder_time, "%Y-%m-%d %H:%M:%S")

        # Calculate the time difference in seconds
        time_diff = (reminder_datetime - datetime.datetime.now()).total_seconds()

        if time_diff <= 0:
            messagebox.showerror("Invalid Time", "Please enter a future time.")
        else:
            # Schedule the notification
            notification.schedule(
                title="Reminder",
                message=reminder_text,
                timeout=time_diff,
            )
            messagebox.showinfo("Reminder Set", "Your reminder has been set successfully.")
    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter time in the format: YYYY-MM-DD HH:MM:SS")

# Create the main window
root = tk.Tk()
root.title("Reminder App")

# Label and Entry for reminder text
label = tk.Label(root, text="Enter Reminder:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Label and Entry for reminder time
time_label = tk.Label(root, text="Enter Time (YYYY-MM-DD HH:MM:SS):")
time_label.pack()
time_entry = tk.Entry(root)
time_entry.pack()

# Button to set the reminder
set_button = tk.Button(root, text="Set Reminder", command=set_reminder)
set_button.pack()

# Run the GUI main loop
root.mainloop()
