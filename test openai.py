import openai

openai.api_key = ""

def split_string(long_string, max_length=2048):
    return [long_string[i:i + max_length] for i in range(0, len(long_string), max_length)]

# Set the string that will contain the summary
long_string = """STANDARD FORM OF APARTMENT LEASE
(FOR APARTMENTS NOT SUBJECT TO THE RENT STABILIZATION LAW)
THE REAL ESTATE BOARD OF NEW YORK. INC
Copyright 2019. All Rights Reserved. Reproduction in whole or in part prohibited.
REBNY Apt non-stab 2019 Rev 7.19
PREAMBLE: This lease contains the agreements between Tenant and Owner concerning the rights and
obligations of each party. Tenant and Owner have other rights and obligations which are set forth in government
laws and regulations.
Tenant should read this Lease carefully. If Tenant has any questions, or if Tenant does not understand any
words or statements herein, obtain clarification from an attorney. Once Tenant and Owner sign this Lease,
Tenant and Owner will be presumed to have read it and understood it completely. Tenant and Owner admit that
all agreements between Tenant and Owner have been written into this Lease. Tenant understands that any
agreements made before or after this Lease was signed and not written into it will not be enforceable.
April
05
2023
THIS LEASE is made as of
between
month
day
year
NEW YORK. NY 10107
and Tenant (hereinafter referred to "Tenant' or "Lessee*) RAID AHMED, MICHAEL ZIEGLER
whose address is
Please note the following paragraphs that require a selection among alternative wording: 2, 3E, 34
Please note the following paragraphs that require deletions If inapplicable: 9D, 12C(), 12E, 25, 32C/0), 33, 34, 35, 36, 37, 38, 59, 60
Please note the following paragraphs that require the insertion of terms (and/or delete if inapplicable): 1, 2, 3A, 3B, 4, 9D, 12B, 12C,
25, 32C, 34A, 35, 38B, Exhibit A (Memorandum Confirming Term), Exhibit C (Owner's Work), Exhibit D (Apartment Furniture)
"""

summary = ""

substrings = split_string(long_string)

for i, substring in enumerate(substrings):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # maybe put in an exception to go to another model in case of rate limiting?
        messages=[
            {"role": "system", "content": "I am going to move to an apartment in NYC and I need you to summarize this part of the lease. I'm prompting you multiple times through an API, and stiching the responses together to get a summary. Keep this in mind. Finally, I need you to alert me if anything seems alarming in the lease."},
            {"role": "user", "content": f"Here is the lease section: {substring}"},
        ],
    )

    page_summary = response["choices"][0]["message"]["content"]
    summary += page_summary + "\n"

    with open("Summary1.txt", "w+") as file:
        file.write(summary)

with open("Summary1.txt", "r") as file:
    print(file.read())







