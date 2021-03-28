import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
def provide_info(mounth,day):
    link="https://www.nba.com/schedule?cal="+mounth
    path='C:\Program Files (x86)\chromedriver.exe'
    driver=webdriver.Chrome(path)
    driver.get(link)
    wait = WebDriverWait(driver, 30)
    page_source = driver.page_source
    driver.close()
    soup = BeautifulSoup(page_source, 'html.parser')
    next_tag=soup.find("div",id="__next")
    one_day_games=next_tag.find_all(class_="flex flex-col pt-5 border-b border-concrete sm:flex-row")
    our_day_games=one_day_games[0]
    for one_day_game in one_day_games:
        time=one_day_game.find(class_="text-sm font-bold leading-tight text-cerulean").get_text()
        stam,our_day,stam1=time.partition(day)
        if our_day==day:
            our_day_games=one_day_game
            break
    date=our_day_games.find(class_="text-sm font-bold leading-tight text-cerulean").get_text()
    games_list=our_day_games.find_all(class_="py-5 border-t border-concrete flex flex-col xl:flex-row")
    times_list=[]
    playing_teams_list=[]
    stadiums_list=[]
    for game in games_list:
       time= game.find("span",class_="text-sm uppercase").get_text()
       times_list.append(time)
       teams=game.find_all(class_="text-cerulean")
       away_team=teams[0].get_text()
       host_team=teams[1].get_text()
       playing_teams_list.append((host_team,away_team))
       hidden_text=game.find(class_="text-sm min-w-3/10 hidden xl:block")
       stadium=hidden_text.find(class_="text-sm").get_text()
       stadiums_list.append(stadium)
    print(times_list)
    print(playing_teams_list)
    print(stadiums_list)




def main():
    provide_info("March",'28')
if __name__ == '__main__':
    main()
