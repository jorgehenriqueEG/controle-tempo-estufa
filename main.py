def processar_estufa(leituras):
    total = 0
    tem_alerta = False
    for hora, temp in leituras:
        total += temp
        if temp > 35.0:
            tem_alerta = True
    media = total / len(leituras)
    return media, tem_alerta

def main():
    dados = [("08:00", 28.5), ("12:00", 36.2), ("16:00", 33.1)]
    media, alerta = processar_estufa(dados)
    status_alerta = "Sim" if alerta else "Não"
    print(f"Media: {media:.1f}C | Alerta: {status_alerta}")

if __name__ == "__main__":
    main()