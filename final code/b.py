import pandas as pd
from pyspark import SparkContext,SparkConf
conf=(SparkConf().setMaster('local'))
sc=SparkContext(conf = conf)
from pyspark.sql import *
sqlContext=SQLContext(sc)
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
from pyspark.mllib.evaluation import MulticlassMetrics




df=sqlContext.read.format('com.databricks.spark.csv').options(header='true',inferschema='true').load('file:/Users/lanyan/Desktop/finaldata.csv')
dfb=df.drop('customer_ID').drop('shopping_pt').drop('time')\
  .drop('day').drop('state').drop('location')\
  .drop('age_oldest').drop('age_youngest')\
  .drop('A').drop('C').drop('D').drop('E').drop('F').drop('G')\
  .drop('plan').drop('hour')

pd.DataFrame(dfb.take(5), columns=dfb.columns).transpose()

def labelData(data):
    return data.map(lambda row: LabeledPoint(row[9],[row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[10], row[11], row[12], row[13], row[14], row[15]]))

trainData,testData=labelData(dfb).randomSplit([0.8,0.2])

model=DecisionTree.trainClassifier(trainData,numClasses=2,maxDepth=5,categoricalFeaturesInfo={},impurity='gini',maxBins=32)

print model.toDebugString()

def getPredictionLabels(model,testData):
  predictions=model.predict(testData.map(lambda r: r.features))
  return predictions.zip(testData.map(lambda r: r.label))

def printMetrics(pred_and_label):
  metrics=MulticlassMetrics(pred_and_label)
  print 'Preicision of 0',metrics.precision(0)
  print 'Preicision of 1',metrics.precision(1)
  print 'Recall of 0',metrics.recall(0)
  print 'Recall of 1',metrics.recall(1)
  print 'Confusion Matrix\n',metrics.confusionMatrix().toArray()

pred_and_label=getPredictionLabels(model,testData)
printMetrics(pred_and_label)
