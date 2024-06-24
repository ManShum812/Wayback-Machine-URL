# Overview
Wayback-Machine-URL fetches known URLs from the Wayback Machine for any given domain. Inspired by Tomnomnom's [waybackurls](https://github.com/tomnomnom/waybackurls) and lc [gau](https://github.com/lc/gau), this script aims to provide more accurate results with fewer false positives and errors.

# Features:
Fetch All URLs: Queries the Wayback Machine for all URLs related to a target domain.

Error Handling: Retries on connection issues and logs errors for better traceability.

Human-like Behavior: Introduces random delays between requests to mimic human behavior and avoid server detection.

Accurate Results: Reduces false positives and errors compared to Tomnomnom's waybackurls and lc gau.

# Why Use This Script?
Tomnomnom's [waybackurls](https://github.com/tomnomnom/waybackurls) and lc [gau](https://github.com/lc/gau) are great tools, but they can produce too many false positives and errors. This script addresses these issues, providing more reliable results and ensuring smoother operation. With detailed logging, random delays to mimic human-like behavior, and robust error handling, this script is a better alternative for fetching URLs from the Wayback Machine.

# Installation
git clone https://github.com/ManShum812/Wayback-Machine-URL.git

cd Wayback-Machine-URL

Install Dependencies: Ensure requests is installed (pip install requests).

python wayback.py

# Usage:
Prepare Input File: Create input.txt with one domain per line.

Run the Script: python wayback.py.

Output: Gathered URLs are saved in gathered_urls.txt.


# Contributing
Let me know if there's anything else you'd like to add or adjust!
