#HSLIDE

##The Kitchen Sink
#####<span style="font-family:Helvetica Neue; font-weight:bold">A <span style="color:#e49436">Git</span>Pitch Feature Tour</span>

#HSLIDE

##Markdown Slides
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> For Details</span>

#VSLIDE

#### Use GitHub Flavored Markdown
#### For Slide Content Creation

<br>

The same tool you use to create project **READMEs** and **Wikis** for your GitHub repos.

#HSLIDE

##Code Slides
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> For Details</span>

#VSLIDE

#### Use Markdown Code Blocks

<br>

And enjoy code syntax highlighting powered by <a target="_blank" href="highlight.js](https://highlightjs.org">highlight.js</a>.

#VSLIDE

```JavaScript
// JavaScript Code Block

$('button').click(function(){
    $('h1, h2, p').addClass('blue')
    $('div').removeClass('important')
    $('h3').toggleClass('error')
    $('#foo').attr('alt', 'Lorem Ipsum')
});
```

#VSLIDE

```scala
// Scala Code Block

HashMap params = HashMap(n -> 10, mean -> 5)

// Define executable for R stats#rnorm function call.
OCPUTask task = OCPU.R()
                    .pkg("stats")
                    .function("rnorm")
                    .input(params.asJava)
                    .library()
```

#HSLIDE

##GIST Slides
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> For Details</span>

#VSLIDE

#### GitHub GIST
#### Building Blocks For Your Presentation

<br>

Enjoy 100% reusable code snippets, excellent syntax highlighting, code indentation and styling. 

#VSLIDE?gist=8da53731fd54bab9d5c6

#VSLIDE?gist=28ee3d19ddef9d51b15adbdfe9ed48da

#HSLIDE

##Image Slides
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> For Details</span>

#VSLIDE

#### Make A Visual Statement

<br>

Use inline and background images to lend a *visual punch* to your presentations.


#VSLIDE

<span style="color:gray; font-size:0.7em">Inline Image at <b>Absolute URL</b></span>

![Image-Absolute](assets/octocat-privateinvestocat.jpg)

<span style="color:gray; font-size: 0.5em;">the <b>Private Investocat</b> by <a href="https://github.com/jeejkang" target="_blank">jeejkang</a></span>


#VSLIDE

<span style="color:gray; font-size:0.7em">Inline Image at GitHub Repo <b>Relative URL</b></span>

![Image-Absolute](assets/octocat-de-los-muertos.jpg)

<span style="color:gray; font-size:0.5em">the <b>Octocat-De-Los-Muertos</b> by <a href="https://github.com/cameronmcefee" target="_blank">cameronmcefee</a></span>


#VSLIDE

<span style="color:gray; font-size:0.7em"><b>Animated GIFs</b> Work Too!</span>

![Image-Relative](assets/octocat-daftpunkocat.gif)

<span style="color:gray; font-size:0.5em">the <b>Daftpunktocat-Guy</b> by <a href="https://github.com/jeejkang" target="_blank">jeejkang</a></span>


#VSLIDE?image=assets/victory.jpg

<br><br><br><br><br><br><br><br><br><br><br><br>
<span style="color:white">Use background images for optimal viewing.</span> 

#HSLIDE?image=assets/video-play.jpg

<span style="font-size:1.3em"><span style="color:white">Video</span><span style="color:white"> Slides</span></span>
<br><br><br><br><br>
<br><br><br><br><br>
<span style="font-size:0.9em; color:#e49436">Embed <span style="color:white">YouTube + </span> MP4 <span style="color:white">+ Vimeo </span></span>

<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch How-To</a> For Details</span>

#VSLIDE

![Cartoon Video](https://www.youtube.com/embed/mkiDkkdGGAQ)

#VSLIDE

![Cartoon Video](http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4)

#VSLIDE

![Cartoon Video](https://player.vimeo.com/video/111525512)


#HSLIDE

Math Formula Slides

#VSLIDE

$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$

#HSLIDE

Slide Fragments

#VSLIDE

- Java
- JavaScript <!-- .element: class="fragment" -->
- Kotlin     <!-- .element: class="fragment" -->
- Go         <!-- .element: class="fragment" -->
- Scala      <!-- .element: class="fragment" -->

#VSLIDE

<table>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr class="fragment">
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
  <tr class="fragment">
    <td>John</td>
    <td>Doe</td>
    <td>80</td>
  </tr>
</table>


#HSLIDE

Slide Custom Backgrounds

#VSLIDE?image=assets/127.jpg

#VSLIDE?image=assets/wally-presentation.jpg

#VSLIDE
- Video-YouTube
#VSLIDE
- Video-Vimeo
#VSLIDE
- Video-MP$

#HSLIDE

Slideshow PITCHME.yaml Customizations

-background
-loop
-mathjax
-autoslide
-etc


#HSLIDE

Slideshow Controls

#VSLIDE
- Full Screen
#VSLIDE
- Overview
#VSLIDE
- Pause

#HSLIDE

Slideshow Theme Switching

#HSLIDE

Slideshow Printing

#HSLIDE

Slideshow Embedding

#HSLIDE

Slideshow Sharing

#HSLIDE

####Slideshow Features Quick Look

- GitHub Flavored Markdown <!-- .element: class="fragment" data-fragment-index="1" -->
- Code Blocks & GISTs <!-- .element: class="fragment" data-fragment-index="2" -->
- Math Formulas <!-- .element: class="fragment" data-fragment-index="3" -->
- Slide Fragments <!-- .element: class="fragment" data-fragment-index="4" -->
- Image Support <!-- .element: class="fragment" data-fragment-index="5" -->
- Video Support <!-- .element: class="fragment" data-fragment-index="6" -->
- Custom Backgrounds <!-- .element: class="fragment" data-fragment-index="7" -->
- YAML Customizations <!-- .element: class="fragment" data-fragment-index="8" -->
- And a whole lot more... <!-- .element: class="fragment" data-fragment-index="9" -->.

