# Scrapper.py Explanation

This script is a web scraper built with Playwright that automatically extracts and downloads citation files from Springer research articles.

## Overview

The script automates the process of:
1. Navigating to a Springer search results page
2. Iterating through each article on the page
3. Clicking on each article to access its detail page
4. Downloading the citation file for each article
5. Navigating back to the results page
6. Moving to the next page of results
7. Repeating until all pages are processed

## Detailed Functionality

### Command Line Interface
- Takes two arguments:
  - The Springer search results URL
  - The path where citation files should be saved

### Main Function: `download_files(link, download_path)`
- Creates the download directory if it doesn't exist
- Initializes Playwright with a visible browser (headless=False)
- Opens the provided Springer URL

### Page Navigation Loop
1. Waits for 5 seconds for the initial page to load
2. For each page of search results:
   - Waits for the results list to appear (selector: "ol.u-list-reset")
   - Processes up to 20 articles per page (the standard number on Springer)

### Article Processing Loop
For each article (1-20) on the current page:
1. Finds the article link using a data-track-context attribute with the current counter
2. Clicks the link to open the article detail page
3. Waits for the bibliographic information section to load
4. Locates the download citation button
5. Sets up a download handler to capture the file
6. Clicks the download button and saves the file with its suggested filename
7. Navigates back to the search results page

### Pagination
After processing all articles on a page:
1. Increments the page counter
2. Looks for the "next page" button
3. If found, clicks it and continues processing
4. If not found, ends the scraping process

### Error Handling
- Includes checks for missing elements (article links, download buttons)
- Outputs warning messages when elements aren't found
- Continues to the next article/page when possible

## Technical Details
- Uses Playwright's synchronous API for browser automation
- Implements explicit waiting for elements and page loads
- Handles file downloads through Playwright's download API
- Maintains state across page navigations
- Provides console output to track progress

The script is designed for batch downloading citation files from Springer research articles for academic or research purposes.
