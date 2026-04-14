import requests
import urllib3

# Suppress SSL warnings if you hit an HTTPS site with a self-signed cert in your lab
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def analyze_http(target_ip, port, user_agent=None):
    """
    Performs Application Layer interrogation while spoofing identity.
    """
    url = f"http://{target_ip}:{port}"
    
    # Professional-grade User-Agent templates
    agents = {
        "chrome": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "iphone": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
        "safari": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    }
    
    # 1. Determine the header value
    # If the user typed 'chrome', use the template. Otherwise, use what they typed.
    # Default to a generic but professional string if nothing is provided.
    header_val = agents.get(user_agent, user_agent) if user_agent else "Mozilla/5.0 (Windows NT 10.0; Win64; x64) GhostRunner/2.0"
    
    headers = {'User-Agent': header_val}
    
    try:
        # We use a short timeout so the scanner doesn't hang on dead web services
        response = requests.get(url, headers=headers, timeout=2, verify=False)
        
        # Extract the 'Server' header (e.g., Apache/2.2.8)
        server_header = response.headers.get('Server', 'No Server Header')
        
        # You could also grab the Page Title for extra recon info
        return f"Web Server: {server_header}"
        
    except requests.exceptions.RequestException:
        # If the port is open but not actually serving HTTP, return None
        return None
