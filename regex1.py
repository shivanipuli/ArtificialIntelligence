import sys; args = sys.argv[1:]
idx = int(args[0])-30

myRegexLst = [
  r"/^0$|^100$|^101$/",
  r"/^[01]*$/",
  r"/0$/",
  r"/\w*[aeiou]\w*[aeiou]\w*/i",
  r"/^[01]*$/",
  r"/^[01]*110[01]*$/",
  r"/^.\w{3}|.\w{1}$/s",
  r"/^\d{3} *-? *\d{2} *-? *\d{4}$/",
  r"/^\w*d\w*/im",
  r"/[01]*"
  ]

if idx < len(myRegexLst):
  print(myRegexLst[idx])


import sys

idx = int(x=sys.argv[1])-30

myRegEx = [r"/^0$|^10[01]$/",
           r"/^[01]*$/",
           r"/0$/",
           r"/\w*[aeiou]\w*[aeiou]\w*/i",
           r"/^0$|^1[01]*0$/",
           r"/^[01]*110[01]*$/",
           r"/^.{2,4}$/s",
           r"/^\d{3} *-? *\d\d *-? *\d{4}$/",
           r"/^.*?d\w*/mi",
           r"/^[01]?$|^1[01]*1$|^0[01]*0$/"]

print(myRegEx[idx])
