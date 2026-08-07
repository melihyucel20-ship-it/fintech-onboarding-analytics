import pandas as pd
import matplotlib.pyplot as plt

events_df = pd.read_csv("data/raw/onboarding_events.csv")

funnel_counts = (
    events_df["event_name"]
    .value_counts()
)

print(funnel_counts)

funnel_order = [
    "registration_completed",
    "kyc_started",
    "kyc_completed",
    "bank_account_linked",
    "first_deposit",
    "first_transaction"
]

print("\nConversion rates:")

for i in range(len(funnel_order)- 1):
    current_step = funnel_order[i]
    next_step = funnel_order[i+1]

    current_count = funnel_counts[current_step]
    next_count = funnel_counts[next_step]

    conversion_rate = next_count / current_count * 100

    print(
        f"{current_step} -> {next_step}: "
        f"{conversion_rate:.2f}%"
    )

print("\nDrop-off rates:")

for i in range(len(funnel_order) - 1):
    current_step = funnel_order[i]
    next_step = funnel_order[i + 1]

    current_count = funnel_counts[current_step]
    next_count = funnel_counts[next_step]

    drop_off_rate = (current_count - next_count) / current_count * 100

    print(
        f"{current_step} -> {next_step}: "
        f"{drop_off_rate:.2f}%"
    )

registered_users = funnel_counts["registration_completed"]
activated_users = funnel_counts["first_transaction"]

activation_rate = activated_users / registered_users * 100

print(f"\nActivation rate: {activation_rate:.2f}%")

funnel_values = [funnel_counts[step] for step in funnel_order]

plt.figure(figsize =(10,6))
plt.bar(funnel_order,funnel_values)

plt.title("Fintech Onboarding Funnel")
plt.xlabel("Onboarding Step")
plt.ylabel("Number of Users")

plt.xticks(rotation=45,ha="right")
plt.tight_layout()

plt.savefig(
    "docs/onboarding_funnel.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

