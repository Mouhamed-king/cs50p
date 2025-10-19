import yt_dlp
import os
import re
from sys import exit

DIR_BASE="downloads"
DIR_VID=os.path.join(DIR_BASE, "video")
DIR_AUD=os.path.join(DIR_BASE, "audio")
os.makedirs(DIR_VID, exist_ok=True)
os.makedirs(DIR_AUD, exist_ok=True)

def CHOICE_QUAL_VID():
    print("\n Choose the qualite of video :")
    print("1- best")
    print("2- 720p max")
    print("3- 480p max")
    choice=input("Option (1/2/3) :").strip()
    if choice=="2":
        return "bestvideo[height<=720]+bestaudio/best[height<=720]"
    elif choice=="3":
        return "bestvideo[height<=480]+bestaudio/best[height<=480]"
    return "bestvideo+bestaudio/best"


def CHOICE_QUAL_AUD():
    print("\n Choose the quality audio :")
    print("1- best")
    print("2- medium")
    choice=input("Option (1/2) :").strip()
    if choice=="2":
        return "bestaudio[abr<=128]/worstaudio"
    return "bestaudio/best"


def DOWNLOAD_VID(url):
    format_video=CHOICE_QUAL_VID()
    print("downloading...")
    ydl_opts={
        "format": format_video,
        "merge_output_format":"mp4",
        "noplaylist":True,
        "cookiefile":"cookies.txt",
        "outtmpl": os.path.join(DIR_VID,"%(title)s.%(ext)s"),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(f"Video saved on {DIR_VID}")


def DOWNLOAD_AUD(url):
    format_audio=CHOICE_QUAL_AUD()
    print("downloading...")
    ydl_opts={
        "format": format_audio,
        "outtmpl": os.path.join(DIR_AUD,"%(title)s.%(ext)s"),
        "postprocessors":[
            {"key":"FFmpegExtractAudio", "preferredcodec":"mp3","Preferredquality":"192"}
        ]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(f"audio saved on {DIR_AUD}")

def VALID_VID_URL(url):
    try:
        pattern_url=re.compile(r'^(https?:\/\/)?'
                               r'([\w.-]+)\.'
                               r'([a-z]{2,})'
                               r'(\/[\w\-._~:/?#[\]@!$&\'()*+,;=%]*)?$'
                                )
        return bool(re.match(pattern_url, url))
    except Exception:
        return False

def main():
    while True:
        print("~welcome to downloader 😀~")
        print("1. Download Video")
        print("2. Download audio")
        print("3. Exit")
        choice=input("Choix (1/2/3) :").strip()
        match choice:
            case "1":
                url=input("URL of the video :")
                if VALID_VID_URL(url):
                    try:
                        DOWNLOAD_VID(url)
                    except Exception:
                        exit()
                else:
                    exit("Invalid URL")
            case "2":
                url=input("URL of the video :")
                if VALID_VID_URL(url):
                    try:
                        DOWNLOAD_AUD(url)
                    except Exception:
                        exit()
                else:
                    exit("Invalid URL")
            case "3":
                print("Bye Bye !")
                break
            case _:
                print("Invalid choice, try again (1/2/3)")

if __name__=="__main__":
    main()

