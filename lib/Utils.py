import configparser
from pyspark import SparkConf
#
# def get_spark_app_config(env):
#
#     spark_conf = SparkConf()
#     print("I am here")
#     config = configparser.ConfigParser()
#     config.read("spark.conf")
#
#     for (key, val) in config.items("SPARK_APP_CONFIGS"):
#         print(val)
#         spark_conf.set(key, val)
#     return spark_conf
#
# def load_survay_data(spark, data_file):
#
#     return spark.read.format("csv") \
#         .option('header', 'true') \
#         .option('inferSchema', 'true') \
#         .load(data_file)
#
# def count_by_survey(spark_df):
#
#     return spark_df \
#             .where("Box > 1") \
#             .select('City', 'Location', 'RowID') \
#             .groupBy("Unit ID")\
#             .count()
#
#
# #
# from pyspark.sql import SparkSession
#
# def get_spark_session(env):
#     if env == "LOCAL":
#         print("inside the local env")
#         return SparkSession.builder \
#                 .master("local[2]") \
#                 .enableHiveSupport() \
#                 .getOrCreate()
#     else:
#         return 'dddddddddd'
#
#
#



#
from pyspark.sql import SparkSession

def get_spark_session(env):
    if env == "LOCAL":
        print("inside the local env")
        return SparkSession.builder \
                .master("local[2]") \
                .enableHiveSupport() \
                .getOrCreate()
    else:
        return 'dddddddddd'



