#!/usr/local/bin/python
# coding: windows-1252
import unittest
from ProfileScraper import *

# with open('testdata.html') as f:
#     for line in f:
#         print line

class ScaperTest(unittest.TestCase):
    def setUp(self):
        self.profile = Profile();
        self.scraper =  ProfileScraper(self.profile)

    def testName(self):
        self.scraper.setLine("<A name=1></a>df=  cOGb| ;'Gb/ g]DjfË<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.NAME);
        self.assertEqual(self.scraper.getFieldValue(), "df=  cOGb| ;'Gb/ g]DjfË");

    def testDOB(self):
        self.scraper.setLine("hGd ldlt M </span><span class=\"ft7\">2034/07/12<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.DOB);
        self.assertEqual(self.scraper.getFieldValue(), "2034/07/12");

    def testBirthPlace(self):
        self.scraper.setLine("hGd :yfg M lhNnf M kfFry/<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.BIRTH_DISTRICT);
        self.assertEqual(self.scraper.getFieldValue(), "lhNnf M kfFry/");

    def testVDCMunicipality(self):
        self.scraper.setLine("uf=lj=;=÷g=kf= M ODj'ª<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.BIRTH_VDC);
        self.assertEqual(self.scraper.getFieldValue(), "ODj'ª");

    def testWard(self):
        self.scraper.setLine("j8f g+= M !<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.BIRTH_WARD);
        self.assertEqual(self.scraper.getFieldValue(), "!");

unittest.main()

