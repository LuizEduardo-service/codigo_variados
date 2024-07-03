lista_consulta = []

consulta = {
    "janela": "qqqefwefw",
    "status": "pendente",
}

consulta2 = {
    "janela": "esfwewe",
    "status": "pendente",
}
lista_consulta.append(consulta)
lista_consulta.append(consulta2)


for idx, janela in enumerate(lista_consulta):
    print(f"iniciando janela: {janela}")
    print("incluindo data inicio")
    print("incluindo data fim")
    print("excutando processo")
    janela['status'] = "finalizado"

    if idx == 1:
        janela['status'] = "erro"
        


print(lista_consulta)