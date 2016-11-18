from DataExplorationEngine import add, eda, vis


# load data 
# datatypes = {
# 	'floats' : ['SepalLength','SepalWidth','PetalLength','PetalWidth']
# }
# add.load_csv("data/iris.csv", "irisdata", datatypes)

# perform EDA 
key = "SepalLength"
group_key = "Species"
uni = eda.univariate_analysis(key, group_key, "irisdata")
vis.create_univariate_table(uni, key)

key1 = "SepalLength"
key2 = "PetalLength"
group_key = "SepalWidth"
bi = eda.bivariate_analysis(key1, key2, group_key, "irisdata")
vis.createBiTable(bi, key1, key2)