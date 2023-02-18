import requests
import whois
import argparse


def is_registered(domain_name):
    """A function that returns a boolean indicating
    whether a `domain_name` is registered"""
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)


def get_discovered_subdomains(domain, subdomain_list, timeout=2):
    discovered_subdomains = []
    for subdomain in subdomain_list:
        url = f"http://{subdomain}.{domain}"
        try:
            # if this raises an ERROR, that means the subdomain does not exist
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print(f"[+] Discovered subdomain : {url}")
            discovered_subdomains.append(url)
    return discovered_subdomains


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Domain name information extractor, user WHOIS db scans for subdomains')
    parser.add_argument('domain', help='The domain name without http(s)')
    parser.add_argument('-t', '--timeout', type=int, default=2,
                        help='The timeout in seconds for prompting the connection, default is 2')
    parser.add_argument('-s', '--subdomains', default='subdomains.txt',
                        help='The file path that contains the list of subdomains to scan, default is subdomains.txt')
    parser.add_argument('-o', '--output',
                        help='The output file path resulting the discovered subdomains, default is {domain}-subdomains.txt')
    args = parser.parse_args()
    if is_registered(args.domain):
        whois_info = whois.whois(args.domain)
        print(f"Domain registrar: {whois_info.registrar}")
        print(f"WHOIS server: {whois_info.whois_server}")
        print(f"Domain creation date: {whois_info.creation_date}")
        print(f"Expiration date: {whois_info.expiration_date}")
    print("=" * 50, "Scanning subdomains", "=" * 50)
    with open(args.subdomains) as file:
        content = file.read()
        subdomains = content.splitlines()
    discovered_subdomains = get_discovered_subdomains(args.domain, subdomains)
    discovered_subdomains_file = f'{args.domain}-subdomains.txt'
    with open(discovered_subdomains_file, 'w') as f:
        for subdomain in discovered_subdomains:
            print(subdomain, file=f)
