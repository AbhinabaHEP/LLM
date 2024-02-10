#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:





# In[1]:
pip install nltk


import nltk
import numpy as np
import random
import string
import bs4 as bs
import urllib.request
import re


# In[3]:


link= urllib.request.urlopen('https://en.wikipedia.org/wiki/Particle_physics')


# In[4]:


#import urllib.request

#class AppURLopener(urllib.request.FancyURLopener):
#    version = "Mozilla/5.0"

#opener = AppURLopener()
#response = opener.open('https://envotechsolutions.co.in/')


# In[95]:


link=link.read()


# In[96]:


from bs4 import BeautifulSoup
data=BeautifulSoup(link,'lxml')


# In[97]:


data


# In[98]:


data_paragraphs= data.find_all('p')  


# In[99]:


data_text=''
for para in data_paragraphs:
    data_text +=para.text


# In[100]:


data_text


# In[101]:


data_text=data_text.lower()


# In[102]:


data_text


# In[103]:


data_text=re.sub(r'\[[0-9]*\]',' ',data_text) #to remove all eqn nos.
data_text=re.sub(r'\s+',' ',data_text)        #to remove all \n


# In[104]:


data_text


# In[105]:


import nltk



# In[106]:


#to make sentences out of data
sen=nltk.sent_tokenize(data_text)
words=nltk.word_tokenize(data_text)


# In[107]:


sen


# In[108]:


words


# In[109]:


import nltk



# In[110]:


#lemmatizer....doggy,doggo,dogs to dog
wnlem=nltk.stem.WordNetLemmatizer()


# In[111]:


#perform lemmatization
def perform_lemmatization(tokens):
    return[wnlem.lemmatize(token) for token in tokens]   #each token is lemmatized using wnlem.lemmatize()


# In[112]:


#remove punctuations
pr=dict((ord(punctuation),None)for punctuation in string.punctuation)   #ord is for unique id out of punctuation....string.punctuation is used to clear all punctuation in string and store it in (pr)


# In[113]:


#Tokenizer to be used later
def get_processed_text(document):
    return perform_lemmatization(nltk.word_tokenize(document.lower().translate(pr)))    #order of data processing in the scrapped document


# In[114]:


#greeting mechanism 
greeting_inputs=("hey","hello","good morning","good evening","morning","evening","hi","whatsup")
greeting_responses=("heyy","hellow","hello, how's your morning?","good evening, what can i do for you?","*nods*","*nods*","heyy","Welcome, I am good and you")
def generate_greeting_response(greeting):   #splits down greeting to check how many tokens in them
    for token in greeting.split():
        if token.lower() in greeting_inputs:  #greeting in lower format
            return random.choice(greeting_responses)


# In[115]:


#for generating response we need vectorization
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 


# In[116]:


#make and generate a response function
def generate_response(user_input):
    bot_response=''    #first response should be a null response
    sen.append(user_input)   #append user commands to sentence list

    
    #develop a vectorizer and check similarity
    word_vectorizer=TfidfVectorizer(tokenizer=get_processed_text, stop_words='english')  #document will go inside this and lemmatization will be performed
    #convert all of our sentences into word vectors
    word_vectors=word_vectorizer.fit_transform(sen)
    #all_word_vectors = word_vectorizer.fit_transform(article_sentences) # this is the problematic line
    similar_vector_values=cosine_similarity(word_vectors[-1],word_vectors)  #cosine similarity
    #similar sentence no
    similar_sentence_number=similar_vector_values.argsort()[0][-2]
    
    #after flattening these valuesv we will sort them out and pick the matched vector
    matched_vector=similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched=matched_vector[-2]
    
    if vector_matched==0:
        bot_response=bot_response + "I am sorry I don't understand"
        return bot_response
    else:
        bot_response=bot_response + sen[similar_sentence_number]
        return bot_response


# In[ ]:


continue_flag=True
print("Hello I am Particle Zoo bot !")
while(continue_flag==True):
    human=input()
    human=human.lower() # convert human input to lower format
    if human!= 'bye':
        if human== 'thanks' or human=='thankyou':
            continue_flag=False
            print("Most welcome form Particle Zoo Bot")
        else:
            if generate_greeting_response(human) != None:
                print("Particle Zoo Bot"+ generate_greeting_response(human))
            else:
                print("Particle Zoo bot", end ="")
                print(generate_response(human))
                sen.remove(human)
    else:
        continue_flag=False
        print('Particle Zoo Bot says Sayonara!')
                


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




