
import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Format: Hours:Minutes:Seconds
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1 second

# 
root = tk.Tk()
root.title("Digital Clock")

# Add a label to display the time
label = tk.Label(root, font=("Arial", 50), bg="black", fg="lime")
label.pack(anchor="center")

update_time()

# Run the app
root.mainloop()
