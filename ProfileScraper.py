#!/usr/local/bin/python
# coding: windows-1252

import re
import copy
import csv
from UnicodeConverter import UnicodeConverter

class ProfileFields:
    NAME = 100
    DOB = 101

    BIRTH_HEADER = 200
    BIRTH_DISTRICT = 201
    BIRTH_VDC = 202
    BIRTH_WARD = 203
    
    PADDRESS_HEADER = 300
    PADDRESS_DISTRICT = 301
    PADDRESS_VDC = 302
    PADDRESS_WARD = 303
    PADDRESS_TOLE = 304
    
    KADDRESS_HEADER = 320
    KADDRESS_DISTRICT = 321
    KADDRESS_VDC = 322
    KADDRESS_WARD = 323
    KADDRESS_TOLE = 324

    CONTACT_MOBILE = 400
    CONTACT_EMAIL = 401
    CONTACT_PHONE_VALLEY = 402 
    CONTACT_PHONE_DISTRICT = 403

    FATHER_NAME = 110
    MOTHER_NAME = 111
    MARITAL_STATUS = 112
    SPOUSE_NAME = 113
    CHILDREN_SONS =  114
    CHILDREN_DAUGHTERS = 115

    EDUCATION_QUALIFICATION = 120
    EDUCATION_MAJOR = 121

    ELECTED_HEADER = 499
    ELECTED_PROCESS = 500
    ELECTED_DISTRICT = 501
    ELECTED_CONSTITUENCY = 502 

    PARTY = 503
    PARTY_STARTED_YEAR = 504

    POLITICAL_UNDERGROUND_YEARS = 505
    POLITICAL_NIRWASAN_YEARS = 506
    POLITICAL_PRISONED_STATUS = 507

    PAST_EXPERIENCE = 125

    PUBLICATIONS = 130
    FOREIGN_VISITS = 140
    OTHER_INFO = 150

    PAGE_NUMBER = 1000

    @staticmethod
    def getFieldOrder():
        return [
            ProfileFields.NAME,
            ProfileFields.DOB,
            ProfileFields.BIRTH_DISTRICT,
            ProfileFields.BIRTH_VDC,
            ProfileFields.BIRTH_WARD,
            ProfileFields.PADDRESS_DISTRICT,
            ProfileFields.PADDRESS_VDC,
            ProfileFields.PADDRESS_WARD,
            ProfileFields.PADDRESS_TOLE,
            ProfileFields.KADDRESS_DISTRICT,
            ProfileFields.KADDRESS_VDC,
            ProfileFields.KADDRESS_WARD,
            ProfileFields.KADDRESS_TOLE,
            ProfileFields.CONTACT_MOBILE,
            ProfileFields.CONTACT_EMAIL,
            ProfileFields.CONTACT_PHONE_VALLEY,
            ProfileFields.CONTACT_PHONE_DISTRICT,
            ProfileFields.FATHER_NAME,
            ProfileFields.MOTHER_NAME,
            ProfileFields.MARITAL_STATUS,
            ProfileFields.SPOUSE_NAME,
            ProfileFields.CHILDREN_SONS,
            ProfileFields.CHILDREN_DAUGHTERS,
            ProfileFields.EDUCATION_QUALIFICATION,
            ProfileFields.EDUCATION_MAJOR,
            ProfileFields.ELECTED_PROCESS,
            ProfileFields.ELECTED_DISTRICT,
            ProfileFields.ELECTED_CONSTITUENCY,
            ProfileFields.PARTY,
            ProfileFields.PARTY_STARTED_YEAR,
            ProfileFields.POLITICAL_UNDERGROUND_YEARS,
            ProfileFields.POLITICAL_NIRWASAN_YEARS,
            ProfileFields.POLITICAL_PRISONED_STATUS,
            ProfileFields.PAST_EXPERIENCE,
            ProfileFields.PUBLICATIONS,
            ProfileFields.FOREIGN_VISITS,
            ProfileFields.OTHER_INFO,
            ProfileFields.PAGE_NUMBER   
        ]   

    @staticmethod
    def getFieldHeader():
        return {
            ProfileFields.NAME : "Name",
            ProfileFields.DOB : "Dob",
            ProfileFields.BIRTH_DISTRICT : "Birth_district",
            ProfileFields.BIRTH_VDC : "Birth_vdc",
            ProfileFields.BIRTH_WARD : "Birth_ward",
            ProfileFields.PADDRESS_DISTRICT : "Paddress_district",
            ProfileFields.PADDRESS_VDC : "Paddress_vdc",
            ProfileFields.PADDRESS_WARD : "Paddress_ward",
            ProfileFields.PADDRESS_TOLE : "Paddress_tole",
            ProfileFields.KADDRESS_DISTRICT : "Kaddress_district",
            ProfileFields.KADDRESS_VDC : "Kaddress_vdc",
            ProfileFields.KADDRESS_WARD : "Kaddress_ward",
            ProfileFields.KADDRESS_TOLE : "Kaddress_tole",
            ProfileFields.CONTACT_MOBILE : "Contact_mobile",
            ProfileFields.CONTACT_EMAIL : "Contact_email",
            ProfileFields.CONTACT_PHONE_VALLEY : "Contact_phone_valley",
            ProfileFields.CONTACT_PHONE_DISTRICT : "Contact_phone_district",
            ProfileFields.FATHER_NAME : "Father_name",
            ProfileFields.MOTHER_NAME : "Mother_name",
            ProfileFields.MARITAL_STATUS : "Marital_status",
            ProfileFields.SPOUSE_NAME : "Spouse_name",
            ProfileFields.CHILDREN_SONS : "Children_sons",
            ProfileFields.CHILDREN_DAUGHTERS : "Children_daughers",
            ProfileFields.EDUCATION_QUALIFICATION : "Education_qualification",
            ProfileFields.EDUCATION_MAJOR : "Education_major",
            ProfileFields.ELECTED_PROCESS : "Elected_process",
            ProfileFields.ELECTED_DISTRICT : "Elected_district",
            ProfileFields.ELECTED_CONSTITUENCY : "Elected_constituency",
            ProfileFields.PARTY : "Party",
            ProfileFields.PARTY_STARTED_YEAR : "Party_started_year",
            ProfileFields.POLITICAL_UNDERGROUND_YEARS : "Political_underground_years",
            ProfileFields.POLITICAL_NIRWASAN_YEARS : "Political_nirwasan_years",
            ProfileFields.POLITICAL_PRISONED_STATUS : "Political_prisoned_status",
            ProfileFields.PAST_EXPERIENCE : "Past_experience",
            ProfileFields.PUBLICATIONS : "Publications",
            ProfileFields.FOREIGN_VISITS : "Foreign_visits",
            ProfileFields.OTHER_INFO : "Other_info",
            ProfileFields.PAGE_NUMBER : "Page_number",      
        }     

