from . import exportFix
import argparse

def main(filepath):
    exportFix.fix_file(filepath)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update mod exported into BeamNG Drive from Automation for turbo overheating bug.')
    parser.add_argument(dest='filepath', help='Filepath to operate on', metavar='FILE')
    args = parser.parse_args()
    main(args.filepath)
