from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

i = 0

start_hours_sunday = (7, 8, 12)
start_mins_sunday = (32, 25, 5)
end_hours_sunday = (8, 9, 12)
end_mins_sunday = (21, 16, 56)

start_hours_monday = (7, 9, 10, 11, 12, 13)
start_mins_monday = (30, 20, 15, 10, 5, 0)
end_hours_monday = (8, 10, 11, 12, 12, 13)
end_mins_monday = (21, 11, 6, 1, 56, 51)

start_hours_tuesday = (7, 8, 9, 11)
start_mins_tuesday = (30, 25, 30, 10)
end_hours_tuesday = (8, 9, 11, 12)
end_mins_tuesday = (21, 16, 1, 1)

start_hours_wednesday = (7, 8, 11, 13)
start_mins_wednesday = (30, 25, 10, 0)
end_hours_wednesday = (8, 9, 12, 13)
end_mins_wednesday = (21, 16, 1, 51)

start_hours_thursday = (7, 8, 9, 10, 12)
start_mins_thursday = (30, 25, 20, 15, 5)
end_hours_thursday = (8, 9, 10, 11, 12)
end_mins_thursday = (21, 16, 11, 6, 56)

userid = "F20190200@dubai.bits-pilani.ac.in"
passw = "0b3545a0"

def login_dets(id, pw):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://a.impartus.com/login/#/")
    driver.find_element_by_xpath('/html/body/ui-view/div/div/ui-view/div/div[1]/form/md-input-container[1]/input').send_keys(id)
    driver.find_element_by_xpath('/html/body/ui-view/div/div/ui-view/div/div[1]/form/md-input-container[2]/input').send_keys(pw)
    sleep(5)
    driver.find_element_by_xpath('/html/body/ui-view/div/div/ui-view/div/div[1]/form/div[2]/div/span').click()
    sleep(5)
    original_window = driver.current_window_handle
    assert len(driver.window_handles) == 1
    driver.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[3]/dashboard-interests/div/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button').click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            print(datetime.datetime.now())
            break
    try:
        sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[5]/button[2]').click()
    except:
        driver.find_elements_by_xpath('//*[contains(text(), \'Join\')]')

    if datetime.datetime.today().weekday() == 1:
        sleep_time = (end_hours_tuesday[i]*60 + end_mins_tuesday[i])-(start_hours_tuesday[i]*60 + start_mins_tuesday[i])
        sleep(sleep_time*60)
        driver.quit()

    elif datetime.datetime.today().weekday() == 0:
        sleep_time = (end_hours_monday[i]*60 + end_mins_monday[i])-(start_hours_monday[i]*60 + start_mins_monday[i])
        sleep(sleep_time*60)
        driver.quit()

    elif datetime.datetime.today().weekday() == 2:
        sleep_time = (end_hours_wednesday[i]*60 + end_mins_wednesday[i])-(start_hours_wednesday[i]*60 + start_mins_wednesday[i])
        sleep(sleep_time*60)
        driver.quit()

    elif datetime.datetime.today().weekday() == 3:
        sleep_time = (end_hours_thursday[i]*60 + end_mins_thursday[i])-(start_hours_thursday[i]*60 + start_mins_thursday[i])
        sleep(sleep_time*60)
        driver.quit()

    elif datetime.datetime.today().weekday() == 6:
        sleep_time = (end_hours_sunday[i]*60 + end_mins_sunday[i])-(start_hours_sunday[i]*60 + start_mins_sunday[i])
        sleep(sleep_time*60)
        driver.quit()


x = True

while x:
    if datetime.datetime.today().weekday() == 1:
        if (datetime.datetime.now().time().hour == start_hours_tuesday[i]) and (datetime.datetime.now().time().minute == start_mins_tuesday[i]):
            login_dets(userid, passw)
            i += 1
            if i == 4:
                x = False
                exit(0)

    elif datetime.datetime.today().weekday() == 0:
        if (datetime.datetime.now().time().hour == start_hours_monday[i]) and (datetime.datetime.now().time().minute == start_mins_monday[i]):
            login_dets(userid, passw)
            i += 1
            if i == 6:
                x = False
                exit(0)

    elif datetime.datetime.today().weekday() == 2:
        if (datetime.datetime.now().time().hour == start_hours_wednesday[i]) and (datetime.datetime.now().time().minute == start_mins_wednesday[i]):
            login_dets(userid, passw)
            i += 1
            if i == 4:
                x = False
                exit(0)

    elif datetime.datetime.today().weekday() == 3:
        if (datetime.datetime.now().time().hour == start_hours_thursday[i]) and (datetime.datetime.now().time().minute == start_mins_thursday[i]):
            login_dets(userid, passw)
            i += 1
            if i == 5:
                x = False
                exit(0)

    elif datetime.datetime.today().weekday() == 6:
        if (datetime.datetime.now().time().hour == start_hours_sunday[i]) and (datetime.datetime.now().time().minute == start_mins_sunday[i]):
            login_dets(userid, passw)
            i += 1
            if i == 3:
                x = False
                exit(0)

