import numpy as np
from heapq import nsmallest

scan_area_resolution = 4.74 #µm/px

def get_stage_coord_mm(repers, cent_x, cent_y):
    x_w_stage = np.array([])
    y_w_stage = np.array([])
    for i in range(len(repers)):
        x_w_stage = np.append(x_w_stage, cent_x + (123 - repers[i,0])*scan_area_resolution/1000)
        y_w_stage = np.append(y_w_stage, cent_y - (123 - repers[i,1])*scan_area_resolution/1000)
    return np.column_stack((x_w_stage, y_w_stage))
"""
def calc_min_dist(data_test, data_work):
    l = np.array([])
    for j in range(0, len(data_test)):
        #i_ = np.empty([n_work, 3])
        i_ = np.zeros((len(data_work), 7))
        for i in range(0, len(data_work)):
            i_[i, 0] = ((data_work[i, 0] - data_test[j, 0])**2 + (data_work[i, 1] - data_test[j, 1])**2)**0.5
            i_[i, 1] = data_work[i, 0]
            i_[i, 2] = data_work[i, 1]
            i_[i, 3] = data_work[i, 2]
            i_[i, 4] = data_work[i, 3]
            i_[i, 5] = data_work[i, 4]
            i_[i, 6] = data_work[i, 5]
        a = i_[:,0].argmin()
        k = i_[a,:]
        l = np.append(l, k)
    l = l.reshape(len(data_test), 7)
    #array = np.append(array, l)
    return l
"""
# ДЛЯ РАСЧЕТА ПОГРЕШНОСТЕЙ:
# reper = data_test
def calc_min_dist(reper, data_work):
    l = np.array([])
    i_ = np.zeros((len(data_work), 8))
    for i in range(0, len(data_work)):
        i_[i, 0] = data_work[i, 0]
        i_[i, 1] = ((data_work[i, 5] - reper[5])**2 + (data_work[i, 6] - reper[6])**2)**0.5
        i_[i, 2] = data_work[i, 1]
        i_[i, 3] = data_work[i, 2]
        i_[i, 4] = data_work[i, 3]
        i_[i, 5] = data_work[i, 4]
        i_[i, 6] = data_work[i, 5]
        i_[i, 7] = data_work[i, 6]
    i1, i2, i3 = map((list(i_[:,1])).index, nsmallest(3, list(i_[:,1])))
    a = [i1, i2, i3]
    #a = i_[:,1].argmin()
    k = i_[a,:]
    l = np.append(l, k)
    l = l.reshape(-1, 8)
    #print(l)
    #array = np.append(array, l)
    return l

def get_anatom_test_coord(data_work, data_test):
    anat_x = np.array([])
    anat_y = np.array([])
    for i in range(len(data_test)):
        anat_x = np.append(anat_x, data_work[i, 3] + data_work[i, 5] - data_test[i, 4])
        anat_y = np.append(anat_y, data_work[i, 4] + data_work[i, 6] - data_test[i, 5])
    return np.column_stack((anat_x, anat_y))
"""
def get_absolute_error(data):
    absolute_error_x = np.array([])
    absolute_error_y = np.array([])
    for i in range(len(data)):
        absolute_error_x = np.append(absolute_error_x, abs(data[i, 2] - data[i, 6]))
        absolute_error_y = np.append(absolute_error_y, abs(data[i, 3] - data[i, 7]))
    return np.column_stack((absolute_error_x, absolute_error_y))

"""
# ДЛЯ РАСЧЕТА ПОГРЕШНОСТЕЙ:
def get_absolute_error(data):
    absolute_error_x = np.array([])
    absolute_error_y = np.array([])
    for i in range(len(data)):
        absolute_error_x = np.append(absolute_error_x, abs(data[i, 3] - data[i, 7]))
        absolute_error_y = np.append(absolute_error_y, abs(data[i, 4] - data[i, 8]))
    return np.column_stack((data[:, 0], absolute_error_x, absolute_error_y))

def calc_min_dist_act(ROIs, data_work):
    l = np.array([])
    for j in range(0, len(ROIs)):
        i_ = np.zeros((len(data_work), 7))
        for i in range(0, len(data_work)):
            i_[i, 0] = ((data_work[i, 0] - ROIs[j, 0])**2 + (data_work[i, 1] - ROIs[j, 1])**2)**0.5
            i_[i, 1] = data_work[i, 0]
            i_[i, 2] = data_work[i, 1]
            i_[i, 3] = data_work[i, 2]
            i_[i, 4] = data_work[i, 3]
            i_[i, 5] = data_work[i, 4]
            i_[i, 6] = data_work[i, 5]
        a = i_[:,0].argmin()
        k = i_[a,:]
        l = np.append(l, k)
    l = l.reshape(len(ROIs), 7)
    #array = np.append(array, l)
    return l

def get_anatom_act_coord(data_work, ROIs_stage):
    anat_x = np.array([])
    anat_y = np.array([])
    for i in range(len(ROIs_stage)):
        anat_x = np.append(anat_x, data_work[i, 3] + data_work[i, 5] - ROIs_stage[i, 0])
        anat_y = np.append(anat_y, data_work[i, 4] + data_work[i, 6] - ROIs_stage[i, 1])
    return np.column_stack((anat_x, anat_y))