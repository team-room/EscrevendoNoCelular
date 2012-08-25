def convert(text):
	result = ''
	oldGroup = None

 	for letter in text.lower():
		for group, number in dictionary.items():
			if letter in group:
				if _isSameGroup(group, oldGroup):
					result += '_'
				result += str(number) * (group.find(letter) + 1)
				oldGroup = group

	return result

def _isSameGroup(text, group):
	return text == group

dictionary = {
	'abc': 2,
	'def': 3,
	'ghi': 4, 
	'jkl': 5,
	'mno': 6,
	'pqrs': 7, 
	'tuv': 8,
	'wxyz': 9,
	' ': 0
} 