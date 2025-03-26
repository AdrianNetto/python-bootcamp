# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    splited_text = text.split(' ')[::-1]

    return " ".join(splited_text)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))