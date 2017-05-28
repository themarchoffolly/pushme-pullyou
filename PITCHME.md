#HSLIDE

### R
### OpenCPU Spark Executor
### (ROSE)

<span style="color:gray">An Apache Spark Package</span>

#HSLIDE

```
package main

import "fmt"

func main() {
    fmt.Println("Hello, world!")
}
```

@[1](Use package main for executable command.)
@[3](Import fmt for use within current package.)
@[5-7](Declare function to execute for command.)

#HSLIDE?code=lib/sample.ex

#HSLIDE?code=lib/math.ex

@[2]
@[11-14]
@[19-21]

#HSLIDE?code=lib/runtime.ex

@[1]
@[30-35]
@[45-55]

#HSLIDE

```
defmodule GenMetrics.GenStage.Monitor do
  use GenServer
  alias GenMetrics.GenStage.Manager
  alias GenMetrics.GenStage.Monitor
  alias GenMetrics.GenStage.Pipeline
  alias GenMetrics.GenStage.Window
  alias GenMetrics.Reporter
  alias GenMetrics.Utils.Runtime

  @moduledoc false
  @handle_demand :handle_demand
  @handle_events :handle_events
  @handle_call   :handle_call
  @handle_cast   :handle_cast

  defstruct pipeline: %Pipeline{}, metrics: nil, start: 0, duration: 0

  def start_link(pipeline) do
    GenServer.start_link(__MODULE__, pipeline)
  end

  def init(pipeline) do
    with {:ok, _}     <- validate_modules(pipeline),
         {:ok, _}     <- validate_behaviours(pipeline),
         {:ok, _}     <- activate_tracing(pipeline),
         state        <- initialize_monitor(pipeline),
      do: start_monitor(state)
  end

  #
  # Handlers for intercepting :erlang.trace/3 and :erlang.trace_pattern/2
  # callbacks for modules registered on the pipeline.
  #

  def handle_info({:trace_ts, pid, :call, {mod, fun, [demand | _]}, ts}, state) do
    {:noreply,
     do_intercept_call_request(state, pid, {mod, fun}, demand, ts)}
  end

  # Intercept {:noreply, [event], new_state} response.
  def handle_info({:trace_ts, pid, :return_from, {mod, _, _},
                   {:noreply, events, _}, ts}, state) do
    {:noreply,
     do_intercept_call_response(state, mod, pid, length(events), ts)}
  end

  # Intercept {:noreply, [event], new_state, :hibernate} response.
  def handle_info({:trace_ts, pid, :return_from, {mod, _, _},
                   {:noreply, events, _, _}, ts}, state) do
    {:noreply,
     do_intercept_call_response(state, mod, pid, length(events), ts)}
  end

  # Intercept {:reply, _reply, [event], new_state} response.
  def handle_info({:trace_ts, pid, :return_from, {mod, _, _},
                   {:reply, _, events, _}, ts}, state) do
    {:noreply,
     do_intercept_call_response(state, mod, pid, length(events), ts)}
  end

  # Intercept {:reply, _reply, [event], new_state, :hibernate} response.
  def handle_info({:trace_ts, pid, :return_from, {mod, _, _},
                   {:noreply, _, events, _, _}, ts}, state) do
    {:noreply,
     do_intercept_call_response(state, mod, pid, length(events), ts)}
  end

  # Intercept {:stop, reason, new_state} response.
  def handle_info({:trace_ts, pid, :return_from, {mod, _, _},
                   {:stop, _, _}, ts}, state) do
    {:noreply,
     do_intercept_call_response(state, mod, pid, 0, ts)}
  end

  # Report and rollover metrics window.
  def handle_info(:rollover_metrics_window, state) do
    now = :erlang.system_time
    state = %Monitor{state | duration: Runtime.nano_to_milli(now - state.start)}
    window = Manager.as_window(state.metrics,
      Runtime.statistics?(state.pipeline), Runtime.sample_rate(state.pipeline))
    window = %Window{window | pipeline: state.pipeline,
                     start: state.start, duration: state.duration}
    Reporter.push(GenMetrics.GenStage.Reporter, window)
    Process.send_after(self(),
      :rollover_metrics_window, Runtime.window_interval(state.pipeline))
    if Runtime.sampling?(state.pipeline) do
      activate_tracing(state.pipeline)
      Process.send_after(self(),
        :silence_metrics_window, Runtime.sample_interval(state.pipeline))
    end
    {:noreply, initialize_monitor(state.pipeline, state.metrics)}
  end

  # Sampling window is closed for current metrics windows
  # so temporarily silence tracing.
  def handle_info(:silence_metrics_window, state) do
    activate_tracing(state.pipeline, true)
    {:noreply, state}
  end

  # Catch-all for calls not intercepted by monitor.
  def handle_info(_msg, state), do: {:noreply, state}

  #
  # Private utility functions follow.
  #

  # Initialize GenServer state for monitor.
  defp initialize_monitor(pipeline, metrics \\ nil)  do
    if metrics do
      %Monitor{pipeline: pipeline,
               metrics: Manager.reinitialize(metrics),
               start: :erlang.system_time}
    else
        %Monitor{pipeline: pipeline,
                 metrics: Manager.initialize(),
                 start: :erlang.system_time}
    end
  end

  # Initialize periodic callback for metrics reporting and window rollover.
  defp start_monitor(state) do
    Process.send_after(self(),
      :rollover_metrics_window, Runtime.window_interval(state.pipeline))
    if Runtime.sampling?(state.pipeline) do
      Process.send_after(self(),
        :silence_metrics_window, Runtime.sample_interval(state.pipeline))
    end
    {:ok, state}
  end

  # Activate tracing for stages within pipeline.
  defp activate_tracing(pipeline, silent \\ false) do

    if silent do
      :erlang.trace(:processes, false, [:call, :monotonic_timestamp])
    else
      :erlang.trace(:processes, true, [:call, :monotonic_timestamp])

      for pmod <- pipeline.producer do
        :erlang.trace_pattern({pmod, :handle_demand, 2},
          [{:_, [], [{:return_trace}]}])
        :erlang.trace_pattern({pmod, :handle_cast, 2},
          [{:_, [], [{:return_trace}]}])
        if Runtime.synchronous?(pipeline) do
          :erlang.trace_pattern({pmod, :handle_call, 3},
            [{:_, [], [{:return_trace}]}])
        end
      end

      for pcmod <- pipeline.producer_consumer do
        :erlang.trace_pattern({pcmod, :handle_events, 3},
          [{:_, [], [{:return_trace}]}])
        :erlang.trace_pattern({pcmod, :handle_cast, 2},
          [{:_, [], [{:return_trace}]}])
        if Runtime.synchronous?(pipeline) do
          :erlang.trace_pattern({pcmod, :handle_call, 3},
            [{:_, [], [{:return_trace}]}])
        end
      end

      for cmod <- pipeline.consumer do
        :erlang.trace_pattern({cmod, :handle_events, 3},
          [{:_, [], [{:return_trace}]}])
      end
    end

    {:ok, pipeline}
  end

  # Validate pipeline modules can be loaded or report failures.
  defp validate_modules(pipeline) do
    case require_modules(pipeline) do
      []   -> {:ok, pipeline}
      errs -> {:stop, {:bad_pipeline, errs}}
    end
  end

  # Ensure pipeline modules are available and can be loaded.
  defp require_modules(pipeline) do
    [pipeline.producer, pipeline.producer_consumer, pipeline.consumer]
    |> Enum.flat_map(fn(modules) -> modules end)
    |> Enum.uniq
    |> Runtime.require_modules
  end

  # Validate pipeline modules implement GenStage or report failures.
  defp validate_behaviours(pipeline) do
    case require_behaviour(pipeline, GenStage) do
      []   -> {:ok, pipeline}
      errs -> {:stop, {:bad_pipeline, errs}}
    end
  end

  # Ensure pipeline modules implement GenStage behaviour.
  defp require_behaviour(pipeline, behaviour) do
    [pipeline.producer, pipeline.producer_consumer, pipeline.consumer]
    |> Enum.flat_map(fn(modules) -> modules end)
    |> Enum.uniq
    |> Runtime.require_behaviour(behaviour)
  end

  defp do_intercept_call_request(state, pid, {mod, fun}, demand, ts) do
    case fun do
      @handle_demand -> do_open_metric(state, mod, pid, demand, ts)
      @handle_events -> do_open_metric(state, mod, pid, length(demand), ts)
      @handle_call   -> do_open_metric(state, mod, pid, 0, ts)
      @handle_cast   -> do_open_metric(state, mod, pid, 0, ts)
      _ -> state
    end
  end

  defp do_intercept_call_response(state, mod, pid, events, ts) do
    do_close_metric(state, mod, pid, events, ts)
  end

  # Open partial metric on handle_ function call trace.
  defp do_open_metric(state, mod, pid, demand, ts) do
    metrics =
      Manager.open_summary_metric(state.metrics, mod, pid, demand, ts)
    state = %Monitor{state | metrics: metrics}

    if Runtime.statistics?(state.pipeline) do
      metrics =
        Manager.open_stats_metric(state.metrics, {mod, pid, demand, ts})
      %Monitor{state | metrics: metrics}
    else
      state
    end
  end

  # Close complete metric on handle_ function return trace.
  defp do_close_metric(state, mod, pid, events, ts) do
    metrics = Manager.close_summary_metric(state.metrics, mod, pid, events, ts)
    state = %Monitor{state | metrics: metrics}

    if Runtime.statistics?(state.pipeline) do
      metrics = Manager.close_stats_metric(state.pipeline,
        state.metrics, {mod, pid, events, ts})
      %Monitor{state | metrics: metrics}
    else
      state
    end
  end

end
```

