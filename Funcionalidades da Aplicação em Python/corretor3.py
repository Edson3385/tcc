from textblob import TextBlob
 
a = "i lov yu"          
print("original text: "+str(a))
 
b = TextBlob(a)
 
print("corrected text: "+str(b.correct()))