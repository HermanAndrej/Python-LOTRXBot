import random
import tweepy

# Enter the keys here
client = tweepy.Client(consumer_key='',
                       consumer_secret='',
                       access_token='',
                       access_token_secret='')

# Function to read quotes from file
def read_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read lines and split quotes by empty lines
        quotes = file.read().strip().split('\n\n')

    formatted_quotes = []
    for quote in quotes:
        lines = quote.strip().split('\n')
        formatted_quote = ''
        for line in lines:
            sentences = line.strip().split('. ')
            for i, sentence in enumerate(sentences):
                # Check if the sentence is not empty (might happen due to split)
                if sentence:
                    formatted_quote += sentence.strip()
                    # Add a period only if it's not the last sentence
                    if i != len(sentences) - 1:
                        formatted_quote += '. '
                    formatted_quote += '\n'  # Add new line after each sentence
        formatted_quotes.append(formatted_quote.strip())

    return formatted_quotes


# Function to select a random quote
def get_random_quote(quotes):
    return random.choice(quotes)

# Function to tweet a quote
def tweet_quote(quote):
    client.create_tweet(text = quote)  # Update status with the quote text
    print("Tweeted:", quote)


if __name__ == "__main__":
    # File path of your quotes file
    quotes_file_path = 'quotes.txt'

    # Read quotes from file
    quotes = read_quotes(quotes_file_path)

    # Get a random quote
    random_quote = get_random_quote(quotes)

    # Tweet the quote
    tweet_quote(random_quote)
