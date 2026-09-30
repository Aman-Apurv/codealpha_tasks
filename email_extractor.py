# ------------------------------------------------------------
# Task 3: Task Automation with Python (CodeAlpha Internship)
# This script reads a text file, finds all the email addresses
# in it, removes duplicates, and saves them to a new file.
# It also prints a small summary report.
# ------------------------------------------------------------

import re

# The pattern below describes what an email address looks like:
# some characters, then @, then a domain name, a dot and an ending
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def read_file(file_name):
    """Read the text file and return its content. Returns None if not found."""
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: the file", file_name, "was not found.")
        return None


def find_emails(text):
    """Find all emails in the text and return a list without duplicates."""
    all_emails = re.findall(EMAIL_PATTERN, text)

    unique_emails = []
    for email in all_emails:
        email = email.lower()          # treat A@x.com and a@x.com as same
        if email not in unique_emails:
            unique_emails.append(email)

    unique_emails.sort()               # keep the list in alphabetical order
    return all_emails, unique_emails


def count_domains(emails):
    """Count how many emails belong to each domain (like gmail.com)."""
    domain_count = {}
    for email in emails:
        domain = email.split("@")[1]
        if domain in domain_count:
            domain_count[domain] = domain_count[domain] + 1
        else:
            domain_count[domain] = 1
    return domain_count


def save_emails(emails, file_name):
    """Write each email on a new line in the output file."""
    with open(file_name, "w") as file:
        for email in emails:
            file.write(email + "\n")


def main():
    print("=" * 40)
    print("      EMAIL EXTRACTOR")
    print("=" * 40)

    input_file = input("Enter input file name (press Enter for input.txt): ").strip()
    if input_file == "":
        input_file = "input.txt"

    output_file = "emails.txt"

    text = read_file(input_file)
    if text is None:
        return                          # stop the program if file is missing

    all_emails, unique_emails = find_emails(text)

    if len(unique_emails) == 0:
        print("No email addresses were found in the file.")
        return

    save_emails(unique_emails, output_file)

    # ---- summary report ----
    print("\n----- REPORT -----")
    print("Total emails found     :", len(all_emails))
    print("Unique emails          :", len(unique_emails))
    print("Duplicates removed     :", len(all_emails) - len(unique_emails))

    print("\nEmails by domain:")
    domains = count_domains(unique_emails)
    for domain in domains:
        print("  ", domain, "->", domains[domain])

    print("\nExtracted emails:")
    for email in unique_emails:
        print("  ", email)

    print("\nAll emails were saved to", output_file)


main()
