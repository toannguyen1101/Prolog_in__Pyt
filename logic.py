
def is_type(line):
    if('.' in line):
        if('-' in line):
            return 2
        return 1
    return 0

def take_rules_laws(rule,fact,fileName):
    file_input=open(fileName,'r')
    line=file_input.readline()
    if(is_type(line)==1):
        fact.append(line[:-1])
    elif(is_type(line)==2):
        rule.append(line[:-1])
    while line!='':
        line=file_input.readline()
        if(is_type(line)==1):
            fact.append(line[:-1])
        elif(is_type(line)==2):
            rule.append(line[:-1])
    file_input.close()    

def take_input():
    question=input("?- " )
    question=question.replace(" ","")
    return question


def main():
    fact=[]
    rule=[]
    fileName='test.txt'
    take_rules_laws(rule,fact,fileName)
    question=take_input()
    
def _arg(ques):
    first_bracket=ques.find('(')
    second_bracket=ques.find(')')
    arg=ques[first_bracket+1:second_bracket]
    return arg

def _fuctor(ques):
    first_bracket=ques.find('(')
    fuctor=ques[:first_bracket]
    return fuctor


def Answer_fact(fact,question):
    check=0
    ques_fuctor=_fuctor(question)
    ques_arg=_arg(question)
    for i in range(0,len(fact)):
        if ques_fuctor==_fuctor(fact[i]):
            if ques_arg==_arg(fact[i]):
                check=1
                print("TRUE")
                break
    if(check==0):
        print("FALSE")
fact=[]
rule=[]
fileName='test.txt'

take_rules_laws(rule,fact,fileName)

question=take_input()
Answer_fact(fact,question)





#arg=all_arg.split(',')
#print(arg)
#fuctor=question[:first_bracket]
#print(fuctor)



    
  
