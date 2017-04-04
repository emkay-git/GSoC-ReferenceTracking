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
				string.append(td.text.replace('\n','').rstrip())
				# print "-------------"
		
		
		
		for i in xrange(1,len(string),5):
			if string[i-1].rstrip() == "Similar articles":
				print string[i-1]
				string.remove("Similar articles")
			if i < len(string):
				title.append(string[i])	

		# print "------------"/
		# for st in string:
		# 	print st	
		for i in xrange(2,len(string),5):
			names.append(string[i])
		# print "------------"
		for i in xrange(3,len(string),5):
			details.append(string[i].replace('\n',''))
		
		self.makeAndWriteJSON()






# body = '''
# 		<?xml version="1.0" encoding="UTF-8"?>
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
# <html xmlns="http://www.w3.org/1999/xhtml">
#     <head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
# 		    <!-- Common JS and CSS -->
#         <link type="text/css" rel="stylesheet" href="http://www.ncbi.nlm.nih.gov/portal/css/ncbi_test.css"/>
#     <link rel="shortcut icon" href="http://www.ncbi.nlm.nih.gov//www.ncbi.nlm.nih.gov/favicon.ico"/><meta name="ncbi_phid" content="A45228D78DE354910000000000A5009F"/>
# <meta name="referrer" content="origin-when-cross-origin"/><link type="text/css" rel="stylesheet" href="http://www.ncbi.nlm.nih.gov//static.pubmed.gov/portal/portal3rc.fcgi/4157465/css/4008682/4156580/3861632/3925293.css"/><link type="text/css" rel="stylesheet" href="http://www.ncbi.nlm.nih.gov//static.pubmed.gov/portal/portal3rc.fcgi/4157465/css/1303451.css" media="print"/></head>
#     <body><p>
#                 This message contains My NCBI what's new results from the
#                 National Center for Biotechnology Information (<a href="http://www.ncbi.nlm.nih.gov">NCBI</a>)
#                 at the U.S. National Library of Medicine (<a href="http://www.nlm.nih.gov">NLM</a>).<br/>
#                 Do not reply directly to this message.
#             </p><p><b>Sender's message: </b></p>

