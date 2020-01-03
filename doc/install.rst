.. _installation_instructions:

===================
Installing wmp-face
===================

There are different ways to install wmp-face:

  * :ref:`Install the latest official release <install_official_release>`. This 
    is the best approach for most users. It will provide a stable version.
  * `Building the package from source`_. This is best for users who want the 
    latest-and-greatest features and aren't afraid of running new code. This is 
    needed for users who want to contribute to the project.

.. _install_official_release:

Installing the latest release
=============================

Install the 64bit version of Python_.

.. _Python: http://www.python.org/

Then run::

  $ pip install -U wmp-face

In order to check your installation you can use

  $ python -m pip show wmp-face # to see which version and where wmp-face is installed
  $ python -m pip freeze # to see all packages installed in the active virtualenv
  $ python -c "import wesface; wesface.show_versions()"  