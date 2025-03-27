# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    final_string = []
    for char in text:
        final_string.append(char * 3)
    return ''.join(final_string)

print(paper_doll('Hello'))