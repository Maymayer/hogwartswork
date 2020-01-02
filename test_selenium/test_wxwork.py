import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# 读取成员列表，并处理成字典列表，每一个成员存储为一个字典members
with open('memberinfo.txt', encoding='UTF-8') as file_object:
    lines = file_object.readlines()
members = []
keys = lines[0].split('\t')
row = 1
row_max = len(lines)
print(row_max)
while row != row_max:
    member_row = lines[row].split('\t')
    i = 0
    member = {}
    for key in keys:
        member.update({key: member_row[i]})
        i += 1
    # print(member)
    members.append(member)
    row += 1
# print(members)


class TestWxwork:

    def setup_method(self):
        options = webdriver.ChromeOptions()
        # 先启动一个带命令行参数--remote-debugging-port=9222的浏览器且登陆到企业微信即可使用以下方法
        options.debugger_address = "127.0.0.1:9222"

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(5)

    @pytest.mark.parametrize('member', members)
    def test_add_member_param(self, member):

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1) '
                                                  '.index_service_cnt_item_title').click()
        # 开始输入员工信息
        self.driver.find_element(By.ID, "username").send_keys(member['username'])
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys(member['english_name'])
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(member['acctid'])
        # 性别选择，默认选中男性，所以只有性别女需要操作
        if member['sex'] == '女':
            self.driver.find_element(By.CSS_SELECTOR, "").click()

        # 联系方式
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(member['phone'])
        self.driver.find_element(By.ID, "memberAdd_telephone").send_keys(member['telephone'])
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys(member['mail'])
        self.driver.find_element(By.ID, "memberEdit_address").send_keys(member['address'])

        # 部门选择
        if member['Group'] == '后勤部':
            self.driver.find_element(By.CSS_SELECTOR,
                                     '[class="member_mainParty_popPanel member_mainParty_popPanel_Float"]').click()
        elif member['Group'] == '生产部':
            self.driver.find_element(By.CSS_SELECTOR,
                                     '[class="member_mainParty_popPanel member_mainParty_popPanel_Float"]').click()
        self.driver.find_element(By.ID, "memberAdd_title").send_keys(member['title'])
        # 只有上级需要点击选择
        if member['position'] == '上级':
            self.driver.find_element(By.CSS_SELECTOR, "").click()

        # 对外信息
        # 只有非同步需要点击选择，并输入
        if member['extern_position'] != '同步':
            self.driver.find_element(By.CSS_SELECTOR, "").click()
            self.driver.find_element(By.CSS_SELECTOR, "").send_keys(member['extern_position'])
        # 是否发送邀请,只有否需要点击取消选择
        if member['auto_send_invite'] == '否':
            self.driver.find_element(By.CSS_SELECTOR, "").click()
        # 保存方式：保存并继续添加
        self.driver.find_element(By.CSS_SELECTOR, '[class="qui_btn ww_btn ww_btn_Blue js_btn_continue'
                                                  '.member_colRight_operationBar:nth-child(3) > .ww_btn_Blue"]').click()

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1) '
                                                  '.index_service_cnt_item_title').click()
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.save_screenshot("1.png")

        # 开始输入员工信息
        self.driver.find_element(By.ID, "username").send_keys("abc")
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("abc")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("12345")
        # 性别选择
        self.driver.find_element(By.CSS_SELECTOR, "").send_keys(1)
        # 联系方式
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("15812341234")
        self.driver.find_element(By.ID, "memberAdd_telephone").send_keys("0000000")
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys("aa@bb.com")
        self.driver.find_element(By.ID, "memberEdit_address").send_keys("朝阳大街A座111号")
        # 部门选择
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[class="member_mainParty_popPanel member_mainParty_popPanel_Float"]').click()
        self.driver.find_element(By.ID, "memberAdd_title").send_keys("经理")
        self.driver.find_element(By.CSS_SELECTOR, "").click()
        # 对外信息
        self.driver.find_element(By.CSS_SELECTOR, "").click()
        # 是否发送邀请
        self.driver.find_element(By.CSS_SELECTOR, "").click()
        # 保存方式：保存并继续添加
        self.driver.find_element(By.CSS_SELECTOR, '[class="qui_btn ww_btn ww_btn_Blue js_btn_continue'
                                                  '.member_colRight_operationBar:nth-child(3) > .ww_btn_Blue"]').click()

