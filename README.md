# ChronoUmaWebScrapper

Web scrapper (made specifically for Chronogenesis.net). It's purpose is to scrap just the table consisting of user names, fan count and daily average and importing it into google sheets using the service account.
__________________________________________________________

For it to work properly User needs to make their own free google service account, generate and download a credentials key (base name in code is "credentials.json" so best to change it to the same one), and add it to the same folder as the script. 

Another thing is changing the url in the script, all the User needs to do is open the script and change the link in variable named 'url' (it's at the top of the script) to the Chronogenesis link of the desired club.
__________________________________________________________

# Requirements:
- Chrome browser
- packages installed from 'requirements.txt'
