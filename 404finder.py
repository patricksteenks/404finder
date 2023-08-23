import requests
import xml.etree.ElementTree as ET
import time
import sys

def load_processed_urls(file_path):
    try:
        with open(file_path, "r") as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

def save_processed_urls(file_path, processed_urls):
    with open(file_path, "w") as f:
        for url in processed_urls:
            f.write(f"{url}\n")

def find_404_urls(sitemap_url, log_file, state_file):
    processed_urls = load_processed_urls(state_file)
    
    response = requests.get(sitemap_url)
    if response.status_code != 200:
        print(f"Failed to fetch sitemap: {response.status_code}")
        return
    
    try:
        root = ET.fromstring(response.text)
    except ET.ParseError:
        print("Failed to parse sitemap XML")
        return
    
    urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    
    for url in urls:
        if url in processed_urls:
            continue
        
        check_response = requests.head(url)
        if check_response.status_code == 404:
            print(f"404 - {url}")
            with open(log_file, "a") as f:
                f.write(f"404 - {url}\n")
        
        processed_urls.add(url)
        save_processed_urls(state_file, processed_urls)
        
        print(".", end='', flush=True)
        time.sleep(0.5)  # Wait for 0.5 seconds before the next request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <sitemap_url>")
        sys.exit(1)
    
    sitemap_url = sys.argv[1]
    log_file = "404_log.txt"  # Name of the log file
    state_file = "processed_urls.txt"  # Name of the state file
    
    find_404_urls(sitemap_url, log_file, state_file)

