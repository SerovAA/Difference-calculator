import pytest
from gendiff import generate_diff
from tests.fixtures.test_results import RESULT_PLAIN, RESULT_DIFF


@pytest.fixture
def paths():
    paths = {
        "json1": "tests/fixtures/file1.json",
        "json2": "tests/fixtures/file2.json",
        "yml1": "tests/fixtures/file1.yml",
        "yml2": "tests/fixtures/file2.yml",
        "path_json1": "tests/fixtures/filepath1.json",
        "path_json2": "tests/fixtures/filepath2.json",
        "path_yml1": "tests/fixtures/filepath1.yml",
        "path_yml2": "tests/fixtures/filepath2.yml",
    }
    return paths


def test_generate_diff(paths):
    result_diff_json = str(generate_diff(paths["json1"], paths["json2"]))
    result_diff_yml = str(generate_diff(paths["yml1"], paths["yml2"]))
    result_diff_json_tree = str(generate_diff(paths["path_json1"],
                                              paths["path_json2"]))
    result_diff_yml_tree = str(generate_diff(paths["path_yml1"],
                                             paths["path_yml2"]))
    assert result_diff_json == RESULT_PLAIN
    assert result_diff_yml == RESULT_PLAIN
    assert result_diff_json_tree == RESULT_DIFF
    assert result_diff_yml_tree == RESULT_DIFF
