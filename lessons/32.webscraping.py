# import bs4
# import requests

# res = requests.get('https://www.metacritic.com/browse/games/score/metascore/all/switch/filtered')
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# soup.select('#main_content > div.browse.movie.new_releases > div.content_after_header > div > div.next_to_side_col > div > div.browse_list_wrapper.one.browse-list-large > table > tbody > tr:nth-child(1) > td.clamp-summary-wrap > a > h3')


from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.google.com')

elem = browser.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
elem.send_keys('almoço para hoje')
elem.submit()

result = browser.find_element_by_css_selector('#rso > div:nth-child(2) > div > div.kp-blk.c2xzTb > div > div.ifM9O > div > div.g > div > div.yuRUbf > a > h3')
result.click()

browser.quit()