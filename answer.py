""" The purpose of this lesson today is to write as many functions as we can in the best way we can.
    All numbers must be formatted in lacs (00,00,000) and crores (00,00,00,000)
    Precision to two decimal places is required. Round any additional precision to two decimal places."""
import csv

def round_off(num):
    return round(num, 2)

def formatting(num):
    first, second, size = num, '', len(num)
    if '.' in num:
        first, second, size = num[:-3], num[-3:], size-3
    index = 3
    while index < len(first):
        first = first[:-index] + ',' + first[-index:]
        index += 3
    return first+second

def simple_interest(principal, term, rate):
    ans = (principal * term * rate)
    ans += principal 
    ans = formatting(str(round_off(ans)))
    return ans
    
def compound_interest(principal, term, rate, n:int=1):
    ans = principal*((1+(rate/n))**(n*term))
    ans = formatting(str(round_off(ans)))
    return ans

def compound_interest_with_payments(principal, payment, term, rate, end_of_period=True, n: int=1):
    if not end_of_period:
        principal += payment
    for _ in range(0,term):
        ans = principal * rate
        principal += payment
        principal += ans
    principal = formatting(str(round_off(principal)))
    return principal
import math
def savings_calculator(present_value, future_value, term, rate, end_of_period=True):
    if not end_of_period:
        rate = rate / (1+rate)
    ans = (future_value - present_value * (1 + rate) ** term) / ((1 + rate) ** term - 1)
    ans = math.ceil(ans * 100)/100
    ans = formatting(str(round_off(ans)))
    return ans 

def files_innerjoin(filename1, filename2, common_column):
    """inner join function on any number of keys"""
    with open(filename1, 'r') as f1, open(filename2, 'r') as f2, open('results.csv', 'w') as f:
        csv_reader_file1 = csv.reader(f1)
        csv_reader_file2 = csv.reader(f2)
        csv_writer_inner_join = csv.writer(f)

        file1_data = [data for data in csv_reader_file1]
        file2_data = [data for data in csv_reader_file2]
        header1 = file1_data[0]
        header2 = file2_data[0]
        print(header1)
        print(header2)
        if common_column not in header1 or common_column not in header2:
            return "r"
        result_header = header1 + [header for header in header2 if header not in header1]
        print(result_header)
        csv_writer_inner_join.writerow(result_header)
        
        for i in range(0,len(header1)):
            if header1[i] == common_column:
                file1_index = i
                break
		
        for i in range(0,len(header1)):
            if header1[i] == common_column:
                file2_index = i
                break
        final_data = []
        for i in range(1,len(file1_data)):
            for j in range(1, len(file2_data)): 
                data1, data2, data= file1_data[i], file2_data[j], []
                print(data1, data2)
                if data1[file1_index] == data2[file2_index]:
                    data = data1 + [i for i in data2 if i not in data1]
                if data not in final_data:
                    final_data.append(data)
        
        csv_writer_inner_join.writerows(final_data)




if __name__ == "__main__":
    print(simple_interest(123456, 23, 0.08))
    print(compound_interest(123456, 23, 0.08))
    print(compound_interest_with_payments(0, 368970.52, 35, 0.10))
    print(savings_calculator(0, 1e8, 35, 0.10))
    print(files_innerjoin('file1.csv', 'file2.csv', 'Name'))
