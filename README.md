# Simulación de Blockchain en Real Estate – BlockEstateSim

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/juliadp/simu-blockchain/blob/main/TP%20Final%20Simulacion.ipynb)

**⏱ Unidad de tiempo de la simulación: _horas_**

---

## 📚 Descripción del Proyecto
Este proyecto simula el proceso de **tokenización de una propiedad** sobre blockchain y la interacción con potenciales compradores. Se modelan eventos de:
- **Emisión de tokens** (`mint`)
- **Quema de tokens** (`burn_token`)
- **Compras exitosas** (`compra_exitosa`)
- **Compras fallidas** por **falta de fondos** o **sin disponibilidad**
- **Actualización de precio** (`actualizacion_precio`)

El objetivo es analizar el **ritmo de oferta vs demanda**, la evolución del **supply en circulación**, y métricas de desempeño como **CTS, PTB, PSC y CTF**. Además, se **ajustan FDPs** para los intervalos entre eventos (TS y LLIN) y se realiza una **verificación** re-muestreando desde la mejor distribución ajustada.

---

## 📑 Índice
- [Simulación de Blockchain en Real Estate – BlockEstateSim](#simulación-de-blockchain-en-real-estate--blockestatesim)
  - [📚 Descripción del Proyecto](#-descripción-del-proyecto)
  - [📑 Índice](#-índice)
  - [📂 Estructura del Proyecto](#-estructura-del-proyecto)
  - [🧩 Configuración y Requisitos](#-configuración-y-requisitos)
  - [🚀 Ejecución Rápida](#-ejecución-rápida)
  - [FDPs desde el dataset (TS/LLIN)](#fdps-desde-el-dataset-tsllin)
  - [🔁 Flujo de la Simulación](#-flujo-de-la-simulación)
  - [📊 Métricas Principales](#-métricas-principales)
  - [🧾 Salidas y Resultados](#-salidas-y-resultados)
  - [🎯 Notas de Reproducibilidad](#-notas-de-reproducibilidad)
  - [🛠 Guía rápida / Runbook](#-guía-rápida--runbook)

---

## 📂 Estructura del Proyecto
```
simu-blockchain/
├── TP Final Simulacion.ipynb        # Notebook principal (Colab/Jupyter)
├── README.md                        # Este archivo
├── requirements.txt                 # Dependencias mínimas para ejecución local
├── docs/                            # Documentación adicional (opcional)
│
├── outputs/                         # Resultados generados automáticamente
│   ├── metricas_all.csv             # CTS, PTB_% (porcentaje), PSC, CTF
│   ├── conteo_eventos.csv           # Frecuencia por tipo de evento
│   ├── tokens_circulacion.csv       # Serie (tiempo, tokens_en_circulacion)
│   ├── tokens_circulacion.png       # Curva del supply acumulado
│   ├── resumen_tiempo.csv           # t_min, t_max, duración, n_registros, tokens_final
│   ├── metricas_bar.png             # Barras con métricas finales
│   ├── saldo_vendedor_tiempo.png    # Evolución del saldo del vendedor
│   ├── dist_saldos_compradores.png  # Histograma de saldos post-compra (si aplica)
│   ├── ajustes_fdp_dataset.csv      # Ajustes FDP estimados directamente del dataset (en horas)
│   ├── ajustes_fdp_dataset.json     # Igual que CSV, en formato JSON
|   ├── fdp_ts_top5_overlay.png      # Overlays TS
|   ├── fdp_llin_top5_overlay.png    # Overlays LLIN
│   └── conclusiones.md              # Conclusiones automáticas de la corrida
│
└── .gitignore                       # Ignora cachés, checkpoints y temporales
```

---

## 🧩 Configuración y Requisitos
- **Python 3.9+** (para local) o **Google Colab** (recomendado).
- Paquetes clave: `numpy<2`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `fitter`.

> En Colab, el notebook incluye un **bloque de setup estable** (fija `numpy==1.26.4` para compatibilidad con `fitter==1.7.1` y evita conflictos con paquetes que fuerzan `numpy>=2`).

Para entorno local:
```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución Rápida
- **En Colab:** clic en el badge “Open in Colab” y luego **Runtime → Run all**.  
- **Local (Jupyter):**
  1) `pip install -r requirements.txt`  
  2) Abrir `TP Final Simulacion.ipynb`  
  3) Ejecutar todas las celdas  

Los resultados se guardan en `outputs/`.

---

## FDPs desde el dataset (TS/LLIN)
Se estiman **FDPs** para:
- **TS** (Δ entre `mint`) usando `mint_delay_min / 60` → horas
- **LLIN** (Δ entre llegadas de interesados) usando `potential_buyer_arrival_delay_time` → horas

**Toolkit:** [`fitter`](https://github.com/cokelaer/fitter) probando **todas** las distribuciones y eligiendo por **SSE**.  
**Salidas:** `outputs/ajustes_fdp_dataset.csv` y `.json`.  
**Integración:** si hay ajuste, se definen **`gen_TS_dataset`** y **`gen_LLIN_dataset`** (horas) y la simulación los usa automáticamente; si no, cae a **Exponencial** con medias del escenario.  
**Opcional:** overlays Top-N PDFs (controlado por `TOP_N_FDPS`).

---

## 🔁 Flujo de la Simulación
- **Tiempo base:** **horas**.
- **TS:** Exponencial(media = `mint_delay_min/60`) o mejor FDP del dataset.
- **LLIN:** Exponencial(media = `potential_buyer_arrival_delay_time`) o mejor FDP del dataset.
- **Secundarios:** Exponencial(media = `time_to_price_update_days * 24`).
- **Estados:** supply, `gas`, KYC, budgets/precios ~ normales con ruido, burns y price updates.

---

## 📊 Métricas Principales
- **CTS** — # tokenizaciones solicitadas (`mint`)
- **PTB_%** — % quemados / emitidos
- **PSC** — saldo promedio post-compra del comprador
- **CTF** — # transferencias fallidas (fondos/stock) 

---

## 🧾 Salidas y Resultados
- **Ajustes FDP (dataset):** `ajustes_fdp_dataset.csv/json` (+ overlays si `TOP_N_FDPS>0`)
- **Métricas por escenario (batch):** `metricas_all.csv`
- **Eventos (opcional, batch):** `eventos_all_sXXX.csv(.gz)` con columna `scenario`
- **Escenario de referencia (EDA/plots):** `metricas.csv`, `conteo_eventos.csv`, `tokens_circulacion.*`, `*_tiempo.png`, `dist_saldos_compradores.png`
- **Conclusiones automáticas:** `conclusiones.md`

---

## 🎯 Notas de Reproducibilidad
- Se fijan semillas (`numpy`, `random`) para resultados consistentes.
- Exportes **idempotentes** (sobre-escritura segura).
- El EDA/plots usa el **primer escenario** del batch para producir gráficos rápidos y representativos sin inflar memoria. 

---

## 🛠 Guía rápida / Runbook
1. Ejecutar **Setup e Ingesta** (bloques 1–2).  
2. (Opcional) Ejecutar **ajuste FDPs** — genera `ajustes_fdp_dataset.*` y define `gen_TS_dataset` / `gen_LLIN_dataset`.  
3. Configurar **Driver**:
   - `RUN_ALL_SCENARIOS = True`
   - Para runs grandes: `SAVE_EVENTS_ALL=False`, `SAVE_METRICAS_ALL=True`
   - Ajustar `N_SCENARIOS`, `BATCH_RANDOM_SAMPLE`, `TOP_N_FDPS`
4. Correr el **Driver (streaming)**. Verás logs de progreso cada 1000 escenarios.
5. Revisar `outputs/metricas_all.csv` (batch) y los gráficos/archivos del escenario de referencia.
6. Ver **conclusiones** en `outputs/conclusiones.md`.

---