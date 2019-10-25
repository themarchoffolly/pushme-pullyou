@snap[north-west span-50]
```ruby zoom-07
def longest_repetition(string)
  max = string
        .chars
        .chunk(&:itself)
        .map(&:last)
        .max_by(&:size)
  max = [max[0], max.size] : ["", 0]
end
```
@snapend

@snap[north-east span-50]
```ruby zoom-07 code-font-victor-mono
def longest_repetition(string)
  max = string
        .chars
        .chunk(&:itself)
        .map(&:last)
        .max_by(&:size)
  max = [max[0], max.size] : ["", 0]
end
```
@snapend

@snap[west span-50]
```ruby zoom-07 code-font-victor-mono-italic
def longest_repetition(string)
  max = string
        .chars
        .chunk(&:itself)
        .map(&:last)
        .max_by(&:size)
  max = [max[0], max.size] : ["", 0]
end
```
@snapend

@snap[east span-50]
```ruby zoom-07 code-font-inconsolata
def longest_repetition(string)
  max = string
        .chars
        .chunk(&:itself)
        .map(&:last)
        .max_by(&:size)
  max = [max[0], max.size] : ["", 0]
end
```
@snapend

@snap[south-west span-50]
```ruby zoom-07 code-font-iosevka
def longest_repetition(string)
  max = string
        .chars
        .chunk(&:itself)
        .map(&:last)
        .max_by(&:size)
  max = [max[0], max.size] : ["", 0]
end
```
@snapend

@snap[south-east span-50]
```ruby zoom-07 code-font-fira-code
def longest_repetition(string)
  max = string
        .chars
        .chunk(&:itself)
        .map(&:last)
        .max_by(&:size)
  max = [max[0], max.size] : ["", 0]
end
```
@snapend

