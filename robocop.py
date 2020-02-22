#!/usr/env python3

# simple robot.txt finder programe

# AUTHOR = RUPANKAR
# EMAIL = rupankar326@gmail.com

import requests
import argparse

parser = argparse.ArgumentParser()
# url to look for the robots.txt
parser.add_argument('-u', '--url', help="the url for crawling")
parser.add_argument('-o', '--output', required=False,
                    help="option for saving the result into a file")

args = parser.parse_args()

# making the complete url
fullUrl = "https://" + args.url + "/robots.txt"

response = requests.get(fullUrl)

print(response.text)
