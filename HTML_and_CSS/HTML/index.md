HTML
====

HTML is a markup language designed to describe the text content
of a document.  The syntac is based around placing specially formatted
tags in angle brackets around the content to describe what the content
between the tags is.

For example, if we have a piece of text which says;

```
Some of this sentence is really important.
```

The HTML tags we would need to add would be tags around the whole sentence
to say that it is a paragraph, and a second pair around the word "really"
to indicate that it should be given more emphasis than the rest of the
paragraph.  This would look like:

```
<p>Some of this sentence is <strong>really</strong> important.</p>
```

You can see from this example that an html tag is just a letter or word
enclosed in <> brackets.  Having the word alone indicates the start of
an HTML element, putting a forward slash after the opening bracket indicates
that this is a closing tag to say where it ceases to have an effect.

In some cases tags can nest within each other (such as a strong part of
  a paragraph)

Document structure
-----------------

A complete HTML document has a larger overall structure than just
marking up the content directly.  The example below shows the overall
structure of a simple HTML document.

```
<html>
  <head>
    <title>An example document</title>
  </head>

  <body>
    <h1>An example document</h1>

    <p>
      This is a simple HTML document.
    </p>
  </body>
</html>
```

The entire document is always surrounded by ```<html></html>``` tags.  Within
this there are then two sections.

### Head
The head section gives information about the document as a whole, but
does not contain any content which is going to be rendered.  Things which
go in the head include:

* The title of the docuemnt.  This is normally the text which appears in
the window bar of the browser and may appear in bookmarks.  It is not shown
in the actual document.

* CSS information.  If your HTML document has an accompanying stylesheet then
this information is nromally placed into the header, either directly, or as
a link to another document.

* Scripts.  If the document included dynamic content written in the javascript
language then this code is placed into the header of the document.

### Body
The body of the document is where the main rendered content goes. It will
contain descriptive tags to mark up the type of information contained in the
text part of the document.  This section can also contain linking information
to either embed other media information (images, videos etc) into the document
or provide links to other documents to allow nagivation around the www.


Common markup tags
------------------

There are a lot of markup tags in HTML, but you only really need to know
a small number in order to correctly be able to mark up most common documents.

### Text information

### Images and Videos

### Tables

### Links
