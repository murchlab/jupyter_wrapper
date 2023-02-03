# Jupyter Wrapper

A python package for starting, stopping, and restarting JupyterLab or Jupyter Notebook with custom configurations.

## Features

- Start and stop JupyterLab or Jupyter Notebook services
- Set a custom configuration directory and file path
- Configure Jupyter using a TOML configuration file

## Usage

### Installation

To install the package, run the following command:

```shell
pip install <download link to jupyter_wrapper>.whl
```

### Import

Import the package in your python script:

```python
from jupyter_service import JupyterLabService, JupyterNotebookService
```

### Initialization

To start a Jupyter service, you need to initialize an instance of `JupyterLabService` or `JupyterNotebookService` with a custom configuration directory.

```python
jupyter_lab = JupyterLabService('/path/to/config/dir') # Contains jupyter_lab_config.toml
jupyter_notebook = JupyterNotebookService('/path/to/config/dir') # Contains jupyter_lab_config.toml
```

You can also provide a custom configuration file path:

```python
jupyter_lab = JupyterLabService('/path/to/config/dir', '/path/to/config/file.toml')
jupyter_notebook = JupyterNotebookService('/path/to/config/dir', '/path/to/config/file.toml')
```

### Start

Start the Jupyter service using the `start` method:

```python
jupyter_lab.start()
jupyter_notebook.start()
```

### Stop

Stop the Jupyter service using the `stop` method:

```python
jupyter_lab.stop()
jupyter_notebook.stop()
```

### Restart

Restart the Jupyter service using the `restart` method:

```python
jupyter_lab.restart()
jupyter_notebook.restart()
```

## Configuration

The package uses a TOML configuration file to configure Jupyter. The file should contain a dictionary with the configuration settings. The package converts the TOML configuration file to a python file and sets the 'JUPYTER_CONFIG_DIR' environment variable to the directory containing the configuration file.

Here is an example of a TOML configuration file:

```toml
# [Application]
# log_datefmt = "%Y-%m-%d %H:%M:%S"
# log_format = "[%(name)s]%(highlevel)s %(message)s"

# [JupyterApp]
# answer_yes = False
# config_file = ""

# [ExtensionApp]
# answer_yes = False
# config_file = ""

# [LabServerApp]
# allowed_extensions_uris = ""
# answer_yes = False

# [LabApp]
# allowed_extensions_uris = ""
# answer_yes = False

[ServerApp]
# allow_credentials = False
# allow_origin = ""
port = 28888
```

## Dependencies

The package depends on the following python packages:

- jupyter
- tomli
- pathlib
- subprocess

## License

The package is licensed under the MIT license.
