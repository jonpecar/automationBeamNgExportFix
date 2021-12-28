from genericpath import isfile
from os import path, getenv, stat, listdir


BEAMNG_VER = '0.24'
BEAMNG_USER_PATH = path.join(getenv('LOCALAPPDATA'), 'BeamNG.drive', BEAMNG_VER, 'mods')

def get_files_sorted():
    files = []
    for file in listdir(BEAMNG_USER_PATH):
        file_path = path.join(BEAMNG_USER_PATH, file)
        if isfile(file_path):
            file_name, ext = path.splitext(file_path)
            if ext.lower() == '.zip':
                files.append(file_path)
    
    sorted_files = sorted(files, key=lambda t: -stat(t).st_mtime)
    return sorted_files