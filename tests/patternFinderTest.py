#!/usr/local/bin/python
# coding: windows-1252
import unittest
import sys

from ProfileScraper import *

class PatternFinderTest(unittest.TestCase):
    def setUp(self):
        self.profile = Profile();
        self.scraper =  LinePatternFinder()

    def testName(self):
        self.scraper.setLine("<A name=1></a>df= cOGb| ;'Gb/ g]DjfË<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.NAME);
        self.assertEqual(self.scraper.getFieldValue(), "cOGb| ;'Gb/ g]DjfË")
        self.scraper.setLine("<A name=11></a>df= c~hgf tfDnL<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.NAME)
        self.assertEqual(self.scraper.getFieldValue(), "c~hgf tfDnL")

    def testDOB(self):
        self.scraper.setLine("hGd ldlt M </span><span class=\"ft7\">2034/07/12<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.DOB);
        self.assertEqual(self.scraper.getFieldValue(), "2034/07/12");

    def testBirthDistrictVDC(self):        
        #hGd :yfg M lhNnf M slkna:t' uf=lj=;=÷g=kf= M si0fgu/
        self.scraper.setLine("hGd :yfg M lhNnf M slkna:t' uf=lj=;=÷g=kf= M si0fgu/<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.BIRTH_DISTRICT);
        self.assertEqual(self.scraper.getFieldValue(), "slkna:t', si0fgu/");

    def testBirthDistrict(self):        
        self.scraper.setLine("hGd :yfg M lhNnf M kfFry/<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.BIRTH_DISTRICT);
        self.assertEqual(self.scraper.getFieldValue(), "kfFry/");

    def testBirthVDC(self):
        self.scraper.setLine("hGd :yfg M lhNnf M kfFry/<br>")
        #uf=lj=;=÷g=kf= M ODj'ª
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
        self.scraper.setLine("/fhgLlts bndf cfa4 ePsf] jif{ M<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PARTY_STARTED_YEAR);
        self.assertEqual(self.scraper.getFieldValue(), "");

    def testElectedDistrict(self):
        self.scraper.setLine("lgjf{rg k|s[of M k|ToIf<br>")
        self.scraper.setLine("lhNnf M slknj:t'<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.ELECTED_DISTRICT);
        self.assertEqual(self.scraper.getFieldValue(), "slknj:t'");

    def testElectedConstituency(self):
        self.scraper.setLine("lgjf{rg k|s[of M k|ToIf")
        self.scraper.setLine("lgjf{rg If]q g+= M !<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.ELECTED_CONSTITUENCY);
        self.assertEqual(self.scraper.getFieldValue(), "!");
        self.scraper.setLine("lgjf{rg If]q g+= M<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.ELECTED_CONSTITUENCY);
        self.assertEqual(self.scraper.getFieldValue(), "");

    def testUndergroundYears(self):
        self.scraper.setLine("s_ e\"ldut jif{ M @)%& b]lv @)^# ;Dd")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.POLITICAL_UNDERGROUND_YEARS);
        self.assertEqual(self.scraper.getFieldValue(), "@)%& b]lv @)^# ;Dd");

    def testNirwasanYears(self):
        self.scraper.setLine("v_ lgjf{;g jif{ M !")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.POLITICAL_NIRWASAN_YEARS);
        self.assertEqual(self.scraper.getFieldValue(), "!");

    def testPrisonedStatus(self):
        self.scraper.setLine("u_ aGbL hLjg M @ jif{<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.POLITICAL_PRISONED_STATUS);
        self.assertEqual(self.scraper.getFieldValue(), "@ jif{");

    def testPastExperience(self):
        self.scraper.setLine("ljutsf] k]zf / cg'ej M lzIfs -!^ jif{_, dlxnf ;+3, blnt ;+3 / lzIfs ;+3df /xL sfo{")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PAST_EXPERIENCE);
        self.assertEqual(self.scraper.getFieldValue(), "lzIfs -!^ jif{_, dlxnf ;+3, blnt ;+3 / lzIfs ;+3df /xL sfo{");
        self.scraper.setLine("ljutsf] k]zf / cg'ej M sfg&quot;g Joj;foL")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PAST_EXPERIENCE);
        self.assertEqual(self.scraper.getFieldValue(), "sfg&quot;g Joj;foL");

    def testPastExperienceMultiLine(self):
        self.scraper.setLine("ljutsf] k]zf / cg'ej M lzIfs -!^ jif{_, dlxnf ;+3, blnt ;+3 / lzIfs ;+3df /xL sfo{")
        self.scraper.setLine("u/]sf] . g]kfnL sfFu|]; lhNnf ;b:o, g]kfnL sfFu|]; s]Gb|Lo ;b:o -jg")              
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PAST_EXPERIENCE);
        self.assertEqual(self.scraper.getFieldValue(), "u/]sf] . g]kfnL sfFu|]; lhNnf ;b:o, g]kfnL sfFu|]; s]Gb|Lo ;b:o -jg");

    def testPublications(self):
        self.scraper.setLine("s[lt÷k|sfzg M<br>")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.PUBLICATIONS);
        self.assertEqual(self.scraper.getFieldValue(), "");

    def testForeignVisits(self):
        self.scraper.setLine("ljb]z e|d0f M ef/t, rLg, hfkfg, yfO{Nof08, kfls:tfg, j]nfot, hd{gL, k|mfG;, 8]gdfs{,")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.FOREIGN_VISITS);
        self.assertEqual(self.scraper.getFieldValue(), "ef/t, rLg, hfkfg, yfO{Nof08, kfls:tfg, j]nfot, hd{gL, k|mfG;, 8]gdfs{,");

    def testForeignVisitsMultiLine(self):
        self.scraper.setLine("ljb]z e|d0f M ef/t, rLg, hfkfg, yfO{Nof08, kfls:tfg, j]nfot, hd{gL, k|mfG;, 8]gdfs{,")
        self.scraper.setLine(":jL8]g, cd]l/sf, stf/ nufotsf b]zx? .")              
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.FOREIGN_VISITS);
        self.assertEqual(self.scraper.getFieldValue(), ":jL8]g, cd]l/sf, stf/ nufotsf b]zx? .");

    def testOtherInfo(self):
        self.scraper.setLine("cGo M @)$")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.OTHER_INFO);
        self.assertEqual(self.scraper.getFieldValue(), "@)$");
        self.scraper.setLine("cGo M")
        self.assertEqual(self.scraper.getFoundField(), ProfileFields.OTHER_INFO);
        self.assertEqual(self.scraper.getFieldValue(), "");

if __name__ == "__main__":
    unittest.main()


