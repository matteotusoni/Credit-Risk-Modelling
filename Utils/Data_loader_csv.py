
import os
import pandas as pd

def Data_loader_csv(folder):

    csv_file_list = []
    for file in os.listdir(folder):
        if file.endswith('.csv'):
            csv_file_list.append(file.rstrip('.csv'))

    #print(csv_file_list)
    dataset_dictionary={}

    for file in csv_file_list:
        full_path = os.path.join(folder, file+".csv")
        separate_words = file.split('_')
        if len(separate_words) >= 2:
            name_root = '_'.join(separate_words[:2])
            if name_root in dataset_dictionary.keys():
                dataset_dictionary[name_root]= pd.concat([dataset_dictionary[name_root], pd.read_csv(full_path)], ignore_index=True)
            if name_root not in dataset_dictionary.keys():
                dataset_dictionary[name_root]=pd.read_csv(full_path)

    return dataset_dictionary