import requests

def get():
    response = requests.get('https://thanhluu.azurewebsites.net/')
    return response

def post():
    json = { "CHAS":{"0":0},"RM":{"0":6.575},"TAX":{"0":296.0},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98} }
    response = requests.post('https://thanhluu.azurewebsites.net/predict', json=json)
    return response

def test_get():
    assert f"{get()}" == "<Response [200]>"

def test_post():
    assert f"{post()}" == "<Response [200]>"