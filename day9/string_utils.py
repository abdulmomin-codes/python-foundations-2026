#• slugify(text): This function should take a regular string and turn it into a URL-friendly "slug." 
#Usually, this means converting the text to lowercase, removing extra outer spaces, and 
#replacing spaces between words with hyphens (e.g., "Hello World" becomes "hello-world").
#• count_vowels(text): This function should loop through the given string 
#and return the total number of vowels (a, e, i, o, u, both uppercase and lowercase) found inside it.

def slugify(text):
    clean = '-'.join(text.lower().split())
    return clean

def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    data = []
    for letters in text:
        if letters in vowels:
            data.append(letters)
    return data, len(data)



