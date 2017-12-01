README
======

Here is some |stuff|.

Here is some |stuff2|.

.. |stuff| raw:: html

   <em>emphasized text containing a
   <a href="http://example.org">hyperlink</a> and
   <tt>inline literals</tt></em>

.. |stuff2| raw:: latex

    \begin{tabular}{|c|c|}
    \hline \multicolumn{2}{|c|}{Ene} \\
    \hline Mene & Muh! \\
    \hline
    \end{tabular}

This project is for extracting text from several ``.txt`` files
to build a large table using Latex syntax.
