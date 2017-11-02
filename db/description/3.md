A common practice when administering web applications is to create a
copy/backup of a particular directory prior to making any
modification. Another common practice is to add an extension or change
the name of the original directory to signify that it is a backup
(examples include `.bak`, `.orig`, `.backup`, etc.).

During the
initial recon stages of an attack, cyber-criminals will attempt to
locate backup directories by adding common extensions onto directories
already discovered on the webserver. By analysing the response headers
from the server they are able to determine if a backup directory
exists. These backup directories can then assist in the compromise of
the web application.

By utilising the same method, the tool was able
to discover a possible backup directory.