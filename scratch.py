# # def add_things(*kwargs):
# #     print(kwargs)
# #
# # add_things({"I like pie": True})
#
# from nltk.corpus import stopwords
# s=set(stopwords.words('english'))
#
#
# from collections import Counter
# delim = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']
# # the above will end up being a really long list!
# word_freq = Counter(recipe_str.lower().split())
# for delim in set(delims):
#     del word_freq[delim]
# return freq.most_common()

# import nltk
# from nltk.corpus import stopwords
# from nltk.corpus import stopwords
# set(stopwords.words('english'))
#
# txt="things and stuff and whatever"
# print filter(lambda w: not w in s,txt.split())
#
#
temp = float(input("thingy: "))
ans = temp * 9/5 - 459.67

print(ans)
