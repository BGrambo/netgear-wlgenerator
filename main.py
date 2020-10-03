adjectivesFile = 'adjectives.txt'
nounsFile = 'nouns.txt'

adjectives = open(adjectivesFile).read().splitlines()
nouns = open(nounsFile).read().splitlines()

out = open('out.txt','w')

"""
def wordpicker():
  for x in adjectives:
    for y in nouns:
      z = (str(x.capitalize()+y.capitalize()))
      i = 0
      while (i < 999 + 1):
        print(z+str(i).zfill(3))
        out.write(z+str(i).zfill(3)+'\n')
        i += 1
"""

def wordpicker():
  out = open('out.txt','w')
  for x in adjectives:
    for y in nouns:
      z = (str(x.capitalize()+y.capitalize())+'\n')
      print(z)
      out.write(str(z))


wordpicker()

#.replace('\n','') if spaces appear (end of capitalize on line 12)
