# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {"platformName": "android",
        "deviceName": "hogwarts",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias"}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(60)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("alibaba")
# el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget
# .LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget
# .LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx
# .recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]") el4.click()

driver.quit()
