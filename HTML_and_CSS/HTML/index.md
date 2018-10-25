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
The main function of HTML is to describe the nature of the text parts of
a document.  There are several HTML tags which can help with this.

**Paragraphs**```<p> ... </p>```
Most text should be enclosed in paragraph tags. These are the basic
textual tag. Most formatting in the text in an HTML document is ignored,
including newlines.  If you want to have a line break in your text then
the usual mechanism is to end one paragraph block and start another.

**Headings**```<h1> ... </h1> <h2> ... </h2>```
If you have headings for different sections of your document then you
would use the heading tags to denote these.  The number associated with
the tag says what level of heading you're using, with ```<h1>``` being
a main top level heading and ```<h2>``` being a lower, second level
heading.

Headings are not contained within paragraphs.  You'd close the
paragraph before opening the heading tag.

**Emphasis**```<strong> ... </strong>   <em> ... </em>```
Sometimes you want to indicate that a few words within a paragraph
are particularly important and should be rendered differently to the
surrounding text.  There are two types of tag which you can use to
indicate this.

The ```<strong>``` tag is where you want a piece of text to stand out
from the text around it.  In a graphical browser it would normally
be expected to be rendered in bold text, but this isn't guaranteed.

The ```<em>``` (emphasis) tag is normally used to indicate that a
stress should be placed on certain works.  In a graphical browser
it would normally be rendered in italics, but this isn't guaranteed.

Importantly, these types of tags are designed to sit within a
paragraph block (in contrast to something like headings). So the
correct structure for using these tags would be.

```
<p>
  This is a paragraph I'm writing. <em>This</em> is an important
  word I want to stress. <strong>It's important I don't close the
  paragraph tag when I use these tags</strong>.
</p>
```


### Lists

### Tables

### Images and Videos

### Links
