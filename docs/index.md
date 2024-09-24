# Welcome

Well met, fellow data analyst!

If you're like me, then you're used to pesky stakeholders, who ask you why a metric changed. These kind of questions are tricky to answer confidently. It usually ends with you sharing a few other related metrics, giving some context, and providing a weak explanation. All the while hoping the stakeholder will be satisfied (or fed up) and go away 😮‍💨

This isn't a good situation to be in. But what if you could tell *exactly* why a metric changed? Wouldn't that be great? 🤩

`icanexplain` is a Python package. It provides a framework to break a metric down into drivers. It attributes the change in a metric to its drivers. Instead of just measuring the evolution of each driver, we can exactly quantify how much of the metric's evolution is due to each driver.

The best way to understand how `icanexplain` works is to see it in action, by checking out the [examples](examples/iowa-whiskey-sales/).

`icanexplain` works with [pandas](https://pandas.pydata.org/) and [Polars](https://pola.rs/) out of the box. Additionally, it can run against other backends (e.g. SQL) because it is implemented with [Ibis](https://ibis-project.org/). Check out [this example](examples/ibis/) for more information.

</br>


