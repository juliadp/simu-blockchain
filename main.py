# main.py
import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.config.config import GAS, VALOR_TOKEN_MEDIA, VALOR_TOKEN_SD, N_EVENTOS, P_BURN, P_UPDATE

def generar_TS():
    return np.random.exponential(scale=5)

def generar_LLIN():
    return np.random.lognormal(mean=2.5, sigma=0.5)

def generar_saldo_comprador():
    return np.random.randint(500, 5000)

def generar_valor_token():
    return max(10, int(np.random.normal(VALOR_TOKEN_MEDIA, VALOR_TOKEN_SD)))

def simular():
    partes_de_prop = 1000
    tokens_vend = []
    saldo_vend = 5000
    eventos = []
    tiempo = 0.0
    CTS = 0
    CTF = 0
    tokens_emitidos = 0
    tokens_burneados = 0
    saldos_compradores = []

    for i in range(N_EVENTOS):
        r = random.random()
        if r < 0.35:
            # TTS -> TM
            TS = generar_TS()
            tiempo += TS
            if partes_de_prop > len(tokens_vend) and saldo_vend >= GAS:
                CTS += 1
                saldo_vend -= GAS
                token_id = f"T{tokens_emitidos}"
                tokens_vend.append({"id": token_id, "precio": generar_valor_token()})
                tokens_emitidos += 1
                eventos.append([tiempo, "mint", token_id, saldo_vend, None])
        elif r < 0.7:
            # TLLI -> TCI
            LLIN = generar_LLIN()
            tiempo += LLIN
            kyc_interesado = random.choice([True, False])
            if kyc_interesado:
                saldo_comprador = generar_saldo_comprador()
                if len(tokens_vend) > 0:
                    token = random.choice(tokens_vend)
                    precio = token["precio"]
                    if saldo_comprador >= precio:
                        saldo_comprador -= precio
                        saldo_vend += precio
                        tokens_vend.remove(token)
                        saldos_compradores.append(saldo_comprador)
                        eventos.append([tiempo, "compra_exitosa", token["id"], saldo_vend, saldo_comprador])
                    else:
                        CTF += 1
                        eventos.append([tiempo, "compra_fallida_fondos", token["id"], saldo_vend, saldo_comprador])
                else:
                    CTF += 1
                    eventos.append([tiempo, "compra_fallida_sin_tokens", None, saldo_vend, None])
        else:
            # eventos secundarios
            tiempo += np.random.exponential(scale=3)
            if len(tokens_vend) > 0:
                token = random.choice(tokens_vend)
                if random.random() < P_BURN:
                    tokens_vend.remove(token)
                    tokens_burneados += 1
                    eventos.append([tiempo, "burn_token", token["id"], saldo_vend, None])
                elif random.random() < P_UPDATE:
                    nuevo_precio = generar_valor_token()
                    token["precio"] = nuevo_precio
                    eventos.append([tiempo, "actualizacion_precio", token["id"], saldo_vend, nuevo_precio])

    df_eventos = pd.DataFrame(eventos, columns=["tiempo","evento","token","saldo_vendedor","extra"])
    os.makedirs("dataset", exist_ok=True)
    os.makedirs("resultados", exist_ok=True)
    df_eventos.to_csv("dataset/blockchain_tokens.csv", index=False)

    CTS_final = CTS
    PTB_final = tokens_burneados / tokens_emitidos if tokens_emitidos > 0 else 0
    PSC_final = float(np.mean(saldos_compradores)) if len(saldos_compradores)>0 else 0
    CTF_final = CTF

    resultados = {
        "CTS":CTS_final, "PTB":PTB_final, "PSC":PSC_final, "CTF":CTF_final
    }
    pd.DataFrame([resultados]).to_csv("resultados/resultados_simulacion.csv", index=False)

    plt.figure(figsize=(10,5))
    sns.histplot(df_eventos['tiempo'], bins=50, kde=True)
    plt.title("Distribución de tiempos de eventos")
    plt.savefig("resultados/tiempos_eventos.png")
    plt.close()

    plt.figure(figsize=(8,6))
    sns.barplot(x=list(resultados.keys()), y=list(resultados.values()))
    plt.title("Resultados finales")
    plt.savefig("resultados/resultados_bar.png")
    plt.close()

    print("Simulación finalizada. Resultados guardados en carpeta resultados/")

if __name__ == "__main__":
    simular()
