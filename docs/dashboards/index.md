# Dashboards

Eskom releases information in several different ways - mainly their short term data portal (updated several times per week), their long-term data set dumps (available by filling out a form, and covering the previous 5 years), and the weely system reports (released on a wednesday for the previous week, but often late).

Here are some dashboards based on each data source.

* [Eskom 5 year dashboard](https://metabase.dwyer.co.za/public/dashboard/8a1e3f60-e53f-44c4-b045-cdcb35254ecb)
* [Eskom Unofficial Data Portal](https://metabase.dwyer.co.za/public/dashboard/d3b40619-d8f0-4be3-a1f2-99fe5b84e961)
* [Weekly System Status Reports](https://metabase.dwyer.co.za/public/dashboard/5b87c941-8734-4510-9c05-87c08b52cbfb)

Some select charts from each are below. Note that they do not look good on mobile devices.

## Selected charts

Eskom generates most of its power from aging coal power plants. When demand is larger than supply, Eskom does manual "load reduction" to make up the difference.

This graph shows total generation, thermal generation (coal), load reduction and generation + reduction (which should be greater than demand to prevent a grid collapse) on a daily basis. Or view a larger version [here](https://metabase.dwyer.co.za/public/question/b71a745a-513a-41ac-b8d7-11bb7be77211).

<iframe    src="https://metabase.dwyer.co.za/public/question/b71a745a-513a-41ac-b8d7-11bb7be77211"    frameborder="0"    width="800"    height="600"    allowtransparency></iframe>

Eskom's most important KPI is "EAF" or "Energy availability factor". This is usually given as a percentage representing how much of their theoretical generation capability is actually producing power. The rest is split between "PCLF" (planned capability loss factor, or units that are down for planned maintenance), "UCLF" (unplanned capability loss factor, or units that are down due to breakdowns), and "OCLF" (other capability loss factor or units that are out "due to constraints out of the power station management control"). This graph shows EAF, PLCF, UCLF, and OCLF. View a larger version [here](https://metabase.dwyer.co.za/public/question/d3c78719-cc25-44b4-8e74-5accced27b88).

<iframe    src="https://metabase.dwyer.co.za/public/question/d3c78719-cc25-44b4-8e74-5accced27b88"    frameborder="0"    width="800"    height="600"    allowtransparency></iframe>

The same metrics can also be calculated in absolute MW instead of as a percentage of installed capacity, as shown below. Or see a larger version [here](https://metabase.dwyer.co.za/public/question/db2e50a8-abd1-41b4-b561-16145008ac79).

<iframe    src="https://metabase.dwyer.co.za/public/question/db2e50a8-abd1-41b4-b561-16145008ac79"    frameborder="0"    width="800"    height="600"    allowtransparency></iframe>

Note that Eskom deliberately does more maintenance in summer, so we should always expect an increase in EAF from approximately December to June. To see long-term trends, it's useful to plot each year separately, which shows how EAF is getting worse year-over-year. Or see a larger version [here](https://metabase.dwyer.co.za/public/question/4f928585-76d8-4984-83c3-0bdfd5accd1e)

<iframe    src="https://metabase.dwyer.co.za/public/question/4f928585-76d8-4984-83c3-0bdfd5accd1e"    frameborder="0"    width="800"    height="600"    allowtransparency></iframe>

Generation has to be higher than demand, otherwise the grid collapses. Eskom does load reduction to ensure that demand does not exceed supply, including a buffer as demand can spike and it takes time to implement more reduction. See a larger version [here](https://metabase.dwyer.co.za/public/question/e9009c2a-e0b0-4eed-b86a-c79b1b213278)

<iframe    src="https://metabase.dwyer.co.za/public/question/e9009c2a-e0b0-4eed-b86a-c79b1b213278"    frameborder="0"    width="800"    height="600"    allowtransparency></iframe>




## OCTG Usage

Eskom has Open Cycle Gas Turbines (OCGTs) which burn diesel to generate power. These were intended to be used only as a last resort for peak demand during emergency breakdowns of the regular plants as they are not efficient and very expensive to run. However they are now regularly used to reduce the gap between supply and demand whenever Eskom has diesel available. Eskom has its own OCGTs and also buys power from some owned by Independent Power Producers. The graph below shows utilization rate of Eskom's OCTTs. See a larger version [here](https://metabase.dwyer.co.za/public/question/96924f74-508f-42ae-9b69-b842a211bc6c).

<iframe    src="https://metabase.dwyer.co.za/public/question/96924f74-508f-42ae-9b69-b842a211bc6c"    frameborder="0"    width="800"    height="600"    allowtransparency></iframe>

## 


