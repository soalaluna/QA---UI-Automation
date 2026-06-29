import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.pldtglobal.com/en/enterprise/pgc-managed-network-and-cloud")
    page.get_by_role("link", name="Enterprise", exact=True).click()
    expect(page.get_by_role("heading", name="Managed Network and Cloud")).to_be_visible()
    expect(page.get_by_text("Engineered on PLDT’s global")).to_be_visible()
    expect(page.locator("section").filter(has_text="Back to").locator("img")).to_be_visible()
    expect(page.locator(".relative.mb-6").first).to_be_visible()
    expect(page.get_by_role("heading", name="SD-WAN")).to_be_visible()
    expect(page.get_by_text("PLDT Global elevates SD-WAN")).to_be_visible()
    expect(page.get_by_text("SD-WANPLDT Global elevates SD")).to_be_visible()
    expect(page.get_by_text("IP VPNA fully managed global")).to_be_visible()
    expect(page.locator("div:nth-child(3) > .gradient-border-card > .relative")).to_be_visible()
    expect(page.get_by_role("heading", name="IP VPN")).to_be_visible()
    expect(page.get_by_text("A fully managed global IP")).to_be_visible()
    expect(page.get_by_text("Global MPLSPowered by PLDT’s")).to_be_visible()
    expect(page.locator("div:nth-child(2) > .gradient-border-card > .relative")).to_be_visible()
    expect(page.get_by_role("heading", name="Global MPLS")).to_be_visible()
    expect(page.get_by_text("Powered by PLDT’s private")).to_be_visible()
    expect(page.get_by_text("Wireless & IoT SolutionsDeploy enterprise wireless and IoT at scale on PLDT’s")).to_be_visible()
    expect(page.locator("div:nth-child(4) > .gradient-border-card > .relative")).to_be_visible()
    expect(page.get_by_role("heading", name="Wireless & IoT Solutions")).to_be_visible()
    expect(page.get_by_text("Deploy enterprise wireless")).to_be_visible()
