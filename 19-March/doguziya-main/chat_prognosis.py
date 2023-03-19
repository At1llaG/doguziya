import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('Data_JSON/prognosis.json', encoding='utf-8') as json_data:
    intents = json.load(json_data)

FILE = "data_prognosis.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"
print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"
    sentence = input("You: ")
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    print("h1")
    
    tag = tags[predicted.item()]

    print("h2")

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    
    print("h3")
    print(tag)
    
    if prob.item() > 0.45:
        print("h4")
        print(tag)
        for prog in intents['progronis']:
            #print("h5")
            #print(prog["tag"])
            if tag == prog["tag"]:
                print("h6")
                print(f"{bot_name}: {prog['id'], prob.item()}")
    else:
        print(f"{bot_name}: I do not understand...")