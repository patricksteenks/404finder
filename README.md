# 404finder
This python script is great! It let's you input a sitemap.xml url, which it retrieves. After that it starts looping the xml and logs each 404 it encounters.

The crawl takes place with a 0.5 second delay.

All 404 url's are logged to a file called '404_log.txt'. When during processing an error occurs, the script logs which url's are processed and does not start again.

Great to find 404's on your website

## Usage
Just run `python 404finder.py <url-to-sitemap.xml>` to run the script.

### Open-source
Feel free to duplicate, replicate or adjust the script.
