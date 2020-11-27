import sys

s=sys.argv[1] #input=string
print(s)
# 1) ...the character at position 2. (Which I don’t need to remind you is not the second character.)
print("#1: " + s[2])
# 2) ...the fifth character. (Which I don’t need to remind you is not the character at position 5.)
print("#2: " + s[4])
# 3) ...the number of characters in the string.
print("#3: " + str(len(s)))
# 4) ...the first character.
print("#4: " + s[0])
# 5) ...the last character.
print("#5: " + s[-1])
# 6) ...the penultimate character.
print("#6: " + s[-2])
# 7) ...the five character long substring starting at position 3.
print("#7: " + s[3:8])
# 8) ...a substring consisting of the last five characters of the string.
print("#8: " + s[-5:])
# 9) ...a substring starting at the third character and continuing to the end of the string.
print("#9: " + s[2:])
# 10) ...a string containing every other character from the input string.
print("#10: " + s[::2])
# 11) ...a string consisting of every third character from the input string, starting from its second character.
print("#11: " + s[1::3])
# 12) ...the input string reversed. (One line!)
print("#12: " + s[::-1])
# 13) ...the position of the first space in the input string.
print("#13: " + str(s.find(" ")))
# 14) ...the string shifted to the right by one (ie, the original string with the last character removed).
print("#14: " + s[:-1])
# 15) ...the string shifted to the left by one (ie, the original string with the first character removed).
print("#15: " + s[1:])
# 16) ...the string all in lower case.
print("#16: " + s.lower())
# 17) ...a list of all the space delimited substrings of the input string. Examples:
# "234"  ["234"]
# "12 35"  ["12", "35"]
# "The quick fox"  ["The", "quick", "fox”]
print("#17: " + str(s.split()))
# 18) ...the number of space delimited words there are in your input string.
print("#18: " + str(len(s.split())))
# 19) ...a list of all characters, including duplicates, in the string
# (eg, "foo"  ["f", "o", "o"]).
print("#19: " + str([char for char in s]))
# 20) ...a new string consisting of the characters of the input string rearranged in ascending ascii order (eg, "quick"
#  "cikqu").
print("#20: "+ "".join(sorted(list(s))))
#
# 21) ...a new string consisting of the substring of your input string starting at the beginning and going up to, but not
# including, the first space. If there is no space at all, it should give the entire input.
print("#21: "+ s.split()[0])
print("#22: " + str(s==s[::-1]))
