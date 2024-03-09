# Test to check if properly formatted

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

quotes = read_quotes("quotes.txt")

print(quotes[18].strip())
