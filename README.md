# fintech-onboarding-analytics
A product analytics case study focused on onboarding, activation, and retention in a digital wallet.

## Current Results

Using a synthetic dataset of 1,000 users, the current onboarding funnel is:

- 1,000 registrations
- 853 KYC starts
- 686 KYC completions
- 546 bank accounts linked
- 442 first deposits
- 377 first transactions

The current activation rate is 37.7%.

The largest percentage drop-off occurs between KYC completion and bank account linking.

## Funnel Visualization

![Onboarding Funnel](docs/onboarding_funnel.png)

## Key Findings

- Overall activation rate is **37.7%**.
- The largest funnel drop-off occurs between **KYC completion** and **bank account linking**.
- In the synthetic dataset, **iOS users** have a slightly higher activation rate than Android users.
- **Organic acquisition** shows the highest activation rate among acquisition channels.
- **Referral** users show the lowest activation rate among the analyzed channels.

## Segment Analysis

### Device Type
- Android: 36.96%
- iOS: 38.48%

### Acquisition Channel
- Organic: 39.42%
- Paid Social: 38.99%
- Search: 37.11%
- Referral: 35.25%

## Visualizations

### Onboarding Funnel

![Onboarding Funnel](docs/onboarding_funnel.png)

### Activation by Device

![Device Activation](docs/device_activation.png)

### Activation by Acquisition Channel

![Channel Activation](docs/channel_activation.png)

### Activation by Age Group

![Age Activation](docs/age_activation.png)

## Product Recommendations

### 1. Improve the bank account linking step

The largest percentage drop-off occurs between KYC completion and bank account linking.

A potential product experiment would be to simplify the bank account linking flow by reducing the number of required steps and providing clearer guidance during the process.

**Primary metric:** Bank account linking conversion rate

**Secondary metrics:**
- First deposit conversion rate
- Overall activation rate
- Time to first transaction

### 2. Investigate acquisition channel quality

Organic users show the highest activation rate, while referral users show the lowest activation rate in the synthetic dataset.

The product and growth teams could investigate whether acquisition channels attract users with different levels of intent.

Possible next analyses include:
- activation by campaign
- cost per activated user
- retention by acquisition channel

### 3. Investigate device-level friction

iOS users show a slightly higher activation rate than Android users.

This difference is small and should not be treated as evidence of a product issue yet. A larger dataset and statistical testing would be required before making a product decision.
