standard_list = [100, 200, 510, 1e3, 1.5e3, 2e3, 2.7e3, 3.9e3, 5.1e3,
 6.8e3, 8.2e3, 10e3, 15e3, 20e3, 27e3, 39e3, 51e3, 68e3, 82e3, 100e3,
 150e3, 200e3, 510e3, 1e6]

a = float(input("请输入分压比："))
c_i = 0
c_j = 0
result = []
delta = -1
for i in standard_list:
    for j in standard_list:
        delta_ = max(abs(a - float(1.1*i) / float(1.1*i + 0.9*j)), abs(a - float(0.9*i) / float(0.9*i + 1.1*j)))
        result.append({"r1": i, "r2": j, "delta": delta_})
        if (delta < 0 or delta_ < delta):
            delta = delta_
            c_i = i
            c_j = j

result = sorted(result, key=lambda x: x["delta"])
print ("最佳设计结果为 %s / (%s + %s) = %s  偏差: %s" % (c_i, c_i, c_j, c_i / (c_i + c_j), delta))
print ("前5设计结果：")
for i in range(0, 5):
    item = result[i]
    print ("r1: %10.1f\tr2: %10.1f\tdelta: %2.5f" % (item["r1"], item["r2"], item["delta"]))
