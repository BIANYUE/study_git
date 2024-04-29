# -*- coding: utf-8 -*-
import time

from click.base_appnium import BaseAppium


# com.hidecat.mine
class ComHidecatMine(BaseAppium):
    def __init__(self, deviceName, appPackage, appActivity, platformVersion, host, port):
        super(ComHidecatMine, self).__init__(deviceName, appPackage, appActivity, platformVersion, host, port)
        self.t = 900

    def main(self):
        # 选择UDP
        self.wait_driver_byid("com.hidecat.mine:id/rb_speed_mode").click()
        # while 1:
        # 打开列表页
        self.wait_driver_byid("com.hidecat.mine:id/cl_line").click()
        for page in range(5):
            self.start(page)

        self.close()

    def start(self, page):
        for i in range(page):
            self.swipeUp(self.t)
        ip_list = self.wait_driver_byids("com.hidecat.mine:id/iv_dbm")
        print(ip_list)
        print(self.driver.page_source)
        for ip_button in ip_list:
            print(ip_button)
            # 选择路线
            self.wait_driver_byids("com.hidecat.mine:id/iv_dbm")[ip_list.index(ip_button)].click()
            if not self.ifsuccess():
                continue
            self.wait_driver_byid("com.hidecat.mine:id/cl_line").click()
            for i in range(page):
                self.swipeUp(self.t)

    def ifsuccess(self):
        time.sleep(5)

        qr = self.driver_byxpath("//android.widget.Button[@text='確認']")
        if qr:
            time.sleep(3)
            qr.click()

        if not self.wait_driver_byid("com.hidecat.mine:id/status_tv"):
            return
        else:
            return True


if __name__ == '__main__':
    deviceName = "HT69H0206647"
    appPackage = "com.hidecat.mine"
    appActivity = "com.lightningcn.mine.activity.SplashPageActivity"
    platformVersion = "8.1.0"
    host = "127.0.0.1"
    port = "4723"
    cpa = ComHidecatMine(deviceName, appPackage, appActivity, platformVersion, host, port)
    cpa.main()
