#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import sys
import re


dicNumber=[]
nbdecimal=5
def initDicNumber():
  #  1 2 3 4 5 6 7 8 9 A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z  Α  Β  Γ  Δ  Ε  Ζ  Η  Θ  Ι  Κ  Λ  Μ  Ν  Ξ  Ο  Π  Ρ  ς  Σ  Τ  Υ  Φ  Χ  Ψ  Ω  α  β  γ  δ  ε  ζ  η  θ  ι  κ  λ  μ  ν  ξ  ο  π  ρ  ς  σ  τ  υ  φ  χ  ψ  ω   
  #                   10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99100101102103104105106107108109110111
  # dicNumber=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','.','?','?','?','?','?']
  # dicNumber=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a'.decode('utf-8'),'ß'.decode('utf-8'),'?'.decode('utf-8'),'d'.decode('utf-8'),'e'.decode('utf-8'),'?'.decode('utf-8'),'?'.decode('utf-8'),'?'.decode('utf-8'),'?'.decode('utf-8'),'?'.decode('utf-8'),'?'.decode('utf-8'),'µ'.decode('utf-8'),'?'.decode('utf-8'),'?'.decode('utf-8'),'?'.decode('utf-8'),'p'.decode('utf-8'),'?'.decode('utf-8'),'s'.decode('utf-8'),'t'.decode('utf-8'),'?'.decode('utf-8'),'f'.decode('utf-8'),'?'.decode('utf-8'),'?'.decode('utf-8'),'?'.decode('utf-8')]
  global dicNumber
  dicNumber = ['0','1','2','3','4','5','6','7','8','9',
               'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
               'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               'Α','Β','Γ','Δ','Ε','Ζ','Η','Θ','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','ς','Σ','Τ','Υ','Φ','Χ','Ψ','Ω',
               'α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','ς','σ','τ','υ','φ','χ','ψ','ω']
# initDicNumber()

def safeDicNumber():
  global dicNumber
  dicNumber = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def majDicNumber():
  global dicNumber
  dicNumber = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def minDicNumber():
  global dicNumber
  dicNumber = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def invertDicNumber():
  global dicNumber
  dicNumber = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def base64DicNumber():
  global dicNumber
  dicNumber = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']

safeDicNumber()

date_re = [
  [re.compile('([\d\.]+?)C'), 1],
  [re.compile('([\d\.]+?)D'), 10],
  [re.compile('([\d\.]+?)y'), 10],
  [re.compile('([\d\.]+?)d'), 365.25],
  [re.compile('([\d\.]+?)h'), 24],
  [re.compile('([\d\.]+?)m(?!s)'), 60],
  [re.compile('([\d\.]+?)s'), 60],
  [re.compile('([\d\.]+?)ms'), 1000] ]
operators = [ # [detect, convertion, number value]
  ['+', '+', ''],
  ['-', '-', ''],
  ['*', '*', ''],
  ['^', '**',''],
  ['/', '/', ''],
  ['%', '%', ''],
  ['=', False,'!']]
brackets =[
  ['(', True],
  ['[', True],
  ['{', True],
  [')', False],
  [']', False],
  ['}', False]]


