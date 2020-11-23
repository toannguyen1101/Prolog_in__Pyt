
#Ham tra ve kieu luat hay su kien
def is_type(line):
    if('.' in line):
        if('-' in line):
            return 2
        return 1
    return 0

#Lay thong tin tu file
def take_rules_laws(rule,fact,fileName):
    file_input=open(fileName,'r')
    print("Mo file thanh cong !!!!")
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
    
    #Kiem tra luat cuoi, cuoi cau co dau cham hay khong
    last_rule=rule[len(rule)-1]
    if(last_rule[len(last_rule)-1]!="."):
        rule[len(rule)-1]=rule[len(rule)-1]+"."
    
    deleted=[]
    #Tach cac truong hop hoac
    #Vi du: A:-B;C. Tach thanh 2 luat khac nhau A:-B va A:-C
    #Sinh ra luat trung ten, xoa luat cu
    temp=[]
    for i in range(0,len(rule)):
        if(";"in rule[i]):
            deleted.append(i)
            rule_header=rule[i][:rule[i].find(":-")]
            rule_functors=rule[i][rule[i].find(":-")+2:len(rule[i])-1]
            functors=rule_functors.split(";")
            for j in functors:
                new_rule=rule_header+":-"+j+"."
                temp.append(new_rule)
        else:
            temp.append(rule[i])
            
    rule.clear()
    rule.extend(temp)
    
#Nhap cau hoi
def take_input():
    question=input("?- " )
    question=question.strip()
    return question

#Lay cac doi so 
def _arg(ques):
    first_bracket=ques.find('(')
    second_bracket=ques.find(')')
    arg=ques[first_bracket+1:second_bracket].split(',')
    for i in range(0,len(arg)):
        arg[i]=arg[i].strip()
    return arg

#Lay ten cua cai ham tu
def _functor(ques):
    first_bracket=ques.find('(')
    fuctor=ques[:first_bracket]
    return fuctor

#Tra loi neu cau hoi la su kien  
def answer_fact(fact,question):
    ques_functor=_functor(question)
    ques_arg=_arg(question)
    for i in range(0,len(fact)):
        if ques_functor==_functor(fact[i]):
            if ques_arg==_arg(fact[i]):
                return True
    return False

#Tach luat thanh cac vi tu con
def parsed_rule(rule):
     predicats=[]
     all_predicats=rule[rule.find('-')+1:rule.find('.')]
     
     predicats=all_predicats.split('*')
     return predicats

#Kiem tra xem co phai la luat 
def is_rule(functor,rule):
    pos_rule=[]
    for i in range(0,len(rule)):
        if functor == _functor(rule[i]):
            pos_rule.append(i)
    return pos_rule

#Kiem tra xem co phai la su kien
def is_fact(functor,fact):
    for i in range(0,len(fact)):
        if functor == _functor(fact[i]):
            return i
    return -1

#Kiem tra doi so co phai la bien khong
def is_var(arg):
    if(arg[0]<='Z' and arg[0]>='A'):
            return True
    return False

#Tim ra tap bien va gia tri cua bien
def _var_fact(question,fact):
    ques_functor=_functor(question)
    ques_arg=_arg(question)
    not_var_pos=[]
    var_dict={}
    #Kiem tra doi so nao la bien
    for i in range(0,len(ques_arg)):
        if(is_var(ques_arg[i])==False):
            not_var_pos.append(i)
            
    
    if(len(not_var_pos)>=0):
        #Xet trong tap su kien cai gia tri cua bien
        for i in range(0,len(fact)):
           check=0
           #Kiem tra ham tu trung voi ham tu nao trong tap su kien
           if(ques_functor==_functor(fact[i])):
               fact_arg=_arg(fact[i])
               for j in range(0,len(not_var_pos)) :
                   #Kiem tra thu tu cac gia tri khong phai bien co trung voi gia tri cua 1 su kien
                   if(ques_arg[not_var_pos[j]] != fact_arg[not_var_pos[j]]):
                       check=1
                       break
               #Tien hanh them hoac tao moi cho tap gia tri cua bien
               if(check==0):
                   for j in range(0,len(fact_arg)):
                       if(j not in not_var_pos):
                           if(ques_arg[j] not in var_dict):
                               var_dict[ques_arg[j]]=[fact_arg[j]]
                           else:
                               var_dict[ques_arg[j]].append(fact_arg[j])
    return var_dict

#Dien doi so cua cau hoi vao luat
def fill_rule(rule,ques_arg):
    #Tach luat thanh 2 phan: Phan luat va phan ham tu tao nen luat
    rule_header=rule[:rule.find(':')]
    rule_header_arg=_arg(rule_header)
    
    
    if(len(rule_header_arg)==len(ques_arg)):
        for i in range(0,len(ques_arg)):
            #Neu doi so cua cau hoi la bien, doi so do nam trong phan luat va khong nam trong phan ham tu tao nen luat
            #Tien hanh doi ten bien trong luat, de tranh trung lap khi xet
            if(is_var(ques_arg[i])):
               if(ques_arg[i] not in rule_header_arg):
                   if(ques_arg[i] in rule):
                       rule=rule.replace(ques_arg[i],ques_arg[i]+ques_arg[i])
                     
            #Doi cac doi so trong luat bang cac doi so trong cau hoi            
            rule=rule.replace(rule_header_arg[i],ques_arg[i])
    return rule

