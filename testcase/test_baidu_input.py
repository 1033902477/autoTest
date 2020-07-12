import pytest, inspect
from common.logger import logger


@pytest.mark.usefixtures('init')
class TestBaiDu():

    def test_input_text(self, init):
        logger.info("%s正在执行测试用例" % (inspect.stack()[0][3]))
        try:
            url = init.baidu.input_text()
            assert 'www.baidu.com' in url
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_baidu_input.py'])