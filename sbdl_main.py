import sys
from lib import Utils

if __name__ == "__main__":

    spark = Utils.get_spark_session('LOCAL')

    print("Finsihed creating spark session")

