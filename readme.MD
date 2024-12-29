# API orquestadora de servicios

El proyecto se basa en una API implementada en python utilizando flask.

Utiliza las siguientes apis públicas:

- Obtener coordenadas de una ciudad
  - <https://nominatim.openstreetmap.org/search>
- Obtener temperatura durante un tiempo determinado de unas coordenadas
  - <https://api.open-meteo.com/v1/forecast>
- Obtener histórico de vuelos desde un aeropuerto durante un periodo de tiempo concreto
  - <https://opensky-network.org/api/flights/departure>
- Bot de mensajería de discord
  - Api integrada en librería `discord.py`.

## Pasos para ejecutar el proyecto

1. Clonar el repositorio de github

   ```bash
   git clone https://github.com/lex8jdt/finalProject
   ```

2. Crear un entorno virtual

   ```bash
   pyhton -m venv .venv
   ```

3. Activar entorno virtual

   - Windows

     ```bash
     .venv\Scripts\activate
     ```

   - Unix

     ```bash
     source venv/bin/activate
     ```

4. Instalar dependencias

   ```bash
   pip install -r requirements.txt
   ```

5. Establecer variables de entorno

   - Renombrar `config.py.template` a `config.py`
   - Cambiar los valores del template a unos propios.

6. Ejecutar el proyecto

   - Sin bot corriendo

   ```bash
   flask run
   ```

   - Con bot corriendo

   ```bash
   python app.py
   ```

7. Exportar y actualizar requirements.tx en caso de modificacion

   ```bash
   pip freeze > requirements.txt
   ```

8. Desplegar en docker

   ```bash
   docker build -t flask-app
   docker run --name flask-app -p 5000:5000 flask-app
   ```

---

## Endpoints del proyecto

1. <http://127.0.0.1:5000/>

2. <http://127.0.0.1:5000/search>

## Funcionamiento

Una vez se acceda a la página principal del proyecto, se podrá hacer uso del buscador para introducir una ciudad de salida y una ciudad de llegada. El resultado serán los vuelos transcurridos entre ambas ciudades el día anterior a la consulta, y la temperatura que hizo en ambas ciudades a lo largo del día.
