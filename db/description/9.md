Web applications are often made up of multiple files and directories.
It is possible that over time some directories may become unreferenced
(unused) by the web application and forgotten about by the
administrator/developer. Because web applications are built using
common frameworks, they contain common directories that can be
discovered (independent of server).

During the initial recon stages
of an attack, cyber-criminals will attempt to locate unreferenced
directories in the hope that the directory will assist in further
compromise of the web application. To achieve this they will make
thousands of requests using word lists containing common names. The
response headers from the server will then indicate if the directory
exists.

The tool also contains a list of common directory names which
it will attempt to access.