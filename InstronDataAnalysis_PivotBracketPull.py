def labeled_values_to_labeled_list(labeled_value_list, no_char_in_lable_to_compare):
    # INPUT: [[["label 1"][data1-1-1,data1-1-2,data1-1-n],[data1-2-1,data1-2-2,data1-2-n],[["label 2"][data2-1-1,data2-1-2,data2-1-n],[data2-2-1,data2-2-2,data2-2-n]]],
    #           Number of characters in lable to compare
    # OUTPUT: ["label 1",[dataX-1, dataY-1, dataZ-1],[dataX-2, dataY-2, dataZ-2]], ["lable 2", [dataA-1, dataB-1, dataC-1],[dataA-2, dataB-2, dataC-2]]
    #               - INTO LIST OF DIFFERENT SAMPLE TYPES FOR DOING STATISTICS ON
    labeled_list = [[labeled_value_list[0][0][no_char_in_lable_to_compare-1],[labeled_value_list[0][1]],[labeled_value_list[0][2]]]] # seed list with firt item
#    print(labeled_list)
    for list_member_id in range(1,len(labeled_value_list)):         # iterate through original list starting with 2nd memver
        match_found = False
        for saved_labeled_list_id in range(0,len(labeled_list)):    # iterate through already saved lists to look for match
#            print("list_member_id: ", list_member_id, ", saved_labeled_list_id: ", saved_labeled_list_id)
#            print(labeled_value_list[list_member_id][0][0:9], labeled_list[saved_labeled_list_id][0])
#            print(labeled_list,"\n\n")
            if labeled_value_list[list_member_id][0][no_char_in_lable_to_compare-1] == labeled_list[saved_labeled_list_id][0]:            # check for match
                labeled_list[saved_labeled_list_id][1].append(labeled_value_list[list_member_id][1])    # if match, add first member
                labeled_list[saved_labeled_list_id][2].append(labeled_value_list[list_member_id][2])    # if match, add second member
                match_found = True
                break                                                                                   # if match, exit inside for loop
        if match_found == False:
            labeled_list.append([labeled_value_list[list_member_id][0][no_char_in_lable_to_compare-1],[labeled_value_list[list_member_id][1]],[labeled_value_list[list_member_id][2]]])
    return labeled_list       


def max_in_list(list_of_numbers):
    maximum_value =  list_of_numbers[0]
    for single_number in list_of_numbers:
        maximum_value = max(single_number, maximum_value)
    return maximum_value


def interpolate_linear(target_value, below_target, above_target, below_result, above_result):      #Return linerarly interpolated value
    return ((target_value - below_target) / (above_target - below_target) * (above_result - below_result) + below_result)


def t_test_diff_len_unpaired(first_list, second_list):      #Return t-test statistic of sample of list of numbers
    import statistics
    from math import sqrt
    return (abs(statistics.mean(first_list) - statistics.mean(second_list)))/sqrt((statistics.variance(first_list)/len(first_list))+(statistics.variance(second_list)/len(second_list)))


def t_test_DOF(first_list, second_list):
    import statistics
    s1_div_n1 = statistics.variance(first_list)/len(first_list)
    s2_div_n2 = statistics.variance(second_list)/len(second_list)
    return int(((s1_div_n1+s2_div_n2)**2) / (((s1_div_n1**2)/(len(first_list)-1)) + ((s2_div_n2**2)/(len(second_list)-1))))


