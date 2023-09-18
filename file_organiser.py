import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def rename_files(folder_path, new_name):
    """
    Rename files in the specified folder with a new name and sequential numbering.

    Args:
        folder_path (str): The path to the folder containing the files to be renamed.
        new_name (str): The new base name for the files.

    Returns:
        None
    """
    try:
        file_list = os.listdir(folder_path)
    except FileNotFoundError:
        messagebox.showerror("Error", "Folder not found. Please select a valid folder.")
        return
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return

    counter = 1
    for file_name in file_list:
        try:
            # Split the file name into base name and extension
            base_name, extension = os.path.splitext(file_name)

            # Create the new file name using the provided new name and counter
            new_file_name = f"{new_name}_{counter}{extension}"

            # Build the full paths for the old and new files
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)

            # Increment the counter
            counter += 1

            # Print the old and new file names
            print(f"Renamed '{file_name}' to '{new_file_name}'")
        except Exception as e:
            messagebox.showerror(
                "Error", f"An error occurred while renaming files: {str(e)}"
            )


def select_folder():
    """
    Open a file dialog to allow the user to select a folder and update the folder path entry field.
    """
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)


def rename_files_gui():
    """
    Get folder path and new name from the user, display a warning message, and rename files if confirmed.
    """
    folder_path = folder_path_entry.get()
    new_name = new_name_entry.get()
    if folder_path and new_name:
        warning_message = "Warning: Renaming files can't be undone. Are you sure you want to continue?"
        user_response = messagebox.askyesno("Warning", warning_message)

        if user_response:
            rename_files(folder_path, new_name)
            tk.messagebox.showinfo("File Renaming", "Files renamed successfully!")
    else:
        tk.messagebox.showwarning(
            "File Renaming", "Please select a folder and enter a new name."
        )


# Create the main window
window = tk.Tk()
window.title("File Renaming")

# Description Label
description_label = tk.Label(
    window,
    text="Efficiently rename files in a folder with sequential numbering.\n Select a folder, provide a new name, and the program will automatically\n assign sequential numbers to each file.",
)
description_label.grid(row=0, column=0, columnspan=3, padx=5, pady=(20, 5))

# Folder Path Label and Entry
folder_path_label = tk.Label(window, text="Folder Path:")
folder_path_label.grid(row=1, column=0, padx=5, pady=5)

folder_path_entry = tk.Entry(window, width=50)
folder_path_entry.grid(row=1, column=1, padx=5, pady=5)

browse_button = tk.Button(window, text="Browse", command=select_folder)
browse_button.grid(row=1, column=2, padx=5, pady=5)

# New Name Label and Entry
new_name_label = tk.Label(window, text="New Name:")
new_name_label.grid(row=2, column=0, padx=5, pady=5)

new_name_entry = tk.Entry(window, width=50)
new_name_entry.grid(row=2, column=1, padx=5, pady=5)

# Rename Button
rename_button = tk.Button(window, text="Rename Files", command=rename_files_gui)
rename_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Start the main GUI loop
window.mainloop()
