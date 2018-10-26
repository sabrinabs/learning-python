# coding:utf-8

x = float(raw_input("x: "))
y = float(raw_input("y: "))


if x == 0 and y == 0 :
	print("Você está na origem, caro pesquisador")

elif x > 0 and y > 0 :
     print("Quadrante 1, onde o valor de x e y são positivos")

elif x < 0 and y < 0 :
	print("Quadrante 3, onde x e y são negativos")

elif x < 0 and y > 0 :
	print("Quadrante 2, onde x é negativo e y é positivo")

elif x > 0 and y < 0 :
	print("Quadrante 4, onde x é positivo e y é negativo")

elif x != 0 and y == 0 :
	print("eixo X")

elif x == 0 and y != 0 :
	print("eixo y")
