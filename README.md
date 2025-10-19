# VOdownloarder
Final project-CS50P
#### Video Demo:  <URL HERE>
#### Description: This program allows users to download videos or audio files easily using a simple command-line interface.


It lets you:
-Choose beetween video or audio-only download
-select your preffered qulity(1080p, 720p, or default)
-automatically organize downloads into separate folders
    -videos/
    -audios

How It Works
1- The user enters a valid YouTube video URL.
2- The program asks whether to download:
    -The full video, or
    -Audio only
3- The user selects the desired quality.
4- The file is downloaded and automatically saved to the correct folder.

Technologies Used
-Python
-yt-dlp -->to handle Youtube downloads
-os,sys and pathlib --> for file and folder management

Installation
1- Clone the repository
git clone https://github.com/Mouhamed-king/cs50p.git

2-install dependencies
pip install yt-dlp

3-install chocolatey if doesn't exist and run
choco install ffmpeg

    -->you can install chocolatey 
    https://chocolatey.org/install

Future Improvement
-Add a simple GUI
-Display download progress percentage
-Allow user-defined output folders

Author
Developped by Mouhamed Sogue/https://github.com/Mouhamed-king/
as part of the CS50P-Introduction to programming with Python course