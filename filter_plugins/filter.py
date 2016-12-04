import re
class FilterModule(object):
    ''' Custom filters are loaded by FilterModule objects '''

    def filters(self):
        return {'urlsubstr': self.urlsubstr}
    def urlsubstr(self,content):
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
        return url[0]
