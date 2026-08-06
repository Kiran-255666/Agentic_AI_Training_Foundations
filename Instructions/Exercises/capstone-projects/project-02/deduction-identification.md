# Capstone Project – 02

## Deduction Identification:

**Identify Short Payment**

Given an invoice amount exists, When the received payment amount is less than the invoice amount. Then the system should calculate the difference as a potential deduction.

**Example**

| Invoice Amount | Payment Received | Deduction |
|---|---|---|
| 10,000 | 9,500 | 500 |

**Read Deduction Reason from Remittance**

Given a remittance advice contains deduction remarks. When the payment is processed, then the system should capture the deduction reason.

**Supported Reasons**

- Pricing Issue
- Freight Claim
- Damage Claim
- Tax Difference
- Discount Taken

**Create Deduction Record**

Given a deduction is identified, When the analyst posts the cash application. Then the system should create a deduction/dispute item for the remaining balance.

**Apply Partial Cash**

Given a customer partially paid an invoice. When the payment is applied. Then the system should:

- close the paid portion
- leave the deduction amount open for investigation

**Assign Deduction Reason Code**

Given a deduction exists. When the analyst selects a reason. Then the system should assign a predefined deduction reason code.

**Sample Reason Codes**

| Code | Description |
|---|---|
| D01 | Pricing |
| D02 | Freight |
| D03 | Damage |
| D04 | Tax |
| D05 | Discount |

**Auto Match Based on Tolerance**

Given the difference amount is within tolerance. When the payment is processed. Then the system may auto-write off the difference instead of creating a deduction.

## Process Flow

1. Receive customer payment
2. Import remittance advice
   - 2.1 Reach out to collector/customer if not received
3. Match invoice number
4. Compare invoice vs payment amount
   - 4.1 Perform the reconciliation (examples below)
5. Identify deduction difference/Over Payment
6. Capture deduction reason (if available)
7. Apply payment
8. Create deduction/dispute item
9. Route deduction for resolution
