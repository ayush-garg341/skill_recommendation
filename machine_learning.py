import numpy, re
import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori, association_rules
import nltk
from get_skills import KeySkills
from preprocess import preprocessing_frame


def antecedent(assoc_cols):
    antecedants_list = []
    for value in assoc_cols['antecedants'].values:
        value_list = [list(x) for x in value]
        s = ''
        for val in value_list:
            s = s + ' '
            for el in val:
                s = s + el
            s = s + ','
        antecedants_list.append(s.strip(', '))

    return antecedants_list


def consequent(assoc_cols):
    consequents_list = []
    for value in assoc_cols['consequents'].values:
        value_list = [list(x) for x in value]
        s = ''
        for val in value_list:
            s = s + ' '
            for el in val:
                s = s + el
            s = s + ','
        consequents_list.append(s.strip(', '))

    return consequents_list



class MachineLearning(object):

	def __init__(self, skill_frame=None):
		self.skill_frame = skill_frame
		if self.skill_frame is None:
			self.skill_frame = KeySkills(None).combine_skills()


	def get_length_of_frame(self):
		return len(self.skill_frame)

	def has_contain_null(self):
		return self.skill_frame.isnull().any()

	def drop_null_from_frame(self):
		self.skill_frame = self.skill_frame.dropna()
		return self.skill_frame

	def remove_empty_from_frame(self):
		self.skill_frame = self.skill_frame[self.skill_frame != 'empty']
		return self.skill_frame

	def get_processed_list(self):
		
		if self.has_contain_null():
			self.skill_frame = self.drop_null_from_frame()

		self.skill_list = preprocessing_frame(self.skill_frame)
		#self.skill_list = [ get_list(rows, specific_skills) for _, rows in self.skill_frame.iteritems() ]
		return self.skill_list

	def get_oht_dataframe(self):
		self.short_list = self.get_processed_list()
		if len(self.short_list) < 15000:
			self.short_list = self.short_list[:]
		else:
			self.short_list = self.short_list[:15000]
		print(len(self.short_list))
		oht = OnehotTransactions()
		oht_ary = oht.fit(self.short_list).transform(self.short_list)
		data_frame = pd.DataFrame(oht_ary, columns = oht.columns_)
		return data_frame


	def get_frequent_itemset(self):
		df = self.get_oht_dataframe()
		frequent_itemsets = apriori(df, min_support = 0.01, use_colnames = True) # earlier 0.001
		return frequent_itemsets
    

	def get_assoc_dataframe(self):
		assoc = association_rules(self.get_frequent_itemset(), metric = "confidence", min_threshold = 0.7) # earlier 0.6
		return assoc


	def get_assoc_columns(self):
		assoc_df = self.get_assoc_dataframe()
		return assoc_df.columns


	def get_processed_frame(self):
		assoc = self.get_assoc_dataframe()
		assoc_cols = assoc[['antecedants', 'consequents']]
		antec_list = antecedent(assoc_cols)
		conseq_list = consequent(assoc_cols)
		new_df = pd.DataFrame({'antecedants': antec_list, 'consequents': conseq_list})
		return new_df