@[1-2]
@[4-6]
@[8-14]
@[90]
@[110]
@[170-180]
@[200]

#HSLIDE

```Elixir
defstruct pipeline: %Pipeline{},
          metrics: nil, start: 0, duration: 0

def start_link(pipeline) do
    GenServer.start_link(__MODULE__, pipeline)
end

def init(pipeline) do
    with {:ok, _}     <- validate_modules(pipeline),
         {:ok, _}     <- validate_behaviours(pipeline),
         {:ok, _}     <- activate_tracing(pipeline),
         state        <- initialize_monitor(pipeline),
      do: start_monitor(state)
end
```

@[1-2]
@[4-6]
@[8-14]
@[9]
@[10]
@[11]
@[12]

#HSLIDE

```
defstruct pipeline: %Pipeline{},
          metrics: nil, start: 0, duration: 0

def start_link(pipeline) do
    GenServer.start_link(__MODULE__, pipeline)
end

def init(pipeline) do
    with {:ok, _}     <- validate_modules(pipeline),
         {:ok, _}     <- validate_behaviours(pipeline),
         {:ok, _}     <- activate_tracing(pipeline),
         state        <- initialize_monitor(pipeline),
      do: start_monitor(state)
end
```

@[1-2](GenStage pipeline data structure.)
@[4-6](GenMetrics monitor launch interface.)
@[8-14](GenMetrics monitor initialization interface.)
@[9](Ensure pipeline modules can be loaded.)
@[10](Ensure pipeline modules GenStage behaviour.)
@[11](Ensure Erlang tracing is initialized.)
@[12](Ensure monitor initialization completes.)

