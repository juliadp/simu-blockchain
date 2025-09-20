# Simulación de Blockchain en Real Estate – BlockEstateSim

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/juliadp/simu-blockchain/blob/main/TP%20Final%20Simulacion.ipynb)

📚 **Descripción del Proyecto**  
Este proyecto simula el proceso de **tokenización de propiedades en blockchain**, modelando los eventos principales:  
- Emisión de tokens (`mint`)  
- Quema de tokens (`burn_token`)  
- Compras exitosas (`compra_exitosa`)  
- Compras fallidas (`compra_fallida_*`)  

A través de esta simulación se analizan métricas clave como la cantidad total de tokenizaciones (CTS), el porcentaje de tokens quemados (PTB), el promedio de saldo de compradores (PSC) y la cantidad de transferencias fallidas (CTF). El sistema también permite evaluar la evolución de tokens en circulación, el saldo del vendedor y los intervalos entre eventos.

---

📑 **Índice de la Estructura del Proyecto**

---

📂 **Estructura General**
```
simu-blockestate/
├── TP Final Simulacion.ipynb       # Notebook principal con la simulación
├── README.md                       # Documentación del proyecto
├── requirements.txt                # Dependencias mínimas para reproducir el análisis
├── mejoras_resumen.txt             # Bitácora de mejoras y ejecución automática
│
├── outputs/                        # Resultados generados por la simulación
│   ├── metricas.csv                # Métricas clave (CTS, PTB, CTF, TS, etc.)
│   ├── conteo_eventos.csv          # Conteo de eventos por tipo
│   ├── tokens_circulacion.csv      # Tokens en circulación en el tiempo
│   ├── freq_eventos.png            # Frecuencia de eventos
│   ├── saldo_vendedor_tiempo.png   # Evolución del saldo del vendedor
│   ├── tokens_circulacion.png      # Evolución de tokens acumulados
│   ├── hist_intervalos_mint.png    # Intervalos entre tokenizaciones
│   ├── tasa_exito_rodante.png      # Tasa de éxito de compras (ventana móvil)
│   └── reporte.html                # Reporte consolidado con tablas y gráficos
```

---

🔍 **Descripción de los Principales Componentes**

📌 **Notebook Principal**  
- `TP Final Simulacion.ipynb`: Contiene la lógica de simulación, generación de eventos, cálculo de métricas y visualizaciones.  

📌 **Resultados (outputs/)**  
- `metricas.csv`: Métricas globales de la simulación (CTS, PTB, CTF, TS, etc.).  
- `conteo_eventos.csv`: Distribución de frecuencia por tipo de evento.  
- `tokens_circulacion.csv`: Evolución del supply de tokens a lo largo del tiempo.  
- Gráficos en formato `.png`: visualizaciones de métricas clave.  
- `reporte.html`: Informe auto-contenido con tablas y gráficos integrados.  

📌 **Documentación y soporte**  
- `README.md`: Explicación del proyecto y guía rápida de uso.  
- `requirements.txt`: Dependencias necesarias para ejecutar el análisis localmente.  

---

📊 **Métricas Principales**
- **CTS**: Cantidad total de tokenizaciones solicitadas.  
- **PTB**: Porcentaje de tokens quemados sobre el total emitido.  
- **CTF**: Cantidad total de transferencias fallidas.  
- **PSC**: Promedio de saldo de los compradores (requiere módulo de compradores, aún no implementado).  
- **TS**: Intervalo promedio entre eventos de tokenización.  

---

💡 **Guía Rápida**
- El punto de entrada es `TP Final Simulacion.ipynb`.  
- Los resultados se almacenan en la carpeta `outputs/`.  
- Para ejecutar localmente:  
  ```bash
  pip install -r requirements.txt
  jupyter notebook
  # Abrir TP Final Simulacion.ipynb
  ```  
- En Google Colab: abrir el notebook, correr el bloque de instalación y luego las celdas de simulación.  

---
