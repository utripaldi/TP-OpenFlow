# TP-OpenFlow
FIUBA Redes (TA048) Cátedra: Alvarez Hamelin  - TP N° 2 - Grupo 12: 

- Máximo Augusto Calderón Vasil, padrón 111810
- Ulises Valentin Tripaldi, padrón 111919
- Alen Monti, padrón 108081
- Jose Ignacio Adelardi, 111701

## Dependencias

Este proyecto requiere las siguientes dependencias:

- **Pox** (https://github.com/noxrepo/pox/tree/dart)
- **Python 2.7**
- **Mininet**
- **Python 3**

## Ejemplo de ejecución

Terminal 1: (desde la carpeta donde se encuentra pox)

```
$ export PYTHONPATH=$PYTHONPATH:<ruta a la carpeta de este repo>/src/
$ python2 ./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning pox_firewall
```


Terminal 2: (desde la carpeta donde se encuentra este repo)

```
$ sudo python3 ./src/init_mininet.py 
```


