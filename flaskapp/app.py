from flask import Flask, request, jsonify
from redis import Redis

# initializing a new flask app
app = Flask(__name__)

# initializing a new redis database
# Hostname will be same as the redis service name
# in the docker compose configuration
redis = Redis(host ="localhost", db = 0, socket_timeout = 5,
			charset ="utf-8", decode_responses = True)

# Our app has a single route allowing two methods POST and GET.


@app.route('/', methods =['POST', 'GET'])
def animals():

	if request.method == 'POST':
		# Take the name of the animal
		name = request.json['name']
		# push the name to the end of animals list in the redis db
		redis.rpush('animals', {'name': name})
		# return a success
		return jsonify({'status': 'success'})

	if request.method == 'GET':
		# return complete list of names from animals
		return jsonify(redis.lrange('animals', 0, -1))

