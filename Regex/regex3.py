import sys; args = sys.argv[1:]
idx = int(args[0])-50

myRegexLst = [
  r"/\w*(\w)\w*\1\w*/i",
  r"/\w*(\w)\w*(\1\w*){3}/i",
  r"/^([01])([10]*\1)*$/",
  r"/(?=\b\w{6}\b)\w*cat\w*/i",
  r"/(?=\b\w{5,9}\b)(?=\w*bri\w*)\w*ing\w*/i",
  r"/\b(?!\w*cat\w*)\w{6}\b/i",
  r"/\b(?!\w*(\w)\w*\1\w*)\w+\b/i",
  r"/^(1(?!0011)|0)*$/",
  r"/\b\w*([aeiou])(?!\1)[aeiou]\w*\b/i",
  r"/^(1(?!11)(?!01)|0)*$/"
  ]

if idx < len(myRegexLst):
    print(myRegexLst[idx])

import sys; args = sys.argv[1:]
idx = int(args[0])-50

myRegexLst = [
  r"/\b\w*(\w)\w*\1\w*\b/i"
  #r"/\b\w*?([a-z])\w*?\1\w*?\b/i",
  #Q51: all words where some letter appears 4 times in the same word.
  r"/\w*(\w)\w*(\1\w*){3}/i",
  #52: all non-empty binary strings with the same number of 01 substrings as 10 substrings.
  r"/^([01])([10]*\1)*$/",
  r"/(?=\b\w{6}\b)\w*cat\w*/i",
  #54: all 5-9 letter words containing both the substrings bri and ing.
  r"/(?=\b\w{5,9}\b)(?=\w*bri\w*)\w*ing\w*/i",
  #55: Match all six letter words not containing the substring cat.
  r"/\b(?!\w*cat\w*)\w{6}\b/i",
  #56: Match all words with no repeated characters.
  r"/\b(?!\w*(\w)\w*\1\w*)\w*\b/i",
  #57: Match all binary strings not containing the forbidden substring 10011.
  r"/^(1(?!0011)|0)*$/",
  #58: Match all words having two different adjacent vowels.
  r"/\b\w*([aeiou])(?!\1)[aeiou]\w*\b/i",
  #Q59: Match all binary strings containing neither 101 nor 111 as substrings
  r"/^(1(?!11)(?!01)|0)*$/"
  ]

if idx < len(myRegexLst):
  print(myRegexLst[idx])


#raunak
import sys
idx = int(sys.argv[1]) - 50
myRegexLst = [
    r"/\w*(\w)\w*(\1\w*)/i",
    r"/\w*(\w)\w*(\1\w*){3}/i",
    r"/^([10])([10]*\1)*$/",
    r"/\b(?=\w*cat\w*)\w{6}\b/i",
    r"/\b(?=\w*bri\w*)(?=\w*ing\w*)\w{5,9}\b/i",
    r"/\b(?!\w*cat\w*)\w{6}\b/i",
    r"/\b(?!\w*(\w)\w*\1\w*)\w+\b/i",
    r"/^(0|1(?!0011))*$/",
    r"/\w*([aeiou])(?!\1)[aeiou]\w*/i",
    r"/^(0|1(?!11)(?!01))*$/"
]
