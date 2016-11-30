import os, sys

file_to_remove = sys.argv[1]
folder_to_remove = os.path.dirname(file_to_remove)
os.system("rm -rf " + folder_to_remove)
