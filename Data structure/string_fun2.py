from data import story

print(f'total chars in the story:{len(story)}')

# counting function
a_count = story.count('a')
print(f'a occurs {a_count} times.')
the_count = story.lower().count('the')
print(f'the occurs {the_count} times .')

# replace

ustory = story.replace('o','a')
print(ustory)

# remove

ustory = story.replace('of','')
print(ustory)

# remove all vowels
no_vowel_story = story.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
print(no_vowel_story)