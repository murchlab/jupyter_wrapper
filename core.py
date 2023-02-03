import tomli
import os
from pathlib import Path
from subprocess import Popen


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
def _jupyter(notebook_or_lab: str, config_dir: str,
             config_file: (None | str) = None) -> None:
    # Creates the config directory if it doesn't exist
    Path(config_dir).mkdir(parents=True, exist_ok=True)
    # Set the default config file name if not provided
    if config_file is None:
        config_file = os.path.join(
            config_dir, f'jupyter_{notebook_or_lab}_config.toml'
        )
    # Load the config file
    with open(config_file, 'rb') as f:
        config_dict = tomli.load(f)
    # Generate the python config file
    config_py_file = os.path.join(
        config_dir, f'jupyter_{notebook_or_lab}_config.py'
    )
    config_py = generate_config_py(config_dict)
    # Write the python config to file
    with open(config_py_file, 'w') as f:
        f.write(config_py)
    # Set the JUPYTER_CONFIG_DIR environment variable
    jupyter_env = os.environ.copy()
    jupyter_env['JUPYTER_CONFIG_DIR'] = config_dir
    # Start Jupyter with the custom config
    args = ["jupyter", notebook_or_lab, "--config", config_py_file]
    process = Popen(args, env=jupyter_env)
    process.communicate()


# Starts Jupyter lab with a custom config
def jupyter_lab(config_dir: str, config_file: (None | str) = None) -> None:
    _jupyter('lab', config_dir, config_file)


# Starts Jupyter notebook with a custom config
def jupyter_notebook(config_dir: str, config_file: (None | str) = None) -> None:
    _jupyter('notebook', config_dir, config_file)
