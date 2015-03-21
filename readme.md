Constituent Assembly Member Profile Scrapper
============================================

It scrapes the members profile of Constituent Assembly (CA) of Nepal from the [PDF files](resources) downloaded from http://www.can.gov.np. The pdf are converted to [html](in) using `pdftohtml`. It uses the pretti font. The scraped data is converted to Unicode using [ttf2utf](https://github.com/anjesh/nep-ttf2utf) and the csv is saved in [out folder](out).

# How it works?

* read each line of html file
* check each line for the pattern
* if the pattern is found, pass the patternFinder to the profileMaintainer
* ProfileMaintainer maintains the collection of profiles 
* CSVProfileExport takes the collection of profiles and generates [csv file](out/profiles.csv)

## Setup

* Clone the repo
* `git submodule init`
* `git submodule update`

### Test

`python -m unittest tests.patternFinderTest`
`python -m unittest tests.profileTest`
`python -m unittest tests.profileExportTest`

or

Execute `bash runtest.sh` to run all above tests at once.

### Run

* `python run.py`
* `out/profiles.csv` will be created

## TODOs

* See problems with the data and there are still things that could be improved. 
* Increase test coverage

## Problems

* There are non ascii characters so they couldn't be converted to Unicode. They are ignored and [x] is added to the value to make manual fixes


