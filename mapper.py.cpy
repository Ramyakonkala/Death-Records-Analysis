#!/usr/bin/python3.5

import pandas as pd
import sys

FILE_MAPPING = {
                 'Main': [], 
                 'ActivityCode': {},
                 'AgeRecode12': {}, 
                 'AgeRecode27' : {},
                 'AgeRecode52' : {},
                 'AgeType' :{},
                 'BridgedRaceFlag' :{},
                 'DayOfweekOfDeath':{},
                 'Education1989Revision':{},
                 'Education2003Revision':{},
                 'EducationReportingfFlag':{},
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
def read_csv_data():
    deathRec = pd.read_csv(sys.stdin)
   # for 
    return deathRec

def find_male_female_ratio(data):
    pass

def Main():
    print(FILE_MAPPING.keys())
    dataframe = pd.read_csv(sys.stdin)
  #  print(dataframe)
   # dataframe = read_csv_data()
 #   if dataframe['prefix'].iloc[0] == "Main":
  #      dataframe = dataframe.drop(['prefix'],axis=1)
   #     FILE_MAPPING['Main'] = dataframe
  #  else:
    #    prefix = dataframe['prefix'].iloc[0]
    for name in FILE_MAPPING.keys():
        # name = 'AgeRecode12'
        if name != 'Main':
            df = dataframe.drop(['prefix'],axis=1)
#           print(df)
            prefix = dataframe['prefix']
            print("******************************************")
 #          print(prefix)
            # df = dataframe.loc[dataframe['prefix'] == name]
            #print("-----------------------Name:{0}".format(name))
           # print(df)
      # FILE_MAPPING[prefix] = dict(zip(dataframe['Code'],dataframe['Description']))
            values = dict(zip(df['Code'],dataframe['Description']))
          #  print(values)
            FILE_MAPPING[name] = values
            print(FILE_MAPPING)  
#    find_male_female_ratio(data)




"""
	try:
		deathRec = pd.read_csv(sys.stdin)
		print(deathRec)
	except:
		print("failed loading!!")

"""

Main()
