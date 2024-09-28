# Wake-on-LAN HTTP Server

Este proyecto implementa un servidor HTTP simple que envía paquetes mágicos (Wake-on-LAN) a equipos específicos en una red local. El servidor escucha solicitudes POST en una ruta determinada y activa el equipo correspondiente basado en su dirección MAC.

## Características

- **Envía paquetes mágicos** a equipos en la red local usando sus direcciones MAC.
- **Interfaz sencilla**: Se puede activar equipos simplemente enviando una solicitud HTTP POST.

## Requisitos

Asegúrate de tener Python 3.x instalado en tu sistema. Además, necesitarás instalar las siguientes bibliotecas:
```bash
pip install wakeonlan
```

Tal vez debas crear un entorno virtual de python para ejecutar este programa:
```bash
python -m venv NombreDeMiEntorno
```

-Activar el entorno en windows:
```bash
    wolVenv\Scripts\activate
```

-Activar en macOS y Linux:ç
```bash
    source wolVenv/bin/activate
```