def calculator(inoperation = False, newDicNumber= False, clear=False) :
  if newDicNumber and not customDicNumber(newDicNumber):
    return
  while True : # my game loop
    input = ""
    if inoperation :
      input = inoperation.strip()
    else :
      input = raw_input('Enter an operation (or help)\n> ').strip() # remove firsts and lasts spaces/tab...
    date_format = False
    
    if input == "help" :
      print('write operation like :\n' +
        '  5 + 5\n' +
        '  15 8 + 21 (the 2nd number (8) is the base)\n' +
        '  438m = h (get the decimal value of hour, otherwise get full convertion (like : 1y2d3h4m5s6ms)\n' +
        '  5h31m0s145ms + 2y4d18h32m42s + 4h32s + 484s (time operation is possible (the order is : CDydhmsms Century Decade year day hour minute second milisecond (ms is the only 2 char unit))\n' +
        '  45 13 * 12 4 = 16 (the answer will be converted by the base mentionned after the =)\n' +
        '  newDic (to change current dicNumber)\n'+
        '  curDic (to get current dicNumber)\n'
        'press enter to leave (empty entry)'
      )
      if inoperation :
        print("As second argument you can change the number dictionnary\n" +
          "  (default) calculator(\"Exemple 62 + of 62 + Calcul 62 = 19\", \"safe\") ->  safe=[0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]\n"+
          "  calculator(\"def 26\", \"min\") -> min=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]\n"+
          "  calculator(\"SPQR 26\", \"maj\") -> maj=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]\n"+
          "  calculator(newDicNumber=\"invert\") -> invert=[0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]\n"+
          "  calculator(newDicNumber=\"base64\") -> base64=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9,+,/]\n"+
          "  or you can use yours, exemple: \"calculator(\"PONY 26\", newDicNumber=['Z','X','Y','P','W','V','U','T','S','R','Q','I','M','L','K','J','N','H','G','F','O','E','D','C','B','A']\"\n"+
          "  if a number is out of the dictionnary size it can be introduce with the [] as : calculator(\"[27][38]5[18] 64 = 10\")\n"+
          "  the dictionnary is kept for future use into global variable : dicNumber")
    elif input == "newDic":
      customDicNumber(raw_input('Enter newDicNumber (min, maj, init, safe, invert, base64, [custom])\nnewDicNumber=').strip())
    elif input == "curDic":
      global dicNumber
      print(dicNumber)
    elif input == "" :
      break
    else :
      operation = ""
      outbase=""
      number = ""
      numlist=[]
      operlist=[]
      bracklist=[]
      for txt in input.split(' ') :
        if len(txt) == 1 :
          conti = False
          for ope in operators : # find operator and add to the list
            if txt == ope[0] :
              if ope[1] :
                operlist.append(ope[1])
              number, date_format = normal_number(number, date_format)
              numlist.append(number)
              number=ope[2]
              conti = True
          if conti :
            continue
          for bra in brackets : # find brackets record if it open or close related to the number
            if txt == bra[0] :
              bracklist.append([len(numlist), bra[1]])
              conti = True
          if conti :
            continue
        if number == "!" :
          outbase = txt
        elif number == "" :
          number = txt
        else : # un nombre est enregisterer il faut convertir sa base
          number = str(todec(number.replace(',', '.'), int(txt)))
      if outbase == "" :
        number, date_format = normal_number(number, date_format)
        numlist.append(number)
      if (len(numlist) % 2) != (len(operlist) % 2) :
        operation = ""
        poplist = []
        for indx, bra in enumerate(bracklist) :
            if bra[0] == 0:
              operation += '( ' if bra[1] else ' )';
              poplist.append(indx)
        for ind in sorted(poplist, reverse=True):
          bracklist.pop(ind)
        operation += '{}'.format(numlist[0])
        i = 1
        opbra = ''
        for op in operlist:
          poplist = []
          for indx, bra in enumerate(bracklist) :
            if bra[0] == i-1 and not bra[1]:
              operation += ' )'
              poplist.append(indx)
            if bra[0] == i and bra[1] :
              opbra += '( '
              poplist.append(indx)
          for ind in sorted(poplist, reverse=True):
            bracklist.pop(ind)
          operation = '{} {} {}{}'.format(operation, op, opbra, numlist[i])
          i+=1
          opbra = ''
        if len(bracklist) != 0 :
          operation += ' )' * len(bracklist)
        result = eval(operation)
        if outbase != "" and not date_format :
          result = tobase(result, outbase)
          print('{} base: {}'.format(result, outbase))
        elif outbase == "" and not date_format :
          print('{} base: 10'.format(result))
        elif outbase != "" and date_format :
          result = unit_date(result, outbase)
          print('{}{}'.format(result, outbase))
        else :
          result = mstodate(result)
          print('{}'.format(result))
      else :
        print('Missing number or operand in {} (len : {} != {})'.format(input, (len(numlist) - 1), len(operlist)))
    if inoperation :
      break

def normal_number (number, date_format) :
  ### Convert number with strange format like hour and date C,D,y,w,d,h,m,s,ms ###
  final = 0
  number = number.replace(',','.')
  if re.search('(\d([CDywdhms]|ms))',number) :
    date_format = True
    for date in date_re :
      unit = date[0].search(number)
      found = 0
      if unit :
        number = number.replace(unit.group(0), "")
        found = float(todec(unit.group(1), 10))
      final = float(found) + float(final * date[1])
    if number != "" :
      print('Error unknow date format, left : {} after filtering known values'.format(number))
    number = final
  else :
    decalage = number.find(".")
    if decalage == -1 :
      number = todec(number, 10)
    else :
      number = number.replace(".","")
      decalage = len(number) - decalage
      number = str(todec(number, 10))
      number = "{}.{}".format(number[:len(number) - decalage], number[len(number) - decalage:])
  return [number, date_format]

