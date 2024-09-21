# Welcome

Well met, fellow data analyst!

If you're like me, then you're used to pesky stakeholders, who ask you why a metric went up or down. These kind of asks are tricky to answer with precision. It usually ends up by sharing a few other metrics, giving some context, and suggesting a hypothesis. All the while hoping the stakeholder will be satisfied and go away 😮‍💨

</br>
<div class="tenor-gif-embed" data-postid="17635701" data-share-method="host" data-aspect-ratio="1.86047" data-width="100%"><a href="https://tenor.com/view/breaking-bad-gustavo-fring-giancarlo-esposito-explain-yourself-series-gif-17635701"></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
</br>

This isn't a good situation to be in. But what if you could tell *exactly* why a metric changed? Wouldn't that be great? 🤩

`icanexplain` is a Python package. It provides a framework to break a metric down into drivers. It allows attributing the change in a metric to each of its drivers. Instead of just measuring the evolution of each driver, we can exactly quantify how much of the metric's evolution is due to each driver.

The best way to understand how `icanexplain` works is to see it in action, by checking out the [examples](examples/iowa-whiskey-sales/). If you're interested in the technical details, you can check out the [methodology](methods/total/) section.

`icanexplain` works with [pandas](https://pandas.pydata.org/) and [Polars](https://pola.rs/) out of the box. Additionally, it can run against other backends, because it is implemented with [Ibis](https://ibis-project.org/). Check out [this example](examples/ibis/) for more information.

</br>


