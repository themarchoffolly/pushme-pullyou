This is `x = 10;` some code.

---

# Start Here

---

```javascript
var a = 0
var b = 1
```
---?gist=onetapbeyond/494e0fecaf0d6a2aa2acadfb8eb9d6e8&lang=Scala&title=GIST: Scala Snippet

@[25-29](Init Spark cluster data source)
@[41-53](Build RDD[AWSTask] from source)
@[57-62](Delegate RDD[AWSTask] to AWS Lambda)

---?gist=onetapbeyond/8da53731fd54bab9d5c6&lang=Groovy&title=GIST: Groovy Snippet

@[6-9]
@[11-12]
@[14-18]

---?gist=onetapbeyond/3b893fa75304db752741145d94d1c2c7&lang=JS&title=GIST: JavaScript Snippet

@[1](React components partition the UI.)
@[1](Each is independent, and reusable.)
@[2-5](React callback on state change.)

---

+++
@title[Sample Block]

```python
from time import localtime

activities = {8: 'Sleeping', 9: 'Commuting', 17: 'Working',
              18: 'Commuting', 20: 'Eating', 22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'
```

###### Code-blocks let you present any <p> **static code** with auto-syntax highlighting

---

### Code-Blocks
##### Using
#### **Code-Presenting**

![Press Down Key](assets/down-arrow.png)

+++
@title[Sample Code Presenting]

```python
from time import localtime

activities = {8: 'Sleeping', 9: 'Commuting', 17: 'Working',
              18: 'Commuting', 20: 'Eating', 22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'
```

@[1]
@[3-4]
@[6-7]
@[9-14]

###### Use code-presenting to **step-thru** code <p> from directly within your presentation 

---

@title[Sample With Annotations]

```python
from time import localtime

activities = {8: 'Sleeping', 9: 'Commuting', 17: 'Working',
              18: 'Commuting', 20: 'Eating', 22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'
```

@[1](Python from..import statement)
@[3-4](Python dictionary initialization block)
@[6-7](Python working with time)
@[9-14](Python for..else statement)

---
@title[Working with Source Files]

### Naturally
### Code-Presenting
### works in exactly the same way on [Code-Delimiter Slides](https://github.com/gitpitch/gitpitch/wiki/Code-Delimiter-Slides) as it does on [Code-Blocks](https://github.com/gitpitch/gitpitch/wiki/Code-Slides).

---
@title[Code Delimiter Syntax]

### Code-Delimiter Slides

```
                  ---?code=path/to/source.file
```

#### The Basics

![Press Down Key](assets/down-arrow.png)

+++?code=src/python/time.py&lang=python
@title[Sample Source File]

###### Code delimiters let you present any <p> **code file** with auto-syntax highlighting

---
@title[Code-Delimiter Slides]

### Code-Delimiter Slides
##### Using
#### **Code-Presenting**

![Press Down Key](assets/down-arrow.png)

+++?code=src/javascript/config.js&lang=javascript
@title[Sample Code Presenting]

@[1-3]
@[5-8]
@[10-16]
@[18-24]

###### Use code-presenting to **step-thru** code <p> from directly within your presentation 

---

### Code-Delimiter Slides
##### Using
#### Code-Presenting
#### **With Annotations**

![Press Down Key](assets/down-arrow.png)

+++?code=src/elixir/monitor.ex&lang=elixir
@title[Sample With Annotations]

@[11-14](Elixir module-attributes as constants)
@[22-28](Elixir with-statement for conciseness)
@[171-177](Elixir case-statement pattern matching)
@[179-185](Elixir pipe-mechanism for composing functions)

---

## The End

