import requests

domain = "google.com"

# getting all the subdomains from a file
with open("subdomains.txt") as file:
    content = file.read()
    subdomains = content.splitlines()

# a list of discovered subdomains
discovered_subdomains = []
for subdomain in subdomains:
    url = f"http://{subdomain}.{domain}"
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print(f"[+] Discovered subdomain : {url}")
        discovered_subdomains.append(url)

# save the discovered subdomains into a file
with open("discovered_subdomains.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)
