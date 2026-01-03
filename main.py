import asyncio
import pathlib

from playwright.async_api import async_playwright

from Script.spider import browse, login_blablalink, like, get_rewards

BOT_PROFILE = pathlib.Path(__file__).with_name('edge_bot_profile')   # 项目目录下新建

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=BOT_PROFILE,
            channel='msedge',
            headless=True,
            args=['--disable-blink-features=AutomationControlled']
        )
        page = browser.pages[0] if browser.pages else await browser.new_page()
        print("跳转到blablalink首页...")
        await page.goto('https://www.blablalink.com/?from=from%3DH5_30monthanni%3Douter_game&lang=zh-TW', wait_until="load")
        # if not await page.wait_for_selector(".w-full.h-full", state="visible", timeout=15000):
        #     print("正在打开登录页面...")
        #     await login_blablalink(page)
        # 截图
        await page.screenshot(path="main.png")
        await login_blablalink(page)

        await browse(page, 5)
        await like(page, 10)
        await get_rewards(page)
        # 正常关闭
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
