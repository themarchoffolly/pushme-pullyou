
0. Hi, this is David, at gitpitch.com...the home of "modern slide deck solutions" for developers.

1. This presentation introduces GitPitch Snap Layouts. A flexible
layout system for your slide content. Snap layouts let you create custom
slide designs. Directly within the markdown for your slide deck.

2. Snap layouts are uniquely supported by GitPitch markdown. Custom slide
designs are achieved using a simple syntax that delivers flexible layouts.

3. The layout system divides each slide into a 3x3 grid. Each
distinct area on the grid can be addressed using compass coordinates,
for example, north, south, east, west, etc.

So lets start by taking a quick look at some samples slides so we can see
GitPitch snap layouts in action.

4. For this series of sample slides I have chosen GraphQL as my subject matter.
But GraphQL is not the focus here. My goal is to demonstrate
GitPitch's capabilities for delivering sophisticated slide designs, the kind of
slides any developer would be proud to present at a tech conference or meetup.

The first sample slide design is pretty simple. But even here
snap layouts are helping to ensure an oversized image fits nicely within the
confines of the slide. We will see exactly how that is achieved in a moment.

5. This next sample slide takes advantage of the east-and-west positions of
the snap-layouts grid to deliver a split-screen effect.

6. And here it is again with an added splash of color.

7. Our third sample slide takes advantage of the north-and-south positions of
the snap layouts grid. We also get our first indication that snap layouts
work with a wide range of content types. Including code.

8. This next sample slide takes advantage of the grid to present a series
of steps spanning the southern sections of our slide. It also provides evidence
that snap layouts work seamlessly with GitPitch markdown widgets. You can
learn more about Markdown Widgets in the GitPitch docs.

9. Our fifth and final sample slide demonstrates a wide range
of capabilities - custom background, custom positioning, custom sizing,
and even auto-generated UML diagrams. Pretty cool!

10. Now that we have seen some sample slides it's time to look at the markdown
syntax that was used to deliver these flexible slide designs.

11. Lets start with some basic slide markdown including a simple heading,
a Font Awesome markdown widget, and some standard image syntax.

12. This is how that slide markdown is rendered by GitPitch. I think
you'll agree, something is not quite right. The image is overflowing the slide.

13. Lets take a quick look at our slide markdown once again.

13.0.0 And see what happens when we wrap the entire block of markdown in
snap-tags.

14. Much better! To understand what just happened, lets take a quick look at
the basic syntax for snap-layouts.

15. To activate snap-layouts for any markdown block simply wrap the block in
opening and closing snap tags. The first property on the opening tag always
indicates a position on the snap-layouts grid. The second property is
typically a span property value that is used to control the width and height
of the snapped content.

16. Looking again at our slide markdown, we can now understand why it
renders so much more cleanly when wrapped in snap-tags. The span property
value controls the size of the image ensuring it fits on our slide. Ok, next
we're going to play with the positioning of our snapped-content.

17. We have just changed the snap-position property on our opening snap tag
from midpoint to west. Lets see what happens when our updated slide is rendered
by GitPitch.

18. Nice! By simply updating the snap-position property on our opening snap tag
- with zero changes to the markdown content itself - we have the beginnings of
a whole new slide design.

19. Before diving more deeply into snap-layouts I want to quickly introduce
a nice feature for controlling the background color of GitPitch slides.

20.0.0 Here is our sample slide markdown once again.

20.0.1 And here we have activated a color delimiter for our slide. In this
case, the entire background for our sample slide would turn yellow.

21. But the color delimiter supports more than just solid background colors.

21.0.0 It also supports color gradients. Powered by CSS color gradients.
Which unlocks all kinds of fun.

22. Our updated sample slide with a custom background gradient is looking good.

23. Ok, it's now time to complete the snap-layouts design for our sample slide.

24. We are going to add the following markdown snippet to our sample slide.

25. See how the markdown heading has been added to the north-east of the
snap-layouts grid. Or top-right corner of our slide.

26. We are not constrained to working with just basic markdown content. Here
we can see further updates to our sample markdown. This time we are using a
GitPitch markdown widget to render a PlantUML diagram based on a plain-text
description of that diagram found within file indicated.

27. Very nice! By using a simple markdown widget plus snap-layouts we have
been able to generate, position, and size a pixel-perfect UML diagram
on our sample slide.

28. So lets quickly revisit the underlying markdown for our slide.
Here's it is before introducing snap-tags. If you have ever worked with
markdown, it should all look pretty familiar. Simple headings. Simple image
syntax. And a couple of GitPitch markdown widgets.

28.0.0 The addition of snap-tags to the markdown is what delivers our
custom slide design.

29. And here it is one final time. A great looking slide created using
markdown. With a custom layout made possible by GitPitch snap-layouts.

30. If you have ever worked with traditional presentation tools like PowerPoint
then you already understand the benefits of drag-and-drop to deliver custom slide
designs. And if you have ever worked with traditional markdown presentation
tools, then you already understand the benefits and simplicity of auto-layout.
With snap-layouts, GitPitch presentation authors enjoy the best of both worlds.

31. That's it for this presentation. I hope you've enjoyed this brief introduction
to GitPitch Snap Layouts. Hopefully you now have one more compelling reason
to consider GitPitch for your next developer slide deck. Thank you.
