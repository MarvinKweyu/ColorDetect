.. _Contributing:
Contributing to ColorDetect
===========================

Thank you for taking your time to  look at the `ColorDetect <https://github.com/MarvinKweyu/ColorDetect>`_ project.

Use the following as guidelines to making your contributions and do feel free to propose changes to this document in a pull request.
The source code, located at `the ColorDetect project page <https://github.com/MarvinKweyu/ColorDetect>`_.

Setup
-----
This project uses `uv <https://docs.astral.sh/uv/>`_ for dependency management.
Install it via::

    curl -LsSf https://astral.sh/uv/install.sh | sh

Then set up the project::

    uv venv
    uv pip install -e ".[dev]"
    pre-commit install


Issues
------
Check if the issue has been addressed or is in progress and if not , only then do you create a new issue.
Remember to give it the appropriate `label <https://github.com/MarvinKweyu/ColorDetect/labels>`_

Enhancements
------------
Describe the enhancement in mind and what you would expect to have resulted from this process.
Submit the enhancement with the `enhancement` tag **along with its test**

Pull requests
-------------
Reference the issue or enhancement being referenced in the pull request and 
submit the pull request to the `development` branch.
