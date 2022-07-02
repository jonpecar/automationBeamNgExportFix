from io import BytesIO
import zipfile
from os import path
from typing import List

TARGET_LINES = [br'"cylinderWallTemperatureDamageThreshold"',
                br'"damageThresholdTemperature"',
                br'"headGasketDamageThreshold"',
                br'"pistonRingDamageThreshold"',
                br'"connectingRodDamageThreshold"']

NEW_VALUE_STRING = b'99999999'

def get_target_file_path(zip_file_path : str):
    dir, file_name = path.split(zip_file_path)
    file_name_no_ext, ext = path.splitext(file_name)

    return '/'.join(('vehicles',  file_name_no_ext,  'camso_engine.jbeam')) #Do this manually (not using path.join()) as this always uses unix separators

def update_line(line : bytes):
    for target_line in TARGET_LINES:
        if target_line in line:
            start_pos = line.find(b':')
            end_pos = line.find(b',')
            new_line = line[:start_pos + 1] + NEW_VALUE_STRING + line[end_pos:]
            return new_line
    
    return line


def fix_file(zip_file_path : str):

    target_file = get_target_file_path(zip_file_path)
    output_object = BytesIO()

    with zipfile.ZipFile(zip_file_path) as inzip, zipfile.ZipFile(output_object, 'w') as outzip:
        for inzipinfo in inzip.infolist():
            with inzip.open(inzipinfo) as infile:
                if inzipinfo.filename == target_file:
                    in_content = infile.readlines()
                    for i in range(len(in_content)):
                        in_content[i] = update_line(in_content[i])
                    out_content = bytes()
                    for line in in_content:
                        out_content += line
                    outzip.writestr(inzipinfo, out_content)
                else:
                    outzip.writestr(inzipinfo, infile.read())

    with open(zip_file_path, 'wb') as f:
        output_object.seek(0)
        f.write(output_object.read())