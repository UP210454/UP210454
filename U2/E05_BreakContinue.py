n=5
for i in range(1,11):
    if i==6:
        continue
    else:
        print(i)
    print(f"Numero {i}")

for j in range (1,11):
    if j==6:
        break
    else:
        print(j)
        print(f'Numero {j}')