#-------------------------------------------------------------------------
# AUTHOR: Michael Melkonian
# FILENAME: Assignment2_3
# SPECIFICATION: Find 1NN given the data set
# FOR: CS 4210- Assignment #2
# TIME SPENT: 3 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
counter=0
#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)


#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    # X =
    X = []
    for j in range(len(db)): 
        if i != j: # in order to remove the instance that will be used for testing 
            subX = [] # we need to instantiate an array in order to house each x and y value given the instance
            for k in range(len(db[j])-1): #db[j] - 1 in order to only focus on attributes and avoid class
                subX.append(float(db[j][k])) #converting features to float
            X.append(subX)
   # print(X)
    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    # Y =
    Y=[]
    classSign = {"+":1,"-":2} #Assigning numerical values to class values

    for j in range(len(db)):
        if i !=j: #while we are not on selected instance in table
            Y.append(float(classSign[db[j][2]]))   #appending class values

   # print(Y)
    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    #testSample =
    testSample = [] #instantiate testSample array
    for j in range(len(instance) - 1):
        testSample.append(float(instance[j])-1) #storing test sample distance values
    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([testSample])[0]
    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
   
    if class_predicted != classSign[instance[len(instance)-1]]: #if the classSign is not the same as the predicted class then we have an error
        counter = counter + 1 #error counter
    error = (counter / len(db)) * 100 # error calculation


#print the error rate
#--> add your Python code here
print("The error observed with 1NN is: ", error, "%")





