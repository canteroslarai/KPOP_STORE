from sqlalchemy import Column, Integer, String, Float, Date, Enum, create_engine, Text
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class TipoProducto(enum.Enum):
    Album = "Album"
    Photocard = "Photocard"
    Lightstick = "Lightstick"
    Ropa = "Ropa"
    Accesorio = "Accesorio"
    Coleccionable = "Coleccionable"

class EstadoProducto(enum.Enum):
    Nuevo = "Nuevo"
    Usado = "Usado"
    Pre_order = "Pre-order"
    Limitado = "Limitado"
    Descatalogado = "Descatalogado"

class Producto(Base):
    __tablename__ = 'productos'
    
    ID_Producto = Column(String(60), primary_key=True, nullable=False)
    Nombre = Column(String(200), nullable=False)
    Grupo = Column(String(100), nullable=False)
    Miembro = Column(String(100))
    Album_Name = Column(String(150))
    Era = Column(String(100))
    Tipo_Producto = Column(Enum(TipoProducto), nullable=False)
    Version = Column(String(100))
    Rarity = Column(String(50))
    Precio = Column(Float, nullable=False)
    Stock = Column(Integer, nullable=False, default=100)
    Descripcion = Column(Text, nullable=False)
    Fecha_Lanzamiento = Column(Date)
    Estado = Column(Enum(EstadoProducto), nullable=False)
    URL_Imagen = Column(String(500), nullable=False)

engine = create_engine('sqlite:///kpopvault.db', echo=True)
Base.metadata.create_all(engine)

print("✅ Tabla de productos creada correctamente.")