from matplotlib import pyplot as plt

my_dic={"Cities":["ahem","surat","rajkot","amreli"],"Cases":[10,20,30,40]}

keys=list(*my_dic)


for i in my_dic.keys():
    keys.append(i)
print(keys)

plt.bar(my_dic["Cities"],my_dic["Cases"])
plt.xlabel(keys[0])
plt.ylabel(keys[1])
plt.show()



