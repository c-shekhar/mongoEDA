from DataExplorationEngine import add, eda, vis


# load data 
# datatypes = {
# 	'floats' : ['SepalLength','SepalWidth','PetalLength','PetalWidth']
# }
# add.load_csv("data/iris.csv", "irisdata", datatypes)

# perform EDA 
key = "Species" #key can be any variable
# print eda.identify_variable_type('SepalLength','irisdata')
# print eda.identify_variable_type('SepalWidth','irisdata')
# print eda.identify_variable_type('PetalLength','irisdata')
# print eda.identify_variable_type('PetalWidth','irisdata')
# print eda.identify_variable_type('Species','irisdata')
# uni = eda.univariate_analysis(key,"irisdata", central_tendencies = False)
# vis.create_univariate_table(uni, key)

key1 = "SepalLength"
key2 = "SepalWidth"
group_key = "Species"
bi = eda.bivariate_analysis(key1, key2, "irisdata")
# vis.createBiTable(bi, key1, key2)