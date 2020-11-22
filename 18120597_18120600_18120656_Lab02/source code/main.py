import logic as lg

fact=[]
rule=[]
fileName=input("Nhap ten file: ")

#Lay thong tin tu file
lg.take_rules_laws(rule,fact,fileName)
#Nhap thong tin
question=lg.take_input()

while(question!="exit"):
  
    ques_arg=lg._arg(question)
    status=0
    #Kiem tra cau hoi co bien hay khong
    for i in range(0,len(ques_arg)):
        if(lg.is_var(ques_arg[i])):
            status=1
            x=ques_arg[i]
            idx=i
    if(status==0):
        print(str(lg.answer_question(rule,fact,question)))
    else:
        lg.print_var_result(question,rule,fact,x,idx)
        
    question=lg.take_input()

print("\n..........EXIT..........")
