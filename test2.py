# encoding:utf-8



import json


with open('Data_JSON/intents.json', encoding='utf-8') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []
# loop through each sentence in our intents patterns
for intent in intents['intents']:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)



#tags = sorted(set(tags))


print(len(tags), "tags:", tags)

