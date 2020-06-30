import random
small="abcdefghijklmnopqrstuvwxyz"
caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
char="!@#$%^&*(){}[]?,><:;/'"
all=small+caps+num+char
final="".join(random.choice(all) for i in range(0,17))
print(final)
