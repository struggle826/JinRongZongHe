'''
登录接口的脚本
'''

import pytest

from JinRongZongHe.caw.DataRead import DataRead
from JinRongZongHe.caw.Assert import Assert
from JinRongZongHe.baw.Member import Member
from JinRongZongHe.baw.DbOp import DbOp

@pytest.fixture(params=DataRead().read_yaml(r"data_case/login_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead().read_yaml(r"data_case/login_success.yaml"))
def success_data(request):
    return request.param

# 登录失败的逻辑
def test_login_fail(fail_data,url,base_requests):
    print(f"执行登录失败的用例，测试数据为:{fail_data}")
    r = Member().login(url,base_requests,fail_data['data'])
    print(r.text)
    Assert().equal(fail_data['expect'],r.json(),"msg,status,code")

# 登录成功的逻辑
def test_login_success(success_data,url,base_requests):
    print(f"执行登录成功的用例，测试数据为:{success_data}")
    r = Member().login(url,base_requests,success_data['data'])
    print(r.text)
    Assert().equal(success_data['expect'],r.json(),"msg,status,code")







