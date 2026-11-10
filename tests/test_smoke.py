def test_core_import():
    import core

def test_api_import():
    from api.main import app
    assert app is not None