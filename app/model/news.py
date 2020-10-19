class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,name, language, description, url, category, country):
        self.name = name
        self.language = language
        self.description = description
        self.url = url
        self.category = category
        self.country = country