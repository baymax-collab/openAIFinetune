import time
import os
import openai
openai.api_key = ""

f = openai.File.create(file=open("test.jsonl", "rb"), purpose='fine-tune')

print(f)

print("Wait file ready 30 seconds")
time.sleep(30) 

openFT = openai.FineTuningJob.create(training_file=f.id, model="gpt-3.5-turbo")

print(openFT)

time.sleep(5)

if (openFT.id) :
	print(openFT.id)
	print(openai.FineTuningJob.retrieve(openFT.id))
else:
	print("Do not start train")

