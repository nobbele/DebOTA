import urllib.request
import bz2
class CydiaDebLocations():
    def __init__(self):
        self.packagedict = {}
    def PackageLocation(self, url, PackageIdentifierOrName="Name"):
        url = url + "/Packages.bz2"
        response = urllib.request.urlopen(url)
        data = response.read()
        
        packages = bz2.decompress(data).decode()
        
        k = packages.replace("Package", "¤").split('¤')
        j = [k[0]] + ['a'+l for l in k[1:]]
        j.pop(0)
        startf = "Filename: "
        endf = "\n"
        starta = "a: "
        enda = "\n"
        startn = "Name: "
        endn = "\n"
        packagedict = {}
        for s in j:
            k = s
            x = s
            
            
            
            t = s.split(startf)[1].split(endf)[0]
            
            
            
            h = k.split(starta)[1].split(enda)[0]

            
            
            y = x.split(startn)[1].split(endn)[0]
            
            packagedict[h if (PackageIdentifierOrName.lower() == "Name") else y] = t
            
        self.packagedict = packagedict
def GrabDebLocations(repo, PackageOrId='Name'):
    xzx = CydiaDebLocations()
    xzx.PackageLocation(repo, PackageOrId)
    return xzx.packagedict
    
