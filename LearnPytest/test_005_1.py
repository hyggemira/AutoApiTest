import pytest
import requests



@pytest.fixture(params=[
    {"casedata": {"mobilephone": '131123456789', "pwd": 123456, "regname": "小丸子"},
     "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}},
    {"casedata": {"mobilephone": 13112345611, "pwd": 1234, "regname": "小丸子"},
     "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
    {"casedata": {"mobilephone": 13112345672, "pwd": None, "regname": "koko"},
     "expect": {"status": 0, "code": "20103", "data": None, "msg": "密码不能为空"}},
    {"casedata": {"mobilephone": 15112345675, "pwd": 123456, "regname": "helloccc"},
     "expect": {"status": 0, "code": "10001", "data": None, "msg": "注册成功"}}])

def data(request):
    return request.param

def test_register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data["casedata"])
    # return r
    assert r.json() == data["expect"]
    # print(f"使用手机号{data['casedata']}测试注册功能，预期结果是{data['expect']}")





