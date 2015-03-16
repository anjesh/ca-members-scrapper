Constituent Assembly Member Profile Scrapper
============================================

It scrapes the members profile of Constituent Assembly (CA) of Nepal from the [PDF files](resources) downloaded from http://www.can.gov.np. The pdf are converted to [html](in) using `pdftohtml`. It uses the pretti font. The scraped data is converted to Unicode using [ttf2utf](https://github.com/anjesh/nep-ttf2utf) and the csv is saved in [out folder](out).

# How it works?

* read each line of html file
* check each line for the pattern
* if the pattern is found, pass the patternFinder to the profileMaintaner
* ProfileMaintainer maintains the collection of profiles 
* CSVProfileExport takes the collection of profiles and generates csv file

### Run

* Clone the repo
* 

`python run.py`

### Test

The tests only covers the LinePatternFinder only. 

`python -m unittest tests.patternFinderTest`

### TOODs

