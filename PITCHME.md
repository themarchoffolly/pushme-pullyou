### R
### OpenCPU Spark Executor
### (ROSE)

<span style="color:gray">An Apache Spark Package</span>

#GPH

> Where Apache SparkR lets data scientists use Spark from R,
> ROSE is designed to let Scala and Java developers use R from Spark.

#GPH

### ROSE Apache Spark Package

  - Offers the full scientific computing power of the R programming language
  - Within Spark batch and streaming apps on the JVM

#GPH

### ROSE API

<ol>
<li class="fragment" data-fragment-index="1">New `analyze` operation on RDD[<span style="color:gray">OCPUTask</span>]</li>
<li class="fragment" data-fragment-index="2">This operation executes R analytics on OpenCPU</li>
<li class="fragment" data-fragment-index="3">And generates RDD[<span style="color:gray">OCPUResult</span>]</li>
</ol>

<span class="fragment" data-fragment-index="4" style="font-size: 0.8em; color:gray">The ROSE API is built on top of the <a target="_blank" href="https://github.com/onetapbeyond/opencpu-r-executor">opencpu-r-executor</a> library.</span>

#GPH

### opencpu-r-executor

- A lightweight, fluent Java library
- For integrating R analytics executed on OpenCPU
- Into any application running on the JVM
- Defines <span style="color:gray">OCPUTask</span> and <span style="color:gray">OCPUResult</span>

#GPV

### OCPUTask

<span style="color:gray">An executable object that represents an R function call.</span>

```scala

// Build R function parameter values as Map.
HashMap params = HashMap(n -> 10, mean -> 5)

// Define executable for R stats#rnorm function call.
OCPUTask task = OCPU.R()
                    .pkg("stats")
                    .function("rnorm")
                    .input(params.asJava)
                    .library()
```

#GPV

### OCPUResult

<span style="color:gray">An object that represents the result of an R function call.</span>

```scala
// Execute R function on OCPUTask.
OCPUResult result = task.execute(OCPU_SERVER_ENDPOINT)

// Retrieve the R function return value from OCPUResult.
Object resp = result.output().get("rnorm")
```

#GPH

### ROSE + Apache Spark Batch Processing

#GPV

#### Step 1. Build RDD[<span style="color:gray">OCPUTask</span>]

```scala
import io.onetapbeyond.opencpu.spark.executor.R._
import io.onetapbeyond.opencpu.r.executor._

// Transform dataRDD into an RDD[OCPUTask].

val rTaskRDD = dataRDD.map(data => {

    // Prepare R fraud#score function call param values.
    val params = prepParams(data)

    OCPU.R()
        .pkg("fraud")
        .function("score")
        .input(params.asJava)
        .library()
})
```

#GPV

#### Step 2. Analyze RDD[<span style="color:gray">OCPUTask</span>]

```scala
// Perform RDD[OCPUTask].analyze operation to execute
// R analytics and generate resulting RDD[OCPUResult].

val rResultRDD = rTaskRDD.analyze
```

#GPV

#### Step 3. Process RDD[<span style="color:gray">OCPUResult</span>]

```scala
// Process RDD[OCPUResult] data per app requirements. 

rResultRDD.foreach { rResult ->

    println("Demo: " + "fraud::score input=" +
            rResult.input + " returned=" + rResult.output)

}
```

#GPH

### ROSE + Apache Spark Stream Processing

#GPV

#### Step 1. Build rTaskStream of RDD[<span style="color:gray">OCPUTask</span>]

```scala
import io.onetapbeyond.opencpu.spark.executor.R._
import io.onetapbeyond.opencpu.r.executor._

// Transform dataStream into rTaskStream of RDD[OCPUTask].
val rTaskStream = dataStream.transform(rdd => {

    rdd.map(data => {

        // Prepare R fraud#score function call param values.
        val params = prepParams(data)

        OCPU.R()
            .pkg("fraud")
            .function("score")
            .input(params.asJava)
            .library()
    })  
})
```

#GPV

#### Step 2. Analyze rTaskStream of RDD[<span style="color:gray">OCPUTask</span>]

```scala
// Perform R Analytics on RDD[OCPUTask] Stream Data

val rResultStream = rTaskStream.transform(rdd => rdd.analyze)
```

#GPV

#### Step 3. Process rResultStream of RDD[<span style="color:gray">OCPUResult</span>]

```scala
// Process rResultStream of RDD[OCPUResult] data per app requirements.

rResultStream.foreachRDD { resultRDD => {

    resultRDD.foreach { rResult => {

        println("Demo: " + "fraud::score input=" +
                rResult.input + " returned=" + rResult.output)

    }}
}}
```

#GPH

#### Deployment 1. Colocated
![ROSE Deployment](https://onetapbeyond.github.io/resource/img/rose/new-rose-deploy.jpg)

<span style="font-size: 0.8em">OpenCPU server per Apache Spark worker node.</span>

#GPH

#### Deployment 2. Remote Cluster
![ROSE Deployment Alt](https://onetapbeyond.github.io/resource/img/rose/alt-rose-deploy.jpg)

<span style="font-size: 0.8em">OpenCPU cluster independent of Apache Spark cluster.</span>

#GPH

#### OpenCPU Remote Cluster Configuration

```scala
// Sample OpenCPU 3 Node Cluster

val OCPU_CLUSTER = Array("http://1.1.1.1/ocpu",
                         "http://2.2.2.2/ocpu",
                         "http://3.3.3.3/ocpu")

// Register cluster endpoints as Apache Spark broadcast variable.

val endpoints = sc.broadcast(OCPU_CLUSTER)

```

#GPV

#### OpenCPU Remote Cluster Usage

```scala
// Use Spark broadcast variable on RDD[OCPUTask].analyze operation.

val rResultRDD = rTaskRDD.analyze(endpoints.value)
```

#GPH

#### Some Related Links

- [GitHub: opencpu-spark-executor](https://onetapbeyond/opencpu-spark-executor)
- [GitHub: opencpu-r-executor](https://onetapbeyond/opencpu-r-executor)
- [GitHub: Apache Spark](https://github.com/apache/spark)
- [Apache Spark Packages](https://spark-packages.org/package/onetapbeyond/opencpu-spark-executor)
