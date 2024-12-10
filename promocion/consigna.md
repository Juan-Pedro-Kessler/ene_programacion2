# Programación II - Universidad Tecnológica Nacional  
## Tecnicatura Universitaria en Programación  
### Segundo Cuatrimestre 2024  

## Proyecto Integrador  

### API REST para Gestión de Eventos  

Crear una API REST en Python utilizando Flask y programación orientada a objetos para gestionar un sistema de eventos. La API debe permitir realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los siguientes recursos:  

### Recursos  

#### Evento  
- **Atributos:**  
  - `id` (entero)  
  - `nombre` (string)  
  - `fecha` (string)  
  - `localizacion_id` (entero)  

#### Participante  
- **Atributos:**  
  - `id` (entero)  
  - `nombre` (string)  
  - `apellido` (string)  
  - `email` (string)  

#### Localización  
- **Atributos:**  
  - `id` (entero)  
  - `nombre` (string)  
  - `direccion` (string)  

---

## Requisitos  

### Clases de Objetos  
- Crear las clases `Evento`, `Participante` y `Localización` utilizando Programación Orientada a Objetos (POO).  
- Considerar las relaciones entre las clases:  
  - Un `Evento` tiene una `Localización` y puede tener varios `Participantes`.  
- Crear clases que funcionen como repositorio de objetos, es decir, cada clase entidad tendrá una clase repositorio que manipule una colección de sus objetos.  

---

## Endpoints  

### Evento  
- **GET** `/eventos`: Obtener todos los eventos.  
- **GET** `/eventos/{id}`: Obtener un evento por ID.  
- **POST** `/eventos`: Crear un nuevo evento.  
- **PUT** `/eventos/{id}`: Actualizar un evento existente.  
- **DELETE** `/eventos/{id}`: Eliminar un evento.  

### Participante  
- **GET** `/participantes`: Obtener todos los participantes.  
- **GET** `/participantes/{id}`: Obtener un participante por ID.  
- **POST** `/participantes`: Crear un nuevo participante.  
- **PUT** `/participantes/{id}`: Actualizar un participante existente.  
- **DELETE** `/participantes/{id}`: Eliminar un participante.  

### Localización  
- **GET** `/localizaciones`: Obtener todas las localizaciones.  
- **GET** `/localizaciones/{id}`: Obtener una localización por ID.  
- **POST** `/localizaciones`: Crear una nueva localización.  
- **PUT** `/localizaciones/{id}`: Actualizar una localización existente.  
- **DELETE** `/localizaciones/{id}`: Eliminar una localización.  

---

## Validaciones y Manejo de Errores  
- Implementar validaciones para las entradas.  
- Manejar errores de manera adecuada (por ejemplo, devolver un mensaje de error claro cuando no se encuentra un recurso).  
