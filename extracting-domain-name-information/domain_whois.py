import whois
from domain_validator import is_registered

domain_name = "google.com"

if is_registered(domain_name):
    whois_info = whois.whois(domain_name)

    # print some info
    print(f"Domain register: {whois_info.register}")
    print(f"WHOIS server: {whois_info.whois_server}")
    print(f"Domain creation date: {whois_info.creation_date}")
    print(f"Expiration date: {whois_info.expiration_date}")

    # print all other info
    print(whois_info)
