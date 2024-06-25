import pytest
from gendiff import generate_diff
import json

@pytest.fixture
def paths():
    paths = {
        "json1": "tests/fixtures/file1.json",
        "json2": "tests/fixtures/file2.json",
        "yml1": "tests/fixtures/file1.yml",
        "yml2": "tests/fixtures/file2.yml",
        "tree_json1": "tests/fixtures/file_tree1.json",
        "tree_json2": "tests/fixtures/file_tree2.json",
        "tree_yml1": "tests/fixtures/file_tree1.yml",
        "tree_yml2": "tests/fixtures/file_tree2.yml",
    }
    return paths


@pytest.fixture
def format_name():
    format_name = {
        "stylish": "stylish",
        "plain": "plain",
        "json": "json",
    }
    return format_name

def read_file_content(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def test_generate_diff(paths, format_name):
    result_diff_json = generate_diff(
        paths["json1"],
        paths["json2"],
        format_name["stylish"],
    )
    result_diff_yml = generate_diff(
        paths["yml1"],
        paths["yml2"],
        format_name["stylish"],
    )
    result_diff_json_tree = generate_diff(
        paths["tree_json1"],
        paths["tree_json2"],
        format_name["stylish"],
    )
    result_diff_yml_tree = generate_diff(
        paths["tree_yml1"],
        paths["tree_yml2"],
        format_name["stylish"],
    )
    result_diff_json_tree_stat = generate_diff(
        paths["tree_json1"],
        paths["tree_json2"],
        format_name["plain"],
    )
    result_diff_yml_tree_stat = generate_diff(
        paths["tree_yml1"],
        paths["tree_yml2"],
        format_name["plain"],
    )
    result_diff_json_view = generate_diff(
        paths["tree_json1"],
        paths["tree_json2"],
        format_name["json"],
    )

    assert result_diff_json == read_file_content('tests/fixtures/stylish_plain')
    assert result_diff_yml == read_file_content('tests/fixtures/stylish_plain')

    #assert result_diff_json_tree == read_file_content('tests/fixtures/stylish')
    #assert result_diff_yml_tree == read_file_content('tests/fixtures/stylish')

    assert result_diff_json_tree_stat == read_file_content('tests/fixtures/plain')
    assert result_diff_yml_tree_stat == read_file_content('tests/fixtures/plain')
    assert result_diff_json_view == read_file_content('tests//fixtures/json')
