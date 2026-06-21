import json

def extract_newsletter(upstream_data):
    """Extract the newsletter from the upstream data."""
    return upstream_data.get('newsletter', '')

def extract_report(upstream_data):
    """Extract the report from the upstream data."""
    return upstream_data.get('report', '')

def process_data(upstream_data):
    """Process the extracted data."""
    newsletter = extract_newsletter(upstream_data)
    report = extract_report(upstream_data)
    return newsletter, report

def main():
    """Main function to read data and process it."""
    with open('context.json', 'r') as f:
        upstream_data = json.load(f)
    newsletter, report = process_data(upstream_data)
    print("Newsletter:")
    print(newsletter)
    print("\nReport:")
    print(report)

if __name__ == "__main__":
    main()