from get_skills_modify import return_skills
from flask import Flask,request
from flask_cors import CORS, cross_origin
#from sql_02 import skill_index
from suggesting import jd_skills
# import skills_recom
from smtp_details import details

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def index():
    return 'Hello Ayush Garg'


@app.route('/keyword_suggestions', methods = ['GET', 'POST'])
@cross_origin()
def run():
    #skill=request.args.get('name','abc')
    #return skill
    if request.method == "POST":
        print(True)
        skill = request.form['keyskills']
    skill = skill.lower()
    a = return_skills(skill)
    print(type(a))
    if a=='':
        return a
    print(a)
    print(skill in a)
    try:
        a.remove(skill)
    except:
        pass
    skill_string = ','.join(a)
    return skill_string


@app.route('/jd_suggestions', methods = ['GET', 'POST'])
@cross_origin()
def run_jd():
    #skill=request.args.get('name','abc')
    rem_list = []
    if request.method == "POST":
        print(True)
        job_desc = request.form['jd']

    print(job_desc)
    a = jd_skills(job_desc)
    if a=='':
        return a
    print(a)
    skill_string = ', '.join(a)
    return skill_string

@app.route('/jd_suggest')
@cross_origin()
def run_null():
    #skill=request.args.get('name','abc')
    #return skill
    rem_list = []
    #a = return_skills(skill)
    a = jd_skills('')
    if a=='':
        return a
    print(a)
    skill_string = ', '.join(a)
    return skill_string

@app.route('/extract_data/<string:check>')
@cross_origin()
def extract(check):
	sec_check = '32kllk234u32lk34lk4553535333'
	if check == sec_check:
		details()
		return 'completed run'

	else:
		return 'somthing went wrong'

if __name__=="__main__":
    app.run(host = '0.0.0.0', debug = True)
