import pytest

from baidu.page.baidu_search import Baidu_Search


class Test_Bds():

    def setup_class(self):
        self.obj = Baidu_Search()

    def test_case_1(self):
        self.obj.search()

    def teardown_class(self):
        self.obj.dev.quit()

if __name__ == '__main__':
    pytest.main(['-s'])