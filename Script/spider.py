from playwright.async_api import Page


async def browse(page: Page):
    """浏览帖子"""
    for i in range(5):
        target = page.locator("div[data-cname='infinite-scroll'] > div").nth(i).locator("> div").nth(1)
        await target.click()
        await page.wait_for_selector(".post-letter-paper", state="visible", timeout=5000)
        await page.get_by_role("img").first.click()
        await page.wait_for_selector("div[data-cname='infinite-scroll'] > div", state="visible")


def login_blablalink(page: Page):
    """通过blablalink账户登录"""
    page.locator(".inline-flex.items-center.justify-center.relative > .fill-current > svg").first.click()
    page.get_by_role("textbox", name="電郵地址").click()
    page.get_by_role("textbox", name="電郵地址").fill("jiangzhonglun@outlook.com")
    page.get_by_role("textbox", name="電郵地址").press("Tab")
    page.get_by_role("textbox", name="密碼").fill("123456asd")
    page.get_by_role("textbox", name="密碼").press("CapsLock")
    page.get_by_role("textbox", name="密碼").fill("123456asdASD")
    page.get_by_role("textbox", name="密碼").press("CapsLock")
    page.get_by_role("button", name="登入", exact=True).click()
