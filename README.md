## VulnDB data
User, contributor and developer-friendly vulnerability database. Our goal is to
provide a vulnerability database which is:

 * Actionable, easy to read and understand for developers and sysadmins who need
 to fix the vulnerability
 
 * Easy to integrate by developers into any vulnerability scanner, report
 generator, penetration testing tool or related tool.
 
 * Trivial to contribute to, by using JSON to store the vulnerabilities

## History
The project founders maintain one or more vulnerability scanners, each of those
tools had a different vulnerability database with different fields, formats,
texts and quality. To reduce our documentation efforts we decided to commoditize
the vulnerability database and created this repository.

It all started with these two github issues ([1](https://github.com/andresriancho/w3af/issues/53),
[2](https://github.com/vulndb/data/issues/5)) and various emails between Slava,
Andres and Tasos.

## SDKs
This repository holds the vulnerability database itself, in order to make the
information easily accessible from different programming languages these SDKs
are available:

 * [python-sdk](https://github.com/vulndb/python-sdk)

## Projects using this database
 * Implementation in progress at [w3af](http://www.w3af.org/)
 
## Contributing
We would love to receive your [pull-requests](https://help.github.com/articles/using-pull-requests/)!
The easiest way to contribute is:
 * Browse our repository and find the JSON file you would like to edit
 * Click on the top-right icon in the github UI that will open the online text editor
 * Change the file
 * Save/commit
