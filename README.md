Mockups/page1.jpg
	-This image is when you have multiple projects already. So open an existing project or make a new project
Mockups/page2.jpg
	-This image is when you enter the curate paper segment, when you go through papers it will have multiple options to work with with that papers
Mockups/page3.jpg
	-This image shows the first time you will be opening the app as there will be no existing projects

PracticeCode
	- IMAP_CONFIG - it will store the imap address for different mail sites (google, hotmail, live)
	- ReceiveMail.py - it starts the connection with the mail and get the email sender's and body's data and passes it to messageParser.py
	- messageParser.py - it checks the sender's address and pass it to Scholar or PubMed depending on the sender's adderess
	- Scholar.py - it parses the email's body and extract the paper's title, publisher's name, details
	- PubMed.py - it parses the email's body and extract the paper's title, publisher's name, details
	- data.json - output of PubMed
	- data2.json - output of PubMed 