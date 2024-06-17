import os
import json
import yaml


def parser(file_path1, file_path2):
    file1_ext = os.path.splitext(file_path1)[1]
    file2_ext = os.path.splitext(file_path2)[1]

    if file1_ext == '.json' and file2_ext == '.json':
        with open(file_path1) as f1, open(file_path2) as f2:
            first_file = json.load(f1)
            second_file = json.load(f2)
    elif file1_ext in ['.yaml', '.yml'] and file2_ext in ['.yaml', '.yml']:
        with open(file_path1) as f1, open(file_path2) as f2:
            first_file = yaml.safe_load(f1)
            second_file = yaml.safe_load(f2)
    else:
        raise ValueError("Unsupported file formats")

    return first_file, second_file
