# Code Reveal Bit-by-Bit

---

```
$sum = 0; $count = 0;
foreach ($employees as $employee) {
    if ($employee['profession'] === 'programmer') {
        foreach ($employee['skills'] as $skill) {
            if (
                isset($skill['name'])
                && $skill['name'] === 'bash'
            ) {
                $sum += $skill['experience'];
                $count++;
            }
        }
    }
}
$result = $count ? $sum / $count : 0;
```

@[1]
@[1,2, 14]
@[1-3, 13-14]
@[1-4, 12-14]
@[1-5, 11-14]
@[1-14]
@[1-15]
