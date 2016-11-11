# googleImagesWebScraping
Helper To scrape Google images in order to build image library to feed tensorflow image recognition deep learning algorithm


## prerequisits
### install chrome web driver
go to:
https://chromedriver.storage.googleapis.com/index.html

installation is explained here:
https://www.youtube.com/watch?v=9kWz5tL4D7w

### pip dependencies
````
pip install selenium
pip install urllib2
pip install BeautifulSoup4

````

usage - in shell:
````
google_image_dowloader.py -i <input_term_filepath> -o <output_image_folder_path> -t <theme> -n <nb_pictures_per_term> -d <web_driver_path>
````

