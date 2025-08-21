import tkinter as tk
import time

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.resizable(False, False)

# Styling
clock_label = tk.Label(root, font=("Arial", 50, "bold"), bg="black", fg="cyan")
clock_label.pack(anchor="center")

def update_time():
    current_time = time.strftime("%H:%M:%S")  # 24-hour format
    clock_label.config(text=current_time)
    root.after(1000, update_time)  # update every second

# Start the clock
update_time()

# Run the GUI
root.mainloop()

# Ask for first name
first_name = input("Enter your first name: ")

# Ask for second name
second_name = input("Enter your second name: ")

# Display full name
print("Your full name is:", first_name, second_name)

