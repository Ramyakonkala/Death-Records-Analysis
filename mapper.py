#!/usr/bin/python3.5

import pandas as pd
import sys

#MAIN_DATASET = []

df = pd.DataFrame()

FILE_MAPPING = { 'Main' : [],
                 'ActivityCode': {},
                 'AgeRecode12': {}, 
                 'AgeRecode27' : {},
                 'AgeRecode52' : {},
                 'AgeType' :{},
                 'BridgedRaceFlag' :{},
                 'DayOfWeekOfDeath':{},
                 'Education1989Revision':{},
                 'Education2003Revision':{},
                 'EducationReportingFlag':{},
                 'HispanicOrigin':{},
                 'HispanicOriginRaceRecode':{},
                 'Icd10Code':{},
                 'InfantAgeRecode22':{},
                 'MannerOfDeath':{},
                 'MaritalStatus':{},
                 'MethodOfDisposition':{},
                 'PlaceOfDeathAndDecedentsStatus':{},
                 'PlaceOfInjury':{},
                 'Race':{},
                 'RaceImputationFlag':{},
                 'RaceRecode3':{},
                 'RaceRecode5':{},
                 'ResidentStatus':{}
                 }

def get_dataframe(file_mapping):
    data = file_mapping['Main']
    header = data.pop(0)
    df = pd.DataFrame(data,columns = header)
    df = df.drop('prefix',axis =1)
    return df


def find_male_female_ratio(df):
    df_gender = df[['Sex']]
    for index, row in df_gender.iterrows():
        print("{0}\t\t{1}".format("find_male_female_ratio##"+row['Sex'],1))

def most_occurance_disease(df):
    diseaseList = pd.Series(df['Icd10Code'])
    diseaseDict = dict(diseaseList.value_counts())
    diseaseDict = {FILE_MAPPING['Icd10Code'][k]:v for k, v in diseaseDict.items()}
   # print(diseaseDict)
    #maximum = max(diseaseDict,key=diseaseDict.get)
    #print(maximum.replace('\r',''))
    for key , value in diseaseDict.items():
#        key.replace('\r','')
        print("most_occurance_disease##{0}\t{1}".format(key.replace('\r','').replace('\n',''),value))


def Main(FILE_MAPPING):
    listOfKeys = []
    for keys in FILE_MAPPING.keys():
        listOfKeys.append(keys)
    for line in sys.stdin:
        df = line.split(',')
        if len(df) < 39 :
            if df[0] in listOfKeys :
                FILE_MAPPING[df[0]][df[1]] = df[2]
        else:
            FILE_MAPPING['Main'].append(df)
    df= get_dataframe(FILE_MAPPING)
    del FILE_MAPPING['Main']
  #  print(df)
  #  print(FILE_MAPPING)
    find_male_female_ratio(df)
  #  most_occurance_disease(df)


Main(FILE_MAPPING)

