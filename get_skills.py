import numpy, csv
import pandas as pd

def get_from_memory(file_path):
	skills_data = pd.read_csv(file_path, encoding = 'latin-1', low_memory=False)
	skill = skills_data['Skills']
	return skill


class KeySkills:

	def __init__(self, db = None):
		self.db = db
		if self.db == None:
			file_path = r'C:\pythoncode\scrapy-crawler\naukri_spider\items_2.csv'
			self.skills = get_from_memory(file_path)

	def get_skill_from_job(self):
		pass

	def get_skill_from_candidate_details(self):
		pass

	def get_skill_from_resumes(self):
		pass

	def combine_skills(self):
		return self.skills
