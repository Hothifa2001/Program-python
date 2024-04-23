#بعض دوال list في python

list1=['C++', 'C','R','Java','Kotlin','Css']
list2=[1,2,4,8,6,5,9,3,65,2,2,7]

#دالة دمج قائمتين 
list1.extend(list2)
print(list1)
#إضافة متغير او قائمة الى list
list1.append('code')
list2.append([99,45,32,'python'])
print('\n',list1)
print(list2)
#إضافة متغير الى مكان محدد مثلا الموق ٢ ضع فيه html
list1.insert(2,'html')
print(list1)
#حذف متغير من list دون الإحتفاض بهذا المتغير
del list1[0]
print(list1)
#حذف متغير من داخل list
list1.remove('html')
print(list1)
#حذف جميع محتويات list
#list1.clear()
#print(list1)
#أهذ أخر قيمة في list و حذفها و يمكن تخزينها في متغير أخر 
list2.pop() 
x=list2.pop()
print(list2)
print('\n',x)
#البحث عن قيمة داخل list  و طباعة موقع القيمة
print(list1.index('C'))

#عدد القيمة (كم تكررت) داخل list
print(list2.count(2))

#ترتيب عناصر list
list2.sort()
print(list2)
#أخذ نسخة من list2 الى list3 دون التأثير على list الأصلية عند التغيير
list3=list2.copy()
print(list3)

#دالة titleتطبع اول حرف في الكلمة كبير
firstName = "hothifa"
lastName = "ALMOLUKEY"
fullName = f'hey \'{firstName}\' \'{lastName}\''
#حرف f هو دمج بين سلسلتين نصيتين مع متغير داخل أقواس مجعدة، يمكن الإستغناء عنه 
print(fullName)
print(firstName.title())
word2='hothifa '+lastName
print(word2.title())

word='hOtHiFa'
#دالة تطبع النص بحروف كبيرة
print(word.upper())
# دالة تطبع النص بحروف صغيرة
print(word.lower())
# يمكن الفصل بين الأرقام الكبيرة لتحديد خانة المئات و الألاف و الملاين من متغير int أو غيره كما يلي :
number1= 14000000000000000
number2= 14_000_000_000_000_000
print(number1)
print(number2)
