from model import get_user_data

def test_user_structure():
    a = 1
    data = get_user_data()
    assert data == {"id": 1, "name": "Cristopher"}
    assert isinstance(data, dict)