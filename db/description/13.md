In the majority of today's web applications, clients are required to
submit forms which can perform sensitive operations.

An example of
such a form being used would be when an administrator wishes to create
a new user for the application.

In the simplest version of the form,
the administrator would fill-in:

* Name * Password * Role (level of
access)

Continuing with this example, Cross Site Request Forgery
(CSRF) would occur when the administrator is tricked into clicking on
a link, which if logged into the application, would automatically
submit the form without any further interaction.

Cyber-criminals will
look for sites where sensitive functions are performed in this manner
and then craft malicious requests that will be used against clients
via a social engineering attack.

There are 3 things that are required
for a CSRF attack to occur:

1. The form must perform some sort of
sensitive action. 2. The victim (the administrator the example above)
must have an active session. 3. Most importantly, all parameter values
must be **known** or **guessable**.

The tool discovered that all
parameters within the form were known or predictable and therefore the
form could be vulnerable to CSRF.

_Manual verification may be
required to check whether the submission will then perform a sensitive
action, such as reset a password, modify user profiles, post content
on a forum, etc._