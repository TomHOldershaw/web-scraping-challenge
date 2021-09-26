# web-scraping-challenge

Contains the files for the Week 12 homework, web scraping.

The challenge set was to:
1. Scrape four websites with information about Mars
2. Store the data in a local Mongo database
3. Retrieve the data and display in a webpage

The webpage displays with no data on initial loading, and contains a button to scrape and reload to display the data

Project files are in the 'Missions to Mars' folder and consist of:
1. mission_to_mars.ipynb - Jupyter notebook containing initial code
2. mars.py - main script with Flask routes
3. scrape_mars.py - script containing the code from the Jupyter notebook to scrape websites
4. templates/index.html - basic webpage to display information, using Bootstrap for responsive sizing
