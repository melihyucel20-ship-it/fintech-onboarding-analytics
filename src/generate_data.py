import random
import pandas as pd
from faker import Faker


fake = Faker()
random.seed(42)
Faker.seed(42)

NUM_USERS = 1000


def generate_users(num_users):
    users = []

    for user_id in range(1, num_users + 1):
        user = {
            "user_id": user_id,
            "registration_date": fake.date_between(
                start_date="-90d",
                end_date="today"
            ),
            "device_type": random.choice(["iOS", "Android"]),
            "acquisition_channel": random.choice(
                ["Organic", "Paid Social", "Referral", "Search"]
            ),
            "age_group": random.choice(
                ["18-24", "25-34", "35-44", "45+"]
            )
        }

        users.append(user)

    return pd.DataFrame(users)

# We are creating fictional 1000 app users and assign a device type, 
# acquisition channel, age group and registration date to each of them.

def generate_onboarding_events(users_df):
    events = []

    for _, user in users_df.iterrows():
        user_id = user["user_id"]
        registration_date = pd.to_datetime(user["registration_date"])

        events.append({
            "user_id": user_id,
            "event_name": "registration_completed",
            "event_timestamp": registration_date
        })

        if random.random() < 0.85:
            events.append({
                "user_id": user_id,
                "event_name": "kyc_started",
                "event_timestamp": registration_date + pd.Timedelta(days=1)
            })

            if random.random() < 0.80:
                events.append({
                    "user_id": user_id,
                    "event_name": "kyc_completed",
                    "event_timestamp": registration_date + pd.Timedelta(days=2)
                })

                if random.random() < 0.75:
                    events.append({
                        "user_id": user_id,
                        "event_name": "bank_account_linked",
                        "event_timestamp": registration_date + pd.Timedelta(days=3)
                    })

                    if random.random() < 0.82:
                        events.append({
                            "user_id": user_id,
                            "event_name": "first_deposit",
                            "event_timestamp": registration_date + pd.Timedelta(days=4)
                        })

                        if random.random() < 0.84:
                            events.append({
                                "user_id": user_id,
                                "event_name": "first_transaction",
                                "event_timestamp": registration_date + pd.Timedelta(days=5)
                            })

    return pd.DataFrame(events)

# This function created a "registration_completed" event for each user


if __name__ == "__main__":
    users_df = generate_users(NUM_USERS)

    print(users_df.head())
    print(f"\nGenerated {len(users_df)} users.")

    onboarding_df = generate_onboarding_events(users_df)

    onboarding_df.to_csv(
    "data/raw/onboarding_events.csv",
    index=False
)

    print(onboarding_df.head())
    print(f"\nGenerated {len(onboarding_df)} onboarding events.")

    users_df.to_csv(
        "data/raw/users.csv",
        index=False
    )