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
It's pretty common to want to put lists of information into a
document.  There are two kinds of lists within HTML, ordered
lists and unordered (bulletted) lists.  Each of these comprises its own
block within HTML and isn't contained within a paragraph.

Lists themselves are split into two components, each with its own set of
HTML tags.  You have the list itself.  This is defined by ```<ol> ... </ol>```
for ordered lists, and ```<ul> ... </ul>``` for unordered lists.

Inside the main list tags you can then have any number of list *items*. Each
of these is a single element within the list and is defined by a pair
of ```<li> ... </li>``` tags.  The list item tags are the same whether you're
in an ordered or unordered list.

Putting this together, a typical ordered list would look like this.

```{html}
<ol>
  <li>First element</li>
  <li>Second element</li>
  <li>Third element</li>
</ol>
```

Once rendered this will look like:

1. First element
2. Second element
3. Third element

The equivalent unordered list would be:

```{html}
<ul>
  <li>First element</li>
  <li>Second element</li>
  <li>Third element</li>
</ul>
```

..and would look like:

* First element
* Second element
* Third element


### Tables
Tables are one of the more complex items to render in HTML, but they are
very versatile and useful for presenting information.

Tables have a 3 level structure within HTML:

1. The table itself represented by ```<table> ... </table>``` tags

2. A table row representing a single row of content, and denoted by ```<tr> ... </tr>```
tags

3. Table data.  The data for one cell in the table.  There are two types of
tag you can use for this, either ```<td> ... </td>``` for normal data, or if
you're putting a heading on the table you can use ```<th> ... </th>``` for those
cells which will then be rendered in a more emphasised way.

It is expected that each row of the table will have the same number of
data cells in it, and the browser will take care of making sure that these
are all correctly aligned with each other.

Thus, the overall structure of a table would look like this:

```
<table>
  <tr>
    <th>First heading</th>
    <th>Second heading</th>
  </tr>

  <tr>
    <td>Content 1</td>
    <td>Content 2</td>
  </tr>

  <tr>
    <td>Content 3</td>
    <td>Content 4</td>
  </tr>
</table>
```

..and this will look like:

|First heading | Second heading |
|--------------|----------------|
|Content 1     | Content 2      |
|Content 3     | Content 4      |


### Links
Navigation around the WWW is built on the concept of hyperlinks.  These are
a way that your viewers can jump from one page to another, either within your
own site, or going to somewhere completely different elsewhere on the web.

Links are used in serveral places within HTML.  We will see in a second that
links form the basis for including images and videos within pages, and we'll
also see that links are used to add styling to pages through the use of CSS.
They are a general mechanism to assemble content from different places into
the final document which the user sees.

In this section though we are going to focus on navigation links - pieces of
text which cause you to navigate away from the current HTML document and go
somewhere else on the web when you click on them.

Navigation links are constructed using anchor tags ```<a> ... </a>```.  Between
the tags you can put whatever content you like - most commonly text, but it
could equally be an image.  The point is that whatever comes between the tags
is the content which will activate the link when you click on it.

The anchor tags require you to provide some additional information though,
specifically they need to know where the link should take the user, and this
is achieved through the use of the href attribute.  The value for this attribute
will be the location the link points to and must be a URL (web address).  These
URLs can either be complete web addresses such as ```https://www.google.com```
or, if you're just pointing to somewhere else within your own site they can
be locations relative to the current page, eg ```../HTML_and_CSS/index.html```
(that would be the folder above this one (```..```), then down into the ```HTML_and_CSS```
folder, and then link to the index.html document).

A complete link would therefore look something like this;

```
<p>
  Maybe you should visit
  <a href="https://www.bioinformatics.babraham.ac.uk">Babraham Bioinformatics</a>
  to learn more about bioinformatics?
</p>
```

..and it would look like:

