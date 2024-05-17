# Eskom's spending and use on diesel, and the SA general elections

**15 May 2024**

There have been a lot of articles and press releases in the last few days about Eskom's diesel use and the upcoming elections. 

One one side there is the DA, ex CEO De Ruyter, and some others claiming broadly that

* The situation at Eskom is as bad as ever
* Our record-setting 50 days without loadshedding is due to excessive diesel use
* After the elections, we'll have used up the diesel budget and things will go back to being bad
* This is due to political pressure that the ANC puts on Eskom

On the other is current Eskom leadership and the ANC who claim that

* Eskom has "turned the corner" and things are long-term improving
* Diesel is being burned responsibly and at a slower pace than before

I think the truth is somewhere in between, but I'm just some guy on the internet with an unhealthy obsession at trawling through data and news about Eskom, so take everything below with a healthy dose of skepticism, and only quote the bits that support whichever side of the debate you were already on.

## Articles and claims

[https://businesstech.co.za/news/energy/771174/the-truth-behind-no-load-shedding-according-to-andre-de-ruyter-2/](https://businesstech.co.za/news/energy/771174/the-truth-behind-no-load-shedding-according-to-andre-de-ruyter-2/)

* He mentioned that during his tenure at Eskom, he and former COO Jan Oberholzer only had a budget of approximately R6 billion per year to spend on diesel to fuel the utility’s open-cycle gas turbines to generate electricity.
* the current budget for diesel this year under new management is R24 billion, which is four times more than what they had at their disposal during his time.
* Public Enterprises Minister Pravin Gordhan recently revealed that Eskom spent R65 billion on diesel over the past five years to fuel its open-cycle gas turbines (OCGTs).

[https://www.da.org.za/2024/05/confirmed-anc-government-is-putting-political-pressure-on-eskom-to-burn-more-diesel-da-wants-answers](https://www.da.org.za/2024/05/confirmed-anc-government-is-putting-political-pressure-on-eskom-to-burn-more-diesel-da-wants-answers)

* According to NERSA, Eskom has already blown more than half of its quarterly budget of diesel for the first quarter of the 2024/2025 financial year in just one month.
* NERSA has confirmed beyond any doubt that the use of diesel-powered OCGT’s was ramped up during the April-June 2024 financial quarter to coincides with the national elections on 29 May.

[https://www.moneyweb.co.za/news/south-africa/eskom-nersa-set-the-facts-straight-on-diesel-usage/](https://www.moneyweb.co.za/news/south-africa/eskom-nersa-set-the-facts-straight-on-diesel-usage/)

* Unplanned outages have been reduced by 4 400MW since 26 April 2024 due to extensive maintenance and the success of the Generation Operational Recovery Plan initiated in March 2023.



## Some concepts

Part of what makes the discussion confusing and convoluted is that everyone quotes different metrics. A simplified version is that Eskom needs diesel to run emergency generators. These were originally designed to be run for very short 'peak' periods where demand exceeded supply at 6pm when everyone came home from work, or when a big coal plant had to be shut down for emergency repairs. Now they are run a lot more than that as demand has exceeded supply for many years.

But this diesel needs to be

1. Budgeted for
2. Bought
3. Used

And this leaves a lot of room for pointing fingers with statements like "Eskom's diesel budget is twice as big as last year" while leaving out inconvenient facts like how much was actually bought (budgets can be overrun) or used.

The main metric that Eskom tracks is "EAF" or energy availability factor, which is a percentage of what percentage of the power generation fleet is currently operational. Big number = good. Small number = bad. But again, it's more complicated because the **inverse** of the EAF (generators that are not operational) is broken into **planned** maintenance (good) and **unplanned** maintenance (bad), so it's possible to increase the EAF (good) by reducing the planned maintenacne (bad).

In reality we want a world where we have 

* High EAF
* High planned maintenance (means we are not sacrificing future performance of the plants to make them work now)
* Low unplanned maintenance (things aren't breaking unexpectedly)
* Low diesel usage (diesel is expensive, and bad for the environment)

### further complications

To make things even more complicated, reporters talking about this stuff are well known for getting facts and numbers very wrong. For example from a [Moneyweb article](https://www.moneyweb.co.za/news/south-africa/eskom-nersa-set-the-facts-straight-on-diesel-usage/).

> Eskom’s budget for diesel in the current **financial year (April to June 2024)** is R5.8 billion, and R1.16 billion has been spent as of 09 May 2024 (19.7% of the total budget). [emphasis added]

And Eskom doesn't really publish its actual diesel budget or purchases in an neat way (at least one that I've found) in their annual reports, so we have to rely on media statements and long NERSA documents to try to figure those out.

## Looking at the OCGT usage data 

The easiest data to look at is the OCGT use. This includes all the emergency power generators that Eskom controls, including its own diesel generators, and those owned by independent power producers like [Peakers](https://peakers.com).

![](https://i.ritzastatic.com/images/4a806b745fd24a54b9d460f6fb5dde90/eskom-ocgt-use.png)

This is daily data, aggregated monthly, so you can see we regularly use these to generate up to 500MW of power and can go up to just over 3GW if necessary (for context, our only Nuclear power station Koeberg generates a maximum of 1.8GW of power, and Kusile our in-progress coal power plant and fourth largest coal power plant in the world if it ever gets completed does 4.8GW).

The highlighted blocks show February, March, and April months, with the arrows showing pre-election months (South African general elections in May 2019 and May 2024). Looking at the 2019 period, it's easy to see where this idea of "we are burning diesel at unsustainable rates to keep the lights on and keep voters happy in the run-up months to the election" came from. Generally we'd expect to need emergency power more in winter, when demand is higher, but in reality we need emergency power when the coal power plants break down.

Whatever is the case for the increased usage in early 2019, the data doesn't really support the theory of using diesel to support this election. We had no loadshedding throughout the whole of April, and yet OCGT use was significantly lower than March and also below April last year. So it's not as simple as "more diesel, less loadshedding".

## What about planned maintenance

While everyone is focused on the diesel use, a 'sneakier' way that Eskom could reduce loadshedding if instructed by the powers that be is to reduce planned maintenance. Remember from earlier that we can increase EAF by reducing unplanned or planned maintenance, but we don't want to reduce planned.

In the 'retaliation' statements, Eskom has been quick to point out its progress in reducing unplanned maintenance, but has failed to mention its reduction in planned maintenance too.

If you look at the black line coming down in the last four months, you'll see it matches the yellow line coming down (bad) far better than it matches the red line coming down (good). The downward trend of the red line in the last 12 months is the strongest argument for a bit of optimism.

Interestingly enough for the conspiracy theorists, a similar pattern was seen before the 2019 elections, though not in the February-April period in any of the in between years.

![](https://i.ritzastatic.com/images/4fea8bd5bb034d5596fdef14e5fd720b/cap-loss.png)

On the other hand, the current planned maintenance is still not low. Generally most maintenance is done in December when demand is lower, and then ramps down in winter, so I would put this one down as something to watch, but not strong evidence that this is due to political pressure related to the elections.

## Summary of claims

* **Eskom's diesel budget is 4x higher than before.** Hard to verify. Probably it is true or close to true but also irrelevant as the previous budget was simply overrun, and diesel use was similar
* **Eskom is burning diesel at a rate of knots.** Weird way to measure, but probably true. Also irrelevant as this has been the case for years and not much has changed recently.
* **Eskom has turned a corner and reduced unplanned breakdowns.** Partly true, but lying by omission if you don't also look at the reduction in planned maintenance.
* **Eskom is under political pressure to reduce loadshedding.** Hard to say. I guess we'll see what happens in June.

## Summary of my impression of the actors

* Eskom: largely incompetent still as a whole, but there seems to be some smaller parts that are trying to improve things. Their media people seem to make the fewest outright false claims, although they do highlight certain parts that make them look good while ignoring some uncomfortable facts.

* De Ruyter: looking for media attention (good for his book sales?) and spouting nonsense without any regard to facts or data. Always happy to claim credit for anything good and deny responsibility for anything bad.

* DA: similar to De Ruyter, ready to jump on anything that riles up the conspiracy theorists.

* NERSA: probably the most competent of the lot, but also the quietest. Most of the 'NERSA said' claims turned out to be false. 

* Conspiracy theorists: always happy to have a logical answer to the chaos that they live in, whether or not the data supports that answer.
