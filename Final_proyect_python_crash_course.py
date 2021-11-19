# Here are all the installs and imports you will need for your word cloud script and uploader widget

!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
        
    # LEARNER CODE START HERE
    
     # We are going to eliminate all the uninteresting words yo can process your text
    #We need to iterate into all the words and then eliminate all this words using the remove method
    #We need to convert the string into a list of strings first 
    
    for letter in file_contents:
        if letter in punctuations:
            file_contents = file_contents.replace(letter, "")
    
    #The we convert file_contents in a list
    file_contents = file_contents.split(" ")
    
    #Converting every strings of the list into lowercase
    for i in range(len(file_contents)):
        file_contents[i] = file_contents[i].lower()
    
    #Then we need to eliminate all uninteresting words
    for word in list(file_contents):
        if word in uninteresting_words:
            file_contents.remove(word)
    
    #Finally we need to make a list with the frequency of every word
    result = {}
    for item in file_contents:
        if (item in result):
            result[item] += 1
        else:
            result[item] = 1
            
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(result)
    return cloud.to_array()

    # Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()