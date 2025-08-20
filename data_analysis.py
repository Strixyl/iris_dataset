from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data

min_flower_length = float(input("Enter the minimum lennght of flower: "))
max_flower_length = float(input("Enter the maximum length of flower: "))

filtered = list(filter(lambda row: min_flower_length <= row[0] <= max_flower_length, data))
columns = list (zip(*filtered)) if filtered else [[], [], [], []]

print("Filtered Sepal Widths:", columns[1])

def avg(col):
    return sum(col) / len(col) if col else 0

avg_flower_length = avg(columns[0])
avg_flower_width = avg(columns[1])
avg_petal_length = avg(columns[2])
avg_petal_width = avg(columns[3])

print("Average Flower Lengthl", avg_flower_length)
print("Average Flower Lengthl", avg_flower_width)
print("Average Flower Lengthl", avg_petal_length)
print("Average Flower Lengthl", avg_petal_width)


from sklearn.datasets import load_wine

wine = load_wine()
x, y = wine.data, wine.target






    



