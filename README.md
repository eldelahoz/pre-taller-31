# Pre taller, Gestion de Biblioteca Digial
`Una biblioteca local está digitalizando su catálogo de libros y quiere crear una API que permita a los usuarios buscar y ver detalles de los libros disponibles. La API deberá gestionar información básica sobre los libros, como el título, autor, fecha de publicación, género, y si están disponibles o prestados.`

# Modelo:

#### 1. **Books Table**
- **Columns:**
  - `book_id` (Primary Key, INT, AUTO_INCREMENT)
  - `title` (VARCHAR(255), NOT NULL)
  - `author_id` (Foreign Key, INT, NOT NULL)
  - `publication_date` (DATE)
  - `genre_id` (Foreign Key, INT)
  - `status` (ENUM('available', 'borrowed'), NOT NULL)
  
#### 2. **Authors Table**
- **Columns:**
  - `author_id` (Primary Key, INT, AUTO_INCREMENT)
  - `first_name` (VARCHAR(100), NOT NULL)
  - `last_name` (VARCHAR(100), NOT NULL)
  - `date_of_birth` (DATE)
  
#### 3. **Genres Table**
- **Columns:**
  - `genre_id` (Primary Key, INT, AUTO_INCREMENT)
  - `genre_name` (VARCHAR(100), NOT NULL)

#### 4. **Borrowers Table**
- **Columns:**
  - `borrower_id` (Primary Key, INT, AUTO_INCREMENT)
  - `first_name` (VARCHAR(100), NOT NULL)
  - `last_name` (VARCHAR(100), NOT NULL)
  - `email` (VARCHAR(255), UNIQUE)
  - `phone_number` (VARCHAR(15))

#### 5. **BorrowingRecords Table**
- **Purpose:** To track which borrowers have borrowed which books and when.
- **Columns:**
  - `record_id` (Primary Key, INT, AUTO_INCREMENT)
  - `book_id` (Foreign Key, INT, NOT NULL)
  - `borrower_id` (Foreign Key, INT, NOT NULL)
  - `borrow_date` (DATETIME, NOT NULL)
  - `return_date` (DATETIME)