class Profile: 
    def __init__(self):
        self.uniconv = UnicodeConverter()
        self.reset()
        pass

    def reset(self):
        self.values = {}

    def __str__(self):
        s = ""
        for f in self.values:
            s = s + "\r\nField " + str(f) + ": " + self.getUnicodeFieldValue(self.values[f])
        return s

    def setFieldValue(self, field, value):
        value = value.replace('&amp;','&');
        value = value.replace('&quot;','"');
        value = self.translateNumbers(field, value)
        self.values[field] = value.strip()

    def translateNumbers(self, field, value):
        if field in [ProfileFields.DOB, ProfileFields.PAGE_NUMBER, ProfileFields.CONTACT_MOBILE, ProfileFields.CONTACT_PHONE_DISTRICT, ProfileFields.CONTACT_PHONE_VALLEY]:
            replaceDict = {'1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')','/':'='} 
            for key, replacement in replaceDict.items():  
                value = value.replace(key, replacement)
            return value
        return value

    def isDate(self, value):
        m = re.findall('([0-9/ ]*)', value)
        if m and m[0]:
            return True
        return False

    def getValue(self, field):
        if field in self.values:
            return self.values[field]
        return ""

    def getUnicodeFieldValue(self, field):
        if field in self.values:
            val = self.values[field]
            valUnicode = self.uniconv.convert(val)
            error = ' [x]' if self.uniconv.hasNonAscii() else '';
            return (valUnicode + error)
        return ""

