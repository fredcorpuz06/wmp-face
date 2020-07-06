.. _installation_instructions:

===================
Installing wmp-face
===================

There are different ways to install wmp-face:

  * :ref:`Install the latest official release <install_official_release>`. This 
    is the best approach for most users. It will provide a stable version.
  * `Building the package from source
    <https://github.com/fredcorpuz06/wmp-face>`_. This is best for users who 
    want the latest-and-greatest features and aren't afraid of running new 
    code. This is needed for users who want to contribute to the project.

.. _install_official_release:

Installing the latest official release
======================================

Install the 64bit version of Python_.

.. _Python: http://www.python.org/

Then run::

  $ pip install --upgrade wmp

In order to check your installation you can use::

  $ pip show wmp # to see which version and where wmp-face is installed
  $ pip freeze # to see all packages installed in the active virtualenv