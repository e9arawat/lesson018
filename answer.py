""" The purpose of this lesson today is to write as 
    many functions as we can in the best way we can.
    All numbers must be formatted in lacs (00,00,000) 
    and crores (00,00,00,000) Precision to two decimal 
    places is required. Round any additional precision to 
    two decimal places."""
import csv
import math


def round_off(num):
    """function to round off values to 2 decimal places"""
    return round(num, 2)


def formatting(num):
    """function for formatting"""
    first, second, size = num, "", len(num)
    if "." in num:
        first, second, size = num[:-3], num[-3:], size - 3
    index = 3
    while index < len(first):
        first = first[:-index] + "," + first[-index:]
        index += 3
    return first + second


def simple_interest(principal, term, rate):
    """function to find simple interest"""
    ans = principal * term * rate
    ans += principal
    ans = formatting(str(round_off(ans)))
    return ans


def compound_interest(principal, term, rate, n: int = 1):
    """function to find compound interest"""
    ans = principal * ((1 + (rate / n)) ** (n * term))
    ans = formatting(str(round_off(ans)))
    return ans


def compound_interest_with_payments(principal, payment, term, rate, end_of_period=True):
    """function to find compound interest with extra payments"""
    if not end_of_period:
        principal += payment
    for _ in range(0, term):
        ans = principal * rate
        principal += payment
        principal += ans
    principal = formatting(str(round_off(principal)))
    return principal


def savings_calculator(present_value, future_value, term, rate, end_of_period=True):
    """function to find EMI"""
    if not end_of_period:
        rate = rate / (1 + rate)
    ans = (future_value - present_value * (1 + rate) ** term) / ((1 + rate) ** term - 1)
    ans = math.ceil(ans * 100) / 100
    ans = formatting(str(round_off(ans)))
    return ans


def files_innerjoin(filename1, filename2, **kwargs):
    # pylint: disable-msg=too-many-locals
    """inner join function on any number of keys"""
    common_column = kwargs.get("common_column", [])
    with open(filename1, "r", encoding="utf8") as f:
        file1_reader = csv.DictReader(f)
        data1 = list(file1_reader)
        header1 = list(data1[0].keys())

    with open(filename2, "r", encoding="utf8") as f:
        file2_reader = csv.DictReader(f)
        data2 = list(file2_reader)
        header2 = list(data2[0].keys())

    if all(bool(x not in header1 and x not in header2) for x in common_column):
        return

    result_header = header1 + [x for x in header2 if x not in header1]
    final_data = []
    for current_data1 in data1:
        for current_data2 in data2:
            if all(current_data1[x] == current_data2[x] for x in common_column):
                current_data1.update(current_data2)
                final_data.append(current_data1)
    with open("results.csv", "w", encoding="utf8") as f:
        result_writer = csv.DictWriter(f, fieldnames=result_header)
        result_writer.writeheader()
        result_writer.writerows(final_data)


def files_leftouterjoin(filename1, filename2, **kwargs):
    # pylint: disable-msg=too-many-locals
    """left outer join function on any number of keys"""
    common_column = kwargs.get("common_column", [])
    with open(filename1, "r", encoding="utf8") as f:
        file1_reader = csv.DictReader(f)
        data1 = list(file1_reader)
        header1 = list(data1[0].keys())

    with open(filename2, "r", encoding="utf8") as f:
        file2_reader = csv.DictReader(f)
        data2 = list(file2_reader)
        header2 = list(data2[0].keys())

    if any(bool(x not in header1 or x not in header2) for x in common_column):
        with open("results.csv", "w", encoding="utf8") as f:
            result_writer = csv.DictWriter(f, fieldnames=header1)
            result_writer.writeheader()
            result_writer.writerows(data1)

    result_header = header1 + [x for x in header2 if x not in header1]
    final_data = []
    for current_data1 in data1:
        match = 0
        for current_data2 in data2:
            if all(current_data1[x] == current_data2[x] for x in common_column):
                current_data1.update(current_data2)
                final_data.append(current_data1)
                match += 1
        if match == 0:
            final_data.append(current_data1)

    with open("results.csv", "w", encoding="utf8") as f:
        result_writer = csv.DictWriter(f, fieldnames=result_header)
        result_writer.writeheader()
        result_writer.writerows(final_data)


def files_rightouterjoin(filename1, filename2, **kwargs):
    # pylint: disable-msg=too-many-locals
    """right outer join function on any number of keys"""
    common_column = kwargs.get("common_column", [])
    with open(filename1, "r", encoding="utf8") as f:
        file1_reader = csv.DictReader(f)
        data1 = list(file1_reader)
        header1 = list(data1[0].keys())

    with open(filename2, "r", encoding="utf8") as f:
        file2_reader = csv.DictReader(f)
        data2 = list(file2_reader)
        header2 = list(data2[0].keys())

    if any(bool(x not in header1 or x not in header2) for x in common_column):
        with open("results.csv", "w", encoding="utf8") as f:
            result_writer = csv.DictWriter(f, fieldnames=header2)
            result_writer.writeheader()
            result_writer.writerows(data2)

    result_header = header1 + [x for x in header2 if x not in header1]
    final_data = []
    for current_data2 in data2:
        match = 0
        for current_data1 in data1:
            if all(current_data1[x] == current_data2[x] for x in common_column):
                current_data1.update(current_data2)
                final_data.append(current_data1)
                match += 1
        if match == 0:
            final_data.append(current_data2)

    with open("results.csv", "w", encoding="utf8") as f:
        result_writer = csv.DictWriter(f, fieldnames=result_header)
        result_writer.writeheader()
        result_writer.writerows(final_data)


def list_to_dict(data: list):
    """List of dicts to dict of lists"""
    ans = {}
    for dic in data:
        for key, value in dic.items():
            if key in ans:
                ans[key].append(value)
            else:
                ans[key] = [value]
    return ans


def dict_to_list(data: dict):
    """Convert a dict of lists to a list of dicts"""
    ans = []
    keys = list(data.keys())
    values_lists = list(data.values())

    for combination in zip(*values_lists):
        dict_item = dict(zip(keys, combination))
        ans.append(dict_item)

    return ans


def split_file(filename, split_cols: list):
    """split a large csv file on values of one or more columns into multiple files"""
    with open(filename, "r", encoding="utf8") as f:
        csv_reader = csv.DictReader(f)
        data = list(csv_reader)
        header = data[0].keys()

    if any(x not in header for x in split_cols):
        return
    for x in data:
        file_name = ""
        for i in split_cols:
            file_name += str(x[i])
        file_name += ".csv"
        with open(file_name, "a", encoding="utf8") as f:
            file_writer = csv.DictWriter(f, fieldnames=header)
            if f.tell() == 0:
                file_writer.writeheader()
            file_writer.writerow(x)


if __name__ == "__main__":
    print(simple_interest(123456, 23, 0.08))
    print(compound_interest(123456, 23, 0.08))
    print(compound_interest_with_payments(0, 368970.52, 35, 0.10))
    print(savings_calculator(0, 1e8, 35, 0.10))
    files_innerjoin("file1.csv", "file2.csv", common_column=["Name"])
    files_leftouterjoin("file1.csv", "file2.csv", common_column=["Name"])
    files_rightouterjoin("file1.csv", "file2.csv", common_column=["Name"])
    print(list_to_dict([{"name": "a", "age": 21}, {"name": "b", "age": 43}]))
    print(dict_to_list({"name": ["a", "b"], "age": [21, 43]}))
    split_file("file1.csv", ["Name", "Age"])
