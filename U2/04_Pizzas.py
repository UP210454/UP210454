pizza=str(input("Quieres pizza vegetariana o no vegetariana? "))
if pizza=='vegetariana' or pizza=='Vegetariana':
    ingrediente=str(input("Ingredientes de la pizza vegetariana:\n*Pimiento\n*Tofu\n"))
    print(f'Elegiste una pizza {pizza} con mozzarella, tomate y {ingrediente}.')
elif pizza=='No vegetariana' or pizza=='no vegetariana':
    ingrediente=str(input("Ingredientes de la pizza no vegetariana:\n*Peperoni\n*Jamón\n*Salmón\n"))
    print(f'Elegiste una pizza {pizza} con mozzarella, tomate y {ingrediente}.')
else:
    print("Error al escoger")
