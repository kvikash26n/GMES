'''
Created on Mar 10, 2019

@author: 29265
'''
import configparser
import os
import pandas as pd
import component as cp
def loadConfigFile(path):
    config = configparser.RawConfigParser()
    config.read(path)
    return config

#print(cp.GEMSComp.sum(5,8))
ob=cp.GEMSComp()
summ=ob.sum(2)
ob.mul(4)
print(summ)
#Reading config file for GEMS

print(os.getcwd())
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR=ROOT_DIR.replace('test','')
config_file_path=ROOT_DIR+'config.properties'
print(config_file_path)
config=loadConfigFile(config_file_path)
details_dict = dict(config.items('Env Details'))
#to get country
country=details_dict['countrycode']
print(country)
testSuite=details_dict['testsuite']
tcsheetname=details_dict['tcsheetname']
testDataSheetName=details_dict['testdatasheetname']
print(testSuite)
print(tcsheetname)
print(testDataSheetName)


#C:\Automation\GMES\GMESmarket\turkey
#C:\Users\29265\GEMS\GMESmarket\turkey
tSuite=pd.read_excel("C:\\Users\\29265\\GEMS\\GMESmarket\\"+country+"\\"+testSuite+".xlsx",sheetname=tcsheetname)
tSuite.fillna('noStep',inplace=True)

tData=pd.read_excel("C:\\Users\\29265\\GEMS\\GMESmarket\\"+country+"\\"+testSuite+".xlsx",sheetname=testDataSheetName)
tData.fillna('noStep',inplace=True)

#transpose
tSuite=tSuite.T
tData=tData.T

for i in range(0,len(tSuite.columns)):
    for j in range(0,len(tData.columns)):
        #TC validation
        if list(tSuite[i])[0]== list(tData[j])[0]:
            allComponentsPerTC=list(tSuite[i])
            allComponentsData=list(tData[j])
            allActualComponentsPerTC = [x for x in allComponentsPerTC if x != 'noStep']
            allActualComponentsData = [x for x in allComponentsData if x != 'noStep']
            #both list will be equal size
            for k in range(1,len(allActualComponentsPerTC)):
                #print(allActualComponentsPerTC[k])
                xx=allActualComponentsPerTC[k]
                #print(xx)
                #need to call function/component with thier data
                #summ=ob.xx(allActualComponentsData[k])
                summ=getattr(ob, xx)(allActualComponentsData[k])
                print(summ)
                #break
#cp.sum(2,5)
#print(cp.sum(2,3))

