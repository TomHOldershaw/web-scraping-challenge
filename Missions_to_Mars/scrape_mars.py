import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    browser = Browser('chrome', executable_path=ChromeDriverManager().install(), headless=False)

    #NASA mars news
    # Set page URL
    url = "https://redplanetscience.com/"

    # Retrieve page
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(browser.html, 'html.parser')

    # Find first news article - only the latest is required
    # Headline is in div 'content_title'
    # Text is in div 'article_teaser_body'

    headline = soup.find('div', class_="content_title").text
    text = soup.find('div', class_="article_teaser_body").text

    # JPL Mars space images
    # Set page URL
    url = "https://spaceimages-mars.com/"

    # Retrieve page
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(browser.html, 'html.parser')

    # Extract image URL
    image = soup.find('img', class_="headerimage fade-in")['src']
    image_url = url + image

    # Mars Facts
    url = 'https://galaxyfacts-mars.com/'

    tables = pd.read_html(url)
    # Desired table is the second one on the page
    facts_table = tables[1].to_html()

    # Mars Hemispheres
    # Set page URL
    url = "https://marshemispheres.com/"

    # Retrieve page
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(browser.html, 'html.parser')

    # Find all hemisphere items
    list_items = soup.find_all('div', class_="item")

    # Iterate through list
    hemisphere_list = []

    for item in list_items:
        # Get title
        title = item.find('h3').text
        hemi_title = title[:-9]
        # Go to page
        browser.links.find_by_partial_text(title).click()
        soup = bs(browser.html, 'html.parser')
        description = soup.find('div', class_="description")
        # Extract image link
        link = description.find('a')['href']
        # Save data
        dictionary = {
            'title': hemi_title,
            'img_url': url + link
        }
        hemisphere_list.append(dictionary)
        # Go back for next image
        browser.back()

    # End browser connection
    browser.quit

    # Single dictionary
    mars_data = {
        'nasa_news': {'headline': headline, 'text': text},
        'JPL_image': image_url,
        'Mars_facts': facts_table,
        'Hemispheres': hemisphere_list
    }

    return mars_data