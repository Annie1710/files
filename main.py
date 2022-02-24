__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil
from zipfile import ZipFile


def clean_cache():
    cwd = os.getcwd()
    print(cwd)
    if os.path.exists('cache'):
        shutil.rmtree("cache")
    os.mkdir('cache')


def cache_zip(zip_file_path, cache_dir_path):  # (source, target)
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)


def cached_files():
    cwd = os.getcwd()
    ab_path = os.path.abspath(cwd)
    path = os.path.join(ab_path, "cache")
    dir_list = []
    for file in os.listdir(path):
        dir_list = dir_list + [os.path.join(path, file)]
    return dir_list


def find_password(dir_list):
    for file in dir_list:
        content = open(file)
        string = content.read()
        if 'password' in string:
            index = string.find('password')
            l_word = len("password")
            password = string[index+l_word+2:index+38]
            print(string[index+l_word+2:index+38])
            return password


if __name__ == "__main__":
    clean_cache()
    cache_zip("./data.zip", "./cache")
    cached_files()
    dir_list = cached_files()
    find_password(dir_list)
