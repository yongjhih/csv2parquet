# -*- coding: future_fstrings -*-

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Union, NewType, Iterable, TypeVar
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import os


if __name__ == "__main__":
    spark = SQLContext(SparkContext(appName="CSV2Parquet"))

    df = spark.read.csv(f"{os.getcwd()}/input.csv", header=True)
    df.write.parquet(f"{os.getcwd()}/input.parquet")
