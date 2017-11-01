Due to the requirement for dynamic content of today's web
applications, many rely on a database backend to store data that will
be called upon and processed by the web application (or other
programs). Web applications retrieve data from the database by using
Structured Query Language (SQL) queries.

To meet demands of many
developers, database servers (such as MSSQL, MySQL, Oracle etc.) have
additional built-in functionality that can allow extensive control of
the database and interaction with the host operating system itself.
An SQL injection occurs when a value originating from the client's
request is used within a SQL query without prior sanitisation. This
could allow cyber-criminals to execute arbitrary SQL code and steal
data or use the additional functionality of the database server to
take control of more server components.

The successful exploitation
of a SQL injection can be devastating to an organisation and is one of
the most commonly exploited web application vulnerabilities.



Injection was detected as it was possible to inject specific SQL
queries, that if vulnerable, result in the responses for each
injection being different. This is known as a blind SQL injection
vulnerability.