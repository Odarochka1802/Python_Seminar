import os
import json
import csv
import pickle


def get_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            f_p = os.path.join(dirpath, file)
            total += os.path.getsize(f_p)
    return total


def directory_walker(dir_path):
    results = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            full_path = os.path.join(root, name)
            results.append({"directory": root,
                            "directory or file": "File",
                            "name": name,
                            "size": str(os.path.getsize(full_path)) + " bytes"})

        for name in dirs:
            full_path = os.path.join(root, name)
            results.append({"directory": root,
                            "directory or file": "Directory",
                            "name": name,
                            "size": str(get_size(full_path)) + " bytes"})

    with open("file.json", "w") as j_file:
        json.dump(results, j_file)

    with open("file.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    with open("file.pickle", "wb") as p_file:
        pickle.dump(results, p_file)


directory_walker(r"C:\Users\odaro\PycharmProjects\PythonSeminar")
