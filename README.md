# Simulación de Blockchain en Real Estate – BlockEstateSim

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/juliadp/simu-blockchain/blob/main/TP%20Final%20Simulacion.ipynb)

**⏱ Unidad de tiempo de la simulación: _días_**

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
  - [🔁 Flujo de la Simulación](#-flujo-de-la-simulación)
  - [📊 Métricas Principales](#-métricas-principales)
  - [🧾 Salidas y Resultados](#-salidas-y-resultados)
  - [📐 Ajuste de FDPs y Verificación](#-ajuste-de-fdps-y-verificación)
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
│   ├── metricas.csv                 # CTS, PTB_% (porcentaje), PSC, CTF
│   ├── conteo_eventos.csv           # Frecuencia por tipo de evento
│   ├── tokens_circulacion.csv       # Serie (tiempo, tokens_en_circulacion)
│   ├── tokens_circulacion.png       # Curva del supply acumulado
│   ├── resumen_tiempo.csv           # t_min, t_max, duración, n_registros, tokens_final
│   ├── ajuste_ts.png                # Resumen gráfico ajuste FDP para TS
│   ├── ajuste_llin.png              # Resumen gráfico ajuste FDP para LLIN
│   ├── metricas_bar.png             # Barras con métricas finales
│   ├── saldo_vendedor_tiempo.png    # Evolución del saldo del vendedor
│   ├── dist_saldos_compradores.png  # Histograma de saldos post-compra (si aplica)
│   ├── ajustes_fdp.csv              # (opcional) Resumen de ajustes FDP (si se exporta)
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

## 🔁 Flujo de la Simulación
- **Unidad de tiempo:** **días**  
- **TS (intervalo entre tokenizaciones):** `Exponencial` con media ≈ **5 días**  
- **LLIN (intervalo entre llegadas de interesados):** `Lognormal` (μ=2.5, σ=0.5) → media ≈ **13.8 días**, mediana ≈ **12.2 días**  
- **Eventos secundarios:** gaps `Exponencial` con media ≈ **3 días**  
- **Estados/Costos:** gasto de gas, saldo del vendedor, precios aleatorios de tokens, KYC del comprador, etc.

---

## 📊 Métricas Principales
- **CTS** — Cantidad total de tokenizaciones solicitadas (mints).  
- **PTB_%** — Porcentaje de tokens quemados sobre emitidos.  
- **PSC** — Promedio del saldo de compradores **post-compra**.  
- **CTF** — Cantidad de transferencias fallidas (por fondos o sin tokens).  

Estas métricas quedan en `outputs/metricas.csv` y se visualizan en `outputs/metricas_bar.png`.

---

## 🧾 Salidas y Resultados
- **Conteo de eventos:** `outputs/conteo_eventos.csv`  
- **Supply en el tiempo:**  
  - Serie `outputs/tokens_circulacion.csv`  
  - Gráfico `outputs/tokens_circulacion.png`  
- **Resumen de tiempo simulado:** `outputs/resumen_tiempo.csv`  
- **Gráficos clave:**  
  - `outputs/saldo_vendedor_tiempo.png`  
  - `outputs/dist_saldos_compradores.png` (si hubo compras)  
  - `outputs/metricas_bar.png`  
- **Conclusiones automáticas:** `outputs/conclusiones.md`  
  (horizonte simulado, supply final y tendencia, tasas de éxito/fallas, recomendaciones)

---

## 📐 Ajuste de FDPs y Verificación
- **Ajuste (solo con `fitter`):**  
  Se ajustan distribuciones candidatas (`expon`, `gamma`, `lognorm`, `norm`, `weibull_min`) para:
  - **TS (Δ entre mints)**  
  - **LLIN (Δ entre compras)**  

  Resúmenes gráficos:
  - `outputs/ajuste_ts.png`  
  - `outputs/ajuste_llin.png`

- **Verificación:**  
  Re-muestreo desde la **mejor FDP** hallada y re-ajuste para chequear coherencia del fit (al estilo del cuaderno del profesor). Resultados y figuras en `outputs/`.

---

## 🎯 Notas de Reproducibilidad
- Se fijan **semillas** (`numpy` y `random`) para resultados reproducibles.  
- Los bloques de export son **idempotentes** (no duplican archivos y pueden sobreescribirse).  

---

## 🛠 Guía rápida / Runbook
1. Correr **Bloque 1 (setup)** y **Bloque 2 (imports)**.  
2. Definir parámetros y **unidad de tiempo** (ya seteado en **días**).  
3. Ejecutar **Generación de datos**, **EDA** y **Métricas**.  
4. Correr **Visualizaciones** y el bloque **Tokens en circulación + Resumen** (unificado) para obtener `tokens_circulacion.csv` y `resumen_tiempo.csv`.  
5. Ejecutar **Ajuste de FDPs (Fitter)** y la **Verificación**.  
6. Revisar `outputs/`: métricas, gráficos, ajustes y **conclusiones.md**.  
7. (Opcional) Subir todo a GitHub (ver `.gitignore`).  

---