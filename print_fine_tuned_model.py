import openai
openai.api_key = ""
# 下面的fid，为train.py的openFT.id，
fid = ''

print(openai.FineTuningJob.retrieve(fid))