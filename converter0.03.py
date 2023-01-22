import os
import subprocess
from tkinter import *
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import ttk

def convert_m4a_to_mp3():
    input_files = filedialog.askopenfilenames(title="Select M4A files", filetypes=(("M4A files", "*.m4a"), ("all files", "*.*")))
    if not input_files:
        messagebox.showerror("Error", "No files selected")
        return
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    total_files = len(input_files)
    current_file = 0
    for input_file in input_files:
        current_file += 1
        input_file_name = os.path.basename(input_file)
        output_file = os.path.join(output_dir, os.path.splitext(input_file_name)[0] + ".mp3")
        subprocess.run(["ffmpeg", "-i", input_file, "-c:a", "libmp3lame", "-q:a", "2", output_file], creationflags=subprocess.CREATE_NO_WINDOW)
        progress_bar["value"] = int((current_file / total_files) * 100)
        root.update()
    messagebox.showinfo("Audio Converter", "Conversion complete!")
    progress_bar.config(value=0)
    root.update()



root = Tk()
root.geometry("500x300")
root.title("M4A to MP3 converter")

# Create a PhotoImage object from the background image file
bg_image = PhotoImage(file="1.PNG")

# Create a Label widget and set its image attribute to the PhotoImage object
bg_label = Label(root, image=bg_image)
bg_label.grid(row=0, column=0, columnspan=2, rowspan=4, sticky="nsew")

convert_button = Button(root, text="Choose file(s)", command=convert_m4a_to_mp3)
convert_button.grid(row=3, column=0, sticky="w")

progress_bar = ttk.Progressbar(root, orient='horizontal', length=100, mode='determinate')
progress_bar.grid(row=3, column=0, sticky="e")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

root.mainloop()

