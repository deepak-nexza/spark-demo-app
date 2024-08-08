spark-submit --master yarn --deploy-mode cluster \
--py-files sbdl_lib.zip  \
--files conf/sbdl.conf/spark.conf \
sbdl_main.py qa 2022--8-09