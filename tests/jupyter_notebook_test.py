import os
import shutil
from context import jupyter_wrapper, test_dir
import time

# Define the path to the Jupyter Notebook configuration directory
config_dir = os.path.join(test_dir, 'config_dir_test')

# Define the path to the Jupyter Notebook configuration file in TOML format
config_file = os.path.join(test_dir, 'jupyter_notebook_config.toml')

# Create an instance of the JupyterNotebookService class and pass in the Jupyter Notebook configuration file path
s = jupyter_wrapper.JupyterLabService(config_dir, config_file, no_browser=True)

# Start the Jupyter Notebook instance with custom configurations
s.start()

# Wait for 15 seconds to allow the Jupyter Notebook instance to start
time.sleep(15)

# Stop the Jupyter Notebook instance
s.stop()

# Clean up the Jupyter Notebook configuration directory
shutil.rmtree(config_dir)
