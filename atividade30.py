# crie uma funcao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

def calcula_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media
    
def verificar_resultados(media):
    if media >= 7:
        return 'aprovado'
    else:
        return 'reprovado'

nota1 = float(input("digite a nota1: "))
nota2 = float(input("digite a nota2:  "))
nota3 = float(input("digite a nota3:  "))

resultado_media = calcula_media(nota1, nota2, nota3)
print(resultado_media)

resultado_final = verificar_resultados(resultado_media)
print(resultado_final)
    



