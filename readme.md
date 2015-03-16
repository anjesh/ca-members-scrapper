Constituent Assembly Member Profile Scrapper
============================================

It scrapes the members profile of Constituent Assembly (CA) of Nepal from the [PDF files](resources) downloaded from http://www.can.gov.np. The pdf are converted to [html](in) using `pdftohtml`. It uses the pretti font. The scraped data is converted to Unicode using [ttf2utf](https://github.com/anjesh/nep-ttf2utf) and the csv is saved in [out folder](out).

# How it works?

* read each line of html file
* check each line for the pattern
* if the pattern is found, pass the patternFinder to the profileMaintaner
* ProfileMaintainer maintains the collection of profiles 
* CSVProfileExport takes the collection of profiles and generates csv file

## Setup

* Clone the repo
* `git submodule init`
* `git submodule update`

### Test

The tests only covers the LinePatternFinder only. 

`python -m unittest tests.patternFinderTest`

### Run

* `python run.py`
* `out/profiles.csv` will be created

## TODOs

* Scrape all the fields
* Write more tests 

## Problems

* There are non ascii characters so they couldn't be converted to Unicode. They are ignored and [x] is added to the value to make manual fixes


