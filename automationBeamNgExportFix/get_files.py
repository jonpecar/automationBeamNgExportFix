from genericpath import isfile
from os import path, getenv, stat, listdir


BEAMNG_USER_DIR_NAME = 'BeamNG.drive'
BEAMNG_USER_MOD_DIR_NAME = 'mods'

def get_latest_ver():
    beam_ng_dir = path.join(getenv('LOCALAPPDATA'), BEAMNG_USER_DIR_NAME)
    if not path.isdir(beam_ng_dir):
        raise Exception(f'Could not find BeamNG.Drive directory at: {beam_ng_dir}')
    dirs = [d for d in listdir(beam_ng_dir) if path.isdir(path.join(beam_ng_dir, d))]
    vers = {}
    for dir in dirs:
        try:
            vers[float(dir)] = dir
        except ValueError as ex:
            pass #Non-number folder, don't care
    if not vers:
        raise Exception(f'Could not determine latest version')
    ver_key = max(vers.keys())
    return vers[ver_key]


def get_user_mod_dir(ver: str):
    return path.join(getenv('LOCALAPPDATA'), BEAMNG_USER_DIR_NAME, ver, BEAMNG_USER_MOD_DIR_NAME)

def get_files_sorted(ver: str):
    if not ver:
        ver = get_latest_ver()
    user_dir = get_user_mod_dir(ver)
    files = []
    for file in listdir(user_dir):
        file_path = path.join(user_dir, file)
        if isfile(file_path):
            _, ext = path.splitext(file_path)
            if ext.lower() == '.zip':
                files.append(file_path)
    
    sorted_files = sorted(files, key=lambda t: -stat(t).st_mtime)
    return sorted_files