import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r', encoding='utf-8') as file1:
        data1 = json.load(file1)

    with open(file_path2, 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = []

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff_lines.append(f"  {key}: {data1[key]}")
            else:
                diff_lines.append(f"- {key}: {data1[key]}")
                diff_lines.append(f"+ {key}: {data2[key]}")
        elif key in data1:
            diff_lines.append(f"- {key}: {data1[key]}")
        elif key in data2:
            diff_lines.append(f"+ {key}: {data2[key]}")

    return "{{\n{0}\n}}".format("\n".join(diff_lines))
