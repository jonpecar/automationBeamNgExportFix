from . import exportFix, get_files
import argparse
import os

def check_file(file):
    if not os.access(file, os.W_OK):
        parser.error('File could not be accessed. Make sure file exists and can be modified')
    else:
        return file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update mod exported into BeamNG Drive from Automation for turbo overheating bug. Can be done either automatically on a set number of most recent files or on a specified file path')
    parser.add_argument('-f', dest='filepath', help='Filepath to operate on', metavar='FILE', type=check_file)
    parser.add_argument('-a', dest='auto_count', help='Automatically operate on latest files in BeamNG mods folder', metavar='N', type=int)
    args = parser.parse_args()
    if not(args.filepath or args.auto_count):
        parser.error('Must select at least one option')
    if args.filepath:
        exportFix.fix_file(args.filepath)
    if args.auto_count:
        for file in get_files.get_files_sorted()[:args.auto_count]:
            exportFix.fix_file(file)
        
