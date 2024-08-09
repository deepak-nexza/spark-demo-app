from pyspark import SparkConf

def get_config(env):
    config = configparser.ConfigParser()
    config.read('conf/sbdl.conf')
    conf = {}
    for (key, value) in config.items(env):
        config[key] = value
    return conf

def get_spark_config(env):
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("conf/spark.conf")

    for (key, val) in config.items(env):
        spark_conf.set(key, val)

    return spark_conf

def get_data_filter(env, data_filter):
    config = get_config(env)
    return "true" if config[data_filter] == "" else config[data_filter]