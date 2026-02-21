# Lecture 8

## Table of Contents

* [Welcome!](#welcome)
* [The Internet](#the-internet)
* [Routers](#routers)
* [DNS](#dns)
* [DHCP](#dhcp)
* [HTTPS](#https)
* [HTML](#html)
* [Regular Expressions](#regular-expressions)
* [CSS](#css)
* [Frameworks](#frameworks)
* [JavaScript](#javascript)
* [Summing Up](#summing-up)

## Welcome

In previous weeks, I was introduced to Python, a high-level programming language that utilized the same building blocks I learned in C.

Today, I will extend those building blocks further in HTML, CSS, and JavaScript.

## The Internet

The internet is a technology that I utilize, interconnecting computers throughout the world.

Using my skills from previous weeks, I can build my own web pages and applications.

The **ARPANET** connected the first points on the internet to one another.

Dots between two points could be considered **routers**.

## Routers

To route data from one place to another, I need to make routing decisions. That is, someone needs to program how data is transferred from point A to point B.

I can imagine how data could take multiple paths from point A and point B, such that when a router is congested, data can flow through another path. **Packets** of data are transferred from one router to another, from one computer to another.

**TCP/IP** are two protocols that allow computers to transfer data between them over the internet.

**IP** or **internet protocol** is a way by which computers can identify one another across the internet. Every computer has a unique address in the world. Addresses are in this form:

```
#.#.#.#
```

Numbers range from 0 to 255. IP addresses are 32-bits (for **IPv4**), meaning that these addresses could accommodate over 4 billion addresses. Newer versions of IP addresses (such as **IPv6**), implementing 128-bits, can accommodate far more computers!

In the real world, servers do a lot of work for me.

Packets are structured as follows:

```
0                   1                   2                   3  
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |Type of Service|          Total Length         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|      Fragment Offset    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |    Protocol   |         Header Checksum       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source Address                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Address                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

Packets are standardized. The source and destination are held within each packet.

**TCP**, or **transmission control protocol**, helps keep track of the sequence of packets being sent.

Further, TCP is used to distinguish web services from one another. For example, 80 is used to denote HTTP and 443 is used to denote HTTPS. These numbers are default **port numbers** for these services.

When information is sent from one location to another, a source IP address, a destination IP address, and a TCP port number are sent.

These protocols are also used to fragment large files into multiple parts or packets. For example, a large photo of a cat can be sent in multiple packets. When a packet is lost, TCP/IP can request missing packets again from the origin server.

TCP will acknowledge when all the data has been transmitted and received.

## DNS

It would be very tedious if I needed to remember an IP address to visit a website.

**DNS**, or **domain name systems**, is a collection of servers on the internet that are used to route website addresses like `harvard.edu` to a specific IP address.

DNS is simply a table or database that links specific, fully qualified domain names to specific IP addresses.

## DHCP

**DHCP** is a protocol that assigns the IP address of my device.

Further, this protocol defines the default gateway and nameservers my device uses.

Now, no more about what’s outside my metaphorical envelope: Let’s look inside the envelope.

## HTTPS

**HTTP** or **hypertext transfer protocol** is an application-level protocol that developers use to build powerful and useful things through the transfer of data from one place to another. **HTTPS** is a secure version of this protocol.

When I see an address such as `https://www.example.com` I am actually implicitly visiting that address with a `/` at the end of it.

The **path** is what exists after that slash. For example, `https://www.example.com/folder/file.html` visits `example.com` and browses to the `folder` directory, and then visits the file named `file.html`.

The `.com` is called a **top-level domain** that is used to denote the location or type of organization associated with this address.

`https` in this address is the protocol that is used to connect to that web address. By protocol, I mean that HTTP utilizes `GET` or `POST` requests to ask for information from a server. For example, I can launch Google Chrome, right-click, and click **inspect**. When I open the developer tools and visit **Network**, selecting **Preserve log**, I will see Request Headers. I’ll see mentions of `GET`. This is possible in other browsers as well, using slightly different methods.

For example, when issuing a `GET` request, my computer may send the following to a server:

```
GET / HTTP/2
Host: www.harvard.edu
```

I noticed that this requests via HTTP the content served on `www.harvard.edu`.

Generally, after making a request to a server, I will receive the following in Response Headers:

```
HTTP/2 200
Content-Type: text/html
```

This approach to inspecting these logs may be a bit more complicated than need be. I can analyze the work of HTTP protocols at `cs50.dev`. For example, type the following in my terminal window:

```bash
curl -I https://www.harvard.edu/
```

I noticed that the output of this command returns all the header values of the responses of the server.

Via developer tools in my web browser, I can see all the HTTP requests when browsing to the above website.

Further, execute the following command in my terminal window:

```bash
curl -I https://harvard.edu
```

I noticed that I will see a `301` response, providing a hint to a browser of where it can find the correct website.

Similarly, execute the following in my terminal window:

```bash
curl -I http://www.harvard.edu/
```

I noticed that the `s` in `https` has been removed. The server response will show that the response is `301`, meaning that the website has permanently moved.

Similar to `301`, a code of `404` means that a specified URL has not been found. There are numerous other response codes, such as:

* `200 OK`
* `301 Moved Permanently`
* `302 Found`
* `304 Not Modified`
* `307 Temporary Redirect`
* `401 Unauthorized`
* `403 Forbidden`
* `404 Not Found`
* `418 I'm a Teapot`
* `500 Internal Server Error`
* `503 Service Unavailable`

It’s worth mentioning that `500` errors are usually my fault as the developer when they concern a product or application of my creation. This will be especially important for next week’s problem set, and potentially for my final project! However, `500` errors can also be due to infrastructure issues and third party services problems.

## HTML

**HTML** or **hypertext markup language** is made up of **tags**, each of which may have some **attributes** that describe it.

In my terminal, I typed `code hello.html` and wrote code as follows:

```html
<!DOCTYPE html>

<!-- Demonstrates HTML -->

<html lang="en">
    <head>
        <title>hello, title</title>
    </head>
    <body>
        hello, body
    </body>
</html>
```

I noticed that the `html` tag both opens and closes this file. Further, I noticed the `lang` attribute, which modifies the behavior of the `html` tag. Also, I noticed that there are both `head` tags and `body` tags. Indentation is not required but does suggest a hierarchy.

I can serve my code by typing `http-server`. This served content is now available on a very long URL. If I click it, I can visit the website generated by my own code.

When I visit this URL, I notice that the file name `hello.html` appears at the end of this URL. Further, I notice, based upon the URL, that the server is serving via port 8080.

The hierarchy of tags can be represented as follows:

![Hierarchy](https://cs50.harvard.edu/x/2024/notes/8/hierarchy.png)

Knowledge of this hierarchy will be useful later as I learn JavaScript.

The browser will read my HTML file top to bottom and left to right.

Because whitespace and indentation are effectively ignored in HTML, I will need to use `<p>` paragraph tags to open and close a paragraph. Consider the following:

```html
<!DOCTYPE html>

<!-- Demonstrates paragraphs -->

<html lang="en">
    <head>
        <title>paragraphs</title>
    </head>
    <body>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis scelerisque quam, vel hendrerit lectus viverra eu. Praesent posuere eget lectus ut faucibus. Etiam eu velit laoreet, gravida lorem in, viverra est. Cras ut purus neque. In porttitor non lorem id lobortis. Mauris gravida metus libero, quis maximus dui porta at. Donec lacinia felis consectetur venenatis scelerisque. Nulla eu nisl sollicitudin, varius velit sit amet, vehicula erat. Curabitur sollicitudin felis sit amet orci mattis, a tempus nulla pulvinar. Aliquam erat volutpat.
        </p>
        <p>
            Mauris ut dui in eros semper hendrerit. Morbi vel elit mi. Sed sit amet ex non quam dignissim dignissim et vel arcu. Pellentesque eget elementum orci. Morbi ac cursus ex. Pellentesque quis turpis blandit orci dapibus semper sed non nunc. Nulla et dolor nec lacus finibus volutpat. Sed non lorem diam. Donec feugiat interdum interdum. Vivamus et justo in enim blandit fermentum vel at elit. Phasellus eu ante vitae ligula varius aliquet. Etiam id posuere nibh.
        </p>
        <p>
            Aenean venenatis convallis ante a rhoncus. Nullam in metus vel diam vehicula tincidunt. Donec lacinia metus sem, sit amet egestas elit blandit sit amet. Nunc egestas sem quis nisl mattis semper. Pellentesque ut magna congue lorem eleifend sodales. Donec tortor tortor, aliquam vitae mollis sed, interdum ut lectus. Mauris non purus quis ipsum lacinia tincidunt.
        </p>
        <p>
            Integer at justo lacinia libero blandit aliquam ut ut dui. Quisque tincidunt facilisis venenatis. Nullam dictum odio quis lorem luctus, vel malesuada dolor luctus. Aenean placerat faucibus enim a facilisis. Maecenas eleifend quis massa sed eleifend. Ut ultricies, dui ac vulputate hendrerit, ex metus iaculis diam, vitae fermentum libero dui et ante. Phasellus suscipit, arcu ut consequat sagittis, massa urna accumsan massa, eu aliquet nulla lorem vitae arcu. Pellentesque rutrum felis et metus porta semper. Nam ac consectetur mauris.
        </p>
        <p>
            Suspendisse rutrum vestibulum odio, sed venenatis purus condimentum sed. Morbi ornare tincidunt augue eu auctor. Vivamus sagittis ac lectus at aliquet. Nulla urna mauris, interdum non nibh in, vehicula porta enim. Donec et posuere sapien. Pellentesque ultrices scelerisque ipsum, vel fermentum nibh tincidunt et. Proin gravida porta ipsum nec scelerisque. Vestibulum fringilla erat at turpis laoreet, nec hendrerit nisi scelerisque.
        </p>
        <p>
            Sed quis malesuada mi. Nam id purus quis augue sagittis pharetra. Nulla facilisi. Maecenas vel fringilla ante. Cras tristique, arcu sit amet blandit auctor, urna elit ultricies lacus, a malesuada eros dui id massa. Aliquam sem odio, pretium vel cursus eget, scelerisque at urna. Vestibulum posuere a turpis consectetur consectetur. Cras consequat, risus quis tempor egestas, nulla ipsum ornare erat, nec accumsan nibh lorem nec risus. Integer at iaculis lacus. Integer congue nunc massa, quis molestie felis pellentesque vestibulum. Nulla odio tortor, aliquam nec quam in, ornare aliquet sapien.
        </p>
    </body>
</html>
```

I noticed that paragraphs start with a `<p>` tag and end with a `</p>` tag.

HTML allows for the representation of headings:

```html
<!DOCTYPE html>

<!-- Demonstrates headings (for chapters, sections, subsections, etc.) -->

<html lang="en">

    <head>
        <title>headings</title>
    </head>

    <body>

        <h1>One</h1>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis scelerisque quam, vel hendrerit lectus viverra eu. Praesent posuere eget lectus ut faucibus. Etiam eu velit laoreet, gravida lorem in, viverra est. Cras ut purus neque. In porttitor non lorem id lobortis. Mauris gravida metus libero, quis maximus dui porta at. Donec lacinia felis consectetur venenatis scelerisque. Nulla eu nisl sollicitudin, varius velit sit amet, vehicula erat. Curabitur sollicitudin felis sit amet orci mattis, a tempus nulla pulvinar. Aliquam erat volutpat.
        </p>

        <h2>Two</h2>
        <p>
            Mauris ut dui in eros semper hendrerit. Morbi vel elit mi. Sed sit amet ex non quam dignissim dignissim et vel arcu. Pellentesque eget elementum orci. Morbi ac cursus ex. Pellentesque quis turpis blandit orci dapibus semper sed non nunc. Nulla et dolor nec lacus finibus volutpat. Sed non lorem diam. Donec feugiat interdum interdum. Vivamus et justo in enim blandit fermentum vel at elit. Phasellus eu ante vitae ligula varius aliquet. Etiam id posuere nibh.
        </p>

        <h3>Three</h3>
        <p>
            Aenean venenatis convallis ante a rhoncus. Nullam in metus vel diam vehicula tincidunt. Donec lacinia metus sem, sit amet egestas elit blandit sit amet. Nunc egestas sem quis nisl mattis semper. Pellentesque ut magna congue lorem eleifend sodales. Donec tortor tortor, aliquam vitae mollis sed, interdum ut lectus. Mauris non purus quis ipsum lacinia tincidunt.
        </p>

        <h4>Four</h4>
        <p>
            Integer at justo lacinia libero blandit aliquam ut ut dui. Quisque tincidunt facilisis venenatis. Nullam dictum odio quis lorem luctus, vel malesuada dolor luctus. Aenean placerat faucibus enim a facilisis. Maecenas eleifend quis massa sed eleifend. Ut ultricies, dui ac vulputate hendrerit, ex metus iaculis diam, vitae fermentum libero dui et ante. Phasellus suscipit, arcu ut consequat sagittis, massa urna accumsan massa, eu aliquet nulla lorem vitae arcu. Pellentesque rutrum felis et metus porta semper. Nam ac consectetur mauris.
        </p>

        <h5>Five</h5>
        <p>
            Suspendisse rutrum vestibulum odio, sed venenatis purus condimentum sed. Morbi ornare tincidunt augue eu auctor. Vivamus sagittis ac lectus at aliquet. Nulla urna mauris, interdum non nibh in, vehicula porta enim. Donec et posuere sapien. Pellentesque ultrices scelerisque ipsum, vel fermentum nibh tincidunt et. Proin gravida porta ipsum nec scelerisque. Vestibulum fringilla erat at turpis laoreet, nec hendrerit nisi scelerisque.
        </p>

        <h6>Six</h6>
        <p>
            Sed quis malesuada mi. Nam id purus quis augue sagittis pharetra. Nulla facilisi. Maecenas vel fringilla ante. Cras tristique, arcu sit amet blandit auctor, urna elit ultricies lacus, a malesuada eros dui id massa. Aliquam sem odio, pretium vel cursus eget, scelerisque at urna. Vestibulum posuere a turpis consectetur consectetur. Cras consequat, risus quis tempor egestas, nulla ipsum ornare erat, nec accumsan nibh lorem nec risus. Integer at iaculis lacus. Integer congue nunc massa, quis molestie felis pellentesque vestibulum. Nulla odio tortor, aliquam nec quam in, ornare aliquet sapien.
        </p>

    </body>

</html>
```

I noticed that `<h1>`, `<h2>`, and `<h3>` denote different levels of headings.

I can also create unordered lists within HTML:

```html
<!DOCTYPE html>

<!-- Demonstrates (unordered) lists -->

<html lang="en">
    <head>
        <title>list</title>
    </head>
    <body>
        <ul>
            <li>foo</li>
            <li>bar</li>
            <li>baz</li>
        </ul>
    </body>
</html>
```

I noticed that the `<ul>` tag creates an unordered list containing three items.

I can also create ordered lists within HTML:

```html
<!DOCTYPE html>

<!-- Demonstrates (ordered) lists -->

<html lang="en">
    <head>
        <title>list</title>
    </head>
    <body>
        <ol>
            <li>foo</li>
            <li>bar</li>
            <li>baz</li>
        </ol>
    </body>
</html>
```

I noticed that the `<ol>` tag creates an ordered list containing three items.

I can also create a table in HTML:

```html
<!DOCTYPE html>

<!-- Demonstrates table -->

<html lang="en">
    <head>
        <title>table</title>
    </head>
    <body>
        <table>
            <tr>
                <td>1</td>
                <td>2</td>
                <td>3</td>
            </tr>
            <tr>
                <td>4</td>
                <td>5</td>
                <td>6</td>
            </tr>
            <tr>
                <td>7</td>
                <td>8</td>
                <td>9</td>
            </tr>
            <tr>
                <td>*</td>
                <td>0</td>
                <td>#</td>
            </tr>
        </table>
    </body>
</html>
```

Tables also have tags that open and close each element within. Also, I noticed the syntax for comments in HTML.

Images can also be utilized within HTML:

```html
<!DOCTYPE html>

<!-- Demonstrates image -->

<html lang="en">
    <head>
        <title>image</title>
    </head>
    <body>
        <img alt="photo of bridge" src="bridge.png">
    </body>
</html>
```

I noticed that `src="bridge.png"` indicates the path where the image file can be located.

Videos can also be included in HTML:

```html
<!DOCTYPE html>

<!-- Demonstrates video -->

<html lang="en">
    <head>
        <title>video</title>
    </head>
    <body>
        <video controls muted>
            <source src="video.mp4" type="video/mp4">
        </video>
    </body>
</html>
```

I noticed that the `type` attribute designates that this is a video of type mp4. Further, I noticed how `controls` and `muted` are passed to video.

I can also link between various web pages:

```html
<!DOCTYPE html>

<!-- Demonstrates link -->

<html lang="en">
    <head>
        <title>link</title>
    </head>
    <body>
      Visit <a href="image.html">Harvard</a>.
    </body>
</html>
```

I noticed that the `<a>` or anchor tag is used to make Harvard a linkable text.

I can also create forms reminiscent of Google’s search:

```html
<!DOCTYPE html>

<!-- Demonstrates form -->

<html lang="en">
    <head>
        <title>search</title>
    </head>
    <body>
        <form action="https://www.google.com/search" method="get">
            <input name="q" type="search">
            <input type="submit" value="Google Search">
        </form>
    </body>
</html>
```

I noticed that a form tag opens and provides the attribute of what action it will take. The input field is included, passing the name `q` and the type as `search`.

I can make this search better as follows:

```html
<!DOCTYPE html>

<!-- Demonstrates additional form attributes -->

<html lang="en">
    <head>
        <title>search</title>
    </head>
    <body>
        <form action="https://www.google.com/search" method="get">
            <input autocomplete="off" autofocus name="q" placeholder="Query" type="search">
            <button>Google Search</button>
        </form>
    </body>
</html>
```

I noticed that `autocomplete` is turned off. `autofocus` is enabled.

I’ve seen just a few of many HTML elements I can add to my site. If I have an idea for something to add to my site that I haven’t seen yet (a button, an audio file, etc.) try Googling “X in HTML” to find the right syntax! Similarly, I can use cs50.ai to help me discover more HTML features!

## Regular Expressions

**Regular expressions** or **regexes** are a means by which to ensure that user-provided data fits a specific format.

I can implement my own registration page that utilizes regexes as follows:

```html
<!DOCTYPE html>

<!-- Demonstrates type="email" -->

<html lang="en">
    <head>
        <title>register</title>
    </head>
    <body>
        <form>
            <input autocomplete="off" autofocus name="email" placeholder="Email" type="email">
            <button>Register</button>
        </form>
    </body>
</html>
```

I noticed that the input tag includes attributes that designate that this is of type `email`. The browser knows to double-check that the input is an email address.

While the browser uses these built-in attributes to check for an email address, I can add a `pattern` attribute to ensure that only specific data ends up in the email address:

```html
<!DOCTYPE html>

<!-- Demonstrates pattern attribute for email -->

<html lang="en">
    <head>
        <title>register</title>
    </head>
    <body>
        <form>
            <input autocomplete="off" autofocus name="email" pattern=".+@.+\.edu" placeholder="Email" type="email">
            <button>Register</button>
        </form>
    </body>
</html>
```

I noticed that the `pattern` attribute is handed a regular expression to denote that the email address must include an `@` symbol and a `.edu`.

I can learn more about regular expressions from Mozilla’s documentation. Further, I can make inquiries to cs50.ai for hints.

## CSS

**CSS**, or **cascading style sheet**, is a style sheet language that allows me to fine-tune the aesthetics of my HTML files.

CSS is filled with **properties**, which include key-value pairs.

In my terminal, I typed `code home.html` and wrote code as follows:

```html
<!DOCTYPE html>

<!-- Demonstrates inline CSS with P tags -->

<html lang="en">
    <head>
        <title>css</title>
    </head>
    <body>
        <p style="font-size: large; text-align: center;">
            John Harvard
        </p>
        <p style="font-size: medium; text-align: center;">
            Welcome to my home page!
        </p>
        <p style="font-size: small; text-align: center;">
            Copyright &#169; John Harvard
        </p>
    </body>
</html>
```

I noticed that some style attributes are provided to the `<p>` tags. The `font-size` is set to large, medium, or small. Then `text-align` is set to center.

While correct, the above is not well-designed. I can remove redundancy by modifying my code as follows:

```html
<!DOCTYPE html>

<!-- Removes outer DIV -->

<html lang="en">
    <head>
        <title>css</title>
    </head>
    <body style="text-align: center">
        <div style="font-size: large">
            John Harvard
        </div>
        <div style="font-size: medium">
            Welcome to my home page!
        </div>
        <div style="font-size: small">
            Copyright &#169; John Harvard
        </div>
    </body>
</html>
```

I noticed that `<div>` tags are used to divide up this HTML file into specific regions. `text-align: center` is invoked on the entire body of the HTML. Because everything inside body is a child of body, the center attribute cascades down to those children.

It turns out that there are newer semantic tags included in HTML. I can modify my code as follows:

```html
<!DOCTYPE html>

<!-- Demonstrates class selectors -->

<html lang="en">
    <head>
        <style>

            .centered
            {
                text-align: center;
            }

            .large
            {
                font-size: large;
            }

            .medium
            {
                font-size: medium;
            }

            .small
            {
                font-size: small;
            }

        </style>
        <title>css</title>
    </head>
    <body class="centered">
        <header class="large">
            John Harvard
        </header>
        <main class="medium">
            Welcome to my home page!
        </main>
        <footer class="small">
            Copyright &#169; John Harvard
        </footer>
    </body>
</html>
```

I noticed all the style tags are placed up in the head in the style tag wrapper. Also, I noticed that I’ve assigned classes, called `centered`, `large`, `medium`, and `small` to my elements, and that I select those classes by placing a dot before the name, as in `.centered`.

It turns out that I can move all my style code into a special file called a CSS file. I can create a file called `style.css` and paste my classes there:

```css
.centered
{
    text-align: center;
}

.large
{
    font-size: large;
}

.medium
{
    font-size: medium;
}

.small
{
    font-size: small;
}
```

I noticed that this is verbatim what appeared in my HTML file.

I then can tell the browser where to locate the CSS for this HTML file:

```html
<!DOCTYPE html>

<!-- Demonstrates external stylesheets -->

<html lang="en">
    <head>
        <link href="style.css" rel="stylesheet">
        <title>css</title>
    </head>
    <body class="centered">
        <header class="large">
            John Harvard
        </header>
        <main class="medium">
            Welcome to my home page!
        </main>
        <footer class="small">
            Copyright &#169; John Harvard
        </footer>
    </body>
</html>
```

I noticed that `style.css` is linked to this HTML file as a stylesheet, telling the browser where to locate the styles I created.

## Frameworks

Similar to third-party libraries I can leverage in Python, there are third-party libraries called **frameworks** that I can utilize with my HTML files.

**Bootstrap** is one of these frameworks that I can use to beautify my HTML and easily perfect design elements such that my pages are more readable.

Bootstrap can be utilized by adding the following link tag in the head of my html file:

```html
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
    <title>bootstrap</title>
</head>
```

Consider the following HTML:

```html
<!DOCTYPE html>

<!-- Demonstrates table -->

<html lang="en">
    <head>
        <title>phonebook</title>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Number</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Kelly</td>
                    <td>+1-617-495-1000</td>
                </tr>
                <tr>
                    <td>David</td>
                    <td>+1-617-495-1000</td>
                </tr>
                <tr>
                    <td>John</td>
                    <td>+1-949-468-2750</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
```

I noticed how, when looking at a served version of this page, it’s quite plain.

Now consider the following HTML that implements the use of Bootstrap:

```html
<!DOCTYPE html>

<!-- Demonstrates table with Bootstrap -->

<html lang="en">
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
        <title>phonebook</title>
    </head>
    <body>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Number</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Kelly</td>
                    <td>+1-617-495-1000</td>
                </tr>
                <tr>
                    <td>David</td>
                    <td>+1-949-468-2750</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
```

I noticed how much prettier this website is now.

I can learn more about this in the Bootstrap Documentation.

## JavaScript

**JavaScript** is another programming language that allows for interactivity within web pages.

Consider the following implementation of `hello.html` that includes both JavaScript and HTML:

```html
<!DOCTYPE html>

<!-- Demonstrates onsubmit -->

<html lang="en">
    <head>
        <script>

            function greet()
            {
                alert('hello, ' + document.querySelector('#name').value);
            }

        </script>
        <title>hello</title>
    </head>
    <body>
        <form onsubmit="greet(); return false;">
            <input autocomplete="off" autofocus id="name" placeholder="Name" type="text">
            <input type="submit">
        </form>
    </body>
</html>
```

I noticed how this form uses an `onsubmit` property to trigger a script found at the top of the file. The script uses `alert` to create an alert pop-up. `document.querySelector('#name').value` selects the textbox with the id `name` on the page and obtains the value typed by the user.

Generally, it’s considered bad design to mix `onsubmit` and JavaScript. I can advance my code as follows:

```html
<!DOCTYPE html>

<!-- Demonstrates DOMContentLoaded -->

<html lang="en">
    <head>
        <script>

            document.addEventListener('DOMContentLoaded', function() {
                document.querySelector('form').addEventListener('submit', function(e) {
                    alert('hello, ' + document.querySelector('#name').value);
                    e.preventDefault();
                });
            });

        </script>
        <title>hello</title>
    </head>
    <body>
        <form>
            <input autocomplete="off" autofocus id="name" placeholder="Name" type="text">
            <input type="submit">
        </form>
    </body>
</html>
```

I noticed that this version of the code creates an `addEventListener` to listen to the form submit being triggered. I noticed how `DOMContentLoaded` ensures that the whole page is loaded before executing the JavaScript.

I can advance this code as follows:

```html
<!DOCTYPE html>

<!-- Demonstrates keyup and template literals -->

<html lang="en">
    <head>
        <script>

            document.addEventListener('DOMContentLoaded', function() {
                let input = document.querySelector('input');
                input.addEventListener('keyup', function(event) {
                    let name = document.querySelector('p');
                    if (input.value) {
                        name.innerHTML = `hello, ${input.value}`;
                    }
                    else {
                        name.innerHTML = 'hello, whoever you are';
                    }
                });
            });

        </script>
        <title>hello</title>
    </head>
    <body>
        <form>
            <input autocomplete="off" autofocus placeholder="Name" type="text">
        </form>
        <p></p>
    </body>
</html>
```

I noticed that the DOM is dynamically updated in memory as the user types out a name. If there is a value inside input, upon the `keyup` on the keyboard, the DOM is updated. Otherwise, default text is presented.

JavaScript allows me to dynamically read and modify the html document loaded into memory such that the user need not reload to see changes.

Consider the following HTML:

```html
<!DOCTYPE html>

<!-- Demonstrates programmatic changes to style -->

<html lang="en">
    <head>
        <title>background</title>
    </head>
    <body>
        <button id="red">R</button>
        <button id="green">G</button>
        <button id="blue">B</button>
        <script>

            let body = document.querySelector('body');
            document.querySelector('#red').addEventListener('click', function() {
                body.style.backgroundColor = 'red';
            });
            document.querySelector('#green').addEventListener('click', function() {
                body.style.backgroundColor = 'green';
            });
            document.querySelector('#blue').addEventListener('click', function() {
                body.style.backgroundColor = 'blue';
            });

        </script>
    </body>
</html>
```

I noticed that JavaScript listens for when a specific button is clicked. Upon such a click, certain style attributes on the page are changed. `body` is defined as the body of the page. Then, an event listener waits for the clicking of one of the buttons. Then, the `body.style.backgroundColor` is changed.

Similarly, consider the following:

```html
<!DOCTYPE html>

<html lang="en">
    <head>
        <script>

            // Toggles visibility of greeting
            function blink()
            {
                let body = document.querySelector('body');
                if (body.style.visibility == 'hidden')
                {
                    body.style.visibility = 'visible';
                }
                else
                {
                    body.style.visibility = 'hidden';
                }
            }

            // Blink every 500ms
            window.setInterval(blink, 500);

        </script>
        <title>blink</title>
    </head>
    <body>
        hello, world
    </body>
</html>
```

I noticed that `window.setInterval(blink, 500)` calls the `blink` function every 500 milliseconds.

I can also use JavaScript to access my location:

```html
<!DOCTYPE html>

<!-- Demonstrates geolocation -->

<html lang="en">
    <head>
        <title>geolocation</title>
    </head>
    <body>
        <script>

            navigator.geolocation.getCurrentPosition(function(position) {
                document.write(position.coords.latitude + ", " + position.coords.longitude);
            });

        </script>
    </body>
</html>
```

I noticed that `navigator.geolocation` is utilized. `document.write` writes the coordinates to the web page.

## Summing Up

In this lesson, I learned how to build my own web pages. Specifically, I delved into…

* Routers
* DNS
* HTTP and HTTPS
* HTML
* CSS
* Bootstrap
* JavaScript

This was CS50 Week 8 HTML, CSS, JavaScript.
