# Deb OTA/Downloader

All OSes: [python command] DebOTAGUI.py

replace [python command] with "py", "python" or "python3"

Windows: Open the correct .bat which specifies the [python command] for you

Dependencies: bz2, urllib, paramiko, pysftp, tk

place deb in "debs" or enter a repo and package name then download

"Install" button will install the deb file with the same name as "Package name" text field


For developers:

The DebLocationsOfRepo file contains the function "GrabDebLocations(repo, PackageOrId='Name'):", in the repo field you put in an URL (can end in / if you want) and then in PackageOrId you place either "Name" or something else like "PackageId" (PackageId = com.nobbele.tweaktest while Name = tweaktest)

The DebDownloader file contains the function "DownloadDeb(repo, IdOrName, ~~NameOrPackageIndentifier~~)", again place repo in the "repo" variable then place either the name of the package (id comming soon) and it'll grab the deb and place it in ./debs
