import re
def convert_to_link(sentence):
    regex = "(#[a-zA-Z0-9_]+)"
    remplacement = r'<a href="">\1</a>'
    result = re.sub(regex, remplacement, sentence)

    return result
the_sentence = "Car je connais les #projets que j'ai formés sur vous,dit l'#Eternel,\n projets de #paix et non de malheur.\n"             
print(the_sentence)
print(convert_to_link("Car je connais les #projets que j'ai formés sur vous,dit l'#Eternel,\n projets de #paix et non de malheur.\n"))