#Tim gia tri chung cua cac bien va dien vao cac ham tu con
def fill_var(predicats,idx,fact,ques_arg):
    var_dict=_var_fact(predicats[idx], fact) 
    var_pos=[]
    if(len(var_dict)>0):
        pre_arg=_arg(predicats[idx])
        for i in range(0,len(pre_arg)):
            if(is_var(pre_arg[i])==True):
                var_pos.append(i) 
        #Kiem tra va dien cac gia tri cua bien vao cai ham tu khac
        for i in range(0,len(predicats)): 
            if(i!=idx):
                for j in var_pos: 
                    temp_dict=_var_fact(predicats[i], fact)
                    #Kiem tra bien do co nam trong ham tu con i 
                    if(pre_arg[j] in temp_dict):          
                        if(len(temp_dict)>0):
                            for k in temp_dict[pre_arg[j]]:
                                #Kiem tra gia tri co nam trong tap gia tri cua ham tu i
                                #Gia tri khong thuoc tap gia tri cua cau hoi
                                if(k in var_dict[pre_arg[j]] and k not in ques_arg):
                                    predicats[i]=predicats[i].replace(pre_arg[j],k)
                                    predicats[idx]=predicats[idx].replace(pre_arg[j],k)
                                    break
                        
#Xu li cac luat   
def processrule(line,fact,rule,rule_pos):
     result={}
     ques_arg=_arg(line)
     
     #Tim vi tri cua luat va tien hanh xu ly
     if(rule_pos!=-1):
         temp=rule[rule_pos]
         temp=temp.replace('),',')*')
         new_rule=fill_rule(temp,_arg(line))
         predicats=parsed_rule(new_rule) 
         #Xu li cac ham tu con
         for i in range(0,len(predicats)):
             #Xu li luat
             #Tap vi tri cac luat co cung ten
             pos=is_rule(_functor(predicats[i]),rule)
            
             if(len(pos)!=0):
                 temp_rest={}
                 #Xu li cac luat cung ten
                 #Tach tung truong hop, xuat ra cac ham tu khac nhau
                 for j in pos:
                     temp=processrule(predicats[i],fact,rule,j)
                     for k in temp:
                         temp_rest[k]=temp[k]
                         
                 list_name=list(result.keys())
                 len_res=len(result)
                 
                 #Them ham tu khac nhau vao tap ket qua
                 #Neu tap ket qua co chua ham tu thi them ham tu moi vao, doi ten key cua dict
                 #Neu khong thi tao key moi
                 for j in temp_rest:
                     if(len_res!=0):
                         for k in list_name:
                             temp=[]
                             temp.extend(result[k])
                             temp.extend(temp_rest[j])
                             key_name= k+"."+j
                             result[key_name]=temp
                     else:
                         key_name= str(rule_pos)+"."+j
                         result[key_name]=temp_rest[j]
                 #Xoa key cu trong tap ket qua     
                 for j in list_name:
                     result.pop(j)
                  
             elif(is_fact(_functor(predicats[i]),fact)!=-1):
                 #Xu li su kien
                 if(len(result)>0):
                     for j in result:
                       result[j].append(predicats[i])  
                 else:
                     if(str(rule_pos) not in result):
                         result[str(rule_pos)]=[predicats[i]]
                     else:
                         result[str(rule_pos)].append(predicats[i])
        
     #Bo sung cac gia tri cho cac bien con thieu
     for i in result:
         for j in range(0,len(result[i])):
             fill_var(result[i],j,fact,ques_arg)
     return result

#Tra loi mot menh de nhieu ham tu 
def valueof(clauses,fact):
    for i in clauses:
        if(answer_fact(fact,i)==False):
            return False
    return True    

#Tra loi cau hoi
def answer_question(rule,fact,question):
    #Tra loi neu la su kien
    if(is_fact(_functor(question),fact)!=-1):
           return answer_fact(fact,question)
    #Tra loi neu la luat
    elif(len(is_rule(_functor(question),rule))!=0):
        #Lay tap vi tri cac luat trung ten
        rule_pos=is_rule(_functor(question),rule)
        for i in rule_pos:
            result=processrule(question,fact,rule,i)
            #Tra loi luat
            for j in result:
                clauses=result[j]
                if(valueof(clauses,fact)):
                    return True
        return False
    #Tra loi neu xay ra loi
    else:     
         return "ERROR!!!"

#Ham thay the bien bang mot gia tri cua doi so
def replace_var(question,x,line,idx):
    ques_arg=_arg(question)
    ques_functor=_functor(question)
    result=ques_functor+"("
    for i in range(0,len(ques_arg)):
        if(i==idx):
            result=result+line
        else:
            result=result+ques_arg[i]
        if(i==len(ques_arg)-1):
            result=result+")."
        else:
             result=result+","
    return result

#Ham in ra tap cac bien ung voi ham tu
def print_var_result(question,rule,fact,x,idx):
    result=[]
    visited=[]
    ques_arg=_arg(question)
    #Them cac doi so co gia tri vao tap da xet
    for i in ques_arg:
        visited.append(i)
    #Kiem tra cac doi so trong tap fact
    for i in range(0,len(fact)):
        fact_args=_arg(fact[i])
        for j in fact_args:
            if(j not in visited):
                visited.append(j)
                temp=question
                temp=replace_var(temp, x, j, idx)
                #Kiem tra xem voi gia tri nao do neu cau hoi dung thi la gia tri cua bien
                if(answer_question(rule,fact,temp)):
                    result.append(j)
    #In tap bien
    if(len(result)>0):
        for i in result:
            print(x," = ",i)
    else:
        print(x," = NONE",)
    
