from selenium import webdriver
import csv
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
csvfile=open('Words.csv', 'w', newline='',encoding='utf-8')
writer = csv.writer(csvfile)
with open('Queries.txt','r') as File:
    Queries=File.readlines()
for Qnum in range(len(Queries)):
    string=str(Queries[Qnum]+str('"Canoo" Article'))
    url = 'https://www.google.com/search?q='+string+'&num=8'
    driver.get(url)
    elements= driver.find_elements('xpath','//a[@jsname="UWckNb"]')
    Links=[]
    for element in elements:
        link = element.get_attribute('href')
        Links+=[link]
        print(link)
    Dict={}
    text=[]
    count=0
    print(len(Links))
    for link in Links:
        if link in Dict:
            pass
        else:
            Dict[link]=True
            try:
                driver.get(link)
                count+=1
                print(count)
                body_elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, 'body'))
                )
                for body_element in body_elements:
                    text.append(body_element.text)
            except TimeoutException:
                print("Timeout occurred while loading", link)
            except Exception as e:
                print("An error occurred:", e)
    data=[]
    for i in range(len(text)):
        temp=text[i].split('\n')
        for j in range(len(temp)):
            t=temp[j].split()
            if(len(t)>6):
                data+=[[temp[j].split()]]
    # with open('Words'+str(Qnum)+'.csv', 'w', newline='',encoding='utf-8') as csvfile:
    #     writer = csv.writer(csvfile)
    for x in data:
        writer.writerows(x)