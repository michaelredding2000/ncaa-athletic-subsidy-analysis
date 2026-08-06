import pandas as pd

# Expects the Knight-Newhouse "Custom Reporting Results" export in the same folder.
# The raw export is not redistributed in this repo; pull it from knightnewhousedata.org.
path = 'Custom Reporting Results Data.xlsx'
df = pd.read_excel(path, sheet_name='Data')

df.columns = ['school','ipeds_id','year','ncaa_subdivision','fbs_conference',
              'total_revenues','media_conf_revenue','ticket_sales',
              'institutional_govt','student_fees']

# core metrics
df['subsidy'] = df['institutional_govt'] + df['student_fees']
df['subsidy_pct'] = df['subsidy'] / df['total_revenues']
df['student_fee_pct'] = df['student_fees'] / df['total_revenues']
df['earned_revenue'] = df['total_revenues'] - df['subsidy']

print(f"\nLoaded {len(df)} schools\n")

print("=== TOP 15 MOST SUBSIDY-DEPENDENT ===")
top = df.sort_values('subsidy_pct', ascending=False).head(15)
print(top[['school','ncaa_subdivision','subsidy_pct']].to_string(index=False))

print("\n=== 15 LEAST SUBSIDY-DEPENDENT (self-funded) ===")
bottom = df.sort_values('subsidy_pct').head(15)
print(bottom[['school','ncaa_subdivision','subsidy_pct']].to_string(index=False))

print("\n=== AVG SUBSIDY DEPENDENCE BY SUBDIVISION ===")
print(df.groupby('ncaa_subdivision')['subsidy_pct'].mean().to_string())

print("\n=== AVG SUBSIDY DEPENDENCE BY FBS CONFERENCE ===")
fbs = df[df['fbs_conference'].notna()]
print(fbs.groupby('fbs_conference')['subsidy_pct'].mean().sort_values(ascending=False).to_string())

# save enriched file for Power BI
out = 'ncaa_analyzed.csv'
df.to_csv(out, index=False)
print(f"\nSaved analyzed data to {out}")
