words = ['environment', 'always', 'protect', 'irreplaceable', 'different', 'absolutely', 'greatest', 'glory', 'predictable', 'predictable', 'flavor', 'should', 'order', 'just', 'different']

def checkSpellingAndSpace(sentence):
    sentence = sentence.split()
    if len(sentence) < 2:
        print('Invalid input')
    else:
        for i in range(len(sentence)):
            if sentence[i] in words:
                continue
            else:
                for word in words:
                    if ''.join(sorted(word)).startswith(''.join(sorted(sentence[i]))[0]) and len(word) == len(sentence[i]):
                        sentence[i] = word
                        break 
        print(' '.join(sentence))
                        

if __name__ == '__main__':
    sentence = input()
    checkSpellingAndSpace(sentence)