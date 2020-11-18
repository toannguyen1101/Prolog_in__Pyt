male(william).
male(james).
male(harper).
male(jackson).
male(jack).
male(madison).
male(ronaldo).
male(messi).
male(lincoln).
male(grayson).
male(trump).
male(biden).

female(mason).
female(ella).
female(avery).
female(eleanor).
female(carter).
female(lily).
female(lucy).

principal(william).
viceprincipal(james).

mathhead(harper).
mathteacher(jackson).
mathteacher(avery).

literaturehead(mason).
literatureteacher(jack).
literatureteacher(madison).

englishhead(ella).
englishteacher(eleanor).
englishteacher(carter).

class(a).
class(b).
class(c).

student(ronaldo).
student(messi).
student(grayson).
student(lily).
student(lincoln).
student(trump).
student(biden).
student(lucy).

schoolleader(Person):-principal(Person);viceprincipal(Person).
divisionhead(Person):-mathhead(Person);literaturehead(Person);englishhead(Person).
teacher(Person):-mathteacher(Person);literatureteacher(Person);englishteacher(Person).
boss(Higher,Lower):-schoolleader(Higher),teacher(Lower).
boss(Higher,Lower):-schoolleader(Higher),divisionhead(Lower).
boss(Higher,Lower):-mathhead(Higher),mathteacher(Lower).
boss(Higher,Lower):-literaturehead(Higher),literatureteacher(Lower).
boss(Higher,Lower):-englishhead(Higher),englishteacher(Lower).

teachin(jackson,a).
teachin(jack,a).
teachin(eleanor,a).
teachin(avery,b).
teachin(madison,b).
teachin(eleanor,b).
teachin(avery,c).
teachin(madison,c).
teachin(carter,c).

teachclass(Teacher,Class):-teachin(Teacher,Class).

classteacher(a,jackson).
classteacher(a,jack).
classteacher(a,eleanor).
classteacher(b,avery).
classteacher(b,madison).
classteacher(b,eleanor).
classteacher(c,avery).
classteacher(c,madison).
classteacher(c,carter).

studentinclass(ronaldo,a).
studentinclass(grayson,a).
studentinclass(messi,a).
studentinclass(lincoln,b).
studentinclass(lily,b).
studentinclass(trump,c).
studentinclass(biden,c).
studentinclass(lucy,c).

classhavestudent(a,ronaldo).
classhavestudent(a,grayson).
classhavestudent(a,messi).
classhavestudent(b,lincoln).
classhavestudent(b,lily).
classhavestudent(c,trump).
classhavestudent(c,biden).
classhavestudent(c,lucy).

classmate(Student1,Student2,Nameclass):-studentinclass(Student1,Nameclass),studentinclass(Student2,Nameclass).
schoolmate(Student1,Student2):-student(Student1),student(Student2).









