#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import os
import sys
import csv
import json
import getopt
import urllib
import urllib2
import requests


webdriver_path = 'C:\opt\chromedriver_win32\chromedriver.exe'

google_search_img_url = "https://www.google.com/search?q="
google_search_img_class = "rg_ic"

download_folder = "img"
google_search_theme = ""
input_term_filepath = "terms.csv"
google_search_terms = []
nb_pictures_per_term = 10

help_msg = "google_image_dowloader.py -i <input_term_filepath> -o <output_image_folder_path> -t <theme> -n <nb_pictures_per_term> -d <web_driver_path>"

def main(argv):

	try:
		opts, args = getopt.getopt(argv, "hi:o:t:n:d:", ["iinput_term_filepath=", "ooutput_image_folder_path=", "ttheme=", "nnb_picture_per_term", "dweb_driver_path"])
	except getopt.GetoptError:
		print(help_msg)
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print(help_msg)
			sys.exit(2)
		elif opt in ("-i", "--input_term_filepath"):
			input_term_filepath = arg
		elif opt in ("-o", "--output_image_folder_path"):
			download_folder = arg
		elif opt in ("-t", "--theme"):
			google_search_theme = arg
		elif opt in ("-n", "--nb_pictures_per_term"):
			nb_pictures_per_term = int(arg)
		elif opt in ("-d", "--driver_path"):
			webdriver_path = arg
		
	google_search_terms = extract_terms(input_term_filepath)
	create_folder(download_folder)
	for term  in google_search_terms:
		get_images(google_search_theme, term, download_folder, nb_pictures_per_term)
	

def create_folder(newpath):
	newpath = newpath[:56]
	if not os.path.exists(newpath):
		created = os.makedirs(newpath)
	return newpath

def clean_name(name):
	name = "".join([c for c in name if c.isalpha() or c.isdigit() or c==' ']).rstrip()
	return name.replace(" ", "_")

def get_soup(url, header):
	return BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)))

def get_images(theme, query, folder, nb_pictures = 150):

	counter = 0
	scrolldown_offset = 40

	url = google_search_img_url + (theme + " " + query).replace("_", " ") + "&source=lnms&tbm=isch"
	
	driver = webdriver.Chrome(executable_path = webdriver_path)
	driver.get(url)

	x = nb_pictures

	while x > 0:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		x = x - scrolldown_offset

	sleep(3)

	html = driver.page_source

	soup = BeautifulSoup(html, 'lxml')

	for img in soup.findAll("img", { "class" : google_search_img_class }):
		
		if img.has_key("src"):
			img_url = img['src']

			create_folder(os.path.join(folder, query))
			path = os.path.join(folder, query , clean_name(theme + " " + query) + "_" + str(counter) + '.jpeg')
			
			if counter < nb_pictures:
				print('progress : ' + str(round(counter / nb_pictures * 100,0)))
				
				if 'base64' in img_url:
					with open(path, "wb") as fh:
						fh.write(img_url.split(',')[1].decode('base64'))
						fh.close()
						counter = counter + 1
				else:
					urllib.urlretrieve(img_url, path)
					counter = counter + 1

	print(str(counter) + " pictures succesfully downloaded over " + str(nb_pictures) + " for " + query)
	driver.close()

def extract_terms(input_term_filepath):
	terms = []
	with open(input_term_filepath, 'rb') as termfile:
		terms_csv = csv.reader(termfile, delimiter = ',')
		for term in terms_csv:
			terms.append(term[0])

	return terms

if __name__ == "__main__":
	main(sys.argv[1:])
	
