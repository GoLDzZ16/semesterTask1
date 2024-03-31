f = open("D:\\private\\for_py.txt")

input_data = []
cnt_iterations = []
time_alg = []

for i in range(0,50):
    t = 0
    while t != 1:
        s = f.readline().split(" ")
        input_data.append(int(s[-1].strip()))
        s = f.readline().split(" ")
        cnt_iterations.append(int(s[-1].strip()))
        s = f.readline().split(" ")
        time_alg.append(int(s[-1].strip()))
        f.readline()
        t = 1



print("входные данные: ", len(input_data), input_data)
print("количество итераций: ", len(cnt_iterations), cnt_iterations)
print("время выполнения: ", len(time_alg), time_alg)