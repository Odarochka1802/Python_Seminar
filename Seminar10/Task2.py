import os
import json
import csv
import pickle


class Directory:
    results = []

    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.results = []

    @classmethod
    def get_size(self, path):
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                f_p = os.path.join(dirpath, file)
                total += os.path.getsize(f_p)
        return total

    def get_results(self):
        for root, dirs, files in os.walk(self.dir_path):
            for name in files:
                full_path = os.path.join(root, name)
                self.results.append({"directory": root,
                                     "directory or file": "File",
                                     "name": name,
                                     "size": str(os.path.getsize(full_path)) + " bytes"})

            for name in dirs:
                full_path = os.path.join(root, name)
                self.results.append({"directory": root,
                                     "directory or file": "Directory",
                                     "name": name,
                                     "size": str(self.get_size(full_path)) + " bytes"})

    def to_json(self):
        with open("file.json", "w") as j_file:
            json.dump(self.results, j_file)

    def to_cvs(self):
        with open("file.csv", "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
            writer.writeheader()
            writer.writerows(self.results)

    def to_pic(self):
        with open("file.pickle", "wb") as p_file:
            pickle.dump(self.results, p_file)


if __name__ == "__main__":
    c1 = Directory(r"C:\Users\odaro\PycharmProjects\PythonSeminar")
    c1.get_results()
    c1.to_pic()
    c1.to_cvs()
    c1.to_json()
