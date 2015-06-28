# Basic Moderation Bot

This is a very basic moderation bot. It kick if :
- Someone says a bad word (bad words are in the badwords.txt file);
- Someone floods (more than 350 characters in a message).

Before run the bot, please edit the config.txt file like this :  
`server:<adress of the server here>`  
`port:<port of the server here, default "6667">`  
`channel:<IRC channel here>`  
`nick:<nick of bot here>`  
`realname:<real name of bot here, default "realname">`  

When the bot is connected, please give op to the bot :  
`/op <nick of bot>`  

### To install :
On GNU/Linux operating systems :  
`sudo apt-get install python-irclib # Install the irclib librairie.`  
`chmod +x bot.py # Give execution right to the python file.`  
`./bot.py # Run the bot.`  
