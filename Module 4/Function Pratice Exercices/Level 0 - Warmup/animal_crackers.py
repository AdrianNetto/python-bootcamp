# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(word):
    splited_words = word.split(' ')

    if splited_words[0][0] == splited_words[1][0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))