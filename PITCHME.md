# Try render MD block 1

```markdown
#### Hello
```

#### End of test slide.

---

# Try render MD block 2

```markdown
<![CDATA[
#### Hello
]]>
-->
```

#### End of test slide 2.

---

# Try render MD block 3

<pre><code>
#### Hello
@title[it has broken code higlight]
## Say something here

 ```scala
 object GitPitch{
   val IsAwesome=true
 }
 ```
</code><pre>

#### End of test slide 3.

---

@title[it has code higlight]
## it has code higlight

```scala
object GitPitch{
  val IsAwesome=true
}
```

---

@title[it has broken code higlight]

## it has broken code higlight

```scala
object GitPitch{
  val IsAwesome=true
}
```

---

@title[What happens here?]

## what happens here, no title?

```scala
object GitPitch{
  val IsAwesome=true
}
```