Maybe you should visit [Babraham Bioinformatics](https://www.bioinformatics.babraham.ac.uk)
to learn more about bioinformatics?

### Images and Videos
The web is a highly visual medium, and images and videos are a core
part of many web sites.  In HTML both images and videos are a form of link,
meaning that the images and videos aren't actually part of the page you're
viewing, but are separately available content which is dynamically inserted
into the page by the web browser.  What you are doing in the HTML is therefore
pointing part of your document to another location on the www where the
multimedia content can be obtained.

This means that the first problem you have is that you need to either find
the image you want to use somewhere available on the internet already, or you
need to need to make the images you want to use available yourself.  Often
this is as simple as uploading the image files alongside your HTML documents
in your web server root.

In the example below we're going to look at inserting our group logo into
a document.  We're assuming for the purposes of this example that we've
copied the image file ```babraham.png``` into the same directory on our
web server as the HTML document we're writing.

![Babraham Bioinformatics Logo](babraham.png)

To insert this into the document we need to use an ```<img>``` tag.  We will
need to provide an option to this tag though to say where it can be found.  This
is set using the ```src``` parameter of the tag.

Images are inline content so ```<img>``` tags should generally be encosed within
some other tag type such as ```<p>``` or maybe ```<td>``` if the image is going
into a table.

Here is a simple example:

```
<p>
  <img src="babraham.png">
</p>
```

Video can theoretically be handled in a similar way by making use of the ```<video>```
tag.  This again requires that the video you want to embed is able to be directly
accessed somewhere on the web already.

One unusual aspect of the ```<video>``` tag is that you can specify multiple
sources for it in different formats so that you can support a wider range of
devices which may only be able to play some of the large number of different
video file formats which exist.

```
<p>
  <video>
    <source src="movie.mp4" type="video/mp4">
  </video>
</p>
```

In practice, although you can serve video in this way it's quite uncommon to
do this, since it means that you need to have the bandwidth to serve the
video content yourself.  Far more commonly you will see sites using large
public video repositories such as YouTube or Vimeo and then embedding their
video players within their HTML pages.  All of these video sites will have
an option to generate some HTML code to allow you to embed a video within
an HTML page as part of their standard player.

For example, within the YouTube sharing options is an option to embed the
video, which gives you something like this:

![YouTube embedding code](youtube_embed.png)

..and if you simply copy and paste that code into your HTML page then the
video will appear alongside the rest of your content.

```
<iframe width="560" height="315" src="https://www.youtube.com/embed/qPxl2hflG9Q" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
```

Putting it all together
-----------------------

Taking what we have learned in the sections above we can now construct an
entire document which can mark up all of the content for a page.  Here is a
more complete example.

First we start with the page header.

```
<html>
  <head>
    <title>A complete web page</title>
  </head>

  <body>
```

We've opened the ```<html>``` and ```<body>``` tags and we will therefore
need to remember to close them again at the end of the document.

Now we can include some content.  We'll start with a simple header and some
text.

```
    <h1>Introduction</h1>

    <p>
      In this section we're going to introduce the topic we want to talk
      about.  This is just plain text, although we might want to make
      some parts look <strong>more important</strong> than others.
    </p>
```

We can include an image.  This time taken from elsewhere on the web

```
    <p>
      <img src="https://www.w3.org/html/logo/downloads/HTML5_1Color_Black.svg">
    </p>
```


Now a list.

```
    <p>
      Things we are going to learn include:
    </p>

    <ul>
      <li>Writing HTML documents</li>
      <li>Adding appropriate markup</li>
      <li>Linking to other web locations</li>
    </ul>
```

Now maybe we should link somewhere else.

```
    <p>
      For more information about HTML you might want to look at the
      excellent <a href="https://www.w3schools.com/">W3Schools</a>
      website.
    </p>
```


Finally, we clean up by closing the ```<body>``` and ```<html>``` tags we
opened at the top of the document.  if you were writing this document yourself
then you should always write the closing tag as soon as you write the opening
tag so that you don't end up with mismatched tags in your document which might
cause the web browser to reject or misinterpret it.

```
  </body>
</html>
```
