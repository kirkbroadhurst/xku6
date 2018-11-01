title: 'IaaS v PaaS' is the new 'Build v Buy'
slug: IaaS-v-PaaS
category: Software
date: 2018-11-01

A decade ago we used to talk about *Build v Buy*. Maybe we still do. IT Managers would passionately argue about the benefits of these approaches. Battles would won and lost. People held deep seated beliefs in the benefits of one over the other, and were frequently stubborn about accepting that both have their place.

Today we see echoes of the *Build v Buy* debate in a modern equivalent: *IaaS v PaaS*.

# Build v Buy

## The 'Build' thesis
The traditional, can-do approach to enterprise software - we can build what we need. Development is in-house. Our needs are so unique that no existing solution will work for us. Options don't have required features and functionality, are not customizable, or can't be extended and integrated. 

Or maybe available products are just too expensive or restrictive.

For whatever reason you believe that your best approach is to spend the effort, money and time building something custom that you'll have to look after. The upside is that it will be *exactly* what you need, and you'll avoid dreaded 'vendor lock in', if everything goes well.

## The 'Buy' thesis
Why recreate the wheel? Take some off-the-shelf solution or product that mostly works for you and use it to bootstrap whatever you're doing. You literally 'buy' something, and it might not be perfect for what you need, but you accept this trade-off because it's quick and simple. 

- Someone else has already done the hard work of building this system, so it's proven to work (in theory).
- Someone else will maintain it for you, delivering bug fixes if necessary. 
- Someone else will do support if things go bad. All at a cost, of course.
- You'll get to market sooner

## Choosing
People will debate this considering organization's core competency, risk tolerance, and priorities.

- Are we a software company? How serious are we about that? Sure, we'll make a website and a database. Are we going to develop our own Word processor?
- If we build a lot of software, we'll have to look after it. That takes time and money, and has the risk of being a huge distraction. What if the thing we build ends up having problems?
- What's the total cost? Some other company is spending the same as we would spend to build this thing, and then they are making a profit on top. If we build it ourself it will be cheaper.
- After we spent the time and money customizing this thing to meet our needs, it will end up costing more than if we just build it from scratch.

And vendor lock-in. The fear of building some your core business around some 3rd party solution, and the fact that you'll be beholden to that 3rd party's licencing fees forever. What if the triple the price? What if they discontinue the product, or force us to upgrade? What if they get purchased by... IBM?

# IaaS v PaaS

Today, as we develop in the cloud, this conversation has shifted to another level. Our applications are becoming products; our systems are becoming platforms. We still have *Build v Buy* on a micro level, but on the macro level we need to consider *IaaS v PaaS*.

## IaaS (Infrastructure)
Ignore the 'as-a-service' buzzword. Infrastructure means leasing servers from a cloud vendor - Amazon, Google, Microsoft. You'll generally pay by time used. And you'll just get a server on which you can run whatever you want.

What do you want to run on that server? Well, you can build some software. Maybe you want 
- an API that can power a website
- a database to store product information
- an ETL process and data pipeline

Just build whatever you want, and deploy it! This is extremely flexible - you can literally do anything. But it takes time, and you'll be supporting that software. 

This is the modern equivalent of *Build*.

## PaaS (Platform)
A platform - in the PaaS sense - is a set of components that provide some out-of-the-box functionality upon which you can build something. These are products in their own right, but you would use them to build your own products. A cloud vendor provides some of the basic plumbing so that you can get your solution up and running rapidly.

- For an API, try API Gateway (AWS), Cloud Endpoints (GCP), or API Management (Azure)
- For a database, try Aurora (AWS), Spanner (GCP), or - I guess - Azure SQL 
- For an ETL process, try Glue (AWS), Dataflow (GCP), or Data Factory (Azure)

You see, cloud vendors are in a race to deliver 'value add' over simple infrastructure. This is a huge differentiator because it allows developers to get stuff done quickly.

This is the modern equivalent of *Buy*. 

## The argument
Many of the same *Build v Buy* arguments appear here, too.

- Does it do exactly what we want? Can we customize it?
- What's the cheapest option?
- What's the fastest option?

But there are some crucial differences to the old argument - all relating to the scale at which the cloud vendors operate.

### Economics

Cloud vendors operate at a scale that no software vendor ever has (perhaps outside of Microsoft), and software has no marginal cost. The platforms that they offer have very little markup over and above the base infrastructure - some are almost free. These platforms are differentiators, and add revenue via increased user base rather than increased per-user-revenue. You almost certainly can't build it for less than it costs to buy.

### Community

These platforms are so ubiquitous that they form their own communities, expertise, and 3rd party support. These are not niche products, and it's (relatively) easy to hire people who already have experience using them. If you have a problem, someone will have already had that problem and posted it on StackOverflow. There are large teams supporting these products, and they are (relatively) well documented.

### Evolution

Again, at the operating scale all of these platforms are continually improving. Run a software team that will deliver features on the cadence of the cloud vendor's platform would be a very expensive operation. 

# But 'lock-in'!

Aha!

People have been burnt over the years with vendor lock-in. Whether it's Oracle (the classic example), Microsoft licencing, big data appliances (Teradata or Netezza), or some industry niche solution, this is a bug bear for IT Managers. It's a huge drain on the bottom line. These systems have big upfront and recurring costs, and often don't even deliver improvements without another big outlay.

I understand that managers are skeptical of platform lock-in. It's a valid concern. I build all my APIs in AWS' API Gateway, and now I'm stuck - the migration effort would be enormous, I'd have to re-implement everything.

**This is fear based decision making.**

Why? I'll address this in my next post.
