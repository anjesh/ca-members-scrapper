#!/usr/local/bin/python
# coding: utf-8

import sys
import copy
import codecs
from ProfileScraper import *

sys.path.append('nep_ttf2utf')
from ttf2utf import rules_loader, converter

all_rules = rules_loader.load_rules('nep_ttf2utf/rules/')
rule = all_rules["preeti"]

profileCollections = []
profileMaintainer = ProfileMaintainer();

with open('testdata.html','rU') as f:
    scraper =  LinePatternFinder()
    for line in f:
        scraper.setLine(line)
        if scraper.getFoundField():
            profileMaintainer.setLinePatternFinder(scraper)
for p in profileMaintainer.profiles:
    v = p.getValues()
    for i in v:
        print i, v[i].encode("utf-8")

# with open('testdata.html','rU') as f:
#     scraper =  LinePatternFinder()
#     for line in f:
#         scraper.setLine(line)
#         if scraper.getFoundField():
#             if scraper.getFoundField() == ProfileFields.NAME:
#                 if not profile.isNew():
#                     profileCollections.append(copy.copy(profile))
#                     profile.reset()
#             try:
#                 value = scraper.getFieldValueAsciiOnly()
#                 conversionError = ""
#                 if len(value) != len(scraper.getFieldValue()):
#                     conversionError = "Error"
#                 value = (converter.word_convert(value, rule)).encode('utf-8')
#                 print value
#             except:
#                 print sys.exc_info()[0]
#                 value = scraper.getFieldValue()
                
                
#             profile.setFieldValue(scraper.getFoundField(), value + conversionError)
#     profileCollections.append(copy.copy(profile))

# for p in profileCollections:
#     print p
    # print p.getValues()
    # for i in p.values:
    #     print i






