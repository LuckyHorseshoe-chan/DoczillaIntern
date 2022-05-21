import os
import copy

path = os.getcwd()
entries = os.listdir(path)
files_list, directories, files, paths = [], {path: []}, {}, [path]

def check_entries(entries, path):
    #print(path)
    global directories, files, files_list, paths
    for entry in entries:
        if entry.find('.') == -1:
            #print("dir: {0}".format(entry))
            directories[path].append(entry)
            directories[path + '\\'+ entry] = []
            files[path + '\\' + entry] = []
            paths.append(path + '\\'+ entry)
        if entry.find('.txt') != -1:
            #print("file: {0} path: {1}".format(entry, path))
            if entry in files:
                files[entry].append(path + "\\" + entry)
            else:
                files[entry] = [path + "\\" + entry]
            files_list.append(entry)
def main():
    global entries, files, files_list
    check_entries(entries, path)
    if directories[path] == [] and files == {}:
        print("There is no text files or directories. Add one and try again")
        return 0
    beg = 1
    while beg < len(directories):
        dict_copy = copy.deepcopy(directories)
        #print("len: {0}".format(len(dict_copy)))
        #print("len paths: {0}".format(len(paths)))
        for i in range(beg, len(dict_copy)):
            #print("i: {0}".format(i))
            entries = os.listdir(paths[i])
            check_entries(entries, paths[i])
        beg = len(dict_copy)
    if files_list == []:
        print("There is no text files. Add one and try again")
        return 0
    files_list = sorted(set(files_list))
    res = open('result.txt', 'w')
    for file in files_list:
        for p in files[file]:
            f = open(p, 'r')
            res.write(f.read())
            f.close()
    res.close()
    return 0
main()