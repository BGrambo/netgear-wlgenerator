#==========================================================

adjectivesFile = 'adjectives.txt'
nounsFile = 'nouns.txt'

adjectives = open(adjectivesFile).read().splitlines()
nouns = open(nounsFile).read().splitlines()

out = open('out.txt','w')

#Wordpicker WITHOUT numerals
def wordpicker1():
  out = open('out.txt','w')
  for x in adjectives:
    for y in nouns:
      z = (str(x.capitalize()+y.capitalize())+'\n')
      #print(z)
      out.write(str(z))

#Wordpicker WITH numerals
def wordpicker2():
  for x in adjectives:
    for y in nouns:
      z = (str(x.capitalize()+y.capitalize()))
      i = 0
      while (i < 999 + 1):
        #print(z+str(i).zfill(3))
        out.write(z+str(i).zfill(3)+'\n')
        i += 1

#.replace('\n','') if spaces appear (end of capitalize on line 12)

#=========================================================

def permutations():
  t1 = 0
  t2 = 0
  for c1 in adjectives:
    t1 += 1
  for c2 in nouns:
    t2 += 1
  t3 = t1*t2
  t4 = t1*t2*999
  print('adjectives.txt contains: ' + str(t1) + ' entries' + '\n')
  print('nouns.txt contains: ' + str(t2) + ' entries' + '\n')
  print('Without numerals: '+ str(t3) + ' permuatations' + '\n')
  print('With numerals: '+ str(t4) + ' permuatations' + '\n')

permutations()

def initialize():
  print('What would you like to run:')
  print('1. All permutations without numerals')
  print('2. All permutations with numerals')
  runtype = int(input('\n'+'Run:'+' '))
  if (runtype == 1):
    print('Running...')
    wordpicker1()
    print('Done!')
  elif (runtype == 2):
    print('Running...')
    wordpicker2()
    print('Done!')
  else:
    initialize()

initialize()
