import asyncio
import pathlib

from playwright.async_api import async_playwright

from Script.spider import browse

BOT_PROFILE = pathlib.Path(__file__).with_name('edge_bot_profile')   # 项目目录下新建

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=BOT_PROFILE,
            channel='msedge',
            headless=False,
            args=['--disable-blink-features=AutomationControlled']
        )
        page = browser.pages[0] if browser.pages else await browser.new_page()
        await page.goto('https://www.blablalink.com/?from=from%3DH5_30monthanni%3Douter_game&lang=zh-TW')
        await browse(page)

        # 正常关闭
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
