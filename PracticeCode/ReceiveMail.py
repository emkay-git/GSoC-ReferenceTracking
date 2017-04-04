import imaplib
import getpass
import email
import json
from messageParser import ParseMessage


class ReceiveMail:
	def __init__(self,):
		pass
	
	def getIMAPAddress(self,username):
		email = username[username.rfind('@'):len(username)]
		with open('IMAP_CONFIG.json') as imapAddress:
		    data = json.load(imapAddress)
		return data[email]


	def login(self,username,password,label):
		imapAddress = self.getIMAPAddress(username)
		inbox = imaplib.IMAP4_SSL(imapAddress)  
		inbox.login(username,password)
		inbox.list()

		inbox.select(label)
		typ, data = inbox.search(None, 'ALL')

		for num in data[0].split():			
			typ, data = inbox.fetch(num,'(RFC822)')
		    # print 'Message %s\n%s\n' % (num, data[0][1])
			self.getDetails(data[0][1])	
		inbox.close()
		inbox.logout()

	def getDetails(self,rawMail):
		emailMessage = email.message_from_string(rawMail)
		
		mailFrom =  emailMessage['From']
		mailTo = emailMessage.get_payload(decode = True)
		mp = ParseMessage()
		mp.parse(mailFrom,mailTo)




receiveMail = ReceiveMail()

username="emkayatiitr@gmail.com"

mailBox=receiveMail.login(username,password,"ResearchPaper")
# receiveMail.getMailList(mailBox,"ResearchPaper")
