
import pytest

from ZongHe.baw import Member
from ZongHe.caw import DataRead

@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_pass.yaml"))
def pass_data(request):
    return request.param

def test_login_pass(pass_data, url, baserequests):
    print(f"测试数据为: {pass_data['casedata']}")
    print(f"预期结果为: {pass_data['expect']}")

    r = Member.login(url, baserequests, pass_data['casedata'])
    # print(r)
    # 检查结果
    assert str(r.json()['msg']) == str(pass_data['expect']['msg'])
    assert str(r.json()['status']) == str(pass_data['expect']['status'])
    assert str(r.json()['code']) == str(pass_data['expect']['code'])



@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_fail.yaml"))
def fail_data(request):
    return request.param

def test_login_fail(fail_data, url, baserequests):
    print(f"测试数据为: {fail_data['casedata']}")
    print(f"预期结果为: {fail_data['expect']}")

    r = Member.login(url, baserequests, fail_data['casedata'])
    # print(r)
    # 检查结果
    assert str(r.json()['msg']) == str(fail_data['expect']['msg'])
    assert str(r.json()['status']) == str(fail_data['expect']['status'])
    assert str(r.json()['code']) == str(fail_data['expect']['code'])


