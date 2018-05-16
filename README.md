## Monitor a cold room

We have a rather large walk in cold room that we store all the beer that is canned or kegged and waiting for delivery. If there were ever a problem with the cooling of this room, especially in summer it would be a mission critical problem. This is a way for us to have a way to know what is happening. 

### watchin.sh

This is ran by RC.local at startup and is the means by which the temps are checked


### textnathan.sh

This is software procured from textmagic.com and is their software. It is sidtrubuted here with the understanding that it is freely available software but is not my software. More information can be found here: https://www.textmagic.com/docs/api/start/


### spreadsheet.py

This is how I not only get the data from the sensors but also record it to Google Sheets