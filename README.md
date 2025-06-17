# 📥 YouTube Video Downloader (Python GUI)

A simple Python desktop application that lets you download YouTube videos by just pasting the video URL. It features a clean and modern user interface built with [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) and uses [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) for downloading. The app relies on `ffmpeg` to properly merge video and audio streams.

---

## 🚀 Features

- ✅ Download YouTube videos by URL
- 🖥️ Modern UI built with `customtkinter`
- ⚡ Fast and reliable downloads using `yt-dlp`
- 🎞️ Automatic video/audio merging using `ffmpeg`
- 🧾 Basic error handling and download status display

---

## 🛠 Requirements

- Python 3.8+
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter)
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
- [`ffmpeg`](https://ffmpeg.org/) (must be installed and available in system PATH)

### Install Python packages:

```bash
pip install -r requirements.txt
