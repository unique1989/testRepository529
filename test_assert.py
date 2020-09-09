import sys
sys.path.append(".")
import requests
import pytest
import is_leap_year
class TestAssert():
    # 1.直接assert断言
    def test_assert(self):
        r = requests.get("http://www.baidu.com")
        assert r.status_code == 100, "返回200说明访问成功"

    # 2.直接用pytest.raises()处理异常
    # 对一个判断是否是闰年的方法进行测试
    def test_exception_typeerror(self):
        with pytest.raises(TypeError):
            is_leap_year.is_leap_year("ss")

    def test_true(self):
        assert is_leap_year.is_leap_year(400) == True
        assert is_leap_year.is_leap_year(300) == False

    # 将异常信息存储到一个变量中，变量的类型则为异常类，包含异常的type、value和traceback等信息
    def test_exception_value(self):
        with pytest.raises(ValueError) as excinfo:
            is_leap_year.is_leap_year(0)
        assert "从公元一年开始" in str(excinfo.value)
        assert excinfo.type == ValueError

    # 可以在用例中定义抛出的异常信息是否与预期的异常信息匹配，若不匹配则用例执行失败
    def test_exception_match(self):
        with pytest.raises(ValueError, match=r'公元33元年是从公元一年开始') as excinfo:
            is_leap_year.is_leap_year(0)
        assert excinfo.type == ValueError

    @pytest.mark.xfail(raises=ValueError)
    def test_a(self):
        is_leap_year.is_leap_year(-100)
