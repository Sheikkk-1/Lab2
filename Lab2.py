def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    input_data = input()  
    temp_list = input_data.split(",")  
    return [float(i) for i in temp_list]  



def calc_average(temp_list):
    return sum(temp_list) / len(temp_list)


def find_min_max(temp_list):
    return [min(temp_list), max(temp_list)]  


def sort_temperature(temp_list):
    return sorted(temp_list)


def calc_median_temperature(temp_list):
    temp_list.sort()
    mid = len(temp_list) // 2
    if len(temp_list) % 2 == 0:
        return (temp_list[mid - 1] + temp_list[mid]) / 2
    return temp_list[mid]


def main():
    display_main_menu()
    temp_list = get_user_input()
    
    avg_temp = calc_average(temp_list)
    print("Average Temperature:", avg_temp)

    min_max_temp = find_min_max(temp_list)
    print(f"Min & Max Temperature: {min_max_temp[0]} and {min_max_temp[1]}")

    sorted_temp = sort_temperature(temp_list)
    print("Sorted Temperature List:", sorted_temp)

    median_temp = calc_median_temperature(temp_list)
    print("Median Temperature Value:", median_temp)


if __name__ == "__main__":
    main()
