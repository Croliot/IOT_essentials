<a id="Presentacion"></a>
# IOT_essentials
Repositorio del curso de [iot Essentials Developers](https://edu.codigoiot.com/course/view.php?id=1042 "Ir al curso")

Aqui se suben los ejercicios del curso

| Modulo | Ejercicio | Fecha |
|:------------:|-------------:|:-------------:|
| Utilizacion de R Pi | Prender LED | 18/Mayo |
| Acceso Vehicular | RFID | 21/Mayo |

## Contenidos
* [Introduccion](#Presentacion)
* [Ejercicios Incluidos](#Incluidos)
* [Advertencias de uso](#Advertencias)

<a id="Incluidos"></a>
## Ejercicios incluidos
1. Parpardear LED
    * Circuito sugerido
    * Codigo para prenderLED desde Python
1. Lectura de Tarjeta RFID
    * Requiere crear un ambiente de trabajo con:
     ```shell
     python -m venv <nombre_de_ambiente>
     source <nombre_de_ambiente>/bin/activate
      ```
    * Requiere las bibliotecas spidev, mfrc522
     ```shell
     python -m pip install spidev
     python -m pip install mfrc522
      ```
    * Consulta [rfid.py](./RFID/rfid.py)

<a id="Advertencias"></a>
## Advertencias de Uso
**Este codigo es expreimental y de fines educativos**  ***Uselo bajo su propio riesgo***
<a id="Pendientes"></a>
## To Do
- [x] Iniciar Documentacion
- [ ] Incorporar Codigo del LED
- [ ] Hacer notas sobre Git