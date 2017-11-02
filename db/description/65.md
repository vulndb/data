Many web applications allow users to upload files that will either be
stored or processed by the receiving web server.



It was possible to identify a form which allows files with arbitrary
content and extension to be uploaded to the remote server, and then
stores the uploaded file to a guessable path in the server's web root.



This could be used by a cyber-criminal to host content from the vulnerable
server for phishing and Cross-Site Scripting attacks. In cases where the
server is configured to execute scripts (PHP, Ruby, etc.) this
vulnerability can be used to gain remote code execution on the server.