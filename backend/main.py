import model_creation

close_predicted = model_creation.prediction()[0]
actual_open = float(model_creation.prediction()[1])

difference = ((close_predicted - actual_open) / actual_open) * 100

if(close_predicted >= actual_open):
    print("A criptomoeda terá uma variação positiva de %.2f daqui a 1 hora." % difference[0])
    
else:
    print("A criptomoeada terá uma variação negativa de %.2f daqui a 1 hora." % difference[0])
