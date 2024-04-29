# -*- coding: utf-8 -*-
import time

from click.base_appnium import BaseAppium


# org.redguest
class ComKeynoteFreeAndroid(BaseAppium):
    def __init__(self, deviceName, appPackage, appActivity, platformVersion, host, port):
        super(ComKeynoteFreeAndroid, self).__init__(deviceName, appPackage, appActivity, platformVersion, host, port)
        self.t = 800

    def main(self):
        time.sleep(20)
        self.click()
        time.sleep(10)
        self.close()

    def click(self):
        self.click_list()

    def click_list(self):
        self.wait_driver_byid("com.keynote.free.android:id/icon_arrow").click()
        # 查询第一层列表页
        list1 = self.wait_driver_byids("com.keynote.free.android:id/item_vpn")[1:]
        for ip in list1:
            # self.wait_driver_byids("com.keynote.free.android:id/item_vpn")[list1.index(ip)].click()
            ip.click()
            if self.if_sucess():
                self.wait_driver_byid("com.keynote.free.android:id/icon_arrow").click()

    def if_sucess(self):
        if self.wait_driver_byid("com.keynote.free.android:id/ic_state"):
            self.wait_driver_byid("com.keynote.free.android:id/vpn_menu").click()
            return 1


if __name__ == '__main__':
    deviceName = "HT7270202673"
    appPackage = "com.keynote.free.android"
    appActivity = ".main.activity.MainActivity"
    platformVersion = "8.1.0"
    host = "127.0.0.1"
    port = "4723"
    or_ = ComKeynoteFreeAndroid(deviceName, appPackage, appActivity, platformVersion, host, port)
    or_.main()
