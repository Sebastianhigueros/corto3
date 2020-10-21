class comporbar_NIT:

	def __init__(self,no_nit):
		self.no_nit = no_nit

	def comprobar(self, no_nit):
		
		nit = no_nit.replace(' ', '')

		sin_guion = nit.replace('-','')	

		multiplicador = 1

		utlimo_digito = sin_guion[-1]

		resto_nit = list(sin_guion[0:-1])

		inverso_resto = resto_nit.reverse()

		try:
			suma = 0

			for n in resto_nit:
				multiplicador += 1
				suma += int(n)*multiplicador

			res = suma % 11
			comprobacion = 11 - res

			if suma >= 11:
				res = suma % 11
				comprobacion = 11 - res

			if comprobacion == 10:
				if utlimo_digito.upper() == 'K':
					return {
						'valor' : True

					}	
			elif comprobacion == int(utlimo_digito):
				return {
					'valor' : True

				}
			else:
				return {
					'valor': False

				}

		except:

			return {
					'valor': False

				}
			

