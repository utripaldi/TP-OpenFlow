<div align="center">
  <h1>TP-OpenFlow - SDN Firewall</h1>

  <p>
    <img src="https://img.shields.io/badge/Controller-POX-blue?style=for-the-badge&logo=python&logoColor=white" alt="POX" />
    <img src="https://img.shields.io/badge/Python-2.7_|_3.x-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
    <img src="https://img.shields.io/badge/Network-Mininet-orange?style=for-the-badge" alt="Mininet" />
    <img src="https://img.shields.io/badge/Protocol-OpenFlow-green?style=for-the-badge" alt="OpenFlow" />
  </p>

  <p>
    Implementación de un Firewall definido por software (SDN) utilizando el controlador <strong>POX</strong> y <strong>Mininet</strong>.<br>
    Permite filtrar tráfico TCP/UDP de forma dinámica basado en reglas configurables.
  </p>
</div>

---

### 🚀 Stack Tecnológico y Características
* **Arquitectura:** SDN (Software Defined Networking) con OpenFlow.
* **Componentes Principales:**
    * 🧠 **Controlador:** POX (Python 2.7) ejecutando `forwarding.l2_learning` + módulo de firewall propio.
    * 🌐 **Topología:** Cadena de switches (ChainTopo) simulada en Mininet (Python 3).
* **Funcionalidades del Firewall:**
    * 📋 **Reglas Configurables:** Lectura dinámica de reglas desde `firewall_rules.json`.
    * 🛡️ **Filtrado Granular:** Bloqueo por puerto destino (TCP/UDP), IP origen/destino y pares de hosts.
    * 🧪 **Testing Automático:** Scripts de prueba integrados con `iperf` y `ping` para validar bloqueos.

---

## 📦 Dependencias

Este proyecto requiere las siguientes dependencias:

- **Pox** (rama `dart`): [https://github.com/noxrepo/pox/tree/dart](https://github.com/noxrepo/pox/tree/dart)
- **Python 2.7** (Para ejecutar POX)
- **Python 3** (Para ejecutar Mininet)
- **Mininet**

## 🛠️ Ejemplo de ejecución

El sistema requiere dos terminales: una para el controlador y otra para la topología.

### Terminal 1: Controlador (POX)
*Desde la carpeta donde se encuentra POX:*

```bash
$ export PYTHONPATH=$PYTHONPATH:<ruta a la carpeta de este repo>/src/
$ python2 ./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning pox_firewall
```

### Terminal 2: Topología (Mininet)
*Desde la carpeta donde se encuentra este repositorio:*

```bash
# El flag -n define la cantidad de switches intermedios
$ sudo python3 ./src/init_mininet.py [-n/--n <SWITCHES>]
```

## 🧪 Ejecución de los tests automáticos

Para verificar el correcto funcionamiento de las reglas del firewall:

### Terminal 1 (Controlador):

```bash
$ export PYTHONPATH=$PYTHONPATH:<ruta a la carpeta de este repo>/src/
$ python2 ./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning pox_firewall
```

### Terminal 2 (Tests):

```bash
$ sudo python3 ./src/test_firewall.py [-n/--n <SWITCHES>]
```

---

## 👥 Integrantes

<div align="center">

FIUBA Redes (TA048) - Cátedra: Alvarez Hamelin TP N° 2 - Grupo 12

| Integrante | Padrón | Contacto |
| :--- | :---: | :---: |
| **Calderón Vasil, Máximo Augusto** | 111810 | [![GitHub](https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github)](https://github.com/maxivasil) [![Email](https://img.shields.io/badge/Email-red?style=flat-square&logo=gmail&logoColor=white)](mailto:mcalderonv@fi.uba.ar) |
| **Tripaldi, Ulises Valentín** | 111919 | [![GitHub](https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github)](https://github.com/utripaldi) [![Email](https://img.shields.io/badge/Email-red?style=flat-square&logo=gmail&logoColor=white)](mailto:utripaldi@fi.uba.ar) |
| **Monti, Alen** | 108081 | [![GitHub](https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github)](https://github.com/alenmonti) [![Email](https://img.shields.io/badge/Email-red?style=flat-square&logo=gmail&logoColor=white)](mailto:amonti@fi.uba.ar) |
| **Adelardi, Jose Ignacio** | 111701 | [![GitHub](https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github)](https://github.com/IgnacioAdelardi12) [![Email](https://img.shields.io/badge/Email-red?style=flat-square&logo=gmail&logoColor=white)](mailto:jadelardi@fi.uba.ar) |

  <p>Facultad de Ingeniería de la Universidad de Buenos Aires (FIUBA)</p> 
</div>