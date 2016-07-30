#HSLIDE

### Apache Spark
### AWS Lambda Executor
### (SAMBA)

<span style="color:gray">An Apache Spark Package</span>

#HSLIDE

### SAMBA Apache Spark Package

  - Offers seamless integration with the AWS Lambda compute service
  - Within Spark batch and streaming apps on the JVM

#HSLIDE

### SAMBA API

<ol>
<li class="fragment" data-fragment-index="1">New `delegate` operation on RDD[<span style="color:gray">AWSTask</span>]</li>
<li class="fragment" data-fragment-index="2">This operation executes an AWS Lambda function</li>
<li class="fragment" data-fragment-index="3">And generates RDD[<span style="color:gray">AWSResult</span>]</li>
</ol>

<span class="fragment" data-fragment-index="4" style="font-size: 0.8em; color:gray">The SAMBA API is built on top of the <a target="_blank" href="https://github.com/onetapbeyond/aws-gataway-executor">aws-gateway-executor</a> library.</span>

#HSLIDE

### aws-gateway-executor

- A lightweight, fluent Java library
- For calling APIs on the Amazon Web Service API Gateway
- Inside any application running on the JVM
- Defines <span style="color:gray">AWSGateway</span>, <span style="color:gray">AWSTask</span> and <span style="color:gray">AWSResult</span>

#VSLIDE

### AWSGateway

<span style="color:gray">A handle that represents an API on the AWS API Gateway.</span>

```Java
AWSGateway gateway = AWS.Gateway(echo-api-key)
                        .stage("beta")
                        .region(AWS.Region.OREGON)
                        .build();
```


#VSLIDE

### AWSTask

<span style="color:gray">An executable object that represents an AWS Gateway call.</span>

```Java
AWSTask aTask = AWS.Task(gateway)
                   .resource("/echo")
                   .get();

```

#VSLIDE

### AWSResult

<span style="color:gray">An object that represents the result of an AWS Gateway call.</span>

```Java
AWSResult aResult = aTask.execute();
```

#HSLIDE

### SAMBA + Apache Spark Batch Processing

#VSLIDE

#### Step 1. Build RDD[<span style="color:gray">AWSTask</span>]

```Scala
import io.onetapbeyond.lambda.spark.executor.Gateway._
import io.onetapbeyond.aws.gateway.executor._

val aTaskRDD = dataRDD.map(data => {
  AWS.Task(gateway)
     .resource("/score")
     .input(data.asInput())
     .post()
  })
```

#VSLIDE

#### Step 2. Delegate RDD[<span style="color:gray">AWSTask</span>]

```Scala
// Perform RDD[AWSTask].delegate operation to execute
// AWS Gateway call and generate resulting RDD[AWSResult].

val aResultRDD = aTaskRDD.delegate
```

#VSLIDE

#### Step 3. Process RDD[<span style="color:gray">AWSResult</span>]

```Scala
// Process RDD[AWSResult] data per app requirements. 

aTaskResultRDD.foreach { result => {
        println("TaskDelegation: compute score input=" +
          result.input + " result=" + result.success)
}}
```

#VSLIDE?gist=494e0fecaf0d6a2aa2acadfb8eb9d6e8

#HSLIDE

### ROSE + Apache Spark Stream Processing

#VSLIDE

#### Step 1. Build rTaskStream of RDD[<span style="color:gray">OCPUTask</span>]

```Scala
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

#VSLIDE

#### Step 2. Analyze rTaskStream of RDD[<span style="color:gray">OCPUTask</span>]

```Scala
// Perform R Analytics on RDD[OCPUTask] Stream Data

val rResultStream = rTaskStream.transform(rdd => rdd.analyze)
```

#VSLIDE

#### Step 3. Process rResultStream of RDD[<span style="color:gray">OCPUResult</span>]

```Scala
// Process rResultStream of RDD[OCPUResult] data per app requirements.

rResultStream.foreachRDD { resultRDD => {

    resultRDD.foreach { rResult => {

        println("Demo: " + "fraud::score input=" +
                rResult.input + " returned=" + rResult.output)

    }}
}}
```

#VSLIDE?gist=5c2d6e8afccf0eb6cf77cb5588850833

#HSLIDE

#### Deployment 1. Colocated
![ROSE Deployment](https://onetapbeyond.github.io/resource/img/rose/new-rose-deploy.jpg)

<span style="font-size: 0.8em">OpenCPU server per Apache Spark worker node.</span>

#HSLIDE

#### Deployment 2. Remote Cluster
![ROSE Deployment Alt](https://onetapbeyond.github.io/resource/img/rose/alt-rose-deploy.jpg)

<span style="font-size: 0.8em">OpenCPU cluster independent of Apache Spark cluster.</span>

#HSLIDE

#### OpenCPU Remote Cluster Configuration

```Scala
// Sample OpenCPU 3 Node Cluster

val OCPU_CLUSTER = Array("http://1.1.1.1/ocpu",
                         "http://2.2.2.2/ocpu",
                         "http://3.3.3.3/ocpu")

// Register cluster endpoints as Apache Spark broadcast variable.

val endpoints = sc.broadcast(OCPU_CLUSTER)

```

#VSLIDE

#### OpenCPU Remote Cluster Usage

```Scala
// Use Spark broadcast variable on RDD[OCPUTask].analyze operation.

val rResultRDD = rTaskRDD.analyze(endpoints.value)
```

#HSLIDE

#### Some Related Links

- [GitHub: ROSE Package](https://github.com/onetapbeyond/opencpu-spark-executor)
- [GitHub: ROSE Examples](https://github.com/onetapbeyond/opencpu-spark-executor#rose-examples)
- [GitHub: opencpu-r-executor](https://github.com/onetapbeyond/opencpu-r-executor)
- [GitHub: Apache Spark](https://github.com/apache/spark)
- [Apache Spark Packages](https://spark-packages.org/package/onetapbeyond/opencpu-spark-executor)