def t_test_critical_values_1_tail_05_alpha(first_list, second_list):      #Return t-test critical values for alpha=0.05, 1-tail, for hypothesis testing
    dof = t_test_DOF(first_list, second_list)
    t_threshold_1_tail_05_alpha = [0,6.3138,2.92,2.3534,2.1319,2.015,1.9432,1.8946,1.8595,1.8331,1.8124,
                                   1.7959,1.7823,1.7709,1.7613,1.753,1.7459,1.7396,1.7341,1.7291,1.7247,
                                   1.7207,1.7172,1.7139,1.7109,1.7081,1.7056,1.7033,1.7011,1.6991,1.6973,
                                   1.6955,1.6939,1.6924,1.6909,1.6896,1.6883,1.6871,1.6859,1.6849,1.6839,
                                   1.6829,1.682,1.6811,1.6802,1.6794,1.6787,1.6779,1.6772,1.6766,1.6759,
                                   1.6753,1.6747,1.6741,1.6736,1.673,1.6725,1.672,1.6715,1.6711,1.6706,
                                   1.6702,1.6698,1.6694,1.669,1.6686,1.6683,1.6679,1.6676,1.6673,1.6669,
                                   1.6666,1.6663,1.666,1.6657,1.6654,1.6652,1.6649,1.6646,1.6644,1.6641,
                                   1.6639,1.6636,1.6634,1.6632,1.663,1.6628,1.6626,1.6623,1.6622,1.662,
                                   1.6618,1.6616,1.6614,1.6612,1.661,1.6609,1.6607,1.6606,1.6604,1.6602,
                                   1.6601,1.6599,1.6598,1.6596,1.6595,1.6593,1.6592,1.6591,1.6589,1.6588,
                                   1.6587,1.6586,1.6585,1.6583,1.6582,1.6581,1.658,1.6579,1.6578,1.6577,
                                   1.6575,1.6574,1.6573,1.6572,1.6571,1.657,1.657,1.6568,1.6568,1.6567,
                                   1.6566,1.6565,1.6564,1.6563,1.6562,1.6561,1.6561,1.656,1.6559,1.6558,
                                   1.6557,1.6557,1.6556,1.6555,1.6554,1.6554,1.6553,1.6552,1.6551,1.6551,
                                   1.655,1.6549,1.6549,1.6548,1.6547,1.6547,1.6546,1.6546,1.6545,1.6544,
                                   1.6544,1.6543,1.6543,1.6542,1.6542,1.6541,1.654,1.654,1.6539,1.6539,
                                   1.6538,1.6537,1.6537,1.6537,1.6536,1.6536,1.6535,1.6535,1.6534,1.6534,
                                   1.6533,1.6533,1.6532,1.6532,1.6531,1.6531,1.6531,1.653,1.6529,1.6529,
                                   1.6529,1.6528,1.6528,1.6528,1.6527,1.6527,1.6526,1.6526,1.6525,1.6525]
    return t_threshold_1_tail_05_alpha[dof], dof


def find_max_in_range(x_list, y_list, y1, x_range):      #Return max 'y' in range from y1 to x(y1)+x_range
    for index in range(len(x_list)):
        if y_list[index] > y1:
            index_start = index - 1
            break
    y_max_in_range = y_list[index_start]
    x1 = x_list[index_start]
    for index in range(index_start+1, len(x_list)):
        if x_list[index] > x1 + x_range:
            break
        y_max_in_range = max(y_list[index], y_max_in_range)
    return y_max_in_range


def output_comparison_results(comparison_type, type1, list1, type2, list2):
    import statistics
    mean1 = statistics.mean(list1)
    stdev1 = statistics.stdev(list1)
    mean2 = statistics.mean(list2)
    stdev2 = statistics.stdev(list2)
    t_test_result = t_test_diff_len_unpaired(list1, list2)
    t_test_threshold, dof = t_test_critical_values_1_tail_05_alpha(list1, list2)
    
    print("\n")
    print("{:>20}".format("Comparison Type: "), comparison_type)
    print("{:>20}".format("Types: "), "{:>15}".format(type1),"{:>15}".format(type2))
    print("{:>20}".format("Means: "), "{:>15}".format(format(mean1, ",.2f")), "{:>15}".format(format(mean2, ",.2f")))
    print("{:>20}".format("Stand. Dev.: "), "{:>15}".format(format(stdev1, ",.2f")), "{:>15}".format(format(stdev2, ",.2f")))
    print("{:>20}".format("Deg. of Free.: "), "{:>15}".format(dof))
    print("{:>20}".format("t-test statistic: "), "{:>15}".format(format(t_test_result, ",.2f")))
    print("{:>20}".format("t-test thresh.: "), "{:>15}".format(format(t_test_threshold, ",.2f")))
    if (t_test_result > t_test_threshold):
        print("Means are statistically significantly different for alpha=0.05")
    else:
        print("Means are NOT statistically significantly different for alpha=0.05")        
    return


import csv
import statistics

