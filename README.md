# YouTube to MP3 Converter

## Description
This script allows any user to convert YouTube videos to MP3 format. 
It uses a menu to start the conversion process or exit the program. The script utilises the `pytube` library to download YouTube videos and `moviepy` to extract and save the audio as an MP3 file.

## Required Libraries
To run this script, you will need the following Python libraries:
- `os`: A standard library used for interacting with the operating system.
- `moviepy.editor`: For handling video files and extracting audio.
- `pytube`: For downloading videos from YouTube.

You can install the required libraries using pip:

```bash
pip install moviepy pytube
```

## Script Functions
### printBanner()
Prints a startup banner.

### printMenu()
Displays menu options to the user:
1. Start the conversion process.
2. System exit.

### startConversion()
This handles the conversion process of a YouTube video to MP3 format. User is prompted to enter the YouTube URL and the desired output filename. This function manages the download, conversion, and the cleanup process.

### main()
Controls the flow of the program based on user input:
- Displays the banner and menu.
- Processes user input to either start the conversion or exit.

## Running the Script
To run the script, follow these steps:
1. Ensure all required libraries are installed.
2. Save the script in a file, for example, `youtube_to_mp3.py`.
3. Open your terminal or command prompt.
4. Navigate to the directory containing the script.
5. Execute the script by running:

```bash
python youtube_to_mp3.py
```

Follow the on-screen prompts to convert YouTube videos to MP3 files or to exit the program.

## Legal Notice
Please ensure you have the right to download YouTube videos and convert them to MP3 format, as this may infringe on copyright laws depending on your specific jurisdiction (and the content). 
Always use this tool both responsibly and of course ethically.
