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
        self.scraper =  LinePatternFinder()

    def testName(self):
        self.scraper.setLine("<A name=1></a>df=  cOGb| ;'Gb/ g]DjfË<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.NAME);
        self.assertEqual(self.scraper.getFieldValue(), "df=  cOGb| ;'Gb/ g]DjfË");

    def testDOB(self):
        self.scraper.setLine("hGd ldlt M </span><span class=\"ft7\">2034/07/12<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.DOB);
        self.assertEqual(self.scraper.getFieldValue(), "2034/07/12");

    def testBirthDistrict(self):
        self.scraper.setLine("hGd :yfg M lhNnf M kfFry/<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.BIRTH_DISTRICT);
        self.assertEqual(self.scraper.getFieldValue(), "lhNnf M kfFry/");

    def testBirthVDC(self):
        self.scraper.setLine("hGd :yfg M lhNnf M kfFry/<br>")
        self.scraper.setLine("uf=lj=;=÷g=kf= M ODj'ª<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.BIRTH_VDC);
        self.assertEqual(self.scraper.getFieldValue(), "ODj'ª");

    def testBirthWard(self):
        self.scraper.setLine("hGd :yfg M lhNnf M kfFry/<br>")
        self.scraper.setLine("j8f g+= M !<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.BIRTH_WARD);
        self.assertEqual(self.scraper.getFieldValue(), "!");

    def testPAddressHeader(self):
        self.scraper.setLine(":yfoL 7]ufgf M")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PADDRESS_HEADER);
        self.assertEqual(self.scraper.getFieldValue(), "");

    def testPAddressDistrict(self):
        self.scraper.setLine(":yfoL 7]ufgf M")
        self.scraper.setLine("lhNnf M kfFry/<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PADDRESS_DISTRICT);
        self.assertEqual(self.scraper.getFieldValue(), "kfFry/");

    def testPAddressVDC(self):
        self.scraper.setLine(":yfoL 7]ufgf M")
        self.scraper.setLine("uf=lj=;=÷g=kf= M s[i0fgu/<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PADDRESS_VDC);
        self.assertEqual(self.scraper.getFieldValue(), "s[i0fgu/");

    def testPAddressWard(self):
        self.scraper.setLine(":yfoL 7]ufgf M")
        self.scraper.setLine("j8f g+= M &<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PADDRESS_WARD);
        self.assertEqual(self.scraper.getFieldValue(), "&");

    def testPAddressTole(self):
        self.scraper.setLine(":yfoL 7]ufgf M")
        self.scraper.setLine("6f]n M em08]gu/<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PADDRESS_TOLE);
        self.assertEqual(self.scraper.getFieldValue(), "em08]gu/");

    def testKAddressHeader(self):
        self.scraper.setLine("sf7df08f} pkTosfsf] 7]ufgf M<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.KADDRESS_HEADER);
        self.assertEqual(self.scraper.getFieldValue(), "");

    def testKAddressDistrict(self):
        self.scraper.setLine("sf7df08f} pkTosfsf] 7]ufgf M<br>")
        self.scraper.setLine("lhNnf M kfFry/<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.KADDRESS_DISTRICT);
        self.assertEqual(self.scraper.getFieldValue(), "kfFry/");

    def testKAddressVDC(self):
        self.scraper.setLine("sf7df08f} pkTosfsf] 7]ufgf M<br>")
        self.scraper.setLine("uf=lj=;=÷g=kf= M s[i0fgu/<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.KADDRESS_VDC);
        self.assertEqual(self.scraper.getFieldValue(), "s[i0fgu/");

    def testKAddressWard(self):
        self.scraper.setLine("sf7df08f} pkTosfsf] 7]ufgf M<br>")
        self.scraper.setLine("j8f g+= M &<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.KADDRESS_WARD);
        self.assertEqual(self.scraper.getFieldValue(), "&");

    def testKAddressTole(self):
        self.scraper.setLine("sf7df08f} pkTosfsf] 7]ufgf M<br>")
        self.scraper.setLine("6f]n M em08]gu/<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.KADDRESS_TOLE);
        self.assertEqual(self.scraper.getFieldValue(), "em08]gu/");

    def testEducationQualification(self):
        self.scraper.setLine("z}lIfs of]Uotf M :gfts<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.EDUCATION_QUALIFICATION);
        self.assertEqual(self.scraper.getFieldValue(), ":gfts");

    def testEducationMajor(self):
        self.scraper.setLine("cWoogsf] ljifo M dfgljsL<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.EDUCATION_MAJOR);
        self.assertEqual(self.scraper.getFieldValue(), "dfgljsL");

    def testParty(self):
        self.scraper.setLine("bnLo ;+nUgtf M t/fO{­dw]z nf]stflGqs kf6L{<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PARTY);
        self.assertEqual(self.scraper.getFieldValue(), "t/fO{­dw]z nf]stflGqs kf6L{");


    def testPartyStartedYear(self):
        self.scraper.setLine("/fhgLlts bndf cfa4 ePsf] jif{ M lj=;= @)#^<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PARTY_STARTED_YEAR);
        self.assertEqual(self.scraper.getFieldValue(), "lj=;= @)#^");


unittest.main()

