import tomli
import os
from pathlib import Path
from subprocess import Popen, PIPE
import signal


# Generates a string containing python code that configures Jupyter
def generate_config_py(config_dict: dict) -> str:
    config_py = 'c = get_config()\n'
    # Iterate over all keys and subkeys in the config dictionary
    for key, value in config_dict.items():
        for subkey, subvalue in value.items():
            # Add a line to the string with the config setting
            config_py += f"c.{key}.{subkey} = {repr(subvalue)}\n"
    return config_py


# Runs Jupyter lab or Jupyter notebook with a custom config
def start_jupyter(lab_or_notebook: str, config_dir: str,
             config_file: (None | str) = None, no_browser: bool=True) -> Popen:
    # Creates the config directory if it doesn't exist
    Path(config_dir).mkdir(parents=True, exist_ok=True)
    # Set the default config file name if not provided
    if config_file is None:
        config_file = os.path.join(
            config_dir, f'jupyter_{lab_or_notebook}_config.toml'
        )
    # Load the config file
    with open(config_file, 'rb') as f:
        config_dict = tomli.load(f)
    # Generate the python config file
    config_py_file = os.path.join(
        config_dir, f'jupyter_{lab_or_notebook}_config.py'
    )
    config_py = generate_config_py(config_dict)
    # Write the python config to file
    with open(config_py_file, 'w') as f:
        f.write(config_py)
    # Set the JUPYTER_CONFIG_DIR environment variable
    jupyter_env = os.environ.copy()
    jupyter_env['JUPYTER_CONFIG_DIR'] = config_dir
    # Start jupyter with the custom config
    args = ["jupyter", lab_or_notebook, "--config", config_py_file]
    if no_browser:
        args.append("--no-browser")
    process = Popen(args, env=jupyter_env)
    return process


def start_jupyter_lab(config_dir: str, config_file: (None | str) = None, no_browser: bool=True) -> Popen:
    return start_jupyter('lab', config_dir, config_file, no_browser)


def start_jupyter_notebook(config_dir: str, config_file: (None | str) = None, no_browser: bool=True) -> Popen:
    return start_jupyter('notebook', config_dir, config_file, no_browser)


class JupyterService:
    def __init__(self, lab_or_notebook: str, config_dir: str, config_path: (None | str) = None, no_browser: bool=True):
        self.lab_or_notebook = lab_or_notebook
        # Store the path to the configuration dir
        self.config_dir = config_dir
        # Store the path to the configuration file
        self.config_path = config_path
        self.no_browser = no_browser
        # Initialize the process variable to None
        self.process = None

    # Function to start the jupyter service
    def start(self) -> None:
        # If the jupyter service is not running, start it
        if self.process is None:
            self.process = start_jupyter(self.lab_or_notebook, self.config_dir, self.config_path, self.no_browser)
        else:
            print('Jupyter service is already running!')

    # Function to stop the jupyter service
    def stop(self) -> None:
        # Terminate the jupyter service
        os.kill(self.process.pid, signal.CTRL_C_EVENT)
        # Set the process variable to None
        self.process = None
    
    # Function to restart the jupyter service
    def restart(self) -> None:
        # Start the jupyter service
        self.start()
        # Stop the jupyter service
        self.stop()


# Subclass of JupyterService for JupyterLab
class JupyterLabService(JupyterService):
    def __init__(self, config_dir: str, config_path: (None | str) = None, no_browser: bool=True):
        super().__init__('lab', config_dir, config_path, no_browser)


# Subclass of JupyterService for JupyterNotebook
class JupyterNotebookService(JupyterService):
    def __init__(self, config_dir: str, config_path: (None | str) = None, no_browser: bool=True):
        super().__init__('notebook', config_dir, config_path, no_browser)
