🎸 MusicPro — E-Commerce de Instrumentos Musicales

Plataforma web de e-commerce desarrollada con Django, orientada a la venta de instrumentos musicales. Incluye catálogo con filtros, carrito de compras, flujo completo de checkout, gestión de órdenes y pagos integrados con Transbank Webpay Plus.

Funcionalidades
Catálogo / Tienda
Productos con imagen, precio, stock y disponibilidad.
Organización por categorías, subcategorías, tipo de instrumento y marca.
Slugs automáticos para URLs amigables.
Usuarios y Autenticación
Modelo de usuario personalizado con login/registro.
Perfil con administración de ubicaciones.
Sistema de roles (bodeguero / vendedor / contador) mediante flags y grupos.
Carrito de Compras
Agregar y remover productos.
Cálculo automático de subtotal e IVA (19%).
Órdenes y Pagos
Creación de órdenes desde el checkout con asociación de productos.
Confirmación de orden con actualización automática de stock.
Integración de pagos con Transbank Webpay Plus (ambiente de integración): crear y confirmar transacción.
API REST
Endpoint de productos implementado con Django REST Framework.
Tech Stack
Capa	Tecnología
Backend	Django 6, Python 3.12
API	Django REST Framework
Base de Datos	PostgreSQL 16 (Docker) · SQLite (local)
Contenedores	Docker, Docker Compose
Pagos	Transbank SDK (Webpay Plus)
UI	django-crispy-forms, crispy-bootstrap4
Otros	Pillow, django-autoslug, dj-database-url
Estructura del Proyecto
musicpro/
├── musicpro/             # Configuración del proyecto (settings, urls, wsgi)
├── app/                  # App principal (tienda, usuarios, CRUD, templates)
├── carts/                # Carrito de compras
├── orders/               # Órdenes y pagos
├── media/img/productos/  # Imágenes de productos
├── Dockerfile            # Imagen de la aplicación
├── docker-compose.yml    # Orquestación: app + base de datos
├── .dockerignore         # Exclusiones del build
├── manage.py             # Entrypoint de Django
└── requirements.txt      # Dependencias
Instalación con Docker (recomendado)

Requiere Docker Desktop en ejecución.

bash
# 1. Clonar repositorio
git clone https://github.com/dacamposk/musicpro.git
cd musicpro

# 2. Construir y levantar los servicios
docker compose up --build

# 3. En otra terminal: migraciones y superusuario
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser

Disponible en http://localhost:8000, admin en http://localhost:8000/admin.

Levanta dos servicios: web (Django) y db (PostgreSQL 16). Los datos persisten en un volumen.

Para detener: Ctrl + C o docker compose down.

Instalación manual (SQLite)

Sin la variable DATABASE_URL, el proyecto usa SQLite.

bash
# 1. Clonar repositorio
git clone https://github.com/dacamposk/musicpro.git
cd musicpro

# 2. Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
# .venv\Scripts\Activate.ps1     # Windows PowerShell

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Migraciones y superusuario
python manage.py migrate
python manage.py createsuperuser

# 5. Ejecutar servidor
python manage.py runserver
Capturas
<img width="1857" height="916" alt="Portada de la tienda" src="https://github.com/user-attachments/assets/a23df510-53d9-47b2-a791-617ec5aecb34" /> <img width="1855" height="921" alt="Catálogo de productos" src="https://github.com/user-attachments/assets/078f6ae8-c66c-45bc-aa63-ca74b731c18c" /> <img width="1854" height="923" alt="Ficha de producto" src="https://github.com/user-attachments/assets/d829622e-3ea9-4d57-913c-f4676b3a0ebd" /> <img width="1849" height="925" alt="Perfil de usuario" src="https://github.com/user-attachments/assets/9a661ee1-47d5-4825-a971-1c1a86dfdfa5" />
