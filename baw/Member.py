'''
业务AW：按模块划分
business action word
'''
REGISTER = "futureloan/mvc/api/member/register"
LOGIN = "futureloan/mvc/api/member/login"

from JinRongZongHe.caw.BaseRequests import BaseRequests

class Member:
    def register(self,url,base_requests,data):
        '''
        用户注册的接口
        :param url: 环境信息 http://host:port/
        :param base_requests:
        :param data: 数据
        :return: 响应信息
        '''
        real_url = url + REGISTER
        r = base_requests.post(real_url,data=data)
        return r

    def login(self,url,base_requests,data):
        '''
        用户登录的接口
        :param url:
        :param base_requests:
        :param data:
        :return:
        '''
        real_url = url + LOGIN
        r = base_requests.post(real_url,data=data)
        return r

# 测试代码
if __name__ == '__main__':

    r = Member().register("http://192.168.150.222:8081/",BaseRequests(),{"mobilephone":"19899202343"})
    print(r.text)