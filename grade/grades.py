import pandas


def opened_file(path):
    data = pandas.read_csv(path, sep=';',
                           names=[
                                  'Фамилия', 'Математика', 'Физика',
                                  'Русский язык'
                           ])
    return data


def counted_mean(data):
    mathematics = data['Математика'].mean()
    phisics = data['Физика'].mean()
    russian = data['Русский язык'].mean()
    data['Среднее оценка ученика'] = (data['Математика'] + data['Физика'] +
                                  data['Русский язык']) / 3
    mean_greade = data['Среднее оценка ученика']
  
    with open(output, 'w') as file:
        for value in mean_greade:
            file.write(str(value)+'\n')
        file.write(str(mathematics) + ' ' + str(phisics) + ' ' + str(russian))


if __name__ == '__main__':
	path = 'dataset_3363_4.txt'
	output = 'result.txt'

	opened = opened_file(path)
	count = counted_mean(opened)