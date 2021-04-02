Programs for the estimation of calculation of stereotaxic coordinates errors for different methods with permutations of landmarks.
SLLM - Locally linear method based on a displacement from the nearest reference landmark
Q - Globally quadratic method based on the construction of a quadratic function of coordinate conversion for the entire dorsal surface
QR - Globally quadratic method with regularization. The approach is identical to the previous one but supplemented with L2 regularization of quadratic coefficients
GLM - Globally linear method
LLM - Locally linear method

You will need: Python 3, Jupyter Notebook (Jupyter Lab); libraries: pandas, NumPy, openpyxl, itertools, xlrd 

Each of the programs will work only if the input file has the same columns as file 'sample.xlsx'.
Columns:
Centers_region - name of the scan area where the landmark is located (possible values: 'a', 'b', 'c', 'd', 'e', 'f', 'g')
Center_x, Center_y - x and y coordinates of the center of this scan area in a stage coordinate system (in mm)
id_point - ID of this landmark (should be set based on your own considerations, values are accepted from 0 to 10)
X_work_st_px, Y_work_st_px - x and y pixel coordinates of the landmark on the 246 x 246 image obtained after processing (stabilization)
X_work_an, Y_work_an - x and y stereotaxic coordinates of the landmark relative to the bregma (in mm)
