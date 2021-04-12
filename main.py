punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
#Remove punctuation
def strip_punctuation(string):
    for char in punctuation_chars:
            string = string.replace(char, '')
    return string
 
#Find positive words
def get_pos(string):
    string = strip_punctuation(string)
    string = string.lower()
    string = string.split()
    tot = 0
    for word in string:
        if word in positive_words:
            tot += 1
    return tot
 
#Find negative words
def get_neg(string):
    string = strip_punctuation(string)
    string = string.lower()
    string = string.split()
    tot = 0
    for word in string:
        if word in negative_words:
            tot += 1
    return tot
 
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
 
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
 
#File + formatting  
data1 = open("project_twitter_data.csv")
data2 = open('resulting_data.csv', 'w')
def write(file):    
    data2.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    data2.write('\n')
    b = data1.readlines()
    print(b)
    b.pop(0)
    for line in b:
        line = line.replace('\n', '')
        a = line.split(",")
        data2.write('{}, {}, {}, {}, {}'.format(a[-2], a[-1], get_pos(line), get_neg(line), get_pos(line)-get_neg(line)))
        data2.write('\n')
write(data2)
