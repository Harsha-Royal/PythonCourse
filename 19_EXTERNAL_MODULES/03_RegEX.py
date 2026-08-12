import re
text = "the quick brown fox jumps over the lazy dog."

# Search for a pattern 

# match = re.search("brown",text)
# print(match)
# if match:
#     print("Match Found!")
#     print("Start index:", match.start())
#     print("End index:", match.end())


#find all occurences of a pattern 

matches = re.findall("the",text,re.IGNORECASE) #case-insensitive search
print("Matches",matches)
