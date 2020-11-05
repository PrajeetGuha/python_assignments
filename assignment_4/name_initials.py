s = input('What is your name?')

phrases = s.split()
initials = ''

for phrase in phrases:
    initials += phrase[0].capitalize()

print(initials)