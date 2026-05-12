import random
import time
from prometheus_client import start_http_server, Counter

# Define our SLI metrics
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')
FAILURES = Counter('http_requests_failed_total', 'Total Failed HTTP Requests')

if __name__ == '__main__':
    # Start the prometheus metrics server on port 8000
    start_http_server(8000)
    print("App is running... sending metrics to :8000/metrics")
    
    while True:
        REQUESTS.inc() # Increment total requests
      
        # Simulate a 20% failure rate
        if random.random() < 0.005:
            FAILURES.inc()
            print("Request Failed!")
        else:
            print("Request Succeeded.")
            
        time.sleep(1) # Wait 1 second before next request
