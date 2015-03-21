#!/usr/local/bin/python
# coding: utf-8

import unittest
import sys

from ProfileScraper import *

class ProfileExportTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def getProfileMaintainer(self, datafile):
        profileMaintainer = ProfileMaintainer()
        with open(datafile,'rU') as f:
            scraper =  LinePatternFinder()
            count = 1
            for line in f:
                scraper.setLine(line)
                if scraper.getFoundField():
                    if scraper.getFoundField() == ProfileFields.NAME:
                        profileId = scraper.getProfileId(line)
                        count += 1
                    profileMaintainer.setLinePatternFinder(scraper)
        return profileMaintainer

    def testProfile1Export(self):
        profileMaintainer = self.getProfileMaintainer('tests/data1.html')
        profileExport = CSVProfileExport("tests/profiles1.csv", "")
        profileExport.setProfiles(profileMaintainer.profiles)
        profile = profileMaintainer.profiles[0]
        row = profileExport.getCSVRow(profile)
        # for v in row:
        #     print v

            # print profile.getUnicodeFieldValue(field).encode('utf-8')

    def testProfile2Export(self):
        profileMaintainer = self.getProfileMaintainer('tests/data2.html')
        profileExport = CSVProfileExport("tests/profiles2.csv", "")
        profileExport.setProfiles(profileMaintainer.profiles)
        profile = profileMaintainer.profiles[0]
        row = profileExport.getCSVRow(profile)
