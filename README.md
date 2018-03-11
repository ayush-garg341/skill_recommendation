# skill_recommendation
This is skill recommendation using apriori algorithm (association mining)<br />
**Description** :- We make a list of list of skills and pre-process them. After that we apply apriori algorithm on this list to get 
frequent patterns and skills which are related to each other or have high probability of occuring together. There are two parameters to adjust
_support_ and _confidence_ .<br />
**get_skills.py** :- this file read the skills coming from various sources but as for now I have data stored in csv file.<br />
**http_api.py** :- This contains the code if one wants to post the data at any URL.<br />
**preprocess.py** :- this is to pre-process the data we have and remove unwanted characters.<br />
**machine_learning.py** :- this is the main file as it generates the dataframe of antecedants and consequents of skill-set.<br />
**file_handle.py** :- to save the datframe into csv so that we can look up afterwards the frequent patterns.<br />
**skill_recom.py** :- this code recommend the related skills of a particular skill by looking into the csv file that we made earlier.<br />
**suggesting_api.py**:- this is Flask api to make the code live.<br />
**database.py** :- this is if we were to connect to database and fetch data directly from there instead of storing it in csv. (still to implement)
