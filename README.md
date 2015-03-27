## VulnDB data
User, contributor and developer-friendly vulnerability database. Our goal is to
provide a vulnerability database which is:

 * Actionable, easy to read and understand for developers and sysadmins who need
 to fix the vulnerability
 
 * Easy to integrate by developers into any vulnerability scanner, report
 generator, penetration testing tool or related tool.
 
 * Trivial to contribute to, by using JSON to store the vulnerabilities

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

## Credits
 * JSON format specification by [Andres Riancho](https://github.com/andresriancho/), [Tasos Laskos](https://github.com/Zapotek) and [Vyacheslav Bakhmutov](https://github.com/m0sth8)
 * Initial data provided by the [Arachni scanner](http://www.arachni-scanner.com/) project

## History
The project founders maintain one or more vulnerability scanners, each of those
tools had a different vulnerability database with different fields, formats,
texts and quality. To reduce our documentation efforts we decided to commoditize
the vulnerability database and created this repository.

At the beginning we tried to use the CWE data, but we found several problems with
it:

 * The target audience for our vulnerability information is too busy to read the
   [long](https://cwe.mitre.org/data/definitions/89.html) descriptions and hundreds
   of fields provided by CWE. We want to provide enough information for the users
   to know what's wrong and point them to information with more detailed info if
   that's what they need.

 * The XML format storing the CWE data is simply too complex for our needs.

 * Mitre never answered our questions on derivated work

We might still use some paragraphs from the CWE data in our database, but manually
migrated and reviewed for clarity.

It all started with these two github issues ([1](https://github.com/andresriancho/w3af/issues/53),
[2](https://github.com/vulndb/data/issues/5)) and various emails between Slava,
Andres and Tasos.

The initial database information was contributed by the [Arachni scanner](http://www.arachni-scanner.com/)
imported in [this commit](https://github.com/vulndb/data/commit/e27222af21b0569525718f591eaa2c517d4c1da2). 