@title[Introduction]
## The test which will save your day
##### by Ivan Styazhkin from DataRobot
`gitpitch.com/inesusvet/tests-talk`

+++
@title[Disclaimer]

## I am not selling
- No particular technology or methodology
- I want to talk about very basic principles
- This is based on my experience and knowledge
- I invite you to share your stories after the talk

+++
@title[Epigraph]

## Quality
> The test of the machine is the satisfaction it gives you.
 There isn't any other test.
 If the machine produces tranquility it's right.
 If it disturbs you it's wrong until either the machine or your mind is changed.

+++
@title[Expectations]

## Target audience
- You know hard way that tests are good for your project
- You do read & write tests on daily basis
- You will think ahead about testability of new system

+++
@title[References]

## Further reading & watching
- "The art of unit testing" by Roy Osherove
- "Extreme programming: TDD by example" by Kent Beck
- "JB Rainsberger Integrated Tests Are A Scam" @youtube
- "Clean Code" video series by Robert C. Martin

---
@title[5 whys]

# Why do we need tests?

+++
@title[5 because]

## We need tests
- To detect program errors faster
- Easier to maintain (bring new changes)
- Easier to understand/reason about the code
- Easier to communicate about new changes
- Easier to develop new features

+++
@title[Extras]

## Nice to have
- Confidence to all parties (pigs & chickens)
- Freedom of choice for a next step

---
@title[Definitions]

## Some Definitions
To reduce misunderstanding

+++
@title[Definitions: Autotest]
### Autotest
a check or group of checks, which can be executed by *one simple human action*

+++
@title[Definitions: Unittest]
### Unittest
a test of a isolated part of the program (unit of work) for correctness

+++
@title[Definitions: Integration test]
### Integration test
a test of interaction of several programs (or it's parts) for correctness and coherence

+++
@title[Definitions: Test utils]
### Test utils
a set of programs for modeling of work environment and execution of checks

---
@title[What is it]

# A good test is

+++
@title[A good test: Three aspects]

## A good test is
- Trustworthy
- Maintainable
- Readable

+++
@title[A good test: Trustworthy]

## Trustworthy
If tests are failed at start because of misconfigurations or it's a
"known issue" of some dependency/part of the system

*No one* will run them!

+++
@title[A good test: Maintainable]

## Maintainable
If we spend more time for setting up, running or required changes than on actual development

*No one* will write them!

+++
@title[A good test: Readable]

## Readable
If we need much time to debug a test and figure out the reason of it's failure

*No one* will care about <span style="color: green; font-weight: bold">green build</span>

---
@title[Readable: Clear name]

### Not so clear name

It's the very first thing which will see a developer

```
def build_cookie(name, value):
    return '%s=%s' % (name, value)

def test_test():
    ...

def test_foobar_failed():
    ...
```

+++
@title[Readable: Better name]

### Better name

Gives more clues what's broken.
Do not fear to use really long names.
Remember that you write that for a human at the first place

```
def build_cookie(name, value):
    return '%s=%s' % (name, value)

def test_build_cookie__regular_name_valid_value__ok():
    name, valid_session = 'sessionid', 1001
    assert build_cookie(small, big) == 'sessionid=1001'
```

+++
@title[Readable: Not so clear steps]

### Not so clear steps

What's mocked here? Gimme answer in 5 seconds!

```
def test_foobar__false_result__ok():
    result = authorize('vasya', 'superstrongpassword')
    assert result.is_ok
    patch('requests.post').start()
    result.send('token')
    assert result.sessionid == ‘token’
```

+++
@title[Readable: Clear steps]

### Clear steps

Save your time

```
def test_authorize__bad_user_and_password__not_authorized():
    setup_auth_ok(‘failed’)

    result = authorize('bad-user’, 'bad-password')

    assert result is False
```

+++
@title[Readable: Magic]

### Magic

No one can understand that.
Only one person can debug it.
This person can't afford vacations

```
def test_foobar__watch_my_magic__ok():
    assert foobar(42) == ‘3,141529'
```

Example from backbone.js

![qr-code](https://github.com/inesusvet/tests-talk/raw/master/assets/bb-test.png)

