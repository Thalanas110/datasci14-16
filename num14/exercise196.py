sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)
#sorting original array by second row
sortArrayByRow = sampleArray[:,sampleArray[1,:].argsort()]
print("Sorting Original array by secoond row")
print(sortArrayByRow)
print("Sorting Original array by second column")
sortArrayByColumn = sampleArray[sampleArray[:,1].argsort()]
print(sortArrayByColumn)
