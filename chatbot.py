#Chatbot de bienvenida al curso de simulación matemática 2018
from time import sleep
def print_words(sentence):
    for word in sentence.split():
        for l in word:
            sleep(.05)
            print(l, end = '')
        print(end = ' ')
prompt= "escribe aqui >>  "
sentence0= "POR FAVOR LAS RESPUESTAS QUE INTRUDUZCAS QUE SEAN EN MINÚSCULAS"
print_words(sentence0)
sentence1= "Que rollo como andas, este es el curso de simulación matemática si te equivocaste de curso estas a tiempo de salirte "
print_words(sentence1)
sentence2= "Veo que si te quedaste, al parecer estas en el curso correcto espero que cumpla tus espectativas amig@"
print_words(sentence2)
sentence3="Mi nombre es Migo y estaré contigo a lo largo de este curso, ¿Qué te parece si nos conocemos aún más?"
print_words(sentence3)
sentence4="¿Es la primera vez que cursas esta materia?"
print_words(sentence4)
answer1=input(prompt)
if answer1 == "si":
    print_words("!Excelente novat@ te va a gustar¡")
elif answer1 == "no":
    print_words("No pasa nada carnal esta es la buena")
sentence5="Disculpa mis modales, se me olvidó preguntarte tu nombre, así que tu eres???"
print_words(sentence5)
answer_name=input(prompt)
sentence6="Me agrada el nombre de "+ answer_name+ " de casualidad sabes su significado"
print_words(sentence6)
answer3=input(prompt)
if answer3 == "si":
    print_words("¿Cuál es?")
    answer_sig=input(prompt)
    print_words("así que tu nombre significa "+ answer_sig+" interesante no tenía ni idea")
elif answer3 == "no":
    print_words("Dame hoy para investigar y mañana te digo que rollo con tu nombre")
sentence7= "Adivino estudias una ingeniería, ¿si o no? desmienteme si me equivoco "+answer_name
print_words(sentence7)
answer4=input(prompt)
if answer4 == "si":
    print_words("jaja lo sabia herman@, ¿Ingenieria en que?")
    prompt2= "Ingeniería..."
    answer_ing=input(prompt2)
    print_words("Buena elección de carrera, siempre me interesó la carrera de ingenieria "+ answer_ing+", lastima que yo no pueda estudiar")

elif answer4 == "no":
    print_words("Entonces ¿Qué estudias?")
    answer_c=input(prompt)
    print_words("para ser honesto prefiero las ingenierías, pero "+answer_c+" no es una mala elección escogiste una que casi le llega a las ingenierías")
sentence8="Bueno con esa información me basta, ¿Quieres que sigamos charlando?"
print_words(sentence8)
answer_charla=input(prompt)
if answer_charla == "si" :
    print_words("Sobre que quieres charlar")
    answerc=input(prompt)
    print_words("Ese tema me parece demasiado aburrido perdón, me tengo que ir si al rato tienes otro tema de conversación en mente me hablas")

elif answer_charla== "no":
    print_words("Sale espero que te guste el curso y nos vemos a la proxima ¡Echale ganas!")
