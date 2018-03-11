import nltk
import pandas as pd
import re

def preprocessing_frame(frame):

	specific_skills = ['c#', '.net', 'asp.net', 'c++']
	big_list = []
	count = 0
	for _, rows in frame.iteritems():
		count = count + 1
		rows = rows.replace('>','')
		rows = rows.replace('<','')
		rows = rows.replace('...','')
		rows_split = rows.split(',')
		list_skill = []
		pattern1 = re.compile(r'([a-z].*[0-9])')
		pattern2 = re.compile(r'([a-z].*[a-z])')
		for elements in rows_split:
			space_split = elements.split(' ')
			if len(space_split) <= 4:
				elements = elements.lower()
				elements = elements.strip()
				if (pattern1.match(elements) or pattern2.match(elements) or elements in specific_skills):
					if '?' in elements:
						elements = elements.replace('?', '')
					if '&amp;' in elements:
						elements = elements.replace('&amp;', '')
					if elements.endswith('.'):
						elements = elements.replace('.', '')
					if '&' in elements:
						elements = elements.replace('&', '')
					if '#x' in elements or '#x22' in elements:
						elements = elements.replace('#x', '')
						elements = elements.replace('#x22', '')
					if elements.startswith('.') and not elements.startswith('.net'):
						elements = elements.replace('.', '')
					if elements not in list_skill:
						list_skill.append(elements.strip())

		big_list.append(list_skill)

	return big_list