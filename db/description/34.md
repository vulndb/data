A NoSQL injection occurs when a value originating from the client's
request is used within a NoSQL call without prior sanitisation.

This
can allow cyber-criminals to execute arbitrary NoSQL code and thus
steal data, or use the additional functionality of the database server
to take control of further server components.

The tool discovered that
the affected page and parameter are vulnerable. This injection was
detected as the tool was able to inject specific NoSQL queries that if
vulnerable result in the responses for each injection being different.
This is known as a blind NoSQL injection vulnerability.