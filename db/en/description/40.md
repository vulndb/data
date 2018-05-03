Private, or non-routable, IP addresses are generally used within a
home or company network and are typically unknown to anyone outside of
that network.

Cyber-criminals will attempt to identify the private IP
address range being used by their victim, to aid in collecting further
information that could then lead to a possible compromise.

The tool
discovered that the affected page returned a RFC 1918 compliant
private IP address and therefore could be revealing sensitive
information.

_This finding typically requires manual verification to
ensure the context is correct, as any private IP address within the
HTML body will trigger it.