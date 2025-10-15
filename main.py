import subprocess
import os
import sys
import platform
import urllib.request
import zipfile
import importlib
import pkg_resources

# Check and install required Python libraries
required_libraries = ['yt-dlp', 'requests']


def install_required_libraries():
    """Installs missing Python libraries."""
    for library in required_libraries:
        try:
            importlib.import_module(library)
        except ImportError:
            print(f"[!] The '{library}' library is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", library])
            print(f"[✓] The '{library}' library has been installed successfully.")
        else:
            print(f"[✓] The '{library}' library is already installed.")


def check_ffmpeg_installed():
    """Checks if FFmpeg is installed."""
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False


def download_and_install_ffmpeg():
    """Downloads and installs FFmpeg."""
    system = platform.system().lower()

    if system == "linux":
        print("[*] Linux system detected. Installing FFmpeg...")
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "ffmpeg"])
        print("[✓] FFmpeg installed successfully!")

    elif system == "windows":
        print("[*] Windows system detected. Downloading FFmpeg...")
        url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz"
        output = "ffmpeg-release.tar.xz"

        # Download FFmpeg
        urllib.request.urlretrieve(url, output)

        print("[*] FFmpeg downloaded, extracting...")

        # Extract
        with zipfile.ZipFile(output, 'r') as zip_ref:
            zip_ref.extractall("ffmpeg")

        os.remove(output)  # Remove tar file

        # Add FFmpeg to PATH
        ffmpeg_dir = os.path.join(os.getcwd(), "ffmpeg", "bin")
        os.environ["PATH"] += os.pathsep + ffmpeg_dir

        print("[✓] FFmpeg downloaded and installed successfully!")

    else:
        print("[!] Unknown operating system. Please install FFmpeg manually.")
        sys.exit(1)


def download_wav(youtube_url, output_name="output.wav", folder="downloads"):
    # 1. Create folder (if not exists)
    os.makedirs(folder, exist_ok=True)

    # 2. File paths
    temp_file = os.path.join(folder, "temp_audio.m4a")

    # If no file name specified, use default 'output.wav'
    if not output_name.endswith(".wav"):
        output_name += ".wav"

    output_path = os.path.join(folder, output_name)

    # 3. Download audio from YouTube
    subprocess.run([
        "yt-dlp", "-f", "bestaudio", "-o", temp_file, youtube_url
    ])

    # 4. Convert to WAV using FFmpeg
    subprocess.run([
        "ffmpeg", "-i", temp_file, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", output_path
    ])

    # 5. Remove temporary file
    os.remove(temp_file)
    print(f"[✓] WAV file created: {output_path}")


if __name__ == "__main__":
    # Install required Python libraries
    install_required_libraries()

    # Check if FFmpeg is installed
    if not check_ffmpeg_installed():
        print("[!] FFmpeg is not installed.")
        print("Starting FFmpeg download and installation...")
        download_and_install_ffmpeg()

    # Get user input from terminal
    youtube_url = input("Enter YouTube link: ")
    output_name = input("Enter output file name (e.g. output): ")

    download_wav(youtube_url, output_name)
