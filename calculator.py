#!/usr/bin/env python
# -*- coding: utf-8 -*-


# import sys
import re
import json

import sys
from os.path import dirname

configFile = 'config.json'

if len(sys.argv) > 1:
  configFile = dirname(sys.argv[0]) + '\\' + configFile

#  ---- Import all data from config file ----  #
cf = open(configFile, 'r')
config = json.load(cf)
nbdecimal = config['nbdecimal'] # nbdecimal=5
dicNumber = config['dicNumber'][config['defaultDicNumber']]
date_re = [[re.compile(a), b] for a,b in config['date_re']]
operators = config['operators'] # [detect, convertion, number value]
brackets = config['brackets']
unitDateConverter = config['unit_date']
cs = config['colorSet']
  # 'd'efault color value white/black : \033[0m -> \u001b[0m
  # 'v'alue green : \033[32m
  # 'b'ase or unit cyan : \033[36m
  # 'o'pertator +, -, *, /... red : \033[31m
  # 'r'esult : orange : \033[33m
  # 'f'unction or variable lightgrey : \033[37m
  # black='\033[30m' red='\033[31m' green='\033[32m' orange='\033[33m' blue='\033[34m' purple='\033[35m' cyan='\033[36m' lightgrey='\033[37m' darkgrey='\033[90m' lightred='\033[91m' lightgreen='\033[92m' yellow='\033[93m' lightblue='\033[94m' pink='\033[95m' lightcyan='\033[96m'
helpString = config['helpString']
helpString2= config['helpString2']
cmdSupport = config['cmdSupport']
del config
cf.close()

if cmdSupport:
  import os
  os.system('')
  del os

#  ----  The real function, I know it's weard but so fast and efficient  ----  #
def calculator(inoperation = False, newDicNumber= False, clear=False) :
  global cs
  if newDicNumber and not customDicNumber(newDicNumber):
    return
  if clear :
    csBackup = cs
    cs = {'d':'','v':'','b':'','o':'','r':'','f':''}
  while True : # my game loop
    txtInput = ""
    if inoperation :
      txtInput = inoperation.strip()
    else :
      txtInput = input('Enter an operation (or help)\n> ').strip() # remove firsts and lasts spaces/tab...
    date_format = False
    
    if txtInput == "help" :
      print(helpString.format(**cs))
      if inoperation :
        print(helpString2.format(**cs))
    elif txtInput == "newDic":
      customDicNumber(input('Enter newDicNumber (min, maj, init, safe, invert, base64, [custom])\nnewDicNumber=').strip())
    elif txtInput == "curDic":
      global dicNumber
      print(dicNumber)
    elif txtInput == "" :
      break
    else :
      operation = ""
      outbase=""
      number = ""
      numlist=[]
      operlist=[]
      bracklist=[]
      for txt in txtInput.split(' ') :
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
          resultf = '{v}{0} {d}base: {b}{1}{d}'.format(result, outbase, **cs)
        elif outbase == "" and not date_format :
          resultf = '{v}{0} {d}base: {b}10{d}'.format(result, **cs)
        elif outbase != "" and date_format :
          result = unit_date(result, outbase)
          resultf = '{v}{0}{b}{1}{d}'.format(result, outbase, **cs)
        else :
          result = mstodate(result)
          resultf = '{}'.format(result)
        if clear :
          cs = csBackup
          return result
        print(resultf)
      else :
        print('Missing {v}number {d}or {b}operand {d}in {0} (len : {1} != {2})'.format(txtInput, (len(numlist) - 1), len(operlist), **cs))
    if inoperation :
      break

def normal_number (number, date_format) :
  ### Convert number with strange format like hour and date C,D,y,w,d,h,m,s,ms ###
  global unitDateConverter
  global date_re
  final = 0
  number = number.replace(',','.')
  if re.search('(\d({}))'.format('|'.join(unitDateConverter)),number) :
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
      # number = todec(number, 10)
      pass
    else :
      # - - - - - Parti à revoir pour les cas de dicNumber décimal
      number = number.replace(".","")
      decalage = len(number) - decalage
      # number = str(todec(number, 10))
      number = str(number)
      number = "{}.{}".format(number[:len(number) - decalage], number[len(number) - decalage:])
  return [number, date_format]

def todec(innumber, base):
  global dicNumber
  innumber, frac = innumber.split('.') if innumber.find('.') != -1 else [innumber, '']
  unit = value = 0
  valfrac = float(0)
  if len(innumber) != 0:
    if innumber[-1] != "]":
      innumber, unit = innumber[:-1], innumber[-1]
      value = dicNumber.index(unit) if unit in dicNumber else int(unit)
    else:
      pos = innumber.rfind('[')
      innumber, unit = innumber[:pos], innumber[pos:].strip('[]')
      value = int(unit)
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
  global dicNumber
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
    scale = int(innumber % base)
    if scale < len(dicNumber) :
      number = '{}{}'.format(dicNumber[scale], number)
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
  global unitDateConverter
  return str(float(date) / unitDateConverter[unit] )

def mstodate(ms) :
  global unitDateConverter
  string = ""
  count = 0
  for uni in unitDateConverter : 
    scale = int(float(ms) / unitDateConverter[uni])
    if scale != 0 :
      string += cs['v'] + str(scale) + cs['b'] + uni
      ms = float(ms) - (scale * unitDateConverter[uni])
  return string + cs['d']

def customDicNumber(newDicNumber) :
  global dicNumber
  if hasattr(newDicNumber, 'append'):
    dicNumber = newDicNumber
  elif hasattr(newDicNumber, 'format'):
    with open(configFile, 'r') as cf:
      config = json.load(cf)
      if newDicNumber in config['dicNumber']:
        dicNumber = config['dicNumber'][newDicNumber]
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


if len(sys.argv) > 1:
  calculator(sys.argv[1])
else :
  print("\033[92mCalculator charged !\033[0m")

