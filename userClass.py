import pickle
sepchr = '-'
seplen = 19
sepline = sepchr * seplen

class User:
	def __init__(self, name, score=0):
		self.name = name
		self.score = score
	
	def writeScore(self):
		with open("userData.cfg", "wb") as file:
			pickle.dump({self.name: self.score}, file)

	def readScore(self):
		try:
			with open("userData.cfg", "rb") as file:
				self.score = pickle.load(file)[self.name]
		except:
			pass
	
	def win(self):
		self.score += 10

	def loss(self):
		self.score -= 10
	
	def __str__(self):
		return "Name: {0}, Score: {1}\n{line}".format(self.name, self.score, line=sepline)
