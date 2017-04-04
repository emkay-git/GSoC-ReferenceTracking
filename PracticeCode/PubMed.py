# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json



string = []
title = []
names = []
details = []
jsonData = {"papers":[]}

class PubMed:

	
	def __init__(self,body):
		
		self.body = body
		self.soup = BeautifulSoup(self.body,'html.parser')
		self.getData()

	def loadJSON(self):
		with open('data.json','r') as f:
			if not f:
				jsonData = json.load(f)
		# print jsonData

	def makeAndWriteJSON(self):
		self.loadJSON()
		data = {}
		# print jsonData
		for i in xrange(len(title)):
			data["title"]=title[i]
			data["names"]=names[i]
			data["details"]=details[i]

			jsonData["papers"].append(data)
			data={}
		
		with open('data.json','w') as f:
			json.dump(jsonData,f)

	
	def getData(self):
		div = self.soup.find_all('div')
		self.body=str(div[2])
		# print self.body
		self.soup = BeautifulSoup(self.body,'html.parser')

		tds= self.soup.find_all('td')
		for td in tds:
			if td.text:
				string.append(td.text)
				# print "-------------"
			
		
		
		for i in xrange(1,len(string),5):
			title.append(string[i])	
		# print "------------"/
		for i in xrange(2,len(string),5):
			names.append(string[i])
		# print "------------"
		for i in xrange(3,len(string),5):
			details.append(string[i].replace('\n',''))

		self.makeAndWriteJSON()




