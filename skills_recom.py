import csv 
import pandas as pd

df = pd.read_csv(r'C:\Users\Admin\PycharmProjects\web_apis\new_suggestions_2.csv', encoding = 'latin-1', low_memory=False)

#print(df_skills_skills.head())

def return_recom(s, rem_list):

    if df['antecedants'].str.contains(s).any():
        df_filtered = df['antecedants'].str.contains(s)
        skill = df.consequents[df_filtered].tolist()
        skill_set = set(skill)
        skill_list = list(skill_set)
        unique_skill_list = []
        for elem in skill_list:
            if ',' not in elem and elem not in unique_skill_list:
                unique_skill_list.append(elem.strip())
                
            elif ',' in elem:
                elem_split = elem.split(',')
                for el in elem_split:
                    if el.strip() not in unique_skill_list:
                        unique_skill_list.append(el.strip())
        
        try:
        	for el in rem_list:
        		try:
        			unique_skill_list.remove(el)
        		except:
        			continue
        except:
        	pass

        if len(unique_skill_list) == 0:
        	return 'empty'
        return unique_skill_list
        
    elif df['consequents'].str.contains(s).any():
        df_filtered = df['consequents'].str.contains(s)
        skill = df.antecedants[df_filtered].tolist()
        skill_set = set(skill)
        skill_list = list(skill_set)
        unique_skill_list = []
        for elem in skill_list:
            if ',' not in elem and elem not in unique_skill_list:
                unique_skill_list.append(elem.strip())
                
            elif ',' in elem:
                elem_split = elem.split(',')
                for el in elem_split:
                    if el.strip() not in unique_skill_list:
                        unique_skill_list.append(el.strip())

        try:
        	for el in rem_list:
        		try:
        			unique_skill_list.remove(el)
        		except:
        			continue
        except:
        	pass
        
        if len(unique_skill_list) == 0:
        	return 'empty'
        return unique_skill_list

    else:
    	return 'empty'
