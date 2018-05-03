The reflected file download vulnerability is an application weakness
which allows a cyber-criminal to perform advanced social engineering
attacks where an arbitrary executable file is downloaded by the user from
vulnerable site. The contents of the executable file are controlled by
the attacker and are never uploaded to the vulnerable site.



This vulnerability, like many other Web attacks, begins by sending a
malicious link to a victim. Unlike other attacks the exploitation finishes
outside of the browser context:



1. The user follows a malicious link to a trusted web site

2. An executable file is downloaded and saved on the user's machine.
All security indicators show that the file is 'hosted' on the trusted web
site

3. The user executes the file which contains shell commands that gain
complete control over the computer.