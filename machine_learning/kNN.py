#python KNN
import from numpy *
def classfiy (inputX, trainData, labels, k):
	trainDataSize = trainData.shape[0]
	diffMat = tile(inputX, (trainDataSize, 1)) - trainData #横向重复inputX trainDataSize次，每次一行，以形成跟trainData一样行列的矩阵
	sqrtDiffMat = diffMat ** 2
	sqDistances = sqrtDiffMat.sum(axis = 1) #axis = 1表示计算矩阵每一行的和
	distances = sqDistances ** 0.5
	sortedDistIndex = distances.argsort() #根据值排序并得到排序后各元素的索引 比如 [3, 1, 2]得到 [0, 2, 1]
	classCount = {}
	for i in range (k):
		votelLabel = labels[sortedDistIndex[i]]
		classCount[votelLabel] = classCount.get(votelLabel, 0) + 1 #统计距离排名前k的类别对应的数量
	sortedClassCount = sorted(classCount.iteritems(),
		key = operator.itemgetter(1), reverse = True) #根据数量排序类别
	return sortedClassCount[0][0]  #输出排名第一的类别作为结果