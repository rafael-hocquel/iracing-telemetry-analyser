def test_core_import():
    import core

def test_app_import():
    from api.main import app

def test_api_import():
    from api.main import app
    assert app is not None