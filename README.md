# Pre taller, Gestion de Biblioteca Digial
`Una biblioteca local está digitalizando su catálogo de libros y quiere crear una API que permita a los usuarios buscar y ver detalles de los libros disponibles. La API deberá gestionar información básica sobre los libros, como el título, autor, fecha de publicación, género, y si están disponibles o prestados.`

# Modelo:

#### 1. **Books Table**
- **Columns:**
  - `book_id` 
  - `title`
  - `author_id`
  - `publication_date` 
  - `genre_id`
  - `status` 
  
#### 2. **Authors Table**
- **Columns:**
  - `author_id` 
  - `first_name`
  - `last_name`
  - `date_of_birth`
  
#### 3. **Genres Table**
- **Columns:**
  - `genre_id`
  - `genre_name`

#### 4. **Status Table**
- **Columns:**
  - `statu_id`
  - `statu_name`

## Instalar dependencias:

```bash
pip install -r requirements.txt
```