# Mental-Health-ChatBot

This is Eva, a mental-health chatbot.

Eva is able to converse and interact with human users using spoken, written, and visual languages.
Eva has the potential to be useful tools for individuals with mental disorders,
especially those who are reluctant to seek mental health advice due to stigmatization.
Eva is your totally anonymous companion.
Say hi and see the magic
Also, she doesn't leak secrets
:wink:




## Deployment:

### Prerequisites:

Python version >= 3.6 and < 3.8
Use  pip install rasa-x -i https://pypi.rasa.com/simple to install rasa-x

Use the code to clone it to your system:
git clone https://github.com/Huzaib/Mental-Health-ChatBot 



## Working:

The general functional framework of mental health chatbots is based on Cognitive Behavioral Therapy methodology. CBT is a form of talking therapy designed to manage mental health states by rearranging the way the patient perceives it, i.e., making negative thoughts positive.
The NLP algorithm performs sentiment analysis to detect trigger words, performs intent classification, select the most probable response and handle the flow of conversation 


Eva makes the impression of a credible and trustworthy conversation partner that can hear you out and offer a detached point of view on things.
The common flow of conversation is as follows:
* Kickstarting a topic for conversation, 
* Asking directional questions, 
* Providing follow-ups to expand responses. 

### Tested using :
* rasa run --debug command
* rasa x command 
* rasa interactive command


## Testing Video

![](https://j.gifs.com/E8okKm.gif)



## Components
* stories.md - Inside data folder - Contains the storylines of different paths the bot can encounter
* nlu.md - Inside data folder - Contains the data on which the bot laerns and decides intent classification
* domain.yml - Contains all the possible actions, entities, responses and intents
* actions.py - Contains custom actions to run custom Python code
* credentials.yml - Consists of all the credentials necessary for connecting the bot to different platforms
* Other auto generated files



### Feel free to contribute
## Don't forget to star the repo :wink:






