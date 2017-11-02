In typical form-based web applications, it is common practice for
developers to allow `autocomplete` within the HTML form to improve the
usability of the page. With `autocomplete` enabled (default), the
browser is allowed to cache previously entered form values.

For
legitimate purposes, this allows the user to quickly re-enter the same
data when completing the form multiple times.

When `autocomplete` is
enabled on either/both the username and password fields, this could
allow a cyber-criminal with access to the victim's computer the
ability to have the victim's credentials automatically entered as the
cyber-criminal visits the affected page.

The tool has discovered that
the affected page contains a form containing a password field that has
not disabled `autocomplete`.