# IPCheckers
This is a small python program that will inform the user if their external ip has changed

N.B If running the files gives an error message saying the files is dos mode error ('/r)'
then open the offending file in vim and use the `:set binary` then save this will correct this problem 

run the `install.sh` file to get required libs and create the directories that are needed.

---

# Telegram messaging

to get started you will need 3 things
* a telegram account (duh)
* the API key for the bot
* the chat id for the bot

open the telegram web interface using the following link `https://web.telegram.org`
and search for `BotFather` account.

start a conversation with the BotFather and type in `/newbot` then give the bot a name for this i have used `IP_Checker` you can use what ever you like and a username i have used `IP_Checker` again to avoid confusion.

this will get you your API key which will look somthing like this `1234567890:ABCDEFGHIJKLMNOPXXXXXXXXXXXX` this will be stored in the settings.json file under `token`

you will need to make a request using this key so copy the following into your browser replacing `<apikey>` with your key : `https://api.telegram.org/bot<apikey>/getMe`

this will give you a json response with your chat ID it should look somthing like this:

```javascript
ok	true
result	
id	11xx3xxxx
is_bot	true
first_name	"IP_Checker"
username	"IP_checker"
can_join_groups	true
can_read_all_group_messages	false
supports_inline_queries	false
```


then add your chat id to the settings.json and you should end up somthing that looks like this:
```javascript
{
        "name": "telegram",
        "id": "1",
        "is_enabled": true,
        "token": "0000000000:1234567890:ABCDEFGHIJKLMNOPXXXXXXXXXXXX",
        "chat_id":"11xx3xxxx",
        "message": "Your new IP address is: "}
        
 ```
