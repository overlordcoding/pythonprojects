import socket
print("""
𝓟𝓸𝓻𝓽 𝓡𝓾𝓹𝓽𝓾𝓻𝓮 𝓢𝓬𝓪𝓷𝓷𝓮𝓻 𝓯𝓻𝓮𝓮 𝓮𝓭𝓲𝓽𝓲𝓸𝓷
""")
def scan_subdomain(domain, subdomains):
    """
    Scan subdomains of a given domain.

    Args:
    domain (str): The main domain to scan.
    subdomains (list): List of subdomains to scan.

    Returns:
    list: List of available subdomains.
    """
    available_subdomains = []
    for subdomain in subdomains:
        subdomain = subdomain.strip()
        full_domain = f"{subdomain}.{domain}"
        try:
            # Attempt to resolve the subdomain
            socket.gethostbyname(full_domain)
            available_subdomains.append(full_domain)
        except socket.gaierror:
            pass
    return available_subdomains

# Example usage
main_domain = input("Please enter the domain name: ")
subdomains_to_scan = ["www", "blog", "mail", "admin"]
available_subdomains = scan_subdomain(main_domain, subdomains_to_scan)
print("Available subdomains:", available_subdomains)
