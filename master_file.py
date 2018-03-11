from get_skills import KeySkills
from preprocess import preprocessing_frame
from machine_learning import MachineLearning
from file_handle import FileHandle
skills = KeySkills(None).combine_skills()
len_skills = len(skills)
num_chunks = int(len_skills/15000)
rest_skills = len_skills%15000
if rest_skills != 0:
	for k in range(0, num_chunks):
		short_skills = skills[15000*k:15000*(k+1)]
		ml = MachineLearning(short_skills)
		ml_dataframe = ml.get_processed_frame()
		csv_file = FileHandle(ml_dataframe)

else:
	short_skills = skills[15000*num_chunks:]
	ml = MachineLearning(short_skills).get_processed_list()
	ml_dataframe = ml.get_processed_frame()
	csv_file = FileHandle(ml_dataframe)
