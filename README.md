# Overview
This script fetches URLs from the Wayback Machine for any given domain. It handles HTTP errors gracefully, includes detailed logging, and introduces random delays between requests to mimic human behavior.

# Features:
Fetch All URLs: Queries the Wayback Machine for all URLs related to a target domain.

Error Handling: Retries on connection issues and logs errors.

Human-like Behavior: Random delays to avoid server detection.

# Installation and Usage:
Install Dependencies: Ensure requests is installed (pip install requests).

Prepare Input File: Create input.txt with one domain per line.

Run the Script: Execute python wayback.py.

Output: Gathered URLs are saved in gathered_urls.txt.

python wayback.py

# Contributing
Let me know if there's anything else you'd like to add or adjust!
