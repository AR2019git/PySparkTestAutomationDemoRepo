{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww28600\viewh15820\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Filename: test_addcol.py\
import pytest\
from pyspark.sql import SparkSession\
from dabdemo.addcol import *\
\
class TestAppendCol(object):\
\
  def test_with_status(self):\
    spark = SparkSession.builder.getOrCreate()\
\
    source_data = [\
      ("paula", "white", "paula.white@example.com"),\
      ("john", "baer", "john.baer@example.com")\
    ]\
\
    source_df = spark.createDataFrame(\
      source_data,\
      ["first_name", "last_name", "email"]\
    )\
\
    actual_df = with_status(source_df)\
\
    expected_data = [\
      ("paula", "white", "paula.white@example.com", "checked"),\
      ("john", "baer", "john.baer@example.com", "checked")\
    ]\
    expected_df = spark.createDataFrame(\
      expected_data,\
      ["first_name", "last_name", "email", "status"]\
    )\
\
    assert(expected_df.collect() == actual_df.collect())}