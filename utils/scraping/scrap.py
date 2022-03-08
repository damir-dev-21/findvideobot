from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")

s = Service(ChromeDriverManager().install()).path

driver = webdriver.Chrome(executable_path=s,options=options)

def getVideos(message: str,count: int):
    result = []

    video_href = "https://www.youtube.com/results?search_query=" + message

    driver.get(video_href)
    sleep(2)
    videos = driver.find_elements_by_id("thumbnail")

    for i in range(len(videos)):
        print(videos[i].get_attribute('href'))
        t = videos[i].get_attribute('href')

        if t != None:
            result.append(t)

        if i == int(count):
            break

    return result


def getPopularVideos(count: int):
    result = []

    video_href = "https://www.youtube.com/feed/explore"

    driver.get(video_href)
    sleep(2)
    videos = driver.find_elements_by_id("thumbnail")

    for i in range(len(videos)):
        print(videos[i].get_attribute('href'))
        t = videos[i].get_attribute('href')

        if t != None:
            result.append(t)

        if i == int(count):
            break

    return result


