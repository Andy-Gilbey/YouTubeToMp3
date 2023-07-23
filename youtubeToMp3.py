# Required libraries
import os
from moviepy.editor import VideoFileClip
from pytube import YouTube

def printBanner():
    """
    Function to print the banner at the start of the program.
    """
    # Define banner as a multi-line string
    banner = """
    _  _    ____    _  _      ___      ____       ____    ____         __  __      ___    ____   
   FJ  L]  /_  _\  FJ  L]    F _ ",   F ___J     /_  _\  F __ ]       F  \/  ]    F _ ", F___ J  
  J |  | L [J  L] J |  | L  J `-'(|  J |___:     [J  L] J |--| L     J |\__/| L  J `-' | `-__| L 
  | |  | |  |  |  | |  | |  | ,--.\  | _____|     |  |  | |  | |     | |`--'| |  |  __/F  |__  ( 
  F L__J J  F  J  F L__J J  F L__J \ F L____:     F  J  F L__J J     F L    J J  F |__/.-____] J 
 J\______/FJ____LJ\______/FJ_______JJ________L   J____LJ\______/F   J__L    J__LJ__|   J\______/F
  J______F |____| J______F |_______F|________|   |____| J______F    |__L    J__||__L    J______F 
                                                                                                 
    Devilware                                                                                                                 
    """
    # Print the banner
    print(banner)

def printMenu():
    """
    Function to print the menu options for the user.
    """
    # Print the menu options
    print("Please choose an option:")
    print("1. Start")
    print("2. Exit")

def startConversion():
    """
    Function to convert a YouTube video into an mp3 file.
    """
    downloadedFile = None
    try:
        # Get user inputs for YouTube URL and output filename
        youtubeUrl = input("Enter the YouTube URL: ")
        outputFileName = input("Enter the output filename: ")

        # Create YouTube object and download the first stream
        youtube = YouTube(youtubeUrl)
        stream = youtube.streams.first()
        downloadedFile = stream.download()

        # Convert the downloaded file to mp3
        clip = VideoFileClip(downloadedFile)
        clip.audio.write_audiofile(f'{outputFileName}.mp3')
        # Close the clip to free the file
        clip.close()

        print("Conversion completed!")
    except Exception as e:
        # If any errors occur during the conversion process, print an error message
        print(f"An error occurred: {e}")
    finally:
        # Delete the downloaded file after conversion, if it exists
        if downloadedFile and os.path.exists(downloadedFile):
            os.remove(downloadedFile)

def main():
    """
    The main function that runs the program.
    """
    while True:
        # Print the banner and menu
        printBanner()
        printMenu()

        # Get the user's choice
        choice = input("Your choice: ")

        if choice == '1':
            # If the user chooses '1', start the conversion process
            startConversion()
        elif choice == '2':
            # If the user chooses '2', break the loop to end the program
            print("Exiting...")
            break
        else:
            # If the user doesn't choose '1' or '2', print an error message
            print("Invalid option. Please try again.\n")

# If this file is the main script, run the main function
if __name__ == "__main__":
    main()
