#!/usr/env python3

# simple robot.txt finder programe

# AUTHOR = RUPANKAR
# EMAIL = rupankar326@gmail.com

import requests
import argparse
import colorama

# sexify the terminal with colorama
# creating color classes


class colors():
    redc = colorama.Fore.RED
    bluec = colorama.Fore.BLUE
    greenc = colorama.Fore.GREEN
    yellowc = colorama.Fore.YELLOW


parser = argparse.ArgumentParser()
# url to look for the robots.txt
parser.add_argument('-u', '--url', help="the url for crawling")
parser.add_argument('-o', '--output', action='store_true', help="option for saving the result into a file")

args = parser.parse_args()

# making the complete url
fullUrl = "https://" + args.url + "/robots.txt"

response = requests.get(fullUrl)


# writing the output to the file
# creating empty file for output result
if args.output:
    file_forOutput = args.url + '.txt'
    nfile = open(file_forOutput, "w+")
    nfile.write(response.text)
    nfile.close()

print(colors.yellowc + response.text)
