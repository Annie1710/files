__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil
from zipfile import ZipFile
import re


def clean_cache():
    cwd = os. getcwd()
    if os.path.exists('cache'):
        shutil.rmtree("cache")
    os.mkdir('cache')


def cache_zip(zip_file_path, cache_dir_path):  # (source, target)
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)


def cached_files():
    path = "f:\\WINC\\Opdrachten DAWP\\files\\cache"
    dir_list = os.listdir(path)
    print(dir_list)
    return dir_list


dir_list = cached_files()


def find_password(dir_list):
    for file in dir_list:
        with open(file):
            if "password" in open(file).read():
                text = file.read()
                x = text.find("password")
                password = text[x:]
            print(password)
            return password
               

if __name__ == "__main__":
    clean_cache()
    cache_zip("./data.zip", "./cache")
    cached_files()
    find_password(dir_list)