def todec(innumber, base):
  innumber, frac = innumber.split('.') if innumber.find('.') != -1 else [innumber, '']
  unit = value = 0
  valfrac = float(0)
  if len(innumber) != 0:
    if innumber[-1] != "]":
      innumber, unit = innumber[:-1], innumber[-1]
    else:
      pos = innumber.rfind('[')
      innumber, unit = innumber[:pos], innumber[pos:].strip('[]')
    value = dicNumber.index(unit) if dicNumber.count(unit) != 0 else int(unit)
    if len(innumber) != 0:
      value += (todec(innumber, base) * base)
  if len(frac) != 0:
    if frac[0] != "[":
      frac, unit = frac[1:], frac[0] # frac[0] === frac[:1]
    else:
      pos = frac.find(']')
      frac, unit = frac[pos + 1:], frac[:pos + 1].strip('[]')
    valfrac = (dicNumber.index(unit) if dicNumber.count(unit) != 0 else int(unit)) / base
    if len(frac) != 0:
      valfrac += (todec(".{}".format(frac), base) / base)
    value += valfrac
  return value

def tobase (innumber, base):
  number=""
  neg = False
  base = int(base)
  if innumber < 0 :
    innumber = abs(innumber)
    neg = True
  innumber = str(innumber)
  innumber, frac = innumber.split('.') if innumber.find('.') != -1 else [innumber, 0]
  innumber = int(innumber)
  frac = float('0.{}'.format(frac))
  while innumber != 0:
    scale = innumber % base
    if scale < len(dicNumber) :
      number = dicNumber[innumber % base] + number
    else :
      number = '[{}]{}'.format(scale, number)
    innumber = (innumber - scale) / base
  if frac > 0 :
    number+= '.'
    global nbdecimal
    decibase = base
    for x in range(nbdecimal):
      scale = int(frac / (1 / decibase))
      frac = frac - (scale * (1 / decibase))
      number += dicNumber[scale] if len(dicNumber) > scale else '[{}]'.format(scale)
      if frac == 0:
        break
      decibase = decibase * base
  return ('' if not neg else '-' ) + number # .decode('latin_1')

def unit_date(date, unit) :
  converter = {
    'C' : 86400000 * 36525,
    'D' : 315576000000, # 86400000 * 3652.5,
    'y' : 31557600000, # 86400000 * 365.25,
    'w' : 86400000 * 7,
    'd' : 86400000,
    'h' : 3600000,
    'm' : 60000,
    's' : 1000,
    'ms': 1
  }
  return str(float(date) / converter[unit] )

def mstodate(ms) :
  string = ""
  unit  = ['y','d','h','m','s','ms']
  value = [31557600000, 86400000, 3600000, 60000, 1000, 1]
  count = 0
  for uni in unit : 
    scale = int(float(ms) / value[count])
    if scale > 0 :
      string += str(scale) + uni
      ms = float(ms) - (scale * value[count])
    count+=1
  return string

def customDicNumber(newDicNumber) :
  global dicNumber
  if hasattr(newDicNumber, 'append'):
    dicNumber = newDicNumber
  elif hasattr(newDicNumber, 'format'):
    if newDicNumber == "min" :
      minDicNumber()
    elif newDicNumber == "maj" :
      majDicNumber()
    elif newDicNumber == "init" :
      initDicNumber()
    elif newDicNumber == "safe" :
      safeDicNumber()
    elif newDicNumber == "invert" :
      invertDicNumber()
    elif newDicNumber == "base64" :
      base64DicNumber()
    else :
      print("Error unknown {} standart format".format(newDicNumber))
      return False
  else :
    print("Error unknown newDicNumber")
    return False
  return True


hfrom = hto = hdif = ['0','0','0']
def flathour(hfrom) :
  hto[1] = (int(hto[0]) - int(hfrom[0])) * 60 + int(hto[1])
  hto[2] = (int(hto[1]) - int(hfrom[1])) * 60 + int(hto[2])

  hdif[2] = (hto[2] - int(hfrom[2])) % 60
  hdif[1] = int(hto[2] / 60) % 60
  hdif[0] = int(hto[2] / 3600) % 60

  print('diff = {}:{}:{}'.format(hdif[2],hdif[1],hdif[0]))

print("Calculator charged !")