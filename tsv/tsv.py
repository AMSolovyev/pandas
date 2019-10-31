import csv
import pandas


def open_file_with_data(path):
    data = pandas.read_csv(path, sep='\t',
                           names=['Class', 'Surname', 'Height'])                   
    return data


def count_parameters(data):
    del data['Surname']
    class_number = data.sort_values(['Class'])
    class_mean = class_number.groupby('Class').mean()
    return class_mean


def printed(class_mean):
    print(class_mean)


if __name__ == '__main__':
    path = '/home/linux/пример/amusing_python/work_with_file/tsv/dataset_3380_5.txt'
    opened = open_file_with_data(path)
    counted = count_parameters(opened)
    printed_data = printed(counted)
