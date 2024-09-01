import os
from pytube import YouTube, Playlist
from pydub import AudioSegment
import tkinter as tk
from tkinter import messagebox
from Parser import convert


def download_and_convert(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        output_file = stream.download(output_path='mp4_downloads')

        base, ext = os.path.splitext(output_file)
        mp3_file = base + '.mp3'
        AudioSegment.from_file(output_file).export(mp3_file, format='mp3')
        os.remove(output_file)

        return yt.title
    except Exception as e:
        return str(e)


def add_url():
    url = url_entry.get()
    if 'playlist' in url:
        process_playlist(url)
    else:
        if url in url_listbox.get(0, tk.END):
            messagebox.showinfo("Warning", "Video already downloaded in this pars.")
            return

        url_listbox.insert(tk.END, url)
        title = download_and_convert(url)
        messagebox.showinfo("Success", f"Download done for: {title}")
    url_entry.delete(0, tk.END)


def process_playlist(url):
    try:
        playlist = Playlist(url)
        for video_url in playlist.video_urls:
            if video_url not in url_listbox.get(0, tk.END):
                url_listbox.insert(tk.END, video_url)
                title = download_and_convert(video_url)
                messagebox.showinfo("Success", f"Download done for : {title}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occured handling the playlist : {e}")


def main():
    root = tk.Tk()
    root.title("Youtube parser")

    if not os.path.exists('mp4_downloads'):
        os.makedirs('mp4_downloads')

    frame = tk.Frame(root)
    frame.pack(pady=20)

    url_entry = tk.Entry(frame, width=50)
    url_entry.pack(side=tk.LEFT, padx=10)

    add_button = tk.Button(frame, text="Add and download", command=add_url)
    add_button.pack(side=tk.LEFT)

    url_listbox = tk.Listbox(root, width=80, height=15)
    url_listbox.pack(pady=20)

    root.mainloop()


if __name__ == '__main__':
    main()
    convert.convert()
