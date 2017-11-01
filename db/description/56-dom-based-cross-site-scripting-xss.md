Client-side scripts are used extensively by modern web applications.
They perform from simple functions (such as the formatting of text) up
to full manipulation of client-side data and Operating System
interaction.

Unlike traditional Cross-Site Scripting (XSS), where the
client is able to inject scripts into a request and have the server
return the script to the client, DOM XSS does not require that a
request be sent to the server and may be abused entirely within the
loaded page.

This occurs when elements of the DOM (known as the
sources) are able to be manipulated to contain untrusted data, which
the client-side scripts (known as the sinks) use or execute an unsafe
way.