Python script for tweeting a quote from a file. A tiny project made out of boredom with a goal of testing the Twitter API. This Python script is designed to tweet random quotes from a file using the Twitter API. It utilizes the Tweepy library to interact with the Twitter API for posting tweets. The script reads quotes from a text file, formats them properly, selects a random quote, and then tweets it. There are still some significant issues to fix, for example Twitter API doesn't allow tweeting identical tweet more than once, so that needs to be addressed, perhaps by making file of indices for keeping track of quotes fetched from a quotes.csv file. Also, there is a character limit for a tweet, and some quotes might exceed that limit. Tweeted text could also be better formatted so it looks nicer. The original idea was to schedule the script to run once a day using Heroku, but after an hour of trying to setup it I gave up. I tried making .bat file and scheduling task via Windows in-built Task scheduler, but something went wrong after a few days and I just didn't bother to fix it.

Twitter profile: https://twitter.com/LOTRxBot

Setup:

Installation: Before running the script, ensure you have Python installed on your system. You'll also need to install the Tweepy library, which can be done via pip:

Copy code pip install tweepy Twitter API Access: To use this script, you need to have a Twitter Developer account and create an application to obtain the necessary API keys and access tokens. You need to fill in these keys and tokens in the script where indicated.

Quotes File: Prepare a text file (quotes.txt in this example) containing quotes separated by empty lines. Each quote can span multiple lines, with sentences separated by periods.

Usage:

Running the Script: Execute the script in a Python environment: python TwitterQuoteBot.py

Tweeting Quotes: Once the script runs, it will select a random quote from the file, format it properly, and tweet it using your Twitter account associated with the provided API keys and access tokens.

File Structure:

TwitterQuoteBot.py: The main Python script file. quotes.txt: The text file containing the quotes. Can be replaced by another file or modified as needed.

Note:

Ensure your Twitter Developer account settings allow for the specified actions (tweeting). Handle the API keys and access tokens securely. Do not share them publicly.

Dependencies:

Python 3.x Tweepy library
