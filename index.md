## Bioinformatics School's Project

This is a set of documentation for a long-running project designed to give a practical introduction to several areas of IT, computer science and bioinformatics to children of secondary school age (roughly 12 - 16 years old).

The project was originally covceived to run as an after-school club, run in one hour sessions over several weeks.  The course is largely modular so you can choose to include or exclude parts as you see fit.

In it's original version this project was run by distributing customised raspberry pi computers to each student so they had an isolated environment they could work in, and take away with them.  Most of the project could be run on other hardware platforms with minimal modification.

# Areas covered in the project

1. Hardware - using the Raspberry Pi to illustrate the different parts of the standard PC architecture

2. Networking - building a small, isolated network to illustrate the basic principles of Ethernet / IPv4 networking

4. Markup languages - Using a web server running on each machine the students will construct a small, static HTML/CSS based site to construct a localised version of the world wide web.

5. Programming - students attending the course will generally have had some exposure to basic programming concepts in their taught classes.  Here we expand on these and get them to construct some simple command line python programs to solve increasingly complex problems.

6. Dynamic web sites - we combine the knowledge the students gained in sections 4 and 5 to get them to write a simple python CGI script in order to generate a dynamic web site.

7. Final project - we provide a number of suggestions for more complex bioinformatics projects which the students can undertake.  In each case they can divide the project into coding an analysis tool, designing a web site to collect information and present results, and then linking the two together to make a dynamic web based tool.

# Hardware used

In the initial running of this project the hardware we used was:

1. Around 30 raspberry pi 3 machines.  We used the starter kits so that each child had not only the pi itself, but also a keyboard, mouse, power supply, HDMI cable and Ethernet cable.  Displays were either provided by a school computing lab, or donated by local busineses or normal household televisions could be used.

2. Network switches. In our case we constructed a routing network by making two initially isolated networks of around 15 pis each before joining them together to create a mini internet.  Each sub-network used a 16 port network switch.  These can be bought cheaply, or older, slower switches are easily obtained from local companies.

3. A small server for the instructor.  We used a mini-itx dual network port box to provide network services (DNS, DHCP and routing).  We could also link this machine to a projector to show presentations.  If you're not using a routing network then you could simply use another raspberry pi for this purpose.
