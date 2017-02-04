# googleImagesWebScraping
Helper To scrape Google images in order to build image library to feed tensorflow image recognition deep learning algorithm


## prerequisits
### install chrome web driver
go to: <br />
https://chromedriver.storage.googleapis.com/index.html

installation is explained here: <br />
https://www.youtube.com/watch?v=9kWz5tL4D7w

### pip dependencies
```shell
pip install selenium
pip install urllib2
pip install BeautifulSoup4
```
## usage
usage - in shell:
```shell
google_image_downloader.py -i <input_term_filepath> -o <output_image_folder_path> -t <theme> -n <nb_pictures_per_term> -d <web_driver_path>
```

-i or --input_term_filepath sets the path to the csv fiel containing all the keywords to scrap <br />
-o or --output_image_folder_path set the path to the root folder where subfolder of terms will be downloaded <br />
output folder structure will be as described below: <br />
|---output_image_folder_path <br />
____|---term 1 <br />
____|---term 2 <br />
____|---term 3 <br />
-t or --theme sets the general theme of the scraping : for instance "car", "cat", "food" in order to refine the search <br />
-n --nb_pictures_per_term sets the number of images to download for each term <br />
-d --web_driver_path sets the path to the chrome driver file <br />


