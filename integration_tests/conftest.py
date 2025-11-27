from uuid import uuid4

import pytest
from starlette.testclient import TestClient

from api.app import app
from common.settings import get_settings
from service.dataset.models import Dataset


@pytest.fixture(scope="session")
def test_app() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="function")
def test_dataset(test_app) -> Dataset:
    dataset_name = f"test_dataset_{uuid4()}"
    # create dataset
    res = test_app.post(
        "/dataset",
        headers={
            "Authorization": f"Bearer {get_settings().api_key.get_secret_value()}"
        },
        json={"name": dataset_name},
    )
    assert res.status_code == 200, "dataset should be created"

    # get dataset
    res = test_app.get(
        "/dataset",
        headers={
            "Authorization": f"Bearer {get_settings().api_key.get_secret_value()}"
        },
        params={"name": dataset_name},
    )
    assert res.status_code == 200, "dataset should exist"
    dataset = Dataset(**res.json())
    yield dataset
    # delete
    res = test_app.delete(
        "/dataset",
        headers={
            "Authorization": f"Bearer {get_settings().api_key.get_secret_value()}"
        },
        params={"name": dataset_name},
    )
    assert res.status_code == 200, "dataset should be deleted"
    return
