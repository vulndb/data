Web applications are often made up of multiple files and directories.
It is possible that over time some files may become unreferenced
(unused) by the web application and forgotten about by the
administrator/developer. Because web applications are built using
common frameworks, they contain common files that can be discovered
(independent of server).

During the initial recon stages of an
attack, cyber-criminals will attempt to locate unreferenced files in
the hope that the file will assist in further compromise of the web
application. To achieve this they will make thousands of requests
using word lists containing common filenames. The response headers
from the server will then indicate if the file exists.

The tool also
contains a list of common file names which it will attempt to access.