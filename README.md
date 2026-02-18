# MusicPro 

**MusicPro** es un proyecto web (Django) orientado a la venta de instrumentos musicales, con catálogo de productos, filtros por categorías, carrito de compras, flujo de checkout y gestión de órdenes. También incluye endpoints API para productos y un flujo de pago integrado con Webpay Plus (Transbank).

##  Funcionalidades

- **Catálogo / Tienda**
  - Productos con imagen, precio, stock y disponibilidad.
  - Organización por **categorías**, **subcategorías**, **tipo de instrumento** y **marca**.
  - Slugs automáticos para URLs amigables.
- **Usuarios y autenticación**
  - Modelo de usuario personalizado.
  - Login/registro.
  - Perfil con administración de ubicaciones.
  - Roles (por flags/grupos) como bodeguero/vendedor/contador.
- **Carrito**
  - Agregar/remover productos.
  - Cálculo de subtotal y **IVA (19%)**.
- **Órdenes**
  - Creación de órdenes desde el checkout.
  - Asociación de productos a la orden.
  - Confirmación y actualización de stock.
- **Pagos**
  - Integración de transacciones vía **Transbank Webpay Plus** (crear/confirmar).
- **API**
  - Router con endpoint para **producto** usando Django REST Framework.

##  Tecnologías

- **Django 4.2**
- SQLite (db local)
- Django REST Framework
- django-crispy-forms + crispy-bootstrap4
- Pillow (imágenes)
- django-autoslug
- Transbank SDK (Webpay Plus)

## Estructura del proyecto

- `musicpro/` → configuración del proyecto (settings/urls/wsgi)
- `app/` → app principal (tienda, usuarios, crud, templates)
- `carts/` → carrito
- `orders/` → órdenes + pagos
- `media/img/productos/` → imágenes de productos
- `manage.py` → entrypoint de Django
- `db.sqlite3` → base de datos local (si viene incluida)

##  Requisitos

- Python 3.x
- pip / virtualenv

## 🚀 Instalación y ejecución (local)

1) Clona el repositorio:
bash
git clone https://github.com/dacamposk/musicpro.git
cd musicpro

2) Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1

3) Instalar dependencias
```
pip install -r requeriments.txt
pip install django-autoslug crispy-bootstrap4 transbank-sdk
```

 5) Migraciones y superusuario
```
python manage.py migrate
python manage.py createsuperuser
```

 7) Ejecutar servidor

```
python manage.py runserver
```
