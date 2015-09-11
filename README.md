# Supporter Signup

- ``/docs`` - It's where the documentation goes.
- ``/tests`` - It's where the tests go.
- ``/setup.py`` - Setup script for the project/application
- ``/requirements.txt`` - See notes below.
- ``/supporter_signup``
- ``/supporter_signup/__init__.py`` - where `__version__` is set
- ``/supporter_signup/config.py`` - configuration
- ``/supporter_signup/application.py`` - main application code
- ``/supporter_signup/wsgi.py`` - wsgi module

## setup.py

Python packaging is interesting to say the least. Writing a setup script can be confusing. The basics are laid out here and should get you 90% of the way. Check out the [official documentation](https://docs.python.org/2/distutils/setupscript.html) if you get stuck.

### requirements.txt

All dependency resolution should be handled in ``setup.py``. This ``requirements.txt`` file is here due to the old pattern that is entrenched in the Python world. The contents of this file (``-e .``) will allow developers to use the familiar ``pip install -r requirements.txt``.
