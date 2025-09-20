# Simulación Blockchain - TokenSys

📚 **Descripción del Proyecto**  
Este proyecto simula el proceso de tokenización de propiedades en una blockchain.  
Se modelan los eventos principales:  
- TTS: Tokenización solicitada  
- TM: Mint  
- TLLI: Llegada de interesado  
- TCI: Compra de interesado  
- TBT: Burn token  
- TAP: Actualización de precio  

📊 **Variables de Resultados**  
- CTS: Cantidad total de tokenizaciones solicitadas  
- PTB: Porcentaje de tokens burneados  
- PSC: Promedio de saldo de los compradores  
- CTF: Cantidad de transferencias fallidas  

📑 **Estructura del Proyecto**  
```
simu-blockchain/
├── main.py
├── README.md
├── requirements.txt
├── dataset/
│   └── blockchain_tokens.csv
├── docs/
│   ├── TP_Simulacion_Blockchain.pdf
│   ├── Resultados.xls
│   ├── Diagramas/
│   └── FDPS/
│       └── TP8_Blockchain.ipynb
├── resultados/
│   ├── resultados_simulacion.csv
│   └── resultados_bar.png
└── src/
    ├── config/config.py
    ├── events/
    ├── fdp/
    └── utils/
```

💡 **Guía Rápida**  
1. Clonar el repositorio  
   ```bash
   git clone https://github.com/usuario/simu-blockchain.git
   cd simu-blockchain
   ```

2. Crear entorno virtual (opcional) e instalar dependencias  
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar la simulación  
   ```bash
   python main.py
   ```

4. Los resultados se almacenan en la carpeta `resultados/`.  