class CSVProfileExport:
    def __init__(self, filename, profiles):
        self.outfile = open(filename, 'w')
        self.csvwriter = csv.writer(self.outfile, delimiter=',',quotechar='"')
        if profiles:
            self.setProfiles(profiles)

    def setProfiles(self, profiles):
        self.profiles = profiles
        self.process()

    def getHeader(self):
        row = []
        header = ProfileFields.getFieldHeader()
        for field in ProfileFields.getFieldOrder():
            row.append(header[field])
        return row


    def process(self):
        self.csvwriter.writerow(self.getHeader())
        for p in self.profiles:
            self.csvwriter.writerow(self.getCSVRow(p))

    def getCSVRow(self, profile):
        row = []
        for field in ProfileFields.getFieldOrder():
            if field in [ProfileFields.CONTACT_EMAIL]:
                row.append(profile.getValue(field))
            else:
                row.append(profile.getUnicodeFieldValue(field).encode('utf-8'))
        return row


class ProfileMaintainer:
    def __init__(self):
        self.profile = Profile()
        self.profiles = []

    def getMultiLineFieldValue(self, field, linePatternFinder):
            previousValue = self.profile.values[field] if field in self.profile.values else ""
            return str(previousValue) + " " + str(linePatternFinder.getFieldValue())

    def setLinePatternFinder(self, linePatternFinder):
        if linePatternFinder.getFoundField():
            if linePatternFinder.getFoundField() in [ProfileFields.FOREIGN_VISITS, ProfileFields.PAST_EXPERIENCE]:
                self.profile.setFieldValue(linePatternFinder.getFoundField(), self.getMultiLineFieldValue(linePatternFinder.getFoundField(), linePatternFinder))
            else:
                self.profile.setFieldValue(linePatternFinder.getFoundField(), linePatternFinder.getFieldValue())
        if linePatternFinder.getFoundField() == ProfileFields.PAGE_NUMBER:
            self.profiles.append(copy.copy(self.profile))
            self.profile.reset()

