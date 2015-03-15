#!/usr/local/bin/python
# coding: utf-8

import sys
import codecs

sys.path.append('nep_ttf2utf')
from ttf2utf import rules_loader, converter

class UnicodeConverter:
    def __init__(self):
        all_rules = rules_loader.load_rules('nep_ttf2utf/rules/')
        self.rule = all_rules["preeti"]

    def convert(self, s):
        self.string = s
        self.asciiString = filter(lambda char: char == '\n' or 32 <= ord(char) <= 126, self.string)
        self.uni = (converter.word_convert(self.asciiString, self.rule))
        return self.uni

    def hasNonAscii(self):
        return not (self.string == self.asciiString)