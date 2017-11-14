---?image=assets/image/ivan_televnyy.jpg

# Code Graffiti

---?image=assets/image/lukas_blazek.jpg

## About Presentation

---?image=assets/image/maarten_deckers.jpg

```go
package main

import "fmt"

func vals() (int, int) {
	return 3, 7
}
```

---?image=assets/image/felicia_d_ascanio.jpg

```scala
scala> val fooList: List[String] = List()
fooList: List[String] = List()

scala> foo :+ "one"
res117: List[String] = List(one)
```

---?image=assets/image/maarten_deckers.jpg

```java
import java.util.Random;

public class main {

    public static void main(String[] args) {

        int[] a = new int[10];
        int max = 0;
        
        final Random random = new Random();
        
        for (int i = 0; i < 10; i++) {
            a[i] = random.nextInt(10) + 1;  //  1 =< a[i] =< 10
        }
        
        max = a[0];
        
        for (int i = 1; i < 10; i++) {
            if (max < a[i]) {
                max = a[i];
            }    
        }
        
        System.out.print(max);   
    }
}
```

---?image=assets/image/felicia_d_ascanio.jpg

### Java Snippet

```java
import java.util.Random;

public class main {

    public static void main(String[] args) {

        int[] a = new int[10];
        int max = 0;

        final Random random = new Random();

        for (int i = 0; i < 10; i++) {
            a[i] = random.nextInt(10) + 1;  //  1 =< a[i] =< 10
        }

        max = a[0];

        for (int i = 1; i < 10; i++) {
            if (max < a[i]) {
                max = a[i];
            }
        }

        System.out.print(max);
    }
}
```

@[1](Package import statement)
@[3,25](Application main function)
@[7-8](Localy variable declarations)

