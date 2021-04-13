import unittest

import actorname
import actorname.english


class TestName(unittest.TestCase):
	def test_works(self):
		self.assertIn(actorname.name(), actorname.english.names)

	# def test_alias(self):
	# 	self.assertIs(actorname.name, actorname.Name)

	# def test_len(self):
	# 	for l in range(4, 10):
	# 		self.assertLessEqual(len(actorname.name(l)), l)


class TestGenerate(unittest.TestCase):
	def test_works(self):
		print("warming up...\n")
		words = 2
		sep = '-'
		target = actorname.Generate()
		print("we are looking for: " + target +"\n")
		self.assertTrue(target.islower())

	# def test_alias(self):
	# 	self.assertIs(actorname.generate, actorname.Generate)


if __name__ == '__main__':
	unittest.main()
