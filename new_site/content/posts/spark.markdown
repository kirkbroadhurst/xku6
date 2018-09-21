title: Debugging Spark logs with YARN
slug: Debugging Spark
category: Software
date: 2015-12-31
save_as: 2015/12/31/debugging_spark_logs_with_yarn/index.html
url: 2015/12/31/debugging_spark_logs_with_yarn/

Debugging Spark can be quite painful. The error that you see in your application, or even in your job, might not reflect the underlying problem. Here’s how I dig into the executor logs to find what (might) be really happening.

From the YARN job list, find your job. If it’s no longer running you’ll need to go to the History page.

[![yarn list]({filename}/images/spark_000-300x126.png)]({filename}/images/spark_000.png)

From here you can navigate to the driver log. There are two here, because the job was retried.

[![application history]({filename}/images/spark_001-300x147.png)]({filename}/images/spark_001.png)

The driver log records the Spark startup, and will log some of the information that the executors provide. Unfortunately if they crash or become unresponsive they often won’t report their status – they’ll just stop.

[![driver log]({filename}/images/spark_002-300x152.png)]({filename}/images/spark_002.png)

The driver log will tell you which executor exited, which is a nice way of saying that it failed. You will have to trawl the driver log a little to find these; there will probably be multiple per job. You now know the name of the container that failed.

[![driver log2]({filename}/images/spark_003-300x70.png)]({filename}/images/spark_003.png)

Now search the driver log for the launch details for the problem container (just do a CTRL+C, CTRL+F in Chrome). Each executor has a “YARN executor launch context” block like the below.

[![exception]({filename}/images/spark_005_stderr_log-300x142.png)]({filename}/images/spark_005_stderr_log.png)

If you browse to the SPARK_LOG_URL_STDERR path you will see the detailed log for that container / executor, wherein you will (hopefully) see a more detailed description of what went wrong. At least you should be able to identify the root ‘Caused by’ exception, and Google from there

