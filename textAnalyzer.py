class textanalysis(object):

	def __init__(self, text):
		
		formattedtext = text.replace("!"," ").replace("?"," ").replace("."," ").replace(",", " ")
		
		formattedtext.lower()
	
		self.fmttext = formattedtext
		
	def countAll(self):

		textset = self.fmttext.split(" ")
		
		textdict = {}
		
		for i in textset:
			textdict[i] = textset.count(i)

		return textdict

	def freqOf(self, word):
		
		textdict = self.countAll()

		if word in textdict:
			return textdict[word]
		else:
			return 0


