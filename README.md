# NCAA Athletic Subsidy Analysis

![NCAA subsidy dashboard](dashboard.png)

Most public Division I athletic departments do not pay for themselves. Across 240 public D-I schools in FY2024, the typical school covered only about a third of its athletic budget with money it earned, and the rest came from student fees and institutional or government support. 151 of those 240 schools leaned on subsidies for more than half their athletic funding.

## The question

Which public universities depend most on student fees and subsidies to fund athletics, and what predicts that dependence?

## Data

Knight-Newhouse College Athletics Database, pulled through its Custom Reporting export. The set covers 240 public Division I schools for fiscal year 2024, with all dollar figures inflation-adjusted. Each row is one school-year. Fields include total revenues, media and conference revenue, ticket sales, institutional or government support, and student fees, along with the school's NCAA subdivision and FBS conference.

## Method

The analysis runs in Python with pandas. The script (`analyze_ncaa.py`) reads the Knight-Newhouse export and renames the raw columns to readable names. From those it builds the fields the question needs:

- `subsidy`: institutional or government support plus student fees
- `subsidy_pct`: subsidy divided by total revenues
- `student_fee_pct`: student fees divided by total revenues
- `earned_revenue`: total revenues minus subsidy

Subsidy dependence is the share of an athletic budget that comes from money the department did not earn. Earned revenue is what is left once that support is removed. The script writes `ncaa_analyzed.csv`, which feeds a Power BI dashboard.

## Findings

The median school funds 63.8% of its athletic budget through subsidies. More than half the schools in the set, 151 of 240, rely on subsidies for over half their athletic money.

Dependence tracks closely with subdivision. Average subsidy dependence by group:

| Subdivision | Average subsidy dependence |
|---|---|
| FBS | ~34% |
| FCS | ~68% |
| No Football | ~76% |

Conference tells the same story inside FBS. A short list of power conferences fund athletics almost entirely on their own, while the smaller conferences lean heavily on subsidies. Average subsidy dependence:

| Conference | Average subsidy dependence |
|---|---|
| Southeastern (SEC) | ~4% |
| Big Ten | ~6% |
| Atlantic Coast (ACC) | ~12% |
| Big 12 | ~13% |
| Sun Belt | ~61% |
| Conference USA | ~63% |
| Mid-American | ~66% |

## What it means

The split is not about school size or how many sports a school fields. It comes down to which schools have a media and ticket business big enough to carry the department. A handful of big-brand programs in the power conferences bring in enough television and gate revenue to run near break-even without touching student money. Everyone else backfills the gap with fees and institutional support, and the smaller the earned-revenue base, the larger that backfill has to be.

The scatter of earned revenue against subsidy dependence shows the relationship directly. Schools fall along an inverse curve. As earned revenue climbs, subsidy dependence drops toward zero, and the schools with almost no commercial athletic revenue sit near 80 to 90% dependence. For most public universities, athletics is not a business that funds itself. It is a service the campus pays to provide, and students cover a real part of the bill.

## Repo contents

- `analyze_ncaa.py`: the pandas script that reads the raw export and writes the analyzed CSV
- `ncaa_analyzed.csv`: the processed dataset that feeds the dashboard
- `NCAA_Subsidies.pbix`: the Power BI dashboard
- `dashboard.png`: screenshot of the dashboard

The raw Knight-Newhouse export is not redistributed here. Pull it yourself from the source below.

## Running it

The analysis was built on a machine with no prior Python install, using uv to manage the environment:

```
uv run --with pandas --with openpyxl analyze_ncaa.py
```

That reads the Knight-Newhouse export and writes `ncaa_analyzed.csv`. Open `NCAA_Subsidies.pbix` in Power BI Desktop to explore the dashboard.

## Data credit

Data: Knight-Newhouse College Athletics Database (knightnewhousedata.org). Used for non-commercial purposes with credit, as the source requires.
