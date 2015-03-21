#!/usr/local/bin/python
# coding: utf-8

import unittest
import sys

from ProfileScraper import *

class Profile1Test(unittest.TestCase):
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

    def testProfile1(self):
        profileMaintainer = self.getProfileMaintainer('tests/data1.html')
        profile = profileMaintainer.profiles[0]
        self.assertEqual(profile.values[ProfileFields.NAME], "cOGb| ;'Gb/ g]DjfË")
        self.assertEqual(profile.values[ProfileFields.DOB], "2034/07/12")
        self.assertEqual(profile.values[ProfileFields.BIRTH_DISTRICT], "kfFry/")
        self.assertEqual(profile.values[ProfileFields.BIRTH_VDC], "ODj'ª")
        self.assertEqual(profile.values[ProfileFields.BIRTH_WARD], "!")
        # self.assertEqual(profile.values[ProfileFields.NAME], "cOGb| ;'Gb/ g]DjfË")
        # self.assertEqual(profile.values[ProfileFields.NAME], "cOGb| ;'Gb/ g]DjfË")
        # self.assertEqual(profile.values[ProfileFields.NAME], "cOGb| ;'Gb/ g]DjfË")
        # self.assertEqual(profile.values[ProfileFields.NAME], "cOGb| ;'Gb/ g]DjfË")
        # self.assertEqual(profile.values[ProfileFields.NAME], "cOGb| ;'Gb/ g]DjfË")
            # print profile.getUnicodeFieldValue(field).encode('utf-8')

    def testProfile2(self):
        profileMaintainer = self.getProfileMaintainer('tests/data2.html')
        profile = profileMaintainer.profiles[0]
        self.assertEqual(profile.values[ProfileFields.NAME], "csafn cxdb zfx")
        self.assertEqual(profile.values[ProfileFields.DOB], "!(^) km]a|'j/L !!")
        self.assertEqual(profile.values[ProfileFields.BIRTH_DISTRICT], "slkna:t',si0fgu/")
        # self.assertEqual(profile.values[ProfileFields.BIRTH_VDC], "")
        # self.assertEqual(profile.values[ProfileFields.BIRTH_WARD], "&")
