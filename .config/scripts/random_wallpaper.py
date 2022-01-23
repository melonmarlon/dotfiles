import os
import random
import time

def main():
    files = os.listdir("/home/marlon/.config/wallpapers/")
    files = random.sample(files, len(files))
    i = len(files) - 1
    while len(files) > 0:
        change_wallpaper("/home/marlon/.config/wallpapers/{}".format(files[i]))
        i -= 1
        time.sleep(120)

def change_wallpaper(file):
    os.system("feh --bg-scale {}".format(file))

if __name__ == "__main__":
    main()
