# Code Reveal Bit-by-Bit

---

```
$sum = 0; $count = 0;
foreach ($employees as $employee) {
    if ($employee['profession'] === 'programmer') {
        foreach ($employee['skills'] as $skill) {
            if ($skill['name'] === 'bash') {
                $sum += $skill['experience'];
                $count++;
            }
        }
    }
}
$result = $count ? $sum / $count : 0;
```

@[1]
@[1,2, 11]
@[1-3, 10-11]
@[1-4, 9-11]
@[1-5, 8-11]
@[1-11]
@[1-12]
