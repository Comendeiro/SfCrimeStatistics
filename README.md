# SfCrimeStatistics
SF Crime statistics project for nanodegree

The images are attached inside images.zip

### Answers to questions:


**How did changing values on the SparkSession property parameters affect the throughput and latency of the data?**
Making changes on the maxOffsetsPerTigger allows sparks to process more records within a batch, increasing the total throughput at the expense of additional latency


**What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?**
It would largelly depend on the specifics of the real use case, e.g. needs for frequency and available harware.
+ Changing maxOffsetsPerTigger to values close to 200 seems to perform better at this size of data.
+ Adjusting the maxRatePerPartition allows to process more messages per partition and batch, having values around 10 seems to work better with the workspace.
