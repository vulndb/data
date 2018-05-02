To perform specific actions from within a web application, it is
occasionally required to run Operating System commands and have the
output of these commands captured by the web application and returned
to the client.

OS command injection occurs when user supplied input
is inserted into one of these commands without proper sanitisation and
is then executed by the server.

Cyber-criminals will abuse this
weakness to perform their own arbitrary commands on the server. This
can include everything from simple `ping` commands to map the internal
network, to obtaining full control of the server.



It was possible to inject and verify the execution of specific Operating
System commands which indicates that proper input sanitisation is not
occurring.