import json
import pytest
from Models.Model import Model


@pytest.fixture
def model():
    return Model()


def test_get_new_id_existing_file(model, tmp_path):

    data = [{'id': 1, 'name': 'test1'}, {'id': 2, 'name': 'test2'}]
    file_path = tmp_path / 'data.json'
    with open(file_path, 'w') as file:
        json.dump(data, file)

    new_id = model.get_new_id(file_path)

    assert new_id == 3


def test_get_new_id_non_existing_file(model, tmp_path):

    file_path = tmp_path / 'non_existing_file.json'
    new_id = model.get_new_id(file_path)

    assert new_id == 1
