from flask import request
from flask_cors import CORS
from  retorno_datos import Retorno
from invertir_cadena import Invertir
from comporbar_Nit import Comprobar

app = Flask(__name__)

CORS(app)

@app.route('/misDatos', methods=['GET'])
def datos():
		
	return Retorno.dump();


@app.route('/inversor', methods = ['POST'])
def invertir():
	
	if request.method == 'POST':

		cadena_entrada = request.form.get('cadena_entrada')

		return Invertir.invertir(cadena_entrada)

@app.route('/comprobarNIT', methods = ['POST'])	
def comprobar():
	
	if request.method == 'POST':

		no_nit = request.form.get('no_nit')	

		return Comprobar.comprobar(no_nit);