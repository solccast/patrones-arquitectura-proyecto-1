from src.core.services.persona import PersonaService
from src.core.services.direccion import DireccionService
from datetime import date

def cargar_seeds():
    # Creación de direcciones
    direccion_1 = DireccionService.crear_direccion(
        {
            "calle": "Calle Falsa",
            "numero": "123",
            "localidad": "Villa Real",
            "provincia": "Buenos Aires",
            "pais": "Argentina",
            "codigo_postal": "1407",
            "tipo": "LABORAL",
            "es_principal": False,
        }
    )

    direccion_2 = DireccionService.crear_direccion(
        {
            "calle": "Av. Siempre Viva",
            "numero": "742",
            "localidad": "Springfield",
            "provincia": "Buenos Aires",
            "pais": "Argentina",
            "codigo_postal": "1000",
            "tipo": "RESIDENCIAL",
            "es_principal": True,    
        }
    )

    direccion_3 = DireccionService.crear_direccion(
        {
            "calle": "Belgrano",
            "numero": "789",
            "localidad": "Córdoba",
            "provincia": "Córdoba",
            "pais": "Argentina",
            "codigo_postal": "5000",
            "tipo": "FACTURACION",
            "es_principal": True,
        }
    )

    direccion_4 = DireccionService.crear_direccion(
        {
            "calle": "San Martín",
            "numero": "456",
            "localidad": "Rosario",
            "provincia": "Santa Fe",
            "pais": "Argentina",
            "codigo_postal": "2000",
            "tipo": "RESIDENCIAL",
            "es_principal": True,
        }
    )

    # Creación de personas

    persona_1 = PersonaService.crear_persona(
        {
            "nombre": "Juan",
            "apellido": "Pérez",
            "fecha_nacimiento": date(1990, 1, 1),
            "direcciones": [direccion_1, direccion_2],
            "dni": "12345678",
            "edad": 33,
        }
    )

    persona_2 = PersonaService.crear_persona(
        {
            "nombre": "Ana",
            "apellido": "Gómez",
            "fecha_nacimiento": date(1995, 5, 15),
            "direcciones": [direccion_3],
            "dni": "87654321",
            "edad": 28,
        }
    )

    persona_3 = PersonaService.crear_persona(
        {
            "nombre": "Luis",
            "apellido": "Martínez",
            "fecha_nacimiento": date(1985, 10, 20),
            "direcciones": [direccion_4],
            "dni": "23456789",
            "edad": 37,
        }
    )

    persona_4 = PersonaService.crear_persona(
        {
            "nombre": "María",
            "apellido": "López",
            "fecha_nacimiento": date(1992, 3, 30),
            "dni": "34567890",
            "edad": 31,
        }
    )

    persona_5 = PersonaService.crear_persona(
        {
            "nombre": "Pedro",
            "apellido": "García",
            "fecha_nacimiento": date(1988, 7, 25),
            "dni": "45678901",
            "edad": 35,
        }
    )