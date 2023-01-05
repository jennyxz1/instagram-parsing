import json
import matplotlib.pyplot as plt
import numpy as np


#FOLLOWERS AND FOLLOWING

def follow(raw_followers, raw_following):
    #open json files into python
    iter_followers = json.load(raw_followers)
    iter_following = json.load(raw_following)

    #initialize empty lists
    followers = []
    following = []

    for i in iter_followers["relationships_followers"]:
        for j in i["string_list_data"]:
            followers.append(j['value'])

    for x in iter_following["relationships_following"]:
        for y in x["string_list_data"]:
            following.append(y['value'])

    for f1 in following:
        if f1 not in followers:
            print(f1)

    #close file 
    raw_followers.close()
    raw_following.close()

#open followers json file
raw_followers = open('path/to/followers.json')
raw_following = open('path/to/following.json')

follow(raw_followers, raw_following)



#MESSAGES
most_frequent = {}

def most_frequent_function(raw):
    iter_dict = json.load(raw)
    for r in iter_dict['messages']:
        try:
            splitted = r['content'].split()
            for word in splitted:
                if word not in most_frequent:
                    most_frequent[word] = 1
                else:
                    most_frequent[word] += 1
        except:
            continue

raw_message1 = open('path/to/message_1.json')
most_frequent_function(raw_message1)

sorted_words = sorted(most_frequent.items(), key = lambda x:x[1], reverse = True)

#pi chart
def pi_chart(sorted):
    numbers = []
    values = []

    for z in sorted[:100]: #top 100
        numbers.append(z[1])
        values.append(z[0])

    plt.pie(numbers, labels = values)
    plt.legend()
    plt.show() 

pi_chart(sorted_words)

#top 100 words
for w in sorted_words[:100]:
    print(w)


