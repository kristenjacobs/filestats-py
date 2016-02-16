#!/usr/bin/python

import codecs
import os.path
import sys

class LineCount:
    def __init__(self):
        self.numLines = 0

    def analyse(self, line):
        self.numLines += 1

    def display(self):
        print "lines: " + str(self.numLines)


class WordCount:
    def __init__(self):
        self.numWords = 0

    def analyse(self, line):
        self.numWords += len(line.split())

    def display(self):
        print "words: " + str(self.numWords)


class AvgLettersPerWord:
    def __init__(self):
        self.numLetters = 0
        self.numWords = 0

    def analyse(self, line):
        self.numLetters += len([c for c in line if c.isalpha()])  
        self.numWords += len(line.split())

    def display(self):
        alpw = float(self.numLetters) / float(self.numWords) \
                   if self.numWords > 0 else 0.0
        print "average letters per word: %.1f" % alpw


class MostCommonLetters:
    def __init__(self):
        self.letterFrequencyMap = {}

    def analyse(self, line):
        for character in line:
            if character.isalpha():
                letter = character.lower()
                if letter in self.letterFrequencyMap:
                    self.letterFrequencyMap[letter] += 1
                else:
                    self.letterFrequencyMap[letter] = 1

    def display(self):
        mostCommonLetters = []
        if self.letterFrequencyMap:
            maxFreq = max(self.letterFrequencyMap.values())
            mostCommonLetters = sorted(
                    [letter for letter, freq in self.letterFrequencyMap.items() 
                        if freq == maxFreq])
        print "most common letter: " + ','.join(mostCommonLetters)


def analyse(fileName, stats):
    """
    This function calculates the stats for the given file. 
    It returns updated versions of the given statistics instances.
    """
    # Reads in the input file, assuming a UTF-8 format, one line at a time.
    with codecs.open(fileName, "r", "utf-8") as f:
        for line in f:
            for stat in stats:
                stat.analyse(line)
    return stats


def display(stats):
    for stat in stats:
        stat.display()


def main():
    if len(sys.argv) != 2:
        print "Error: Invalid arguments."
        print "  Usage:"
        print "    python filestats.py <file>"
        sys.exit(1)

    fileName = sys.argv[1]
    
    if not os.path.isfile(fileName):
        print "Error: Unable to open file: " + fileName
        sys.exit(1)

    try:
        stats = [LineCount(), WordCount(), AvgLettersPerWord(), MostCommonLetters()]
        display(analyse(fileName, stats))
    except UnicodeDecodeError:
        print "Error: File is not UTF-8 format"


if __name__ == "__main__":
    main()
