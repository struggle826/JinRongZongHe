import pytest

from JinRongZongHe.caw.DataRead import DataRead
from JinRongZongHe.caw.Assert import Assert
from JinRongZongHe.baw.Member import Member
from JinRongZongHe.baw.DbOp import DbOp

# @pytest.fixture(params=DataRead().read_yaml(r"data_case/login_setup.yaml"))
# def setup_data(request):
#     return request.param

@pytest.fixture(params=DataRead().read_yaml(r"data_case/login_data.yaml"))
def login_data(request):
    return request.param


# 登录的测试逻辑
def test_login(url,base_requests,register,login_data):
    r = Member().login(url, base_requests,login_data['data'])
    Assert().equal(login_data['expect'],r.json(),"msg,status,code")

