# CIS41 Jihye Choi

import csv

expected_result_order_dict = {'1': 91, '2': 100, '3': 32, '4': 62, '5': 64}

order_dict = {}

def read_order(input_file):

    with open(input_file) as infile:
        reader = csv.reader(infile)

        for line in reader:
            value_list = []
            for index in range(1, len(line)):
                value_list.append(int(line[index]))
            order_dict[line[0]] = value_list
    
    total_order_dict = dict()
    for key in order_dict:
        value_total = sum(order_dict[key])
        total_order_dict[key] = value_total
    return total_order_dict

def test_sum():
    assert actual_result_total_order_dict['1'] == 91

def write_order_csv(actual_result_total_order_dict, outputFile):
    with open(outputFile, 'w') as outfile:
        for key in actual_result_total_order_dict.keys():
            outfile.write("%s,%s\n"%(key, actual_result_total_order_dict[key]))

if __name__ == "__main__":
    actual_result_total_order_dict = read_order("/Users/jihyechoi/DeAnza/CIS41/Ch12Ex1/order.csv")
    test_sum()
    print("Everything passed")
    write_order_csv(actual_result_total_order_dict, "outputfile.csv")