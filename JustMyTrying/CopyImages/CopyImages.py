import os
import shutil
import keyboard as key
import time as tm


# from PIL import Image

def exi_t(farewell="Goodbye"):  # Exiting the program
    print('\n' + farewell)
    exit()


def main(start_dir):  # The main algorithm of the program
    if not os.path.exists(start_dir):  # No directory entered
        print("There is no such way!")
        exi_t('We are very sorry that we could not help you. Goodbye.')  # exit

    print("Current directory(startup):", os.getcwd())
    os.chdir(start_dir)
    print("Current directory(new):", os.getcwd())

    if not os.path.exists("new_folder_for_files"):  # Creating a folder for copying files
        os.mkdir("new_folder_for_files")

    # print("All folders and files:", os.listdir())
    new_loc_folder = start_dir + r'\new_folder_for_files'

    for file in os.listdir():
        # print(file, type(file), file[-3:])
        if file[-3:].lower() in ['jpg', 'png']:
            os.startfile(file)  # don't know how that close
            # img = Image.open(file)
            # img.show()
            while True:
                if key.is_pressed('Ctrl'):
                    tm.sleep(0.15)
                    break
                if key.is_pressed('Q'):
                    shutil.copyfile(start_dir + start_dir[2] + file, new_loc_folder + start_dir[2] + file)
                    tm.sleep(0.15)
                if key.is_pressed('Esc'):
                    exi_t()
    exi_t()


if __name__ == "__main__":
    greeting = '''
    A program for copying the viewed images. Click for:
    Ctrl - next file;
    Q - copy a file to a folder;
    Esc - for early exit;
    Enjoy using it!
    '''
    print(greeting)
    start_dir = input('Start_dir: ')
    main(start_dir)
