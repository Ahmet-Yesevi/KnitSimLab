import pandas as pd
import simulate

#product_list

file_path = 'C:/Users/Ahmet/Desktop/simulation.xlsx'
df = pd.read_excel(file_path)
order_list = df.to_dict(orient='records')
print(order_list)


#machine list

file_path = 'C:/Users/Ahmet/Desktop/machine.xlsx'
df = pd.read_excel(file_path)
machine_list = df.to_dict(orient='records')
print(machine_list)


simulate.printWhatsNext(order_list, machine_list)
simulate.workLoadDetection(machine_list,order_list)
