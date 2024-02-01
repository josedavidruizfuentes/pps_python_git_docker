from bayeta import frotar

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/frotar/<int:n_frases>', methods=['GET'])
# ‘/’ URL is bound with hola_mundo() function.
def hola_mundo(n_frases):
	frases = frotar(n_frases)
	return frases




# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run(host='0.0.0.0', port=5000)
