# Basic IRC Moderation Bot

This is a very basic IRC moderation bot. It kicks if :
- Someone says a bad word (bad words are in the badwords.txt file);
- Someone floods (more than 350 characters in a message).

Before running the bot, please edit the config.txt file like this :  
`server:<server adress>`  
`port:<server port, default "6667">`  
`channel:<IRC channel>`  
`nick:<nickname of the bot>`  
`realname:<real name of the bot, default "realname">`  

When the bot is connected, please give channel operator status to the bot :  
`/op <nick of bot>`  

### How to install it ?

On GNU/Linux operating systems :  
`sudo apt-get install python-irclib # Installs the python-irclib librarie.`  
`chmod +x bot.py # Gives the execution right to the python file. (normally, this command is unnecessary because the bot.py file has already the execution right)`  
`./bot.py # Runs the bot.`  
