Client-side scripts are used extensively by modern web applications.
They perform from simple functions (such as the formatting of text) up
to full manipulation of client-side data and Operating System
interaction.



Cross Site Scripting (XSS) allows clients to inject arbitrary scripting
code into a request and have the server return the script to the
client in the response. This occurs because the application is taking
untrusted data (in this example, from the client) and reusing it
without performing any validation or encoding.



Persistent Cross Site Scripting vulnerabilities occur when the application
stores user controlled information and then uses it to render HTTP
response bodies to other clients.



This type of vulnerability can be used by a cyber-criminal to perform
session hijacking, phishing or denial of service attacks against other
web application users.