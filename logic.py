
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
    question=question.strip()
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
    arg=ques[first_bracket+1:second_bracket].split(',')
    for i in range(0,len(arg)):
        arg[i]=arg[i].strip()
    return arg

def _functor(ques):
    first_bracket=ques.find('(')
    fuctor=ques[:first_bracket]
    return fuctor

    
def answer_fact(fact,question):
    ques_functor=_functor(question)
    ques_arg=_arg(question)
    for i in range(0,len(fact)):
        if ques_functor==_functor(fact[i]):
            if ques_arg==_arg(fact[i]):
                return True
    return False
        
def parsed_rule(rule):
     predicats=[]
     all_predicats=rule[rule.find('-')+1:rule.find('.')]
     
     predicats=all_predicats.split('*')
     return predicats


def is_rule(functor,rule):
    for i in range(0,len(rule)):
        if functor == _functor(rule[i]):
            return i
    return -1
def is_fact(functor,fact):
    for i in range(0,len(fact)):
        if functor == _functor(fact[i]):
            return 1
    return 0

def is_var(arg):
    if(arg[0]<='Z' and arg[0]>='A'):
            return True
    return False

def _var_fact(question,fact):
    ques_functor=_functor(question)
    ques_arg=_arg(question)
    not_var_pos=[]
    var_dict={}
    for i in range(0,len(ques_arg)):
        if(is_var(ques_arg[i])==False):
            not_var_pos.append(i)
    if(len(not_var_pos)>=0):
        for i in range(0,len(fact)):
           check=0
           if(ques_functor==_functor(fact[i])):
               fact_arg=_arg(fact[i])
               for j in range(0,len(not_var_pos)) :
                   if(ques_arg[not_var_pos[j]] != fact_arg[not_var_pos[j]]):
                       check=1
                       break
               if(check==0):
                   for j in range(0,len(fact_arg)):
                       if(j not in not_var_pos):
                           if(ques_arg[j] not in var_dict):
                               var_dict[ques_arg[j]]=[fact_arg[j]]
                           else:
                               var_dict[ques_arg[j]].append(fact_arg[j])
    return var_dict

def fill_rule(rule,ques_arg):
    not_var_pos=[]
    rule_header=rule[:rule.find(':')]
    rule_header_arg=_arg(rule_header)
    for i in range(0,len(ques_arg)):
        if(is_var(ques_arg[i])==False):
            not_var_pos.append(i)
    if(len(rule_header_arg)==len(ques_arg)):
        for i in not_var_pos:
            rule=rule.replace(rule_header_arg[i],ques_arg[i])
    return rule
def fill_var(predicats,idx):
    var_dict=_var_fact(predicats[idx], fact) 
    var_pos=[]
    if(len(var_dict)>0):
        pre_arg=_arg(predicats[idx])
        for i in range(0,len(pre_arg)):
            if(is_var(pre_arg[i])==True):
                var_pos.append(i) 
        for i in range(1,len(predicats)): 
            if(i!=idx):
                for j in var_pos:  
                    if(pre_arg[j] in predicats[i]):
                        temp_dict=_var_fact(predicats[i], fact)
                        if(len(temp_dict)>0):
                            for k in temp_dict[pre_arg[j]]:
                                if(k in var_dict[pre_arg[j]]):
                                    predicats[i]=predicats[i].replace(pre_arg[j],k)
                                    predicats[idx]=predicats[idx].replace(pre_arg[j],k)
                                    break
        for i in range(0,len(predicats)):
           var_dict=_var_fact(predicats[i], fact) 
           if(len(var_dict)>0):
              for j in var_dict:
                  for k in var_dict[j]:
                      predicats[i]=predicats[i].replace(j,k)
      
             
def processrule(line,fact,rule):
     result=[]
     rule_pos=is_rule(_functor(line),rule)
     if(rule_pos!=-1):
         rule[rule_pos]=rule[rule_pos].replace('),',')*')
         new_rule=fill_rule(rule[rule_pos],_arg(line))
         predicats=parsed_rule(new_rule) 
         for i in range(0,len(predicats)):
             if(is_fact(_functor(predicats[i]),fact)==False):
                 temp=processrule(predicats[i],fact,rule)
                 for j in range(0,len(temp)):
                     result.append(temp[j])
             else:
                 fill_var(predicats,i)
                 result.append(predicats[i])
             
             #result.append(predicats[i])
     for i in range(0,len(result)):
         fill_var(result,i)
     return result
     
def answer_question(rule,fact,question):
    if(is_fact(_functor(question),fact)):
           return answer_fact(fact,question)
    else:
        result=processrule(question,fact,rule)
        
    for i in range(0,len(result)):
        if(answer_fact(fact,result[i])==False):
            return False
    return True
fact=[]
rule=[]
fileName='test.txt'

take_rules_laws(rule,fact,fileName)
#question=take_input()
question="nephew('Prince George','Prince Harry')."
#question="sibling(Parent,'Prince Harry')."
#new_rule=fill_rule(rule_t, question)

temp=["parent(Parent,Per1)", "parent(Parent,'Prince Harry')"]
#print(temp)
#fill_var(temp,0)
#fill_var(temp,0)
print(processrule(question,fact,rule))
#print(temp)
#print(temp)
#test=_var_fact('parent(Parent,prince_harry)',fact)
print(str(answer_question(rule,fact,question)))
#answer_question(rule,fact,question)






    
  
