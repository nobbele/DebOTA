import DebLocationsOfRepo as debloc
import urllib.request

class DebDownloader():
    def __init__(self):
        self.test = 'test'
    def Download(self, repo, IdOrNameSTR, NameOrPackageIdentifier='Name'):
        packages = debloc.GrabDebLocations(repo)
        if IdOrNameSTR in packages:
            link = repo + '/' + packages.get(IdOrNameSTR)
            return link
        else:
            print('Error: no such Identifier/Name')
            return 'null'
def DownloadDeb(repo, IdOrName, NameOrPackageIndentifier='Name'):
    xyx = DebDownloader()
    url = repo
    url = xyx.Download(url, IdOrName)
    urllib.request.urlretrieve(url, 'debs/'+ IdOrName + ".deb")

        
