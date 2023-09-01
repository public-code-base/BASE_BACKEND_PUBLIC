import __init__
import settings.settings as settings
import couchdb2

class CouchDB:
    def __init__(self, url=settings.COUCHDB_URL, username=settings.COUCHDB_USER, password=settings.COUCHDB_PASSWORD):
        self.server = couchdb2.Server(href=url, username=username, password=password)

if __name__ == '__main__':
    CouchDB()