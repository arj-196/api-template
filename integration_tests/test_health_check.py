def test_root(test_app):
    res = test_app.get("/")
    assert res.status_code == 200
