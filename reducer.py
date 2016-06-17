#!/usr/bin/python3.5

import pandas as pd
import sys
 
Findings = {'find_male_female_ratio':'find_male_female_ratio'}
genderCount = {}

def maleFemaleRatio():
    try:
        print("hello")
        listOfGender = []
        for line in sys.stdin:
            listOfGender.append(line)
        print(listOfGender)
        header = listOfGender.pop(0)
        df = pd.DataFrame(listOfGender)
        print(df)
        ratio = df[0].value_counts().reset_index()
        ratio.columns = ['Sex','Count']
        print(ratio)
  #      print(listOfGender.count('M'),listOfGender.count('F'))
    except Exception as ex:
      #  temp = "An exception of type {0} occured.Arguments:\n{1!r}"
      #  msg = temp.format(type(ex).__name__, ex.args)
      #  print(msg)
        print(ex)


def find_male_female_ratio(key,value,genderCount=genderCount):
    value = int(value)
    if not genderCount.get(key):
        genderCount[key] = 0
    genderCount[key] += value

diseaseMax = {}

def most_occurance_disease(diseaseMax):
    dMax = max(diseaseMax,key=diseaseMax.get)
    print(dMax,diseaseMax[dMax])

def Main():
    for line in sys.stdin:
        line = line.strip()
        prefix , keyvalue = line.split("##")
        key, value = keyvalue.split("\t",1)
        if prefix == 'find_male_female_ratio':
            find_male_female_ratio(key,value)
        if prefix == 'most_occurance_disease':
            diseaseMax[key] = value
    if prefix == 'most_occurance_disease':
        most_occurance_disease(diseaseMax)
    if prefix == 'find_male_female_ratio':
        for key,value in genderCount.items():
            print("{0}\t{1}".format(key,value))

 #       if prefix in Findings:
  #          Findings[prefix](key,value)
 #   for key,value in genderCount.items():
  #      print("{0}\t{1}".format(key,value))
  #  for key,value in diseaseCount.items():
   #     print("{0}\t{1}".format(key,value))




Main()


