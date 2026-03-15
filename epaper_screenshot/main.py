from playwright.sync_api import sync_playwright
import json
import time
import os
import http.server
import socketserver
import threading

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/share", **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

def get_options():
    try:
        with open('/data/options.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("options.json not found. Using environment variables for development.")
        return {
            "url": os.getenv("HA_URL"),
            "username": os.getenv("HA_USERNAME"),
            "password": os.getenv("HA_PASSWORD"),
            "delay": int(os.getenv("DELAY", 300))
        }

def take_screenshot(url, username, password):
    with sync_playwright() as p:
        user_data_dir = "/share/playwright_session"
        
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir,
            headless=True,
            viewport={'width': 800, 'height': 400},
            device_scale_factor=1
        )
        
        page = browser_context.pages[0]

        try:
            print(f"Loading page: {url}")
            page.goto(url, wait_until="networkidle")
            
            if page.locator('input[name="username"]').count() > 0:
                print("Login form found. Logging in...")
                page.type('input[name="username"]', username, delay=50)
                page.type('input[type="password"]', password, delay=50)
                
                login_button = page.locator('ha-button').first
                login_button.click()
                
                print("Waiting for dashboard to load...")
                page.wait_for_selector("ha-app-layout", timeout=15000)
                print("Dashboard loaded.")
            else:
                print("Already logged in.")

            page.wait_for_timeout(5000) 

            screenshot_path = "/share/dashboard.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

        except Exception as e:
            print(f"An error occurred: {e}")
            error_path = "/share/error.png"
            page.screenshot(path=error_path)
            print(f"Error screenshot saved to {error_path}")
        
        finally:
            browser_context.close()

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    options = get_options()
    url = options.get("url")
    username = options.get("username")
    password = options.get("password")
    delay = options.get("delay", 300)

    if not all([url, username, password]):
        print("Missing required options: url, username, or password. Exiting.")
    else:
        while True:
            take_screenshot(url, username, password)
            print(f"Waiting for {delay} seconds before next screenshot.")
            time.sleep(delay)