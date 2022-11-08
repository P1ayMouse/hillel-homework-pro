def query_func(query):
    if isinstance(query, dict):
        str_query = ''
        for key, value in query.items():
            str_query += f'?{key}={value}' if key == 'q' else f'&{key}={value}'
        return str_query
    else:
        return query


class Url:
    def __init__(self, scheme='', authority='', path='', query='', fragment=''):
        self.scheme = scheme
        self.authority = authority
        self.path = '/' + '/'.join(path) if isinstance(path, list) else path
        self.query = query_func(query)
        self.fragment = fragment

    def __str__(self):
        return f'{self.scheme}://{self.authority}{self.path}{self.query}' \
               f'{self.fragment}'

    def __eq__(self, other):
        return str(self) == str(other)


class HttpsUrl(Url):
    def __init__(self, scheme='https', authority='', path='', query='',
                 fragment=''):
        super().__init__(scheme=scheme, authority=authority, path=path,
                         query=query, fragment=fragment)


class HttpUrl(Url):
    def __init__(self, scheme='http', authority='', path='', query='',
                 fragment=''):
        super().__init__(scheme=scheme, authority=authority, path=path,
                         query=query, fragment=fragment)


class GoogleUrl(Url):
    def __init__(self, scheme='https', authority='google.com', path='',
                 query='', fragment=''):
        super().__init__(scheme=scheme, authority=authority, path=path,
                         query=query, fragment=fragment)


class WikiUrl(Url):
    def __init__(self, scheme='https', authority='wikipedia.org', path='',
                 query='', fragment=''):
        super().__init__(scheme=scheme, authority=authority, path=path,
                         query=query, fragment=fragment)


class UrlCreator(Url):
    def __init__(self, scheme='', authority=''):
        super().__init__(scheme=scheme, authority=authority)

    def __getattr__(self, item):
        self.path += f'/{item}'
        return self

    def __call__(self, *args, **kwargs):
        if len(args) > 0:
            self.path = ''
            self.path += f'/{"/".join(args)}'
        if len(kwargs) > 0:
            self.query = ''
            for key, value in kwargs.items():
                self.query += f'?{key}={value}' if key == 'q' \
                    else f'&{key}={value}'
        return self

    def _create(self):
        return self.__str__()


if __name__ == '__main__':
    assert GoogleUrl() == HttpsUrl(authority='google.com')
    assert GoogleUrl() == Url(scheme='https', authority='google.com')
    assert GoogleUrl() == 'https://google.com'
    assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
    assert WikiUrl(path=['wiki', 'python']) \
           == 'https://wikipedia.org/wiki/python'
    assert GoogleUrl(query={'q': 'python', 'result': 'json'}) \
           == 'https://google.com?q=python&result=json'

    url_creator = UrlCreator(scheme='https', authority='docs.python.org')
    assert url_creator.docs.v1.api.list \
           == 'https://docs.python.org/docs/v1/api/list'
    assert url_creator('api', 'v1', 'list') \
           == 'https://docs.python.org/api/v1/list'
    assert url_creator('api', 'v1', 'list', q='my_list') \
           == 'https://docs.python.org/api/v1/list?q=my_list'
    assert url_creator('3').search(q='getattr', check_keywords='yes',
                                   area='default')._create() == \
           'https://docs.python.org/3/search?q=getattr' \
           '&check_keywords=yes&area=default'
