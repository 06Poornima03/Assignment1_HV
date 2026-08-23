from flask import Flask
from flask import jsonify

app = Flask(__name__)
votes={}

@app.route('/')
def home():
    return "Welcome to the App"

@app.route('/health')
def health():
    return "App is running"

def vote_resp(name):
   return jsonify({
      "message":"Voted",
      "Name":name,
      "votecount":votes[name]
   })

@app.route('/vote/<name>')
def vote(name):
  if name in votes:
     votes[name] +=1
  else:
    votes[name] = 1
  return vote_resp(name)


@app.route('/results')
def results():
   return jsonify(votes)

@app.route('/reset')
def reset():
   votes.clear()
   return jsonify({
      "message":"Votes reset successfully"
   })