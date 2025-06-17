import tkinter
import customtkinter
import yt_dlp
import re

# Regex to remove ANSI escape codes
ANSI_ESCAPE_PATTERN = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

# Function to handle download progress updates
def progress_hook(d):
    if d['status'] == 'downloading':
        percentage_str_from_yt_dlp = d.get('_percent_str', '0.0%') 
        clean_percentage_str = ANSI_ESCAPE_PATTERN.sub('', percentage_str_from_yt_dlp)
        
        progress = d.get('downloaded_bytes', 0) / (d.get('total_bytes') or d.get('total_bytes_estimate', 1))
        progress_bar.set(progress) # Update the progress bar strip
            
        # --- Display the percentage string in the status label ---
        status_label.configure(text=clean_percentage_str, text_color="#00b4d8")
        
        app.update_idletasks() # Crucial for refreshing the GUI during download
    elif d['status'] == 'finished':
        progress_bar.set(1) # Ensure bar is full when finished
        status_label.configure(text="Download Complete!", text_color="#00b4d8")
        app.update_idletasks() # Final update


def startDownload():
    url = url_var.get()
    
    if not url:
        status_label.configure(text="Please enter a URL!", text_color="#e63946")
        return

    # Reset UI for a new download
    status_label.configure(text="Starting download...", text_color="#00b4d8") # Initial status
    progress_bar.set(0) # Reset progress bar to 0 at start of new download
    downloadButton.configure(state="disabled", text="Downloading...") # Disable button during download
    app.update_idletasks() # Refresh UI

    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'progress_hooks': [progress_hook], # <-- IMPORTANT: Add our progress hook here
            'outtmpl': '%(title)s.%(ext)s' # Save with video title
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Status for completion is handled by progress_hook 'finished' state
        downloadButton.configure(text="Download", state="normal") # Re-enable button
        url_var.set("") # Clear URL input
        
    except Exception as e:
        status_label.configure(text=f"Error: {e}", text_color="#e63946") # Error status
        downloadButton.configure(text="Download", state="normal") # Re-enable button on error
        progress_bar.set(0) # Reset progress bar on error
        print(f"Error: {e}") # Keep printing to console for debugging
    finally:
        app.update_idletasks() # Final UI update

# System settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Our app frame:
app = customtkinter.CTk()
app.geometry('720x480')
app.title("YouTube Downloader")

# Adding UI elements:
title = customtkinter.CTkLabel(app,text="Insert your YouTube link", font=customtkinter.CTkFont(size=28, weight="bold"))
title.pack(padx=10,pady=(40, 10))

# link input 
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var,
                              placeholder_text="Enter video URL here...",
                              font=customtkinter.CTkFont(size=14))
link.pack(padx=10,pady=10)

# Download Button:
downloadButton = customtkinter.CTkButton(app,text="Download",command=startDownload,
                                         font=customtkinter.CTkFont(size=16, weight="bold"),
                                         hover_color="#00b4d8")
downloadButton.pack(padx=10,pady=20)

# IMPORTANT: Progress bar widget must be defined before progress_hook is used
progress_bar = customtkinter.CTkProgressBar(app, width=400,progress_color="#00b4d8")
progress_bar.set(0) # Initialize at 0%
progress_bar.pack(padx=10,pady=10)

# Status Label:
status_label = customtkinter.CTkLabel(app, text="", font=customtkinter.CTkFont(size=20)) # Initial text
status_label.pack(padx=10,pady=10)

# Run app
app.mainloop()