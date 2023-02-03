import os
import shutil
from context import jupyter_wrapper, test_dir
import time

# Define the path to the JupyterLab configuration directory
config_dir = os.path.join(test_dir, 'config_dir_test')

# Define the path to the JupyterLab configuration file in TOML format
config_file = os.path.join(test_dir, 'jupyter_lab_config.toml')

# Create an instance of the JupyterLabService class and pass in the JupyterLab configuration file path
s = jupyter_wrapper.JupyterLabService(config_dir, config_file, no_browser=True)

# Start the JupyterLab instance with custom configurations
s.start()

# Wait for 15 seconds to allow the JupyterLab instance to start
time.sleep(15)

# Stop the JupyterLab instance
s.stop()

# Clean up the JupyterLab configuration directory
shutil.rmtree(config_dir)
