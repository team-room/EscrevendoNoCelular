import unittest
import smsinput

class SMSInputTest(unittest.TestCase):

	def testA(self):
		self.assertEquals(smsinput.convert("a"), "2")

	def testAB(self):
		self.assertEquals(smsinput.convert("ab"), "2_22")

	def testABD(self):
		self.assertEquals(smsinput.convert("abd"), "2_223")

	def testB(self):
		self.assertEquals(smsinput.convert("b"), "22")

	def testC(self):
		self.assertEquals(smsinput.convert("c"), "222")

	def testD(self):
		self.assertEquals(smsinput.convert("d"), "3")

	def testE(self):
		self.assertEquals(smsinput.convert("e"), "33")

	def testF(self):
		self.assertEquals(smsinput.convert("f"), "333")

	def testPhrase(self):
		self.assertEquals(smsinput.convert("foobar"), '333666_66622_2777')

	def testEverything(self):
		self.assertEquals(smsinput.convert("SEMPRE ACESSO O DOJOPUZZLES"),"77773367_7773302_222337777_777766606660366656667889999_9999555337777")

if __name__ == '__main__':
	unittest.main()