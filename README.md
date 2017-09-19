The program is based on hadoop 1.x and pySpark, make sure the environment is configured for the program. 

1.	How to execute the source code.

1.1  Models for all the coverage option were saved separately  in 7 python files, compressed in the ‘final code’ package. Put the files under the spark folder.

1.2 Change the path in the python files: 
  "df=sqlContext.read.format("com.databricks.spark.csv").options(header='true',inferschema='true').load('your file location')
  In order to execute the file accurately, it should be changed to correct absolute path for csv file.

1.3 Use the following spark-submit code to run the python file:
  ./bin/spark-submit --packages com.databricks:spark-csv_2.10:1.3.0 --master local[3] [filename](e.g. a.py) [file:/the local path of the file.]
  Each file is the decision tree code for A—G option.

1.4 After execute .py file, the results will appear and pay attention to the accuracy.

1.5 Exit
