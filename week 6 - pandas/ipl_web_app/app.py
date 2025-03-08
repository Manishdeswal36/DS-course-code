from flask import Flask,render_template,request
import requests
# i not complete the project because tag in html and api not work
# may me I complete in future . 
# current file
app = Flask(__name__)

# make a url router using decorator 
@app.route('/')
def home():
    respone = requests.get('http://127.0.0.1:5000/api/teams')
    teams = respone.json()['teams']
    #print(teams)
    return render_template('index.html',teams = sorted(teams))

@app.route('/team_vs_team')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = requests.get(url='http://127.0.0.1:5000/api/teams_vs_team?team1={}&team2={}'.format(team1,team2))
    response = response.json()
    
    respone1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = respone1.json()['teams']
    
    return render_template('index.html',result = response,teams = sorted(teams))

app.run(debug=True,port=7000)
        


