class Articles:
    '''
    Articles class to define Articles Objects
    '''

    def __init__(self,author, title, description, url, urlImage, publishedAt, content):
        
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlImage = urlImage
        self.publishedAt = publishedAt
        self.content = content