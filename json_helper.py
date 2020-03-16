from glob import glob
import json
import os
import pickle


# PART A
def read_json(path_name):
    file_name = path_name
    with open(file_name) as f_name:
        data = json.load(f_name)
    print(data)


path_name = ""
read_json("/Users/mtessema/PythonFundamentals.Exercises.Part9/data/super_smash_bros/link.json")


# PART B
def read_all_json_files(path_name):
    # glob pattern
    my_pc = os.path.join(path_name, '*.json')
    for file_name in glob(my_pc):
        with open(file_name) as f_name:
            data = json.load(f_name)
        print(data)


path_name = ""
read_all_json_files(path_name)


# PART C


def write_pickle(dump_to_path, pickle_path):
    pickle_out = open(dump_to_path, "wb")
    pickle.dump(pickle_path, pickle_out)
    pickle_out.close()

    return


write_pickle("/Users/mtessema/PythonFundamentals.Exercises.Part9/data/super_smash_bros/super_smash_characters.pickle",
             "/Users/mtessema/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json")


def load_pickle():
    pickle_in = open("/Users/mtessema/PythonFundamentals.Exercises.Part9/data/super_smash_bros/"
                     "super_smash_characters.pickle", "rb")
    read_file = pickle.load(pickle_in)
    print(read_file)


load_pickle()

# it works but the last one opens the file path not the data in it
