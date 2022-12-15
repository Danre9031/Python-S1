#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = None
y = None
z = None

for i in range(0,2):
    for j in range(0,2):
        for g in range(0,2):
            if (not(i and j and g))==(not i or not j or not g):
                x=i
                y=j
                z=g
                print(f'{x},{y},{z}->истина')
            else:
                print(f'{x},{y},{z}->лож')