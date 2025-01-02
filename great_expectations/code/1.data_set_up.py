import great_expectations as gx

context = gx.get_context()

# Define the Data Source's parameters:
# This path is relative to the `base_directory` of the Data Context.
source_folder = "./data"
data_source_name = "iris_data.csv"

# Create the Data Source:
data_source = context.data_sources.add_pandas_filesystem(
    name=data_source_name, base_directory=source_folder
)