from  random import choice

while True:

 q = input("")

 l = ["Камінь", "ножиці", "папір"]
 x = choice(l)

 print(f"Ти вибрав {q}, бот вибрав {x}")


 if q == x:
     print("Нічия!")
 elif q == "Камінь" and x == "ножиці":
     print("Ти виграв!")
 elif q == "ножиці" and x == "папір":
     print("Ти виграв!")
 elif q == "папір" and x == "Камінь":
     print("Ти виграв!")
 else:
     print("Ти програв!")