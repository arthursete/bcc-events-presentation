"""Capture screenshots of each wireframe page from wireframes.html using Playwright."""
from playwright.sync_api import sync_playwright
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_DIR, 'wireframes.html')
OUTPUT_DIR = os.path.join(BASE_DIR, 'wireframe_screenshots')

PAGES = [
    {'id': 'home',      'filename': 'wireframe_home.png',      'label': 'Home Page'},
    {'id': 'browse',    'filename': 'wireframe_browse.png',     'label': 'Browse / Search Results'},
    {'id': 'detail',    'filename': 'wireframe_detail.png',     'label': 'Venue Detail'},
    {'id': 'login',     'filename': 'wireframe_login.png',      'label': 'Admin Login'},
    {'id': 'dashboard', 'filename': 'wireframe_dashboard.png',  'label': 'Admin Dashboard'},
    {'id': 'form',      'filename': 'wireframe_form.png',       'label': 'Add / Edit Venue'},
]

os.makedirs(OUTPUT_DIR, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1200, 'height': 900})
    page.goto(f'file://{HTML_PATH}')
    page.wait_for_load_state('networkidle')

    for wp in PAGES:
        element = page.locator(f'#{wp["id"]}')
        element.scroll_into_view_if_needed()
        out_path = os.path.join(OUTPUT_DIR, wp['filename'])
        element.screenshot(path=out_path)
        print(f'Captured: {wp["label"]} -> {out_path}')

    browser.close()

print('All wireframe screenshots captured successfully.')
