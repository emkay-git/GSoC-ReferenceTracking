#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json

linksArray = []
title= []
names = []
details = []
string = []
jsonData = {"papers":[]}

class Scholar:

	def __init__(self,body):
	
		self.body = body
		self.soup = BeautifulSoup(self.body,'html.parser')
		self.getData()

	def makeJSON(self):
		data = {}
		for i in xrange(len(title)):
			data["title"]=title[i]
			data["names"]=names[i]
			data["details"]=details[i]

			jsonData["papers"].append(data)
			data={}
		# data = json.dumps(jsonData)
		with open('data2.json','wa') as f:
			json.dump(jsonData,f)


	def getData(self):
		links = self.soup.find_all('a')
		for link in links:
			if link.text:
				linksArray.append(link)
				
			print "-----------------------"
		
		print "ok"
		fonts = self.soup.find_all('font')
		
		for font in fonts:
			if font.text:
				string.append(font.text.replace('\n',''))
		
		subject = string[0]
		for i in xrange(1,len(string)-3,3):
			print string[i]
			title.append(string[i])	
		for i in xrange(2,len(string)-3,3):
			print string[i]
			names.append(string[i])
		for i in xrange(3,len(string)-3,3):
			print string[i]
			details.append(string[i])
		self.makeJSON()

