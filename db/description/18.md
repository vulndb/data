The design of many web applications require that users be able to
upload files that will either be stored or processed by the receiving
web server.

The tool has flagged this not as a vulnerability, but as a
prompt for the penetration tester to conduct further manual testing on
the file upload function.

An insecure form-based file upload could
allow a cyber-criminal a means to abuse and successfully exploit the
server directly, and/or any third party that may later access the
file. This can occur through uploading a file containing server
side-code (such as PHP) that is then executed when requested by the
client.