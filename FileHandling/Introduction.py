# File Handling 
# A file is a collection of data stored on a secondary storage device like hard disk 
# Each and every single file inside the hard disk will named in an unique way, where two different file doesn't have the same meaning 
# Below is the file path diagrammatic representation 
# D           <--- Acts a root where all the files stored inside this drive or location path
# |\ 
# | \
# |  \__________________--> File 1 ------------------------------|                     # When we are accessing File1 from D the path then the path we are in the File 1 looks like this D:/File1
# |____________________________--> File 2  -----|                |                     # Same goes for File2 too -> when we are inside the File2 the path looks like this D:/File2
#                                               |                |
#                             __________________|               / \
#                             |          |                     /   \
#                             |          |                    /     \
#                             |          |                 File 3  File 4              # We came across D drive location path and File1 location path where to access both the File 3 and File 4 
#                           File 5     File 6                                          # File4 location path looks like this D:/File1/File4
#                                                                                      # File3 location path looks like this D:/File1/File3
#
#                                                                                      # Same goes for the File5 and File6
#                                                                                      # D  -->  File 2  -->  File 5        the path location for this  -->  D:/File2/File5
#                                                                                      # D  -->  File 2  -->  File 6        the path location for this  -->  D:/File2/File6
# 
# Two types of path are there one is relative path and absolute path
# Absolute path defines the specific root location of the file where we can able to access the file directly 
# While on the other hand the relative path needs two different location paths that will help us to access the file (Sometimes it prones to error)