author = "moonware.inc"
print("welcome to python youtube vedio downloader  that help you to download youtube vedio by a url");
print("this is a software that work faster and safer than orther malware websites ");
print("this is soft. code  that created by ",author);
print("to get more free and safer  software  like this vissit us on our web site","comming soon");


import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def browse():
    global save_path
    save_path = filedialog.askdirectory()
    if save_path:
        messagebox.showinfo("Save Location", f"Selected location: {save_path}")

def download():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube video URL")
        return

    if format_var.get() == 1:  # MP4 selected
        download_video(url)
    elif format_var.get() == 2:  # MP3 selected
        download_audio(url)

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully")

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        messagebox.showinfo("Success", "Audio downloaded successfully")

# GUI Setup
root = tk.Tk()
root.title("YouTube Downloader")

# Set the icon
root.iconbitmap("your_icon.ico")  # Replace with the path to your .ico file

# URL Entry
tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Save As button
tk.Button(root, text="Save As", command=browse).grid(row=1, column=1, padx=10, pady=10)

# Format Selection
format_var = tk.IntVar()
format_var.set(1)

tk.Label(root, text="Select Format:").grid(row=2, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="MP4", variable=format_var, value=1).grid(row=2, column=1, sticky='w', padx=10, pady=5)
tk.Radiobutton(root, text="MP3", variable=format_var, value=2).grid(row=3, column=1, sticky='w', padx=10, pady=5)

# Download Button
download_button = tk.Button(root, text="Download", command=download)
download_button.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
