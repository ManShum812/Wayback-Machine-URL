import requests
import json
import time
import random
import logging

# Set up logging
logging.basicConfig(filename='script.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_urls_from_wayback(target_domain):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    wayback_url = f"https://web.archive.org/cdx/search/cdx?url={target_domain}/*&limit=-1*&output=json"
    try:
        response = requests.get(wayback_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 200:
            data = response.json()
            # The first row is metadata, so skipping it
            return [row[2] for row in data[1:]] if len(data) > 1 else None
    except requests.exceptions.RequestException as e:
        if "Failed to establish a new connection" in str(e):
            logging.warning(f"Connection issue with {target_domain}. Retrying after 30 seconds...")
            time.sleep(30)  # Wait for 30 seconds before retrying
            return get_urls_from_wayback(target_domain)  # Retry recursively
        else:
            logging.error(f"Error occurred while fetching URLs for {target_domain}: {e}")
    return None

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        for line in f:
            target_domain = line.strip()
            urls = get_urls_from_wayback(target_domain)
            if urls is None:
                logging.error(f"Failed to fetch URLs for {target_domain}.")
                continue
            with open(output_file, 'a') as output:
                for url in urls:
                    output.write(url + '\n')
            # Random delay between 3 to 5 seconds to mimic human-like behavior
            time.sleep(random.uniform(3, 5))

if __name__ == "__main__":
    input_file = "input.txt"  # Provide the path to your input file containing target domains
    output_file = "gathered_urls.txt"  # Output file to store the gathered URLs
    main(input_file, output_file)
