# Databricks notebook source
pip install pytest

# COMMAND ----------

username = dbutils.notebook.entry_point.getDbutils(
).notebook().getContext().userName().get()

# COMMAND ----------

abs_path = f"/Repos/{username}/cicd_with_databricks_GH/src/main/tests"

# COMMAND ----------

num_of_rows = int(dbutils.widgets.get("num_rows"))

# COMMAND ----------

env = dbutils.widgets.get("env")

# COMMAND ----------

dbutils.notebook.run(abs_path+"/cleanup_tests", 300, {"env":env})

# COMMAND ----------

dbutils.notebook.run(abs_path + "/../python/setup/initiate_setup", 300, {"num_rows":num_of_rows, "env":env})

# COMMAND ----------

dbutils.notebook.run(abs_path+"/bronze/test_load_data_into_bronze", 300, {"env":env})

# COMMAND ----------

dbutils.notebook.run(abs_path+"/silver/test_transform_to_scd2", 300, {"env":env})

# COMMAND ----------

dbutils.notebook.run(abs_path+"/silver/test_standardise_retail_dataset", 300, {"env":env})

# COMMAND ----------

dbutils.notebook.run(abs_path+"/gold/test_gold_layer_etl", 300, {"env":env})

# COMMAND ----------

dbutils.notebook.run(abs_path+"/cleanup_tests", 300, {"env":env})
