import os
import pytest
from gendiff import generate_diff


@pytest.fixture
def paths():
    fixtures_dir = "tests/fixtures"
    return {
        "json1": os.path.join(fixtures_dir, "file1.json"),
        "json2": os.path.join(fixtures_dir, "file2.json"),
        "yml1": os.path.join(fixtures_dir, "file1.yml"),
        "yml2": os.path.join(fixtures_dir, "file2.yml"),
        "tree_json1": os.path.join(fixtures_dir, "file_tree1.json"),
        "tree_json2": os.path.join(fixtures_dir, "file_tree2.json"),
        "tree_yml1": os.path.join(fixtures_dir, "file_tree1.yml"),
        "tree_yml2": os.path.join(fixtures_dir, "file_tree2.yml"),
    }


def read_file_content(filepath):
    with open(filepath, 'r') as file:
        return file.read()


@pytest.mark.parametrize("file1_key, file2_key, format_name, expected_file", [
    ("json1", "json2", "stylish", "stylish_plain"),
    ("yml1", "yml2", "stylish", "stylish_plain"),
    ("tree_json1", "tree_json2", "stylish", "stylish"),
    ("tree_yml1", "tree_yml2", "stylish", "stylish"),
    ("tree_json1", "tree_json2", "plain", "plain"),
    ("tree_yml1", "tree_yml2", "plain", "plain"),
    ("tree_json1", "tree_json2", "json", "json")
])
def test_generate_diff(file1_key, file2_key, format_name, expected_file, paths):
    file1_path = paths[file1_key]
    file2_path = paths[file2_key]
    expected_file_path = os.path.join('tests/fixtures', expected_file)

    result = generate_diff(file1_path, file2_path, format_name)
    expected_output = read_file_content(expected_file_path)

    assert result == expected_output
