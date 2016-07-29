#HSLIDE

##The Kitchen Sink
#####<span style="font-family:Helvetica Neue; font-weight:bold">A <span style="color:#e49436">Git</span>Pitch Feature Tour</span>

#HSLIDE

##Tip!
For best viewing experience press **F** key to go fullscreen.

#HSLIDE

##Markdown Slides
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>


#VSLIDE

####Use GitHub Flavored Markdown
####For Slide Content Creation

<br>

The same tool you use to create project **READMEs** and **Wikis** for your GitHub repos.

#HSLIDE

##Code Slides
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>

#VSLIDE

####Use Markdown Code Blocks

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
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>

#VSLIDE

####GitHub GIST
####Building Blocks For Your Presentation

<br>

Enjoy 100% reusable code snippets, excellent syntax highlighting, code indentation and styling. 

#VSLIDE?gist=8da53731fd54bab9d5c6

#VSLIDE?gist=28ee3d19ddef9d51b15adbdfe9ed48da

#HSLIDE

##Image Slides
##[ Inline ]
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>

#VSLIDE

####Make A Visual Statement

<br>

Use inline images to lend a *visual punch* to your slideshow presentations.


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

#HSLIDE

##Image Slides
##[ Background ]
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>

#VSLIDE

####Make A Bold Visual Statement

<br>

Use high-resolution background images for maximum impact.

#VSLIDE?image=assets/victory.jpg

#VSLIDE?image=assets/127.jpg


#HSLIDE

##Video Slides
##[ Inline ]
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>

#VSLIDE

####Bring Your Presentations Alive

<br>

Embed *YouTube*, *Vimeo* and *MP4* inline on any slide.

#VSLIDE

![YouTube Video](https://www.youtube.com/embed/mkiDkkdGGAQ)

#VSLIDE

![Vimeo Video](https://player.vimeo.com/video/111525512)

#VSLIDE

![MP4 Video](http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4)


#HSLIDE

##Video Slides
##[ Background ]
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>

#VSLIDE

####Maximize The Viewer Experience

<br>

Go fullscreen with *YouTube*, *Vimeo* and *MP4* videos.

#VSLIDE?video=https://www.youtube.com/embed/mkiDkkdGGAQ

#VSLIDE?video=https://player.vimeo.com/video/111525512

#HSLIDE

##Math Notation Slides
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>

#VSLIDE


####Beautiful Math Rendered Beautifully

<br>

Use *LaTeX* and *MathML* markup powered by <a target="_blank" href="https://www.mathjax.org/">MathJax</a>.

#VSLIDE

Expand the following:
\begin{align}
  (x+1)^2
    &\cssId{Step1}{= (x+1)(x+1)}\\
    &\cssId{Step2}{= x(x+1) + 1(x+1)}\\
    &\cssId{Step3}{= (x^2+x) + (x+1)}\\
    &\cssId{Step4}{= x^2 + (x + x) + 1}\\
    &\cssId{Step5}{= x^2+2x+1}\\
\end{align}

#VSLIDE

$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$

#VSLIDE

$$\begin{matrix} 1 & x & x^2 \\ 1 & y & y^2 \\ 1 & z & z^2 \\ \end{matrix}$$

#VSLIDE

$$\begin{array}{c|lcr} n & \text{Left} & \text{Center} & \text{Right} \\ \hline 1 & 0.24 & 1 & 125 \\ 2 & -1 & 189 & -8 \\ 3 & -20 & 2000 & 1+10i \end{array}$$

#HSLIDE

##Slide Fragments
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>

#VSLIDE

####Reveal Slide Concepts Piecemeal

<br>

Step through slide content in sequence to slowly reveal the bigger picture.

#VSLIDE

- Java
- Groovy     <!-- .element: class="fragment" -->
- Kotlin     <!-- .element: class="fragment" -->
- Scala     <!-- .element: class="fragment" -->
- The JVM rocks! <!-- .element: class="fragment" -->

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
##PITCHME.yaml Settings
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>

#VSLIDE

####Stamp Your Own Look and Feel

<br>

Set a default theme, custom logo, background image, and preferred code syntax highlighting style.

#VSLIDE

####Customize Slideshow Behavior

<br>

Enable auto-slide with custom intervals, looping, and RTL.


#HSLIDE
##Slideshow Keyboard Controls
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>

#VSLIDE

####Try Out These Great Features Now!

<br>

| Mode | On Key | Off Key |
| ---- | :------: | :--------: |
| Fullscreen | F |  Esc |
| Overview | O |  O |
| Blackout | B |  B |
| Help | ? |  Esc |

#HSLIDE
##Slideshow Theme Switcher
<span style="font-size:0.6em; color:gray">Available bottom-left of screen.</span> |
<span style="font-size:0.6em; color:gray">Start switching themes right now!</span>

#HSLIDE

##Slideshow Extras
<span style="font-size:0.6em; color:gray">See slides below for examples.</span> |
<span style="font-size:0.6em; color:gray">See <a href="#" target="_blank">GitPitch Wiki</a> for details.</span>

#VSLIDE

####Available For Every Slideshow

<br>

- Print To PDF Document
- GitHub Badge Markdown Snippet 
- Embed HTML Snippet
- Share By E-Mail And Social Media

#HSLIDE

##GO FOR IT.
##JUST ADD <span style="color:#e49436; text-transform: none">PITCHME.md</span> ;)


