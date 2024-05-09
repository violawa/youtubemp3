import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
from moviepy.editor import *
import threading
import os


def download_youtube_audio(url, output_path):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio_file_path = audio.download(output_path=output_path)
        return audio_file_path
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
        return None


def convert_to_mp3(video_path, output_path):
    try:
        video = AudioFileClip(video_path)
        audio = video.subclip()
        audio.write_audiofile(output_path)
        audio.close()
        video.close()
        messagebox.showinfo(
            "Success", f"Successfully converted {video_path} to MP3: {output_path}"
        )
        root.quit()  # Close the application after successful conversion
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")


def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        output_folder_entry.delete(0, tk.END)
        output_folder_entry.insert(0, folder_selected)


def download_and_convert():
    youtube_url = url_entry.get()
    output_folder = output_folder_entry.get()

    if not youtube_url or not output_folder:
        messagebox.showwarning("Warning", "Please enter YouTube URL and output folder.")
        return

    download_thread = threading.Thread(
        target=download_audio, args=(youtube_url, output_folder)
    )
    download_thread.start()


def download_audio(url, output_folder):
    video_path = download_youtube_audio(url, output_folder)
    if video_path:
        mp3_output_path = (
            f"{output_folder}/{os.path.splitext(os.path.basename(video_path))[0]}.mp3"
        )
        convert_to_mp3(video_path, mp3_output_path)


# Create main window
root = tk.Tk()
root.title("YouTube Audio Downloader")

# Create URL input
url_label = ttk.Label(root, text="YouTube URL:")
url_label.grid(row=0, column=0, padx=10, pady=5)
url_entry = ttk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

# Create output folder input
output_folder_label = ttk.Label(root, text="Output Folder:")
output_folder_label.grid(row=1, column=0, padx=10, pady=5)
output_folder_entry = ttk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=10, pady=5)
browse_button = ttk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=1, column=2, padx=10, pady=5)

# Create download button
download_button = ttk.Button(
    root, text="Download and Convert", command=download_and_convert
)
download_button.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
