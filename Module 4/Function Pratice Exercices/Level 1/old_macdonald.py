# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    if len(name) >= 4:
        uppercase1 = name[0].upper()
        uppercase2 = name[3].upper()
        return uppercase1 + name[1:3] + uppercase2 + name[4:]
    else:
        return "Name lenght not big enough"

print(old_macdonald('macdonald'))
print(old_macdonald('mac'))