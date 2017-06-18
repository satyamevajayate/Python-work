import os

import nltk

from nltk import *
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
#
#
#
# filepath = os.path.join(os.getcwd(), "file2.txt")
# with open(filepath) as obj:
#     fullData = obj.read()
#     fullData = fullData.decode('utf8', 'ignore')

def get_sentence(fullData):
    sentence = fullData.replace("\n", ". ")
    return sentence.split(". ")


def re_order(output_sents, input):
    output_sents.sort(lambda s1, s2:
                      input.find(s1) - input.find(s2))
    return output_sents

# get_sentence(fullData)

def summary(fullData, summary_length):
    myregex = RegexpTokenizer('\w+')

    # convert all the words to lowercase for ease of processing
    words = [word.lower() for word in myregex.tokenize(fullData)]

    #remove all stopwords
    word = [withoutStopwords for withoutStopwords in words if withoutStopwords not in stopwords.words()]

    frequency = FreqDist(word)
    # print(frequency.most_common(50))

    fifty_most_frequent = [wordd[0] for wordd in frequency.items()[:100]]

    # actual_sents contains all the original sentences with the case intact
    my_token = nltk.data.load('tokenizers/punkt/english.pickle')    #Visit http://www.nltk.org/_modules/nltk/tokenize/punkt.html for more information.
    sentence = my_token.tokenize(fullData)
    usable_sentence = [lines.lower() for lines in sentence]
    # usable_sentence = get_sentence(fullData.lower())
    # usable_sentence = [item for item in get_sentence(fullData) if item != '']
    sentence_length = len(usable_sentence)
    # usable_sentence = []
    # for item in usable_sentence:
    #     if item != '':
    #         usable_sentence.append(item)

    # total_sentences = len(usable_sentence)
    #num_freqWords_inSents stores the number of times a frequent word occurs in each of the sentences
    num_freqWords_inSents = [0] * sentence_length

    output_sents = []
    # Loop through all the sentences and all the words to see which sentences contain occurences of the most frequent words
    for elem in fifty_most_frequent:
        for i in range(0,sentence_length):
            if elem in usable_sentence[i] and sentence[i] not in output_sents:
                output_sents.append(usable_sentence[i])
                break
            if len(output_sents) >= summary_length: break
        if len(output_sents) >= summary_length: break
                # num_freqWords_inSents[i] = num_freqWords_inSents[i] + 1
                # if (usable_sentence[i] not in output_sents):
                #     output_sents.append(usable_sentence[i])

    #store the contents of usable_sentence in a list so that it can be used later
    # num_freqWords_inSents[:] = [something for something in num_freqWords_inSents if something != 0]

    #map the elements in two lists using the zip function for easy comparision
    # zipped = zip(num_freqWords_inSents, output_sents)

    #sort the output so that the sentences which contain the most frequent words is displayed first.
    # sorted_output = [two for (one,two) in sorted(zipped, reverse=True)]

    #take the first two sentence with the most frequent words
    # final_output = sorted_output[0:7]

    # out_sentence = re_order(final_output, fullData)

    # return " ".join(final_output)
    return re_order(output_sents, fullData)

def get_summary(fullData,summary_length):
    print "\n".join(summary(fullData, summary_length))





