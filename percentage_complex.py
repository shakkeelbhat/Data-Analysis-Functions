# Function to compute the percentage of complex words in a text
def percentage_complex(text):

  
  words = re.findall (r"\w+", text)
  words = [word for word in words if word.isalpha()]

  complex_count = sum(map(is_complex, words))
  total_count = len(words)

  percentage = complex_count / total_count * 100

  return round(percentage, 2)