#             Sent on Friday, 2017 March 31
#             <br/>
#             Search: <b>breast cancer</b><br/><br/><a href="http://www.ncbi.nlm.nih.gov/myncbi/searches/17457585/1XUlkc0Srb6tgVfS375x4RcofcqzfeROuq8pgqWjzbhxloohrZgBrGh35L8canYsPB">View</a> complete results in PubMed (results may change over time).
#             <br/><br/><a href="http://www.ncbi.nlm.nih.gov/myncbi/searches/17457585/">Edit</a> saved search settings, or <a href="http://www.ncbi.nlm.nih.gov/myncbi/searches/17457585/unsubscribe/1VQWqcZE6gE5t">unsubscribe</a> from these e-mail updates.

            
#         <div>	
#         	<br/>
#         	<br/>
#         	<div><table width="100%" bgcolor="#CCCCCC"><tr><td align="center">PubMed Results</td></tr></table>Items 1 - 5 of 72<br/></div>
#         	<br/>
#         	<div><table cellpadding="0" cellspacing="5" width="100%"><tbody><tr><td valign="top" nowrap="nowrap" width="10">1.</td><td valign="top"><a href="http://www.ncbi.nlm.nih.gov/pubmed/26389187" ref="ordinalpos=1">Breast Cancer Treatment (PDQ®): Health Professional Version.</a></td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top">PDQ Adult Treatment Editorial Board.</td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top">PDQ Cancer Information Summaries [Internet]. Bethesda (MD): National Cancer Institute (US); 2002-.</td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top">PMID: 26389187 [PubMed]<span style="color: #985735; font-weight: bold;">   Free Books &amp; Documents   </span></td></tr><tr><td align="left" valign="top" width="10"/><td><a
# href="http://www.ncbi.nlm.nih.gov/pubmed?linkname=pubmed_pubmed&amp;from_uid=26389187" ref="ordinalpos=1">Similar articles</a>   </td></tr></tbody></table><table cellpadding="0" cellspacing="5" width="100%"><tbody><tr><td valign="top" nowrap="nowrap" width="10">2.</td><td valign="top"><a href="http://www.ncbi.nlm.nih.gov/pubmed/28359110" ref="ordinalpos=2">Influence of Body Image in Women Undergoing Treatment for Breast Cancer.</a></td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top">Prates AC, Freitas-Junior R, Prates MF, Veloso MF, Barros NM.</td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top"><span class="jrnl" title="Revista brasileira de ginecologia e obstetricia : revista da Federacao Brasileira das Sociedades de Ginecologia e Obstetricia">Rev Bras Ginecol Obstet</span>. 2017 Mar 30. doi: 10.1055/s-0037-1601453self.
# [Epub ahead of print]</td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top">PMID: 28359110 [PubMed - as supplied by publisher]</td></tr><tr><td align="left" valign="top" width="10"/><td/></tr></tbody></table><table cellpadding="0" cellspacing="5" width="100%"><tbody><tr><td valign="top" nowrap="nowrap" width="10">3.</td><td valign="top"><a href="http://www.ncbi.nlm.nih.gov/pubmed/28359079" ref="ordinalpos=3">Evaluating wait times from screening to breast cancer diagnosis among women undergoing organised assessment vs usual care.</a></td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top">Chiarelli AM, Muradali D, Blackmore KM, Smith CR, Mirea L, Majpruz V, O'Malley FP, Quan ML, Holloway CM.</td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top"><span class="jrnl" title="British journal of cancer">
# Br J Cancer</span>. 2017 Mar 30. doi: 10.1038/bjc.2017.87. [Epub ahead of print]</td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top">PMID: 28359079 [PubMed - as supplied by publisher]</td></tr><tr><td align="left" valign="top" width="10"/><td/></tr></tbody></table><table cellpadding="0" cellspacing="5" width="100%"><tbody><tr><td valign="top" nowrap="nowrap" width="10">4.</td><td valign="top"><a href="http://www.ncbi.nlm.nih.gov/pubmed/28359077" ref="ordinalpos=4">Sleep and survival among women with breast cancer: 30 years of follow-up within the Nurses' Health Study.</a></td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top">Trudel-Fitzgerald C, Zhou ES, Poole EM, Zhang X, Michels KB, Eliassen AH, Chen WY, Holmes MD, Tworoger SS, Schernhammer ES.</td></tr><tr><td align="left" valign="top" width="10"/><td align="left"
# valign="top"><span class="jrnl" title="British journal of cancer">Br J Cancer</span>. 2017 Mar 30. doi: 10.1038/bjc.2017.85. [Epub ahead of print]</td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top">PMID: 28359077 [PubMed - as supplied by publisher]</td></tr><tr><td align="left" valign="top" width="10"/><td/></tr></tbody></table><table cellpadding="0" cellspacing="5" width="100%"><tbody><tr><td valign="top" nowrap="nowrap" width="10">5.</td><td valign="top"><a href="http://www.ncbi.nlm.nih.gov/pubmed/28359054" ref="ordinalpos=5">Cepharanthine Induces Autophagy, Apoptosis and Cell Cycle Arrest in Breast Cancer Cells.</a></td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top">Gao S, Li X, Ding X, Qi W, Yang Q.</td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top"><span class="jrnl"
# title="Cellular physiology and biochemistry : international journal of experimental cellular physiology, biochemistry, and pharmacology">Cell Physiol Biochem</span>. 2017 Mar 28;41(4):1633-1648. doi: 10.1159/000471234. [Epub ahead of print]</td></tr><tr><td align="left" valign="top" width="10"/><td align="left" valign="top">PMID: 28359054 [PubMed - as supplied by publisher]</td></tr><tr><td align="left" valign="top" width="10"/><td/></tr></tbody></table></div>
#         </div>
    

# <!-- 24D957408DE30981_0000SID /projects/entrez/pubmed/PubMedGroup@1.107 portal309 v4.1.r526566 Fri, Feb 03 2017 14:27:04 -->


# </body>
# </html>
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																					
# '''

# p = PubMed(body)