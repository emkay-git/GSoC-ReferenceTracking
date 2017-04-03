from bs4 import BeautifulSoup
from PubMed import PubMed
from Scholar import Scholar
class ParseMessage:
	def __init__(self):
		pass;

	def parse(self,mailFrom,mailBody):
		if mailFrom == "My NCBI <efback@ncbi.nlm.nih.gov>":
			s = PubMed(mailBody)
		else:
			s = Scholar(mailBody)

		print  mailBody