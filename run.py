#!/usr/local/bin/python
# coding: utf-8

import sys
import copy
import codecs
from ProfileScraper import *

profileMaintainer = ProfileMaintainer();

with open('in/Member_of_CA_from_Serial_No.1-319s.html','rU') as f:
    scraper =  LinePatternFinder()
    count = 1
    for line in f:
        scraper.setLine(line)
        if scraper.getFoundField():
            if scraper.getFoundField() == ProfileFields.NAME:
                profileId = scraper.getProfileId(line)
                if int(profileId) != count:
                    print "Scrapped profile " + profileId
                count += 1
            profileMaintainer.setLinePatternFinder(scraper)

with open('in/Member_of_CA_Serial_No.320_to_597s.html','rU') as f:
    scraper =  LinePatternFinder()
    for line in f:
        scraper.setLine(line)
        if scraper.getFoundField():
            if scraper.getFoundField() == ProfileFields.NAME:
                profileId = scraper.getProfileId(line)
                print "Scrapped profile " + profileId 
            profileMaintainer.setLinePatternFinder(scraper)

CSVProfileExport("out/profiles.csv", profileMaintainer.profiles)






