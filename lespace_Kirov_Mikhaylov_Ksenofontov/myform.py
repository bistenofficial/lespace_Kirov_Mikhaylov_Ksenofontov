from bottle import post, request 

import re
import pdb
@post('/home', method='post')

def my_form():
    mail = request.forms.get('ADRESS')
    Question = request.forms.get('QUEST')
    Hystory = {}
    pattern=r"^\w+[@][a-z]{2,6}(\.[a-z]{2,4}){1,2}$"
    number_re=re.compile(pattern)
    Hystory[mail] = Question
    pdb.set_trace()
    if number_re.findall(mail) and Question:
        return "Thanks! The answer will be sent to the mail %s" % mail
    else:
        return "Error, make suer the mail is entered correctly and that all fields are filled"

    