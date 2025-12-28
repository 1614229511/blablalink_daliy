from playwright.async_api import Page


async def browse(page: Page, post_count: int = 5):
    """浏览帖子"""
    for i in range(post_count):
        target = page.locator("div[data-cname='infinite-scroll'] > div").nth(i).locator("> div").nth(1)
        await target.click()
        # 显式等待
        await page.wait_for_selector(".post-letter-paper", state="visible", timeout=5000)
        await page.wait_for_load_state("networkidle")

        await page.get_by_role("img").first.click()
        # 显式等待
        await page.wait_for_selector("div[data-cname='infinite-scroll'] > div", state="visible", timeout=5000)
        await page.wait_for_load_state("networkidle")


async def login_blablalink(page: Page):
    """通过blablalink账户登录"""
    if await (cookie_btn := page.get_by_role("button", name="接受所有可選 cookies")).is_visible():
        await cookie_btn.click()

    await page.locator("img").nth(1).click()
    await page.get_by_role("listitem").filter(has_text="日本/韓國/北美/東南亞/全球").click()
    await page.get_by_role("textbox", name="電郵地址").click()
    await page.get_by_role("textbox", name="電郵地址").fill("jiangzhonglun@outlook.com")
    await page.get_by_role("textbox", name="電郵地址").press("Tab")
    await page.get_by_role("textbox", name="密碼").fill("123456asdASD")
    await page.get_by_role("button", name="登入", exact=True).click()

    await page.wait_for_selector(".w-full.h-full", state="visible", timeout=15000)

