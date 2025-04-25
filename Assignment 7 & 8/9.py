import re

def tokenize(text):
    # Define regular expressions for different token types
    patterns = {
        "url": r"https?://(?:www\.)?\S+|www\.\S+",
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "date": r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
        "number": r"\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b",
        "username": r"@\w+",
        "punctuation": r"[!\"#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~]",
        "word": r"[\u0900-\u097F\w]+"  # Replace \u0900-\u097F with your language's Unicode block
    }

    # Combine all patterns into a single regex
    combined_pattern = "|".join(f"(?P<{key}>{pattern})" for key, pattern in patterns.items())
    regex = re.compile(combined_pattern)

    # Tokenize the text
    tokens = []
    for match in regex.finditer(text):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        tokens.append((token_type, token_value))

    return tokens

# Example usage
if __name__ == "__main__":
    # Take input from the user
    sample_text = input("Enter the text to tokenize: ")
    
    # Tokenize the user-provided text
    tokens = tokenize(sample_text)
    
    # Print the tokens
    for token_type, token_value in tokens:
        print(f"{token_type}: {token_value}")