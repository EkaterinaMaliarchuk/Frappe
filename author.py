class Author(metaclass=DocType):
    name = fields.String("Author Name")
    books = fields.ManyToMany("Book")