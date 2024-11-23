# API orquestadora de servicios

El proyecto se basa en una API implementada en python utilizando flask.

Utiliza las siguientes apis públicas:

- Obtener coordenadas de una ciudad
  - <https://nominatim.openstreetmap.org/search?q=Madrid&format=json>
- Obtener tiempo de unas coordenadas
  - <https://api.weatherbit.io/v2.0/current?lat=40.4168&lon=-3.7038&key=df382b05ec56493b865063e984862441>
- Obtener vuelos y precios
  - URL QUE NO SE
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

---

## Endpoints del proyecto

1. <http://127.0.0.1:5000/>

2. <http://127.0.0.1:5000/weather/forecast?ciudad=Madrid>
