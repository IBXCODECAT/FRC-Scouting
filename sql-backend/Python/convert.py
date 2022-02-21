#Imports from python
import json

#Imports from os
import os
from os import listdir

#Imports from os.path
from os.path import isfile
from os.path import join

def FetchData():
	searchForFileType = ".scout" #The filetype to include in the file search
	cwd = os.getcwd() #Get current working directory (cwd)
	files = os.listdir(cwd) #Read all files from cwd and add to file list
	
	data_list = [] #Declaring a list of data dicts
	
	for file in files: #Loop through all files in the file list
		if(searchForFileType in file): #If the filetype is of ".scout"...
			with open(file) as json_data: #Read json data of file into "json_data"
				data = json.load(json_data) #Save loaded json data to "data"
				data_list.append(data)
	
	return data_list

def CreateSQL(data_dict): #Create SQL satement from a data dictionary
	TABLE_NAME = "db0.MatchMaster1" #The name of the SQL table we inserting data into
	
	statement = "INSERT INTO " + TABLE_NAME + "(" + ""
	
data = FetchData()
print(data)

#with open(jsonFile) as json_data:
#	data = json.load(json_data)
	
	

