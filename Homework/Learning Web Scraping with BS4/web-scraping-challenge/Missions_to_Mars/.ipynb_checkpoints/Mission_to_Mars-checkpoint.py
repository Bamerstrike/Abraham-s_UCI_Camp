{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 203,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import time\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {},
   "outputs": [],
   "source": [
    "url1 = 'https://mars.nasa.gov/news/'\n",
    "url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "url3 = 'https://twitter.com/marswxreport?lang=en'\n",
    "url4 = 'https://space-facts.com/mars/'\n",
    "url5 = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Mars Scientists Investigate Ancient Life in Australia',\n",
       " \"NASA's Mars 2020 Will Hunt for Microscopic Fossils\",\n",
       " 'With Mars Methane Mystery Unsolved, Curiosity Serves Scientists a New One: Oxygen',\n",
       " \"NASA's Mars 2020 Heads Into the Test Chamber\",\n",
       " \"Screening Soon: 'The Pathfinders' Trains Lens on Mars\",\n",
       " \"InSight's 'Mole' Team Peers into the Pit\",\n",
       " \"Common Questions about InSight's 'Mole'\",\n",
       " 'Mars 2020 Stands on Its Own Six Wheels',\n",
       " 'New Selfie Shows Curiosity, the Mars Chemist',\n",
       " 'Naming a NASA Mars Rover Can Change Your Life',\n",
       " 'Mars 2020 Unwrapped and Ready for More Testing',\n",
       " \"HiRISE Views NASA's InSight and Curiosity on Mars\",\n",
       " \"NASA's Curiosity Rover Finds an Ancient Oasis on Mars\",\n",
       " \"NASA's Mars 2020 Rover Tests Descent-Stage Separation\",\n",
       " \"NASA's Push to Save the Mars InSight Lander's Heat Probe\",\n",
       " \"NASA's InSight 'Hears' Peculiar Sounds on Mars\",\n",
       " 'NASA Mars Mission Connects With Bosnian and Herzegovinian Town',\n",
       " \"Deadline Closing for Names to Fly on NASA's Next Mars Rover\",\n",
       " 'NASA Wins Two Emmy Awards for Interactive Mission Coverage',\n",
       " \"NASA's Mars 2020 Comes Full Circle\",\n",
       " 'NASA Invites Students to Name Mars 2020 Rover',\n",
       " \"NASA's Mars Helicopter Attached to Mars 2020 Rover \",\n",
       " \"What's Mars Solar Conjunction, and Why Does It Matter?\",\n",
       " 'Scientists Explore Outback as Testbed for Mars ',\n",
       " \"NASA-JPL Names 'Rolling Stones Rock' on Mars\",\n",
       " \"Robotic Toolkit Added to NASA's Mars 2020 Rover\",\n",
       " \"Space Samples Link NASA's Apollo 11 and Mars 2020\",\n",
       " 'Small Satellite Mission of the Year',\n",
       " \"NASA 'Optometrists' Verify Mars 2020 Rover's 20/20 Vision\",\n",
       " 'New Finds for Mars Rover, Seven Years After Landing',\n",
       " 'MEDLI2 Installation on Mars 2020 Aeroshell Begins',\n",
       " \"NASA's Mars 2020 Rover Does Biceps Curls \",\n",
       " \"Fueling of NASA's Mars 2020 Rover Power System Begins\",\n",
       " 'What Does a Marsquake Look Like?',\n",
       " 'Mars 2020 Rover: T-Minus One Year and Counting ',\n",
       " 'NASA Racks Up Two Emmy Nominations for Mission Coverage',\n",
       " 'Want to Colonize Mars? Aerogel Could Help',\n",
       " 'A Rover Pit Stop at JPL',\n",
       " 'Mars 2020 Rover Gets a Super Instrument',\n",
       " 'A Neil Armstrong for Mars: Landing the Mars 2020 Rover',\n",
       " 'NASA Garners 7 Webby Award Nominations',\n",
       " \"NASA's Opportunity Rover Mission on Mars Comes to End\",\n",
       " \"NASA's InSight Places First Instrument on Mars\",\n",
       " 'NASA Invites Students to Name Mars 2020 Rover',\n",
       " \"NASA's Curiosity Mars Rover Finds a Clay Cache\",\n",
       " 'Why This Martian Full Moon Looks Like Candy',\n",
       " 'NASA Garners 7 Webby Award Nominations',\n",
       " \"NASA's Opportunity Rover Mission on Mars Comes to End\",\n",
       " \"NASA's InSight Places First Instrument on Mars\",\n",
       " 'NASA Invites Students to Name Mars 2020 Rover',\n",
       " \"NASA's Curiosity Mars Rover Finds a Clay Cache\",\n",
       " 'Why This Martian Full Moon Looks Like Candy']"
      ]
     },
     "execution_count": 225,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Get Titles\n",
    "browser.visit(url1)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "title_divs = soup.find_all('div', class_=\"content_title\")\n",
    "titles = []\n",
    "links = []\n",
    "paragraphs = []\n",
    "for title_div in title_divs:\n",
    "    titles.append(title_div.find('a').text.replace(\"\\n\",\"\"))\n",
    "    links.append(f\"https://mars.nasa.gov{title_div.find('a').get('href')}\")\n",
    "\n",
    "#Get paragraph Text\n",
    "main_section = []\n",
    "# for link in links:\n",
    "for link in links:\n",
    "    browser.visit(link)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    time.sleep(1)    \n",
    "    main_section.append(soup.find(\"div\",class_=\"wysiwyg_content\").find(\"p\").get_text())\n",
    "    #     class=\"wysiwyg_content\"\n",
    "\n",
    "titles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 346,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"As any geologist worth his or her salt will tell you, there are rocks, and then there are rocks. Next July, NASA and the European Space Agency (ESA) are launching rovers to Mars that will search for signs of past microbial life, and to find them, the scientists with NASA's Mars 2020 mission and ESA's ExoMars will need to examine different kinds of rocks that lend compelling insights into the environment in which they were made — all from 100 million miles away. \""
      ]
     },
     "execution_count": 346,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "main_section[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 347,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23539_hires.jpg'"
      ]
     },
     "execution_count": 347,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Get Space Images\n",
    "featured_image_urls = []\n",
    "\n",
    "browser.visit(url2)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "section = soup.find('section', class_=\"grid_gallery module grid_view\")\n",
    "list_items = section.find_all('a',class_=\"fancybox\")\n",
    "for list_item in list_items:\n",
    "    image_url = list_item.get(\"data-fancybox-href\")\n",
    "    featured_image_urls.append(f\"https://www.jpl.nasa.gov{image_url}\")\n",
    "\n",
    "\n",
    "featured_image_url = featured_image_urls[0]\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 348,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'InSight sol 344 (2019-11-15) low -99.9ºC (-147.9ºF) high -23.3ºC (-9.9ºF)\\nwinds from the SSE at 5.7 m/s (12.9 mph) gusting to 18.9 m/s (42.3 mph)\\npressure at 6.80 hPa'"
      ]
     },
     "execution_count": 348,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Mars Weather\n",
    "Mars_Weathers = []\n",
    "browser.visit(url3)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "\n",
    "tweet_box = soup.find_all(\"p\", class_=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\")\n",
    "\n",
    "\n",
    "for tweet in tweet_box:\n",
    "    if \"º\" in tweet.get_text():\n",
    "        try:\n",
    "            link_begone = tweet.find('a').get_text()\n",
    "            Mars_Weathers.append(tweet.get_text().replace(link_begone,\"\"))\n",
    "        except(AttributeError):\n",
    "            Mars_Weathers.append(tweet.get_text())\n",
    "            \n",
    "\n",
    "Mars_Weather = Mars_Weathers[0]\n",
    "Mars_Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 327,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Mars Facts\n",
    "\n",
    "Mars_Facts = []\n",
    "Mars_Facts = pd.read_html(url4)\n",
    "Mars_Properties = Mars_Facts[0]\n",
    "Mars_Comparison = Mars_Facts[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 325,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Mars Hemispheres\n",
    "Mars_Hemispheres = []\n",
    "Picture_Site = []\n",
    "browser.visit(url5)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "Planet_Hemispheres = soup.find_all(\"section\",class_=\"block\")[0]\n",
    "Titles = Planet_Hemispheres.find_all(\"h3\")\n",
    "\n",
    "\n",
    "for extension in Planet_Hemispheres.find_all(\"div\", class_=\"item\"):\n",
    "    link = \"https://astrogeology.usgs.gov\"+extension.a[\"href\"]\n",
    "    browser.visit(link)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,'html.parser')\n",
    "    Picture_Site.append(soup.find_all('a',{\"target\":\"_blank\"})[1][\"href\"])\n",
    "\n",
    "for i in range(len(Titles)):\n",
    "    Mars_Hemispheres.append({\"Title\":Titles[i].get_text(), \"img_url\" : Picture_Site[i]})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData]",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