class LinePatternFinder:
    def __init__(self):
        self.stage = 0;
        pass

    def setLine(self, line):
        #remove tags
        self.line = re.sub('<[^>]*>', '', line).strip()
        self.foundField = False
        self.value = False;
        self.process()

    def getFoundField(self):
        return self.foundField;

    def getFieldValue(self):
        return self.value.strip()

    def process(self):
        self.checkName() or \
        self.checkDob() or \
        self.checkBirthDistrictVDC() or self.checkBirthDistrict() or self.checkBirthVDC() or self.checkBirthWard() or \
        self.checkPAddressHeader() or self.checkPAddressDistrict() or self.checkPAddressVDC() or self.checkPAddressWard() or self.checkPAddressTole() or \
        self.checkKAddressHeader() or self.checkKAddressDistrict() or self.checkKAddressVDC() or self.checkKAddressWard() or self.checkKAddressTole() or \
        self.checkContactMobileAndPhoneValley() or self.checkContactEmailAndPhoneValley() or \
        self.checkContactMobile() or self.checkContactEmail() or self.checkPhoneValley() or self.checkPhoneDistrict() or \
        self.checkFatherName() or self.checkMotherName() or self.checkSpouseName() or self.checkSonCount() or self.checkDaughterCount() or \
        self.checkEducationQualifcation() or self.checkEducationMajor() or \
        self.checkParty() or self.checkPartyStartedYear() or \
        self.checkElectedProcess() or self.checkElectedDistrict() or self.checkElectedConstituency() or \
        self.checkUndergroundYears() or self.checkNirwasanYears() or self.checkPrisonedStatus() or \
        self.checkPastExperience() or \
        self.checkPublications() or \
        self.checkForeignVisits() or \
        self.checkOtherInfo() or \
        self.checkEndPageNumber() or \
        self.checkFreeText() 
        
    
    def getProfileId(self, line):
        m = re.findall('<A name=([0-9]*)', line)
        if m and m[0]:
            return m[0]
        return False

    def checkName(self):
        # <A name=1></a>df=  cOGb| ;'Gb/ g]DjfË<br>
        m = re.findall('df= (.*)', self.line)
        if m and m[0]:
            self.foundField = ProfileFields.NAME
            self.value = m[0]
            return True
        return False

    def checkDob(self):
        # hGd ldlt M </span><span class="ft7">2034/07/12<br>
        m = re.findall('hGd ldlt M (.*)', self.line)
        if m and m[0]:
            self.foundField = ProfileFields.DOB
            self.value = m[0]
            return True
        return False

    def checkBirthDistrictVDC(self):
        # there are cases where district and vdc appears in the same line
        # hGd :yfg M lhNnf M slkna:t' uf=lj=;=÷g=kf= M si0fgu/
        # include both district and vdc in the same field. We will have to manually get to the vdc field.
        m = re.findall('hGd :yfg M lhNnf M (.*) uf=lj=;=÷g=kf= M(.*)', self.line)
        if m and m[0]:
            self.stage = ProfileFields.BIRTH_HEADER
            self.foundField = ProfileFields.BIRTH_DISTRICT
            self.value = m[0][0] + "," + m[0][1]
            return True
        return False

    def checkBirthDistrict(self):
        m = re.findall('hGd :yfg M lhNnf M (.*)', self.line)
        if m and m[0]:
            self.stage = ProfileFields.BIRTH_HEADER
            self.foundField = ProfileFields.BIRTH_DISTRICT
            self.value = m[0]            
            return True
        return False

    def checkBirthVDC(self):
        # uf=lj=;=÷g=kf= M ODj'ª<br>        ÷
        m = re.findall('uf=lj=;=÷g=kf= M(.*)', self.line)
        if self.stage == ProfileFields.BIRTH_HEADER and m and m[0]:
            self.foundField = ProfileFields.BIRTH_VDC
            self.value = m[0]
            return True
        return False

    def checkBirthWard(self):
        # j8f g+= M !<br>
        m = re.findall('j8f g\+= M (.*)', self.line)
        if self.stage == ProfileFields.BIRTH_HEADER and m and m[0]:
            self.foundField = ProfileFields.BIRTH_WARD
            self.value = m[0]
            return True
        return False

    def checkPAddressHeader(self):
        m = re.findall(':yfoL 7]ufgf M', self.line)
        if m and m[0]:
            self.stage = ProfileFields.PADDRESS_HEADER
            self.foundField = ProfileFields.PADDRESS_HEADER
            self.value = ""
            return True
        return False

    def checkPAddressDistrict(self):
        #lhNnf M kfFry/<br>
        m = re.findall('lhNnf M (.*)', self.line)
        if self.stage == ProfileFields.PADDRESS_HEADER and m and m[0]:
            self.foundField = ProfileFields.PADDRESS_DISTRICT
            self.value = m[0]
            return True
        return False

    def checkPAddressVDC(self):
        #lhNnf M kfFry/<br>
        m = re.findall('uf=lj=;=÷g=kf= M (.*)', self.line)
        if self.stage == ProfileFields.PADDRESS_HEADER and m and m[0]:
            self.foundField = ProfileFields.PADDRESS_VDC
            self.value = m[0]
            return True
        return False

    def checkPAddressWard(self):
        #lhNnf M kfFry/<br>
        m = re.findall('j8f g\+= M (.*)', self.line)
        if self.stage == ProfileFields.PADDRESS_HEADER and m and m[0]:
            self.foundField = ProfileFields.PADDRESS_WARD
            self.value = m[0]
            return True
        return False

    def checkPAddressTole(self):
        #6f]n M em08]gu/<br>
        m = re.findall('6f]n M (.*)', self.line)
        if self.stage == ProfileFields.PADDRESS_HEADER and m and m[0]:
            self.foundField = ProfileFields.PADDRESS_TOLE
            self.value = m[0]
            return True
        return False

    def checkKAddressHeader(self):
        m = re.findall('sf7df08f} pkTosfsf] 7]ufgf M', self.line)
        if m and m[0]:
            self.stage = ProfileFields.KADDRESS_HEADER
            self.foundField = ProfileFields.KADDRESS_HEADER
            self.value = ""
            return True
        return False

    def checkKAddressDistrict(self):
        #lhNnf M kfFry/<br>
        m = re.findall('lhNnf M (.*)', self.line)
        if self.stage == ProfileFields.KADDRESS_HEADER and m and m[0]:
            self.foundField = ProfileFields.KADDRESS_DISTRICT
            self.value = m[0]
            return True
        return False

    def checkKAddressVDC(self):
        m = re.findall('uf=lj=;=÷g=kf= M (.*)', self.line)
        if self.stage == ProfileFields.KADDRESS_HEADER and m and m[0]:
            self.foundField = ProfileFields.KADDRESS_VDC
            self.value = m[0]
            return True
        return False

    def checkKAddressWard(self):
        m = re.findall('j8f g\+= M (.*)', self.line)
        if self.stage == ProfileFields.KADDRESS_HEADER and m and m[0]:
            self.foundField = ProfileFields.KADDRESS_WARD
            self.value = m[0]
            return True
        return False

    def checkKAddressTole(self):
        m = re.findall('6f\]n M (.*)', self.line)
        if self.stage == ProfileFields.KADDRESS_HEADER and m and m[0]:
            self.foundField = ProfileFields.KADDRESS_TOLE
            self.value = m[0]
            return True
        return False

    def checkContactMobileAndPhoneValley(self):
        # there are cases where both mobile and phone-valley are in the same line, put that in the email
        # df]afOn M 9851143079, 9801143079 lgjf; -pkTosf_ M )!Â­$))))!%
        m = re.findall('df]afOn M(.*)lgjf; -pkTosf_ M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.CONTACT_MOBILE
            self.value = m[0][0] + "," + m[0][1]
            return True
        return False

    def checkContactMobile(self):
        #df]afOn M 9851032405
        m = re.findall('df\]afOn M(.*)', self.line)
        if m and m[0]:
            self.foundField = ProfileFields.CONTACT_MOBILE
            self.value = m[0]
            return True
        return False

    def checkContactEmailAndPhoneValley(self):
        # there are cases where both email and phone-district are in the same line, put that in the email
        # Od]n M paudel.ananta@yahoo.com lgjf; -lhNNff_ M
        m = re.findall('Od]n M(.*)lgjf; -lhNNff_ M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.CONTACT_EMAIL
            self.value = m[0][0] + "," + m[0][1]
            return True
        return False

    def checkContactEmail(self):
        # Od]n M arjunnkc@gmail.com
        m = re.findall('Od]n M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.CONTACT_EMAIL
            self.value = m[0]
            return True
        return False

    def checkPhoneValley(self):
        # lgjf; -pkTosf_ M 01-433270
        m = re.findall('lgjf; -pkTosf_ M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.CONTACT_PHONE_VALLEY
            self.value = m[0]
            return True
        return False

    def checkPhoneDistrict(self):
        # lgjf; -lhNNff_ M
        m = re.findall('lgjf; -lhNNff_ M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.CONTACT_PHONE_DISTRICT
            self.value = m[0]
            return True
        return False

    def checkFatherName(self):
        # afa'sf] gfd M cAb'nf ;nfd zfx
        m = re.findall('afa\'sf\] gfd M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.FATHER_NAME
            self.value = m[0]
            return True
        return False

    def checkMotherName(self):
        # cfdfsf] gfd M cfP;f vft'g
        m = re.findall('cfdfsf\] gfd M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.MOTHER_NAME
            self.value = m[0]
            return True
        return False

    def checkSpouseName(self):
        #klt÷kTgLsf] gfd M gkmL; hFxf zfx
        m = re.findall('klt÷kTgLsf\] gfd M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.SPOUSE_NAME
            self.value = m[0]
            return True
        return False

    def checkSonCount(self):
        #5f]/f M #
        m = re.findall('5f\]\/f M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.CHILDREN_SONS
            self.value = m[0]
            return True
        return False

    def checkDaughterCount(self):
        #5f]/L M @
        m = re.findall('5f\]/L M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.CHILDREN_DAUGHTERS
            self.value = m[0]
            return True
        return False

    def checkEducationQualifcation(self):
        #z}lIfs of]Uotf M :gfts<br>
        m = re.findall('z\}lIfs of\]Uotf M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.EDUCATION_QUALIFICATION
            self.value = m[0]
            return True
        return False

    def checkEducationMajor(self):
        #cWoogsf] ljifo M dfgljsL<br>
        m = re.findall('cWoogsf\] ljifo M (.*)', self.line)
        if m and m[0]:
            self.foundField = ProfileFields.EDUCATION_MAJOR
            self.value = m[0]
            return True
        return False

    def checkParty(self):
        #bnLo ;+nUgtf M t/fO{­dw]z nf]stflGqs kf6L{<br>
        m = re.findall('bnLo ;\+nUgtf M (.*)', self.line)
        if m and m[0]:
            self.foundField = ProfileFields.PARTY
            self.value = m[0]
            return True
        return False

    def checkPartyStartedYear(self):
        #/fhgLlts bndf cfa4 ePsf] jif{ M lj=;= @)#^<br>
        m = re.findall('/fhgLlts bndf cfa4 ePsf\] jif\{ M(.*)', self.line)
        if m and len(m):
            self.foundField = ProfileFields.PARTY_STARTED_YEAR
            self.value = m[0]
            return True
        return False

    def checkElectedProcess(self):
        m = re.findall('lgjf{rg k\|s\[of M(.*)', self.line)
        if m and m[0]:
            self.stage = ProfileFields.ELECTED_HEADER
            return True
        return False

    def checkElectedDistrict(self):
        m = re.findall('lhNnf M(.*)', self.line)
        if self.stage == ProfileFields.ELECTED_HEADER and m and m[0]:
            self.foundField = ProfileFields.ELECTED_DISTRICT
            self.value = m[0]
            return True
        return False

    def checkElectedConstituency(self):
        m = re.findall('lgjf{rg If\]q g\+= M(.*)', self.line)
        if self.stage == ProfileFields.ELECTED_HEADER and m and len(m)>0:
            self.foundField = ProfileFields.ELECTED_CONSTITUENCY
            self.value = m[0]
            return True
        return False

    def checkUndergroundYears(self):
        # s_ e"ldut jif{ M @)%& b]lv @)^# ;Dd
        m = re.findall('s_ e"ldut jif{ M(.*)', self.line)
        if m and len(m)>0:
            self.foundField = ProfileFields.POLITICAL_UNDERGROUND_YEARS
            self.value = m[0]
            return True
        return False

    def checkNirwasanYears(self):
        # v_ lgjf{;g jif{ M !
        m = re.findall('v_ lgjf{;g jif{ M(.*)', self.line)
        if m and len(m)>0:
            self.foundField = ProfileFields.POLITICAL_NIRWASAN_YEARS
            self.value = m[0]
            return True
        return False

    def checkPrisonedStatus(self):
        # u_ aGbL hLjg M @ jif{
        m = re.findall('u_ aGbL hLjg M(.*)', self.line)
        if m and len(m)>0:
            self.foundField = ProfileFields.POLITICAL_PRISONED_STATUS
            self.value = m[0]
            return True
        return False

    def checkPastExperience(self):
        #ljutsf] k]zf / cg'ej M lzIfs -
        m = re.findall('^ljutsf\] k\]zf / cg\'ej M(.*)', self.line)
        if m and len(m)>0:
            self.stage = ProfileFields.PAST_EXPERIENCE
            self.foundField = ProfileFields.PAST_EXPERIENCE
            self.value = m[0]
            return True
        return False

    def checkPublications(self):
        # s[ltÃ·k|sfzg M
        # s[lt÷k|sfzg M<br>
        m = re.findall('s\[lt÷k\|sfzg M(.*)', self.line)
        if m and len(m)>0:
            self.stage = 0
            self.foundField = ProfileFields.PUBLICATIONS
            self.value = m[0]
            return True
        return False

    def checkForeignVisits(self):
        m = re.findall('ljb\]z e\|d0f M(.*)', self.line)
        if m and m[0]:
            self.stage = ProfileFields.FOREIGN_VISITS
            self.foundField = ProfileFields.FOREIGN_VISITS
            self.value = m[0]
            return True
        return False

    def checkFreeText(self):
        m = re.findall('^(.*)$', self.line)
        if self.stage == ProfileFields.PAST_EXPERIENCE and m and m[0]:
            self.foundField = ProfileFields.PAST_EXPERIENCE
            self.value = m[0]
            return True
        if self.stage == ProfileFields.FOREIGN_VISITS and m and m[0]:
            self.foundField = ProfileFields.FOREIGN_VISITS
            self.value = m[0]
            return True
        return False

    def checkOtherInfo(self):
        m = re.findall('cGo M(.*)', self.line)
        if m and len(m)>0:
            self.stage = 0
            self.foundField = ProfileFields.OTHER_INFO
            self.value = m[0]
            return True
        return False

    def checkEndPageNumber(self):
        #2<br>
        m = re.findall('^([0-9]{1,3})$', self.line)
        if m and m[0]:
            self.stage = 0
            self.foundField = ProfileFields.PAGE_NUMBER
            self.value = m[0]
            return True
        return False
        
