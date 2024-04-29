# -*- coding: utf-8 -*-
import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from lib.tool import catch_exception


class BaseAppium:
    def __init__(self, deviceName, appPackage, appActivity, platformVersion, host, port):
        # appium服务监听地址
        server = f'http://{host}:{port}/wd/hub'
        # app启动参数
        desired_caps = {
            "platformName": "Android",
            "platformVersion": platformVersion,
            "deviceName": deviceName,
            "appPackage": appPackage,
            "appActivity": appActivity,
            "skipServerInstallation": True,
            "skipDeviceInitialization": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "noReset": True,
            "newCommandTimeout": 60,
            "automationName": "Uiautomator2",
            # UiAutomator
            "adbExecTimeout": 30000,
            "waitForIdleTimeout": 1000,
            "ignoreUnimportantViews": True,
        }
        self.find_time = 10
        self.driver = webdriver.Remote(server, desired_caps)
        self.wait = WebDriverWait(self.driver, 30)

    @catch_exception
    def wait_driver_by(self, by, driver_):
        data = WebDriverWait(self.driver, self.find_time).until(lambda x: x.find_element(by, driver_))
        return data

    @catch_exception
    def wait_driver_bys(self, by, driver_):
        data = WebDriverWait(self.driver, self.find_time).until(lambda x: x.find_elements(by, driver_))
        return data

    @catch_exception
    def wait_driver_byid(self, driver_):
        data = self.wait_driver_by(By.ID, driver_)
        return data

    @catch_exception
    def wait_driver_byxpath(self, driver_):
        data = self.wait_driver_by(By.XPATH, driver_)
        return data

    @catch_exception
    def wait_driver_byxpathes(self, driver_):
        data = self.wait_driver_bys(By.XPATH, driver_)
        return data

    @catch_exception
    def wait_driver_byname(self, driver_):
        data = self.wait_driver_by(By.NAME, driver_)
        return data

    @catch_exception
    def wait_driver_byclass(self, driver_):
        data = self.wait_driver_by(By.CLASS_NAME, driver_)
        return data

    @catch_exception
    def wait_driver_byclasses(self, driver_):
        data = self.wait_driver_bys(By.CLASS_NAME, driver_)
        return data

    @catch_exception
    def wait_driver_byids(self, driver_):
        data = self.wait_driver_bys(By.ID, driver_)
        return data

    @catch_exception
    def driver_byclass(self, driver_):
        data = self.driver.find_element(By.CLASS_NAME, driver_)
        return data

    @catch_exception
    def driver_byid(self, driver_):
        data = self.driver.find_element(By.ID, driver_)
        return data

    @catch_exception
    def driver_byname(self, driver_):
        data = self.driver.find_element(By.NAME, driver_)
        return data

    @catch_exception
    def driver_byxpath(self, driver_):
        data = self.driver.find_element(By.XPATH, driver_)
        return data

    @catch_exception
    def driver_bytext(self, text):
        data = self.driver.find_element_by_android_uiautomator(f'new UiSelector().text("{text}")')
        return data

    # 获得机器屏幕大小x,y
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 屏幕向上滑动
    def swipeUp(self, t):
        '''
        :param t: 屏幕滑动时间
        :return:
        '''
        time.sleep(3)
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipeDown(self, t):
        time.sleep(3)
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipLeft(self, t):
        time.sleep(3)
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipRight(self, t):
        time.sleep(3)
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    def close(self):
        self.driver.quit()


class Swipe(object):
    def __init__(self, driver):
        self.driver = driver

    # 获得机器屏幕大小x,y
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 屏幕向上滑动
    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)
