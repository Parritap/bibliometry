# Scraper_Springer
Simple Springer Scraper to download masive searches metadata in a .ris format

# Version funcional
The script works in Python 3.9.8

# Instructions
Before run the script, make sure you have an active virtual environment with python 3.9.8

1. `pip install -U pip`
2. `pip infstall -r requirements.txt`
3. `playwright install`

Go to the browser and get the link of the search you wanto to scrape, maybe you want to include some filters, like the publication date, the type ofpublication, etc.

Besides, you have to create a directory where the script will save the .ris files

  
4. `python scrapper.py "https://link-to-your-search" "/path/to/save/ris/files"` 
    or `python3 scrapper.py "https://link-to-your-search" "/path/to/save/ris/files"`

Note: maybe you have to restart your shell after `pip install -r requirements.txt` in order to the shell recognizes the next command

Note: you should change constants on top of the script to adapt it to you necesities
