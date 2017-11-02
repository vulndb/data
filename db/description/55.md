Client-side scripts are used extensively by modern web applications.
They perform from simple functions (such as the formatting of text) up
to full manipulation of client-side data and Operating System
interaction.



Cross Site Scripting (XSS) allows clients to inject arbitrary scripting
code into a request and have the server return the script to the
client in the response. This occurs because the application is taking
untrusted data (in this example, from the client) and reusing it
without performing any validation or encoding.