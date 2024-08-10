import os

def parse_cf_file(filepath):
    data = {}
    with open(filepath, 'r') as file:
        for line in file:
            if "->" in line:
                key, value = line.split("->", 1)
                data[key.strip()] = value.strip()
    return data

def read_all_cf_files(folder):
    cf_data = {}
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder, filename)
            cf_data[filename] = parse_cf_file(filepath)
    return cf_data
