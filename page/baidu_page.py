from common.handlebase import HandleBase
from loctor.baidu_loctor import BaiDuLoctor as bdl


class BaiDuPage(HandleBase):

    def input_text(self):
        ele = self.wait_element(loctor=bdl.input_box, timeout=20, module='baidu_input_text')
        ele.send_keys('测试')
        return self.get_current_url