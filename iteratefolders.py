#DON"T RUN THIS CODE AGAIN you've already moved all the correct zipfiles to eventfiles folder 
import os
import pathlib
import timeit
import glob
import gzip
import shutil

path = r"w3browse-49652"
def a():
    list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]
    #print(len(list_subfolders_with_paths))
    i=0
    j=len(list_subfolders_with_paths)
    while(i<j):
        path2=os.path.join(list_subfolders_with_paths[i]+'/xrt/event') #joining a Python variable with an extension to obtain a path name
        list_swift_files_paths = [f.path for f in os.scandir(path2) if f.is_file()]
        #print(path2)
        #print(list_swift_files)
        k=0
        l=len(list_swift_files_paths)
        while(k<l):
            if(list_swift_files_paths[k].find('pcw3po_cl.evt.gz') != -1):
                myfile = list_swift_files_paths[k][37:]
                #gzip.GzipFile(list_swift_files_paths[k], mode='r')
                with gzip.open(list_swift_files_paths[k], 'rb') as f_in:
                    with open('eventfiles/'+myfile, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                '''
                file2 = open(list_swift_files_paths[k], 'r')
                file2.extractall('./eventfiles')
                
                with ZipFile(list_swift_files_paths[k]) as myzip:
                    with myzip.open(myfile) as myfile2:
                        print(myfile2.read())
                '''
            k=k+1
        i=i+1
a()