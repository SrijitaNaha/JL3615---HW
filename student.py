import tkinter as tk
from tkinter import ttk

def add_new_student():
    # Add new student logic here
    pass

def edit_student():
    # Edit student logic here
    pass

def delete_student():
    # Delete student logic here
    pass

def open_student():
    # Open student logic here
    pass

def save_student():
    # Save student logic here
    pass

root = tk.Tk()
root.title("Student Information and Marks Logger")

# Create a frame for the student report log
report_frame = tk.Frame(root, bg="#f0f0f0")
report_frame.pack(padx=10, pady=10)

# Create labels and entry fields for student information
name_label = tk.Label(report_frame, text="Name:", bg="#f0f0f0", fg="#007bff")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(report_frame, width=20, font=("Arial", 12), bg="#ffffff", fg="#000000")
name_entry.grid(row=0, column=1, padx=5, pady=5)

roll_number_label = tk.Label(report_frame, text="RollNumber:", bg="#f0f0f0", fg="#007bff")
roll_number_label.grid(row=1, column=0, padx=5, pady=5)
roll_number_entry = tk.Entry(report_frame, width=20, font=("Arial", 12), bg="#ffffff", fg="#000000")
roll_number_entry.grid(row=1, column=1, padx=5, pady=5)

# Create labels and entry fields for marks
science_marks_label = tk.Label(report_frame, text="Science_Marks:", bg="#f0f0f0", fg="#007bff")
science_marks_label.grid(row=0, column=2, padx=5, pady=5)
science_marks_entry = tk.Entry(report_frame, width=20, font=("Arial", 12), bg="#ffffff", fg="#000000")
science_marks_entry.grid(row=0, column=3, padx=5, pady=5)

maths_marks_label = tk.Label(report_frame, text="Maths_Marks:", bg="#f0f0f0", fg="#007bff")
maths_marks_label.grid(row=1, column=2, padx=5, pady=5)
maths_marks_entry = tk.Entry(report_frame, width=20, font=("Arial", 12), bg="#ffffff", fg="#000000")
maths_marks_entry.grid(row=1, column=3, padx=5, pady=5)

percentage_label = tk.Label(report_frame, text="Percentage:", bg="#f0f0f0", fg="#007bff")
percentage_label.grid(row=2, column=2, padx=5, pady=5)
percentage_entry = tk.Entry(report_frame, width=20, font=("Arial", 12), bg="#ffffff", fg="#000000")
percentage_entry.grid(row=2, column=3, padx=5, pady=5)

# Create a frame for buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(padx=10, pady=10)

# Create buttons for various operations
edit_button = tk.Button(button_frame, text="Edit", command=edit_student, bg="#007bff", fg="#ffffff", font=("Arial", 12))
edit_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete", command=delete_student, bg="#dc3545", fg="#ffffff", font=("Arial", 12))
delete_button.grid(row=0, column=1, padx=5, pady=5)

open_button = tk.Button(button_frame, text="Open", command=open_student, bg="#28a745", fg="#ffffff", font=("Arial", 12))
open_button.grid(row=0, column=2, padx=5, pady=5)

update_add_button = tk.Button(button_frame, text="Update/Add", command=add_new_student, bg="#007bff", fg="#ffffff", font=("Arial", 12))
update_add_button.grid(row=0, column=3, padx=5, pady=5)

save_button = tk.Button(button_frame, text="Save", command=save_student, bg="#28a745", fg="#ffffff", font=("Arial", 12))
save_button.grid(row=0, column=4, padx=5, pady=5)

root.mainloop()