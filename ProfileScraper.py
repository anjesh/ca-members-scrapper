#!/usr/local/bin/python
# coding: windows-1252

import re

class ProfileFields:
    NAME = 100
    DOB = 101
    BIRTH_DISTRICT = 200
    BIRTH_VDC = 201
    BIRTH_WARD = 202
    
    PADDRESS_DISTRICT = 300
    PADDRESS_VDC = 301
    PADDRESS_WARD = 302
    PADDRESS_TOLE = 303
    
    KADDRESS_DISTRICT = 300
    KADDRESS_VDC = 301
    KADDRESS_WARD = 302
    KADDRESS_TOLE = 303

    CONTACT_MOBILE = 400
    CONTACT_EMAIL = 401
    CONTACT_PHONE_VALLEY = 402 
    CONTACT_PHONE_DISTRICT = 403

    FATHER_NAME = 110
    MOTHER_NAME = 111
    MARITAL_STATUS = 112
    SPOUSE_NAME = 113
    CHILDREN_SONS =  114
    CHILDREN_DAUGHERS = 115

    EDUCATION_QUALIFICATION = 120
    EDUCATION_MAJOR = 121

    ELECTION_PROCESS = 500
    ELECTED_DISTRICT = 501
    ELECTED_CONSTITUENCY = 502 

    PARTY = 503
    PARTY_STARTED_YEAR = 504

    POLITICAL_UNDERGROUND_YEARS = 505
    POLITICAL_NIRWASAN_YEARS = 506
    POLITICAL_PRISONED_STATUS = 507

    PAST_EXPERIENCE = 120

    PUBLICATIONS = 130
    FOREIGN_VISITS = 140

class FieldPatterns:
    def setPatterns(self):
        self.patterns[ProfileFields.NAME] = '<A name=[0-9]*></a>([^<]*)<';
        self.patterns[ProfileFields.DOB] = 'hGd ldlt M </span><span[^>]*>([^<]*)<';

class Profile: 
    def __init__(self):
        self.values = {}
        pass

    def setFieldValue(self, field, value):
        self.values[field] = value

class ProfileScraper:
    def __init__(self, profile):
        self.profile = profile
        pass

    def setLine(self, line):
        self.line = line
        self.found = False
        self.foundField = False
        self.value = False;
        self.process();

    def getFoundField(self):
        return self.foundField;

    def getFieldValue(self):
        return self.value

    def process(self):
        self.checkName() or \
        self.checkDob() or self.checkBirthPlace() or\
        self.checkVDCMunicipality() or self.checkWard()
            
    def checkOneLineFieldPattern(self, fieldname, pattern):
        m = re.findall(pattern, self.line)
        if m and m[0]:
            self.foundField = fieldname
            self.value = m[0]
            self.profile.setFieldValue(self.foundField, self.value)
            return True

    def checkName(self):
        # <A name=1></a>df=  cOGb| ;'Gb/ g]DjfË<br>
        m = re.findall('<A name=[0-9]*></a>([^<]*)<', self.line)
        if m and m[0]:            
            self.foundField = ProfileFields.NAME
            self.value = m[0]
            self.profile.setFieldValue(self.foundField, self.value)
            return True
        return False

    def checkDob(self):
        # hGd ldlt M </span><span class="ft7">2034/07/12<br>
        m = re.findall('hGd ldlt M </span><span[^>]*>([^<]*)<', self.line)
        if m and m[0]:
            self.foundField = ProfileFields.DOB
            self.value = m[0]
            self.profile.setFieldValue(self.foundField, self.value)
            return True
        return False

    def checkBirthPlace(self):
        # hGd :yfg M lhNnf M kfFry/<br>
        m = re.findall('hGd :yfg M ([^<]*)<', self.line)
        if m and m[0]:
            self.foundField = ProfileFields.BIRTH_DISTRICT
            self.value = m[0]
            self.profile.setFieldValue(self.foundField, self.value)
            return True
        return False

    def checkVDCMunicipality(self):
        # uf=lj=;=÷g=kf= M ODj'ª<br>
        m = re.findall('uf=lj=;=÷g=kf= M ([^<]*)<', self.line)
        if m and m[0]:
            self.foundField = ProfileFields.BIRTH_VDC
            self.value = m[0]
            self.profile.setFieldValue(self.foundField, self.value)
            return True
        return False

    def checkWard(self):
        # j8f g+= M !<br>
        m = re.findall('j8f g\+= M ([^<]*)<', self.line)
        if m and m[0]:
            self.foundField = ProfileFields.BIRTH_WARD
            self.value = m[0]
            self.profile.setFieldValue(self.foundField, self.value)
            return True
        return False








