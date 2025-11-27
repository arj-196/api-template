from uuid import uuid4

from common.settings import get_settings


def test_create_and_delete_dataset(test_app):
    dataset_name = f"test_dataset_{uuid4()}"
    res = test_app.get(
        "/dataset",
        headers={
            "Authorization": f"Bearer {get_settings().api_key.get_secret_value()}"
        },
        params={"name": dataset_name},
    )
    assert res.status_code == 404, "dataset should not exist"

    # create
    res = test_app.post(
        "/dataset",
        headers={
            "Authorization": f"Bearer {get_settings().api_key.get_secret_value()}"
        },
        json={
            "name": dataset_name,
            "description": "test description",
            "meta": {"key": "value"},
        },
    )
    assert res.status_code == 200, "dataset should be created"

    # find again
    res = test_app.get(
        "/dataset",
        headers={
            "Authorization": f"Bearer {get_settings().api_key.get_secret_value()}"
        },
        params={"name": dataset_name},
    )
    assert res.status_code == 200, "dataset should now exist"

    # delete
    res = test_app.delete(
        "/dataset",
        headers={
            "Authorization": f"Bearer {get_settings().api_key.get_secret_value()}"
        },
        params={"name": dataset_name},
    )
    assert res.status_code == 200, "dataset should be deleted"

    # find again
    res = test_app.get(
        "/dataset",
        headers={
            "Authorization": f"Bearer {get_settings().api_key.get_secret_value()}"
        },
        params={"name": dataset_name},
    )
    assert res.status_code == 404, "dataset should not exist"
    return
