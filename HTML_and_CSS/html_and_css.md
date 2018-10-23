HTML and CSS
============

Introduction
------------

The world wide web (WWW) is one of the main uses of the internet. Much
of the www is build around the exchange and viewing of *web pages*, which
are multi-media documents viewed in a web browser.

One of the early design decisions for the www was that since the web was
likely to be accessed from a variety of different devices and software, from
large graphical workstations, to small handheld devices, to sepecialised
devices such as speech synthesisers, that it would be inappropriate to
design it using a file format which would distribute fully designed and
renders pages of information.  Instead the decision was that the information
on the web should be distributed in a presentation neutral format which
allowed each machine and program to render this in the most appropriate way
for the hardware platform it was running on.

The language which was chosen to distribute the information on the www was
HyperText Markup Language, commonly abbreviated to HTML.

HTML
----

HTML is a markup language.  This means that it is not a programming
language - it does not have logic or data processing.  Its purpose is
to add a layer of descriptive annotation to text documents with the aim
of either describing their content (eg this part is a heading, this is
a paragram, this is a cell of a table etc), or linking different resources
togehter (eg, include an image here, allow the user to jump to a different
document here etc.).  HTML is not intended to have anything to say about
how this information is interpreted by the reading application.  It might
be that a heading is make larger in one browser, turns a differnet colour
in another and is read more loudly in a speech browser.  The point is that
HTML simply 'marks up' the content and then lets the browser decide on the
presentation.

At various points in the history of HTML extensions have been added which
aimed to provide varying levels of explicit suggestions for the way that
information is presented visually.  This goes against the original intent
of the language and these additions are now largely deprecated, leaving
HTML to fulfill its original purpose again.

People who write web pages are vain though, and they want to have control
over how their information is presented.  To make sure that there is a
clear separation of the marking up of information (using HTML), a separate
layer of annotation based on presentation was added, using a concept called
Casscading Style Sheets (CSS).
