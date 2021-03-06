title: 5 Minute Rest API with Docker
slug: Docker
category: Software
date: 2016-07-18
save_as: 2016/07/18/5-minute-rest-api-docker/index.html
url: 2016/07/18/5-minute-rest-api-docker/


Docker is a wonderful technology to manage environment consistency. It delivers on the promise of Vagrant without having to use Vagrant. All the things that you thought you’d be able to do with virtual machines are easy with Docker.

In this post I wanted to see how long it would take me to start a REST API using a Dockerfile. It actually took more than 5 minutes, but if you knew what you were doing it would take even less.

Firstly, a warning: this won’t work on Windows. Docker on Windows is just not worth trying.

* * *

### Step 1: Write your REST API.

[I’m going to use uWSGI, because it’s easy](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html). You just need to implement the request handler contract, give the response headers to the start_response object, and then return some string.

Create a python file like this:

```
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
```

Save this as `foobar.py` – we’ll reference it in the next step.

### Step 2: Write your Dockerfile

The Dockerfile is the instruction to docker. It includes all the instructions to create the environment – mostly dependencies, but also configuration like which ports to open, etc. Our Dockerfile is quite succinct.
```
FROM ubuntu

RUN apt update
RUN apt-get -y install build-essential python-dev
RUN apt-get -y install python-pip
RUN pip install uwsgi
COPY foobar.py /foobar.py

EXPOSE 8011
CMD uwsgi --http :8011 --wsgi-file foobar.py
```
Line by line, we are

- Starting with an ubuntu image. You could build a container from this image and inspect it if you want to see what it includes, but it’s just an empty image for my purposes.
- Get the latest package lists, and install Python and pip (the Python package manager)
- Install uWSGI, the web server.
- Copy the API implementation from Step 1 into the container
- Expose the port we want to connect on.
- Start uWSGI with port 8011 pointing to my foobar.py file

Save this file and put it in the same directory as the `foobar.py` file.

### Step 3: Build the image

Docker takes the Dockerfile and builds an image. A docker image is much like a virtual machine image, or an AWS AMI – it’s a snapshot which can be ‘started’ into an environment.

In the directory containing your files, run
```
docker build -t my_api .
```
This is saying ‘docker, please build something for me, and tag it “my_api”, and use the Dockerfile in the current directory’.

At this point Docker will need to do a few things. Okay, it might take more than 5 minutes.

- Get the ubuntu image. If you don’t have it (first time building from it) then it needs to be downloaded. It’s ~200MB
- Update package lists.
- Get the various packages that are listed. Another ~100MB or so.

### Step 4: Create the container
```
docker create -it -p 8011:8011 --name my_container my_api
```
We ask docker to create a container in interactive mode (`-i`) with a [pseudo terminal](http://unix.stackexchange.com/questions/21147/what-are-pseudo-terminals-pty-tty) (`t`). We also ask that docker publish port 8011 on the host through to port 8011 in the container, name the container ‘my_container’, and create it from the my_api image.

If we don’t name the container docker will come up with a clever name involving a famous scientist. We would then need to go find the name of that container. It’s easier to just name it ourselves.

### Step 5: Start the container

There are plenty of ways to create, build and start containers. I’m walking through one-by-one process. In this case we can run `docker images` to see the images that have been created (you should see ‘my_api’ in there). You can run `docker ps` to see running containers, or `docker ps -a` to see all containers. The ‘my_container’ won’t be on the running containers until you start it.

```
docker start my_container
```

### Step 6: Test it

Just curl to the URL and watch.

```
curl http://localhost:8011
```

If you want to be clever you can attach to your container (in another terminal instance) before you hit the URL and watch uWSGI log activity.
```
docker attach my_container
```
That’s it! We just built a REST API on a web server in about a dozen lines of code. The world is amazing.
