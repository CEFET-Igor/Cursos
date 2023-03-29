"""
Faça um programa que leia a largura e a
altura de uma parede em metros, calcule a sua
área e a quantidade de tinta necessária para
pintá-la, sabendo que cada litro de tinta pinta
uma área de 2 metros quadrados.
"""
altura = float(input("Qual a altura da parede (m)? "))
largura = float(input("Qual a largura da parede (m)?"))
print(f"""
Você tem um comodo de {altura*largura} (m²)
considerando uma tinta que a cada litro pinte 2m²
você ira precisar de {(altura*largura)/2} litros de tinta.
""")