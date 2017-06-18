import os
from final import get_sentence, get_summary

filepath = os.path.join(os.getcwd(), "file2.txt")
with open(filepath) as obj:
    fullData = obj.read()
    fullData = fullData.decode('utf8', 'ignore')



title_of_summary = get_sentence(fullData)
title_of_summary = title_of_summary[0]
# last_line = title_of_summary[-1]
print "\t\t\t\t\t\t\t\t\t*---------------------------------Title------------------------------*\n%s"%title_of_summary

summary_length = raw_input("Enter the number of lines you want your summary to be.\n")
summary_length = int(summary_length)
print("\n\t\t\t\t\t\t\t\t\t*---------------------------------Summary------------------------------*\n")
ss = get_summary(fullData, summary_length)
# print "\t\t\t\t\t\t\t\t\t*---------------------------------Title------------------------------*\n%s" % last_line


