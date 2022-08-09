from data import story

print(f'total chars in the story: {len(story)}')
words = story.split()
print(f'total word in the story: {len(words)}')
print(words)
print(f'total unque words in the story:{len(set(words))}')

print(words)

sentences = story.split('.')
print(f'total sentences in the story:{len(sentences)}')
print(sentences)

lines = story.split('\n')
print(f'total lines in the story: {len(lines)}')
print(lines)

poem_list = [
    'twinkle , twinkle , little star ',
    'how i wonder what you are!',
    'up above the world so high,',
    'like a dimond in the sky.',
]
poem = '\n'.join(poem_list)
print(poem)