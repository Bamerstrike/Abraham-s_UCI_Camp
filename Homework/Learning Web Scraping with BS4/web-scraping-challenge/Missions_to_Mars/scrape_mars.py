from splinter import Browser
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    #Create Browser instance
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Create a dictionary to collect all the data
    Return_This_Data = {}


    #Create urls to scrape
    url1 = 'https://mars.nasa.gov/news/'
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    url3 = 'https://twitter.com/marswxreport?lang=en'
    url4 = 'https://space-facts.com/mars/'
    url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


    #Scrape URL 1 for Titles and News Paragraphs
    browser.visit(url1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title_divs = soup.find_all('div', class_="content_title")
    titles = []
    links = []
    paragraphs = []
    for title_div in title_divs:
        titles.append(title_div.find('a').text.replace("\n",""))
        links.append(f"https://mars.nasa.gov{title_div.find('a').get('href')}")

    #Get paragraph Texts
    main_section = []
    for link in links:
        browser.visit(link)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        main_section.append(soup.find("div",class_="wysiwyg_content").find("p").get_text())

    #URL 1 Result
    #------------------------------
    news_title = titles[0]
    news_p = main_section[0]
    Return_This_Data["URL1"] = [news_title, news_p]
    #------------------------------

    #Scrape URL 2 for JPL Mars Space Images
    featured_image_urls = []

    browser.visit(url2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    section = soup.find('section', class_="grid_gallery module grid_view")
    list_items = section.find_all('a',class_="fancybox")
    for list_item in list_items:
        image_url = list_item.get("data-fancybox-href")
        featured_image_urls.append(f"https://www.jpl.nasa.gov{image_url}")


    #URL 2 Result
    #------------------------------
    featured_image_url = featured_image_urls[0]
    Return_This_Data["URL2"] = [featured_image_url]
    #------------------------------

    #Scrape URL 3 for Mars Weather
    Mars_Weathers = []
    browser.visit(url3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    tweet_box = soup.find_all("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")


    for tweet in tweet_box:
        if "º" in tweet.get_text():
            try:
                link_begone = tweet.find('a').get_text()
                Mars_Weathers.append(tweet.get_text().replace(link_begone,""))
            except(AttributeError):
                Mars_Weathers.append(tweet.get_text())
                
    #URL 3 Result
    #------------------------------
    Mars_Weather = Mars_Weathers[0]
    Return_This_Data["URL3"] = Mars_Weather
    #------------------------------


    #Scrape URL 4 for Mars Facts
    Mars_Facts = []
    Mars_Facts = pd.read_html(url4)

    #URL 4 Result
    #------------------------------
    Mars_Properties = Mars_Facts[0]
    Mars_Comparison = Mars_Facts[1]
    
    Return_This_Data["URL4"] = []
    for i in range(len(Mars_Properties[0])):
        Return_This_Data["URL4"].append([Mars_Properties[0][i],Mars_Properties[1][i]])
    #------------------------------


    #Scrape URL 5 for Mars Hemispheres
    Mars_Hemispheres = []
    Picture_Site = []
    browser.visit(url5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    Planet_Hemispheres = soup.find_all("section",class_="block")[0]
    Titles = Planet_Hemispheres.find_all("h3")


    for extension in Planet_Hemispheres.find_all("div", class_="item"):
        link = "https://astrogeology.usgs.gov"+extension.a["href"]
        browser.visit(link)
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        Picture_Site.append(soup.find_all('a',{"target":"_blank"})[0]["href"])

    for i in range(len(Titles)):  
        #URL 5 Result
        #------------------------------
        Mars_Hemispheres.append({"Title":Titles[i].get_text(), "img_url" : Picture_Site[i]})
        #------------------------------
    Return_This_Data["URL5"] = Mars_Hemispheres

    browser.driver.close()

    return Return_This_Data


    
    
