# ⚡ YTDL-RF-Converter

**YTDL-RF-Converter** is a lightweight Python utility designed for **HackRF users and RF audio engineers** who need to quickly download and convert YouTube audio into clean, lossless `.wav` files — ready for analysis, signal generation, or transmission experiments.

It automates all the boring setup:  
- Installs missing Python dependencies (`yt-dlp`, `requests`)  
- Checks and installs **FFmpeg** (Linux & Windows supported)  
- Downloads the best quality YouTube audio  
- Converts it into high-fidelity `.wav` format automatically  

---

## 🧠 How It Works

1. The script checks your system for **required Python packages** and installs them if missing.  
2. It verifies whether **FFmpeg** is installed — if not, it downloads and sets it up automatically.  
3. You provide a **YouTube video URL**, and it:
   - Downloads the **best audio stream** available (`.m4a`)
   - Converts it into a **44.1kHz 16-bit stereo WAV** file
   - Cleans up temporary files

Perfect for feeding into tools like **HackRF, GNURadio, SDR#, or custom RF pipelines**.

---

## ⚙️ Requirements

- Python 3.8 or newer  
- Internet connection (for first-time setup and downloads)  
- FFmpeg (automatically installed if not found)  

### Python Dependencies
- `yt-dlp`
- `requests`

If missing, they’ll be installed automatically — no manual pip commands required.

---

## 🚀 Usage


python ytdl_rf_converter.py
Then:

Enter the YouTube link when prompted.

Choose a name for your WAV file (e.g. signal_test).

Your converted file will appear in the downloads folder.

Example:

Enter YouTube link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter output file name (e.g. output): test_signal
[✓] WAV file created: downloads/test_signal.wav

🧩 Folder Structure
YTDL-RF-Converter/
│
├── ytdl_rf_converter.py     # Main script
├── downloads/               # Output folder for .wav files
└── README.md

🧠 Notes

Works on Windows and Linux systems (macOS support possible with manual FFmpeg setup).

The script automatically adjusts the PATH variable to access FFmpeg after installation.

Produces lossless WAV files suitable for RF experiments and digital signal processing.

🧰 Tech Stack

Python 3

yt-dlp → For YouTube audio extraction

FFmpeg → For audio decoding and format conversion

🧠 Author

Efe
AI & Cybersecurity Developer • Hardware tinkerer • RF enthusiast

“Convert sound into signals, and signals into stories.”
— YTDL-RF-Converter
