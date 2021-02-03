=====================
ColorDetect Changelog
=====================


.. _1.3.0:
1.3.0 (02-02-2021)
====================

Features
--------

- Add a return of human readable colors.

Documentation
-------------

- Update ColorDetect module documentation to show method params

.. _1.3.0rc:
1.3.0rc (18-01-2021)
====================

Features
--------

- Add a return of human readable colors.

Documentation
-------------

- Update ColorDetect module documentation to show method params
- Move to version ``1.3.0rc`` due to error in ``1.1.1`` packaging

.. _1.1.1:
1.1.1 (17-01-2021)
==================

Documentation
-------------
- Update setup to show correct package version.

.. _1.1.0:
1.1.0 (17-01-2021)
==================

Features
--------
- Enable customization of text input from the user as well as color count being
  written to the image

Documentation
-------------

- Add contributors to readme and update project documentation with relevant parameter methods

.. _1.0.1:
1.0.1 (23-11-2020)
==================

Features
--------
- Add pre-commit hooks for better contribution styling

Documentation
-------------

- Update readme with development guide.

.. _1.0.0:
1.0.0 (03-10-2020)
==================

Features
--------
- Creation of col_share module. Split methods non-exclusive to `VideoColor` and `ColorDetect`

Documentation
-------------

- Include col_share documentation.
- Update readme to reflect col_share.

.. _0.3.1:
0.3.1 (17-10-2020)
==================

Bug fix
-------

- Perform check to ensure the color description has content before writing color count.


.. _0.3.0:
0.3.0 (26-09-2020)
==================

Features
--------
- Video color detection and recognition

Documentation
-------------

- Include video color detection documentation
- Correction in package imports

.. _0.2.0:
0.2.0 (13-08-2020)
==================

Features
--------
- Enable input of custom text onto the image

Documentation
-------------

- Add ``write_text`` method along with other breaking changes to the documentation

.. _0.1.7:
0.1.7 (17-04-2020)
==================

Features
--------

- Invert return of recognized colors dictionary. Return the colors
  as keys and percentages as values to avoid duplicate dictionary keys.

.. _0.1.6:
0.1.6 (17-04-2020)
==================

Features
--------

- Add color format return options. Include RGB, hex and hsv

Misc
----

- Add tests suite and move test files out of project root.
- Add contributions file
- Update dev requirements
- Improve methods types specification and exception catching.

.. _0.1.5:
0.1.5 (11-04-2020)
==================

Features
--------

- Return a whole number for the RGB value instead of float.

Documentation
-------------

- Add changelog to the documentation.

.. _0.1.4:
0.1.4 (5-04-2020)
==================

Features
--------

- Allow recognition of non pre-defined color sets
- Allow a plain dictionary to be obtained with color recognition
  from the image before writing onto it.
- Format display of percentage and RGB values

Bugfixes
--------

- Update CI config file with correct requirements path.
- Correct test running instructions on README.


Improved Documentation
----------------------

- Publish package documentation
  `ColorDetect <https://colordetect.readthedocs.io/en/latest/>`_

Misc
----

- Add versioning to readme and edit dev requirements.


----

.. _0.1.3:
0.1.3 (22-03-2020)
==================

Features
--------
- Change image reading from command-line
  to ColorDetect object initialization.

Bug fixes
---------

- Fix image reading.

Misc
----

- Split dev and base requirements.


----

.. _0.1.2:
0.1.2 (22-03-2020)
==================
Features
--------
- Include project license

----

.. _0.1.1:
0.1.1 (22-03-2020)
==================
- Initial release
