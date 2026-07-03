<img width="1857" height="916" alt="image" src="https://github.com/user-attachments/assets/a23df510-53d9-47b2-a791-617ec5aecb34" /># 🎸 MusicPro — E-Commerce de Instrumentos Musicales

Plataforma web de e-commerce desarrollada con **Django 4.2**, orientada a la venta de instrumentos musicales. Incluye catálogo con filtros, carrito de compras, flujo completo de checkout, gestión de órdenes y pagos integrados con **Transbank Webpay Plus**.

## Funcionalidades

### Catálogo / Tienda
- Productos con imagen, precio, stock y disponibilidad.
- Organización por **categorías**, **subcategorías**, **tipo de instrumento** y **marca**.
- Slugs automáticos para URLs amigables.

### Usuarios y Autenticación
- Modelo de usuario personalizado con login/registro.
- Perfil con administración de ubicaciones.
- Sistema de roles (bodeguero / vendedor / contador) mediante flags y grupos.

### Carrito de Compras
- Agregar y remover productos.
- Cálculo automático de subtotal e **IVA (19%)**.

### Órdenes y Pagos
- Creación de órdenes desde el checkout con asociación de productos.
- Confirmación de orden con actualización automática de stock.
- Integración de pagos vía **Transbank Webpay Plus** (crear/confirmar transacción).

### API REST
- Endpoint de productos implementado con **Django REST Framework**.

## Tech Stack

| Capa | Tecnología |
|------|-----------|
| Backend | Django 4.2, Python 3.x |
| API | Django REST Framework |
| Base de Datos | SQLite |
| Pagos | Transbank SDK (Webpay Plus) |
| UI | django-crispy-forms, crispy-bootstrap4 |
| Otros | Pillow, django-autoslug |

## Estructura del Proyecto

```
musicpro/
├── musicpro/          # Configuración del proyecto (settings, urls, wsgi)
├── app/               # App principal (tienda, usuarios, CRUD, templates)
├── carts/             # Carrito de compras
├── orders/            # Órdenes y pagos
├── media/img/productos/  # Imágenes de productos
├── manage.py          # Entrypoint de Django
├── requeriments.txt   # Dependencias
└── db.sqlite3         # Base de datos local
```

## Instalación y Ejecución

```bash
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
```

La aplicación estará disponible en `http://localhost:8000`
