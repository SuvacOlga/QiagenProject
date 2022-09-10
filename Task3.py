import time

from selenium import webdriver

# initialize chrome driver

path = '/Users/olgasuvac/Downloads'
driver = webdriver.Chrome(executable_path='/Users/olgasuvac/Downloads')

# open the browser
driver.get('http://www.hotwire.com/')
driver.maximize_window()

#search flights, car, hotel
search_flights_hotel_car = driver.find_element_by_xpath(
    '//*[@id="root"]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[3]/form/div[10]/button')
search_flights_hotel_car.click()

round_trip = driver.find_elements_by_id('RoundTrip')
round_trip.click()
time.sleep(5)

# search flight to SFO
departure = driver.find_element_by_id('text')
departure.click()
departure.send_keys('sfo')
time.sleep(5)

cities_departure = driver.find_elements_by_path(
    '//*[@id="root"]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/ul/li[2]')
for city_1 in cities_departure:
    if 'SFO' in city_1.text:
        city_1.click()
        break
time.sleep(5)

# search flight from LAX
arrival = driver.find_element_by_id('text')
arrival.click()
arrival.send_keys('lax')
time.sleep(5)

cities_arrival = driver.find_elements_by_path(
    '//*[@id="root"]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[3]/form/div[3]/div/div[2]/div[2]/div/div/div[2]/div/ul/li[1]')
for city_2 in cities_departure:
    if 'LAX' in city_2.text:
        city_2.click()
        break
time.sleep(5)

departure_date = driver.find_element_by_xpath(
    '//*[@id="picker-modal"]/div/div/div[2]/div/div[1]/div/div[2]/table/tbody/tr[3]/td[2]')
departure_date.click()
time.sleep(5)

return_date = driver.find_elements_by_xpath(
    '//*[@id="picker-modal"]/div/div/div[2]/div/div[1]/div/div[2]/table/tbody/tr[6]/td[1]')
return_date.click()
time.sleep(5)
