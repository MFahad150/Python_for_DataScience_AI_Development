space_String = "Space is the area outside the earth. Planets, meteors, stars, and other celestial objects can be found in space. Meteors are objects that fall from the sky. There is a lot of silence in space. If you scream loudly enough in space, no one will hear you. Air does not exist in space! What a strange experience that would be! Yes, indeed! Basically, its just a vacuum. No sound waves can travel in this space and no sunlight can scatter in it. A black blanket can sometimes cover space. There is some life in space. Stars and planets are separated by a vast distance. Gas and dust fill this gap. Celestial bodies also exist in other constellations. There are many of them, including our planet."

# Create a class called TextAnalyzer to analyze text.
class textAnalyzer(object):

    # The __init__ method initializes the class with a 'text' parameter.
    # We will store the provided 'text' as an instance variable
    def __init__ (self,text):

        # remove punctuation
        formattedText = text.replace(',','').replace('.','').replace('!','').replace('?','')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll(self):

        # split text into words
        wordList = self.fmtText.split(' ')

        #Create Dictionary
        freqMap = {}
        for word in set(wordList):      # use set to remove duplicates in list
            freqMap[word]= wordList.count(word)

        return freqMap
    
    def freqof(self,word):

         # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0


# Instance of TextAnalyzer Class.
analyzed = textAnalyzer(space_String)

# Call the function that converts the data into lowercase
print("Formatted Text:", analyzed.fmtText)

# Call the function that counts the frequency of all unique words from the data.
freqMap = analyzed.freqAll()
print(freqMap)

# Call the function that counts the frequency of specific word
word = "celestial"
frequency = analyzed.freqof(word)
print("\nThe word",word,"appears",frequency,"times.")