#HSLIDE

> Where Apache SparkR lets data scientists use Spark from R,
> ROSE is designed to let Scala and Java developers use R from Spark.

#HSLIDE

### ROSE Apache Spark Package

  - Offers the full scientific computing power of the R programming language
  - Within Spark batch and streaming apps on the JVM

#HSLIDE

### ROSE API

<ol>
<li class="fragment" data-fragment-index="1">New `analyze` operation on RDD[<span style="color:gray">OCPUTask</span>]</li>
<li class="fragment" data-fragment-index="2">This operation executes R analytics on OpenCPU</li>
<li class="fragment" data-fragment-index="3">And generates RDD[<span style="color:gray">OCPUResult</span>]</li>
</ol>

<span class="fragment" data-fragment-index="4" style="font-size: 0.8em; color:gray">The ROSE API is built on top of the <a target="_blank" href="https://github.com/onetapbeyond/opencpu-r-executor">opencpu-r-executor</a> library.</span>

#HSLIDE

### opencpu-r-executor

- A lightweight, fluent Java library
- For integrating R analytics executed on OpenCPU
- Into any application running on the JVM
- Defines <span style="color:gray">OCPUTask</span> and <span style="color:gray">OCPUResult</span>

#VSLIDE

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

@[1-9]
@[2-5](Highlight lines 2-5)
@[6]
@[6-8](End of code highlights)

#VSLIDE

### OCPUResult

<span style="color:gray">An object that represents the result of an R function call.</span>

```scala
// Execute R function on OCPUTask.
OCPUResult result = task.execute(OCPU_SERVER_ENDPOINT)

// Retrieve the R function return value from OCPUResult.
Object resp = result.output().get("rnorm")
```

#HSLIDE

### ROSE + Apache Spark Batch Processing

#VSLIDE

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

#VSLIDE

#### Step 2. Analyze RDD[<span style="color:gray">OCPUTask</span>]

```scala
// Perform RDD[OCPUTask].analyze operation to execute
// R analytics and generate resulting RDD[OCPUResult].

val rResultRDD = rTaskRDD.analyze
```

#VSLIDE

#### Step 3. Process RDD[<span style="color:gray">OCPUResult</span>]

```scala
// Process RDD[OCPUResult] data per app requirements. 

rResultRDD.foreach { rResult ->

    println("Demo: " + "fraud::score input=" +
            rResult.input + " returned=" + rResult.output)

}
```

#HSLIDE

### ROSE + Apache Spark Stream Processing

#VSLIDE

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

#VSLIDE

#### Step 2. Analyze rTaskStream of RDD[<span style="color:gray">OCPUTask</span>]

```scala
// Perform R Analytics on RDD[OCPUTask] Stream Data

val rResultStream = rTaskStream.transform(rdd => rdd.analyze)
```

#VSLIDE

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

```scala
// Sample OpenCPU 3 Node Cluster

val OCPU_CLUSTER = Array("http://1.1.1.1/ocpu",
                         "http://2.2.2.2/ocpu",
                         "http://3.3.3.3/ocpu")

// Register cluster endpoints as Apache Spark broadcast variable.

val endpoints = sc.broadcast(OCPU_CLUSTER)

```

#VSLIDE

#### OpenCPU Remote Cluster Usage

```scala
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
