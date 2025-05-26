
# 🍽️ CyberRecipes

**CyberRecipes** es una aplicación web desarrollada con Python y Flask que permite a los usuarios explorar, agregar y gestionar recetas de cocina de manera sencilla y eficiente.

## 🚀 Características

- 📝 Añadir, editar y eliminar recetas.
- 🔍 Buscar recetas por nombre o ingredientes.
- 📂 Organización de recetas por categorías.
- 📸 Posibilidad de agregar imágenes a las recetas.
- 🌐 Interfaz web intuitiva y responsiva.

## 🛠️ Tecnologías utilizadas

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Base de datos:** SQLite
- **Despliegue:** Heroku

## 📦 Estructura del proyecto

```
CyberRecipes/
├── API/
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── recetas/
├── .env
├── Procfile
├── main.py
└── requirements.txt
```

## ⚙️ Instalación y ejecución local

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/MariamGutierrez/CyberRecipes.git
   cd CyberRecipes
   ```

2. **Crear y activar un entorno virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**

   Crea un archivo `.env` en la raíz del proyecto y agrega las variables necesarias, por ejemplo:

   ```env
   FLASK_APP=main.py
   FLASK_ENV=development
   SECRET_KEY=tu_clave_secreta
   ```

5. **Iniciar la aplicación:**

   ```bash
   flask run
   ```

   La aplicación estará disponible en `http://localhost:5000`.

## 🌍 Despliegue en Heroku

Para desplegar la aplicación en Heroku:

1. **Iniciar sesión en Heroku:**

   ```bash
   heroku login
   ```

2. **Crear una nueva aplicación:**

   ```bash
   heroku create nombre-de-tu-app
   ```

3. **Subir el código a Heroku:**

   ```bash
   git push heroku main
   ```

4. **Abrir la aplicación en el navegador:**

   ```bash
   heroku open
   ```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar CyberRecipes, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agregar nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
