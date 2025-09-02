.. vim: syntax=rst

Sphinx Directives Reference Document
====================================

This document includes various examples that, when converted to an RST format, will require the use of Sphinx directives.

Introduction
------------

Sphinx is a powerful tool for generating documentation.
Below are different content types typically used in documentation.

Code Example
~~~~~~~~~~~~

.. code-block:: python

   import sys from pandocfilters import toJSONFilter, RawBlock, Para def detect_code_blocks(key, value, format, meta): """ Detect preformatted text in
   Word documents and convert it to ..
   code-block:: directives in RST.
   """ if key == "Para":  # Word preformatted text might be wrapped in Para text = value[0].get("c", "") if isinstance(text, str) and text.startswith("
   "):  # Detect indented text return RawBlock("rst", "..
   code-block::\n\n    " + text.replace("\n", "\n    "))


   from pandocfilters

   import toJSONFilter, RawBlock, Para

   def detect_code_blocks(key, value, format, meta):

       """

       Detect preformatted text in Word documents and convert it to ..
       code-block:: directives in RST.

       """

       if key == "Para":  # Word preformatted text might be wrapped in Para

           text = value[0].get("c", "")

           if isinstance(text, str) and text.startswith(" "):  # Detect indented text

               return RawBlock("rst", "..
               code-block::\\n\\n    " + text.replace("\\n", "\\n    "))

Tables
^^^^^^

.. list-table::
   :widths: 50 50
   :header-rows: 0


   * - Column 1
     - Column 2

   * - Data 1
     - Data 2


..

.. code-block:: html

   <!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <title>HTML Test Page</title> </head> <body> <h1>Welcome to My Test Page</h1> <p>This
   is a simple paragraph to test HTML rendering.</p> <h2>Sample Image</h2> <img src="https://via.placeholder.com/150" alt="Placeholder Image"> <h2>Sample
   Code Block</h2> <pre><code>def hello_world(): print("Hello, world!")</code></pre> </body> </html>


   <html lang="en">

   <head>

   <meta charset="UTF-8">

   <title>HTML Test Page</title>

   </head>

   <body>

   <h1>Welcome to My Test Page</h1>

   <p>This is a simple paragraph to test HTML rendering.</p>

   <h2>Sample Image</h2>

   <img src="https://via.placeholder.com/150" alt="Placeholder Image">

   <h2>Sample Code Block</h2>

   <pre><code>def hello_world():

   print("Hello, world!")</code></pre>

   </body>

   </html>

Hyperlinks
^^^^^^^^^^

Visit the `Sphinx Website <https://www.sphinx-doc.org/>`__ for more details.

Mathematical Equations
^^^^^^^^^^^^^^^^^^^^^^

Einstein's famous equation:

.. math:: E\  = \ mc²

.. math:: \ \ \ {(a\  + \ b)}^{2}\  = \ a^{2}\  + \ 2ab\  + \ b^{2}

Images
^^^^^^

|sphinx002|

Indexing
========

.. code-block:: text

   Keyword for indexing: keyword


.. attention:: Please may I have your attention.

.. caution:: Exercise due caution.

.. danger:: Let none think to fly the danger for soon or late love is his
   own avenger.

.. error:: ERROR 418: I’m a teapot.

.. hint:: Look under the flowerpot.

.. important:: This is a statement of paramount importance.

.. note:: This function is not suitable for sending tins of spam.

.. tip:: Remember your sun cream!

.. warning:: Beware of the dog.

.. seealso:: Module zipfile. Documentation of the zipfile standard module.

Glossary
========

This Document
^^^^^^^^^^^^^

This document ensures that when converted to an RST format, appropriate Sphinx directives will be required for correct formatting.

environment
^^^^^^^^^^^

A structure where information about all documents under the root is saved and used for cross-referencing: the environment is pickled after the parsing
stage so that successive runs only need to read and parse new and changed documents.

source directory
^^^^^^^^^^^^^^^^

The directory, including its subdirectories, contains all source files for one Sphinx project.

This directive creates a centered boldfaced line of text.

Hlist
^^^^^

Column 1 Column 2 Column 3

A list of short items that should be

displayed horizontally (next item if exists)

.. |sphinx002| image:: media/sphinx002.png
   :width: 6.5in
   :height: 3.62639in
