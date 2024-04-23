class Book(metaclass=DocType):
    name = fields.String("Book Name")
    author = fields.Link("Author")
    publication_date = fields.Date("Publication Date")
    description = fields.Text("Description")