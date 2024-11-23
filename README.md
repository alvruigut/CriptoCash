# Objetivo General del Proyecto:
El objetivo de este proyecto es crear un sistema de criptomonedas de confianza que permita emitir monedas electrónicas firmadas por un banco usando su clave privada, validarlas, evitar el doble gasto mediante la técnica Pow, para realizar transacciones entre usuarios de una manera segura y simple. El sistema está basado en la idea de un banco central que emite monedas electrónicas (criptocash), usuarios, y comerciantes, los cuales pueden interactuar con estas monedas.

## Componentes Principales del Proyecto:

### Banco Central:
- El banco emite monedas electrónicas utilizando firmas digitales para garantizar su validez.
- Los usuarios pueden solicitar monedas al banco, las cuales están firmadas digitalmente.
- El banco valida las monedas y detecta intentos de doble gasto.

### Usuario:
- El usuario solicita una moneda al banco.
- Luego, realiza transacciones o pagos con esa moneda, que pueden ser aceptados por los comerciantes.

### Comerciante:
- El comerciante recibe los pagos de los usuarios.
- El comerciante deposita las monedas en el banco para que se verifiquen.
- El banco valida si la moneda ha sido utilizada antes (para evitar el doble gasto).

### Base de Datos:
- Se utiliza SQLite para almacenar información sobre las monedas, las transacciones y su estado.
- Esto permite que el sistema sea persistente y que los registros no se pierdan al reiniciar la aplicación.

### Interfaz Gráfica:
- Tkinter se utiliza para crear una interfaz visual donde el usuario puede interactuar con el sistema: solicitar monedas, hacer pagos, depositar monedas y ver el historial de transacciones.
- Además, se implementó una visualización de la blockchain usando matplotlib y networkx para mostrar cómo las transacciones se registran en un gráfico, con cada moneda representando un nodo y las transacciones siendo las conexiones entre ellos.

## Flujo de Trabajo del Proyecto:

### Retiro de Moneda:
- El usuario ingresa su ID en la interfaz y hace clic en "Retirar Moneda".
- El banco genera una moneda firmada digitalmente para el usuario y la guarda en la base de datos.

### Transacción de Pago:
- El usuario transfiere la moneda al comerciante.
- El comerciante valida la moneda con el banco, asegurándose de que no haya sido utilizada antes (verificación de la firma y el estado de la moneda).

### Depósito de Moneda:
- El comerciante deposita la moneda en el banco.
- El banco verifica que la moneda no haya sido utilizada anteriormente. Si es válida, la marca como utilizada en la base de datos para evitar el doble gasto.

### Historial de Transacciones y Visualización de Blockchain:
- Cada transacción se guarda en la base de datos, y se muestra un historial en la interfaz.
- Además, cada vez que se realiza una transacción o depósito, el gráfico de la blockchain se actualiza, mostrando cómo las monedas y transacciones están conectadas en una red de bloques.

## Propósito y Sentido del Proyecto:

### Implementación Práctica de Conceptos Criptográficos:
El sistema utiliza **firmas digitales**, **curvas elípticas** y técnicas criptográficas para garantizar que las monedas sean auténticas y seguras, lo cual refleja cómo funcionan las criptomonedas en la vida real (como Bitcoin o Ethereum).

#### **Firma Digital**:
- **Firmas Digitales**: Utilizamos el algoritmo **ECDSA** (Elliptic Curve Digital Signature Algorithm) para firmar las monedas electrónicas generadas por el banco. Esto asegura que las monedas no puedan ser falsificadas.
- **Curvas Elípticas**: Usamos **ECC (Elliptic Curve Cryptography)** con la curva **P-256**, que proporciona un nivel de seguridad elevado con claves relativamente pequeñas.
- **SHA-256**: La **función de hash SHA-256** se usa para generar resúmenes únicos de los datos de la moneda (como el ID del usuario) antes de ser firmados con la clave privada del banco.


# Manual de Instalación

Sigue los pasos a continuación para configurar el entorno y ejecutar el proyecto:

## Requisitos Previos
Asegúrate de tener instalados:
- **Git**
- **Python** (versión 3.x)
- **Pip** (gestor de paquetes de Python)

---

## Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/alvruigut/CriptoCash.git
   cd CriptoCash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt

# Ejecución
   ```bash
  python gui.py

