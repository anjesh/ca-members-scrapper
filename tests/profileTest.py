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
                # print line
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
        self.assertEqual(profile.values[ProfileFields.DOB], profile.translateNumbers(ProfileFields.DOB, "2034/07/12"))
        self.assertEqual(profile.values[ProfileFields.BIRTH_DISTRICT], "kfFry/")
        self.assertEqual(profile.values[ProfileFields.BIRTH_VDC], "ODj'ª")
        self.assertEqual(profile.values[ProfileFields.BIRTH_WARD], "!")
        self.assertEqual(profile.values[ProfileFields.ELECTED_DISTRICT], "kfFry/")
        self.assertEqual(profile.values[ProfileFields.ELECTED_CONSTITUENCY], "")
        self.assertEqual(profile.values[ProfileFields.PARTY], "g]skf -dfn]_")
        self.assertEqual(profile.values[ProfileFields.PARTY_STARTED_YEAR], "@)$% ;fn")
        self.assertEqual(profile.values[ProfileFields.PAST_EXPERIENCE], "")
        self.assertEqual(profile.values[ProfileFields.PUBLICATIONS], "dfu{lrq ;fKtflxs ænfdÆ")
        #multiline foreign visits
        self.assertEqual(profile.values[ProfileFields.FOREIGN_VISITS], "ef/t, rLg, hfkfg, yfO{Nof08, kfls:tfg, j]nfot, hd{gL, k|mfG;, 8]gdfs{, :jL8]g, cd]l/sf, stf/ nufotsf b]zx? .")

    def testProfile2(self):
        profileMaintainer = self.getProfileMaintainer('tests/data2.html')
        profile = profileMaintainer.profiles[0]
        self.assertEqual(profile.values[ProfileFields.NAME], "csafn cxdb zfx")
        self.assertEqual(profile.values[ProfileFields.DOB], profile.translateNumbers(ProfileFields.DOB, "!(^) km]a|'j/L !!"))
        self.assertEqual(profile.values[ProfileFields.BIRTH_DISTRICT], "slkna:t', si0fgu/")
        self.assertEqual(profile.values[ProfileFields.PAST_EXPERIENCE], "sfg\"g Joj;foL")
        self.assertEqual(profile.values[ProfileFields.FOREIGN_VISITS], "cd]l/sf, ?;, ax/fOg, ;fpbL c/laof, a+unfb]z / ef/t .")
        # self.assertEqual(profile.values[ProfileFields.BIRTH_VDC], "")
        # self.assertEqual(profile.values[ProfileFields.BIRTH_WARD], "&")
