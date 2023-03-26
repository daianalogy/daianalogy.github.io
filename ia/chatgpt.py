#!/usr/bin/env python3

import openai
import sys

openai.api_key = "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"

print("Bienvenido a ChatGPT")

cont = "s"
pregunta = sys.argv[1]

while(cont.lower() == "s"):
	
	
	#pregunta = input("\n¿Dime en qué puedo ayudarte?\n ")
		
	if pregunta == "exit":
		break
	
	completion = openai.Completion.create(engine = "text-davinci-003",
										  prompt = pregunta, 
										  max_tokens = 2048)										 
	print(completion.choices[0].text)
	
	cont = input("\n¿Tienes más dudas? [s para continuar/N] ")
	if cont == "s":
		pregunta = input("\n¿Dime en qué puedo ayudarte?\n ")
	else:
		break
		