with open("15-0257-Pull with PreLoad_6.csv") as instron_file:
    reader = csv.reader(instron_file)
    data_input = []
    for rows in reader:
        data_input.append(rows)
    sample_start_row=[]
    for row_count in range(len(data_input)):                                                # find start of each specimin data
        if data_input[row_count][1] == "BeginSpecimen":
            sample_start_row.append(row_count)
        else:
            next
    for dataStartOffset in range(1,100):
        if data_input[sample_start_row[0]+dataStartOffset][2] == "BeginData":
            break
    dataStartOffset += 3
    for nameOffset in range(1,100):
        if data_input[sample_start_row[0]+nameOffset][2] == "SpecimanName":
            break
    sample_data=[]
    no_samples = len(sample_start_row)
    for sample_no in range(no_samples):                                                     # add sample name to first element of array empty lists for loads, deflections
        if data_input[sample_start_row[sample_no]+nameOffset][2] == "SpecimanName":
            sample_data.append([data_input[sample_start_row[sample_no]+nameOffset][3][2:4],[],[]])
        else:
            print("ut-oh")
    start_data_row = []
    end_data_row = []
    data_points = []
    for sample_no in range(len(sample_start_row)):                                          # count data points for each sample, add data to sample_data
        start_data_row.append(sample_start_row[sample_no] + 22)
        end_data_row.append(start_data_row[sample_no] + 1)                                  # assume at least two lines of data
        while data_input[end_data_row[sample_no]+1][2] != "EndData":                        # count number of data lines for each sample
            end_data_row[sample_no] = end_data_row[sample_no] + 1
        data_points.append(end_data_row[sample_no]+ 1 - start_data_row[sample_no])
        for data_point_row in range(start_data_row[sample_no],end_data_row[sample_no]+1):   # add Force and Deflection to 2nd, 3rd element of data_input
            sample_data[sample_no][1].append(float(data_input[data_point_row][3]))
            sample_data[sample_no][2].append(float(data_input[data_point_row][5]))
    instron_file.close()
del data_input

# Output data files to CSV more easily inputed to Excel
"""
with open("temp_output.txt", "w") as OutputFile:
    writer = csv.writer(OutputFile, delimiter=",")
    listToWrite = []
    
    writer.writerow(
"""

# Start Data Analysis

# Find Max Load, Deflection for each sample

sample_max_load = []
for sample_no in range(no_samples):
    sample_max_load.append([sample_data[sample_no][0],sample_data[0][1][0],sample_data[0][2][0]])   # Seed max matrix with intial data point
    for data_point in range(data_points[sample_no]):
        if sample_data[sample_no][1][data_point] > sample_max_load[sample_no][1]:
            sample_max_load[sample_no][1] = sample_data[sample_no][1][data_point]
            sample_max_load[sample_no][2] = sample_data[sample_no][2][data_point]
no_char_in_lable_to_compare = 1
max_load_lists = labeled_values_to_labeled_list(sample_max_load, no_char_in_lable_to_compare)
print("\n")
for sample_id in range(len(max_load_lists)):
    print("Sample ID, ", max_load_lists[sample_id][0], "Overall Peak Loads")
    for sample_no in range(len(max_load_lists[sample_id][1])):
        print(sample_no+1, ", ", max_load_lists[sample_id][1][sample_no])
    print("\n")

output_comparison_results("Max Load", max_load_lists[0][0], max_load_lists[0][1], max_load_lists[1][0], max_load_lists[1][1])


# COMPARE FIRST PEAK with 5% DROP after load > 10,000 N
sample_first_peak_load = []
for sample_no in range(no_samples):
    sample_first_peak_load.append([sample_data[sample_no][0],sample_data[0][1][0],sample_data[0][2][0]])   # Seed first peak matrix with intial data point
    for data_point in range(data_points[sample_no]):
        if sample_data[sample_no][1][data_point] < 10000:                                  #start looking for first peak after 350 N
            continue
        if sample_data[sample_no][1][data_point] > sample_first_peak_load[sample_no][1]:
            sample_first_peak_load[sample_no][1] = sample_data[sample_no][1][data_point]
            sample_first_peak_load[sample_no][2] = sample_data[sample_no][2][data_point]
        elif sample_data[sample_no][1][data_point] < (1-0.05) * sample_first_peak_load[sample_no][1]: #define first peak after 5% drop
            break
no_char_in_lable_to_compare = 1
first_peak_load_lists = labeled_values_to_labeled_list(sample_first_peak_load, no_char_in_lable_to_compare)

