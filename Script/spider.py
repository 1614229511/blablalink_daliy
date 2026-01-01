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

async def like(page: Page, post_count: int = 5):
    """点赞未点赞过的帖子"""
    like_selector = "div.flex.justify-around.items-center > span:nth-child(3)"
    await page.wait_for_selector(like_selector, timeout=10000)
    like_buttons = page.locator(like_selector)

    count = await like_buttons.count()
    print(f"页面上一共发现了 {count} 个点赞按钮")

    for i in range(min(post_count, count)):
        try:
            # 滚动到该按钮位置，防止被遮挡
            await like_buttons.nth(i).scroll_into_view_if_needed()
            # 点击
            await like_buttons.nth(i).click()
            print(f"成功点击第 {i + 1} 个点赞")
            # 适当停顿，防止被反爬虫识别太快
            await page.wait_for_timeout(1000)
        except Exception as e:
            print(f"点击第 {i + 1} 个失败: {e}")


async def get_rewards(page: Page):
    """领取奖励"""
    await page.locator("div:nth-child(5) > .w-\\[44px\\]").click()
    await page.wait_for_load_state("networkidle")

    await page.locator(".w-\\[24px\\].h-\\[24px\\].bg-\\[length\\:100\\%_100\\%\\]").first.click()
