# text-generation
Hi everyone!
So as it stands there's two files in this repository:

+ MarkovChain.py
+ TextPrediction.py

MarkovChain.py can be run from the command line as 
python3 MarkovChain.py numberOfWords nameOfFile
where you need to provide the number of words to use for text generation and what file to use to seed the Markov chain

TextPrediction.py is an inversion of the idea of the Markov chain where you have a similar dictionary approach but instead of randomly picking words for you, you can get suggestions based on things you've already typed.

run this program as 

python3 TextPrediction.py

and enter a message one word at a time. When you hit repeated patterns in sentences you should start getting new suggestions for words to choose.