print("\n\n\n")
for sample_id in range(len(first_peak_load_lists)):
    print("Sample ID, ", first_peak_load_lists[sample_id][0], "First Peak Loads")
    for sample_no in range(len(first_peak_load_lists[sample_id][1])):
        print(sample_no+1, "{:>15}".format(format(first_peak_load_lists[sample_id][1][sample_no], ",.2f")))
    print("\n")

output_comparison_results("First Peak Load", first_peak_load_lists[0][0], first_peak_load_lists[0][1], first_peak_load_lists[1][0], first_peak_load_lists[1][1])


# COMPARE DEFLECTION at LOAD X N past LOAD Y N

#for start_delay_load in range(2000, 4000, 2000):

start_delay_load = 2000
saved_delta_load_points = []
for load_eval in range(4000, 14000, 2000):
    sample_load = []
    for sample_no in range(no_samples):
        for data_point in range(data_points[sample_no]):    #first find data point at starting load (Y)
            if sample_data[sample_no][1][data_point] >= start_delay_load:
                starting_data_point = data_point
                break
            else:
                continue
            print("Ut-oh, starting data point not found")
        for data_point in range(data_points[sample_no]):
            if sample_data[sample_no][1][data_point] >= load_eval:
                sample_load.append([sample_data[sample_no][0],sample_data[sample_no][1][data_point]-sample_data[sample_no][1][starting_data_point],sample_data[sample_no][2][data_point]-sample_data[sample_no][2][starting_data_point]])
                break
    no_char_in_lable_to_compare = 1
    load_lists = labeled_values_to_labeled_list(sample_load, no_char_in_lable_to_compare)
    saved_delta_load_points.append([load_eval-start_delay_load, load_lists])
    list_lable = "Start Delay: " + str(start_delay_load) + " N, Load Eval. Point: " + str(load_eval) + " mm"
    output_comparison_results(list_lable, load_lists[0][0], load_lists[0][2], load_lists[1][0], load_lists[1][2])

print("\n\nSample ID, ", end='')
for load_eval in range(len(saved_delta_load_points)):
    print(saved_delta_load_points[load_eval][0], ", ", end='')
print()
for sample_type in range(len(saved_delta_load_points[0][1])):
    for sample_no in range(len(saved_delta_load_points[0][1][0][1])):
        print(saved_delta_load_points[0][1][sample_type][0], sample_no+1, ", ", end='')
        for load_eval in range(len(saved_delta_load_points)):
            print("{:>5}".format(format(saved_delta_load_points[load_eval][1][sample_type][2][sample_no], ",.2f")), ", ", end='')
        print()

"""
# COMPARE LOAD X mm past LOAD Y N

for start_delay in range(0, 1050, 50):
    for distance_eval in range(1, 11, 1):
        sample_load = []
        for sample_no in range(no_samples):
            sample_load.append([sample_data[sample_no][0],0,0])  # Seed matrix with [data label, 0, 0]
            started_check = 0                                    # set flag to ignore distance eval until start delay exceeded
            for data_point in range(data_points[sample_no]):
#                print("sample_data[sample_no][1][data_point]: ",sample_data[sample_no][1][data_point],
#                      "start_delay: ", start_delay, "started_check: ", started_check,
#                      "sample_data[sample_no][2][data_point]: ", sample_data[sample_no][2][data_point],
#                      "sample_load[sample_no][2]: ", sample_load[sample_no][2], "distance_eval: ", distance_eval)
                if sample_data[sample_no][1][data_point] < start_delay:
                    continue
                if started_check == 0:
                    started_check = 1
                    initial_deflection = sample_data[sample_no][2][data_point]
                    end_deflection = initial_deflection + distance_eval
                if started_check == 1 and sample_data[sample_no][2][data_point] > end_deflection:
                    break
                if sample_data[sample_no][1][data_point] > sample_load[sample_no][1]:
                    sample_load[sample_no][1] = sample_data[sample_no][1][data_point]
                    sample_load[sample_no][2] = sample_data[sample_no][2][data_point]
        no_char_in_lable_to_compare = 9
#        print("start_delay: ", start_delay, "distance_eval: " N, distance_eval, "sample_load: ", sample_load, " mm")
        load_lists = labeled_values_to_labeled_list(sample_load, no_char_in_lable_to_compare)
        list_lable = "Start Delay: " + str(start_delay) + " N, Distance Eval. Range: " + str(distance_eval) + " mm"
        output_comparison_results(list_lable, load_lists[0][0], load_lists[0][1], load_lists[1][0], load_lists[1][1])
"""
