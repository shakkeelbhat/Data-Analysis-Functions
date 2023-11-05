# Function to count the number of syllables in a word
import re
def count_syllables(word):
  word = word.lower()
  vowels = "aeiouy"
  syllables = re.findall (f"[{vowels}]+", word)

  count = len(syllables)

  if count == 0:
    return 1
  if word.endswith ("e"):
    count -= 1
  if word.endswith ("le"):
    count += 1
  if count == 0:
    count += 1
  return count
