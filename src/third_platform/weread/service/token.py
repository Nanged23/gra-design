# 获取用户 token
import asyncio
from pyppeteer import launch


async def init_browser(browser_instance):
    if not browser_instance:
        # 初始化浏览器实例
        browser_instance = await launch(
            headless=True,
            executablePath="/Users/dongliwei/Downloads/chrome自动化/test_google.app/Contents/MacOS/Google Chrome for Testing"
        )
        return browser_instance


async def get_qrcode(browser_instance):
    """
    前端发起请求，通过使用无头浏览器爬取到官网的登录二维码，最终传递给前端
    :return: 登录二维码
    """
    page = await browser_instance.newPage()
    await page.goto('https://r.qq.com#login', {'waitUntil': 'load'})

    # 等待二维码加载完成，这里可以根据实际情况调整选择器和等待时间
    await page.waitForSelector('img[src^="data:image/png;base64"]')

    # 获取二维码图像
    qrcode_data = await page.evaluate('''() => {
        const img = document.querySelector('img[src^="data:image/png;base64"]');
        return img ? img.src : null;
    }''')

    if qrcode_data:
        return qrcode_data
    else:
        return


async def get_cookies(browser_instance, max_retries=5):
    """
    前端展示二维码之后，再次发出新请求，调用本函数，本函数将轮询 5 次登录状态，尝试获取 cookie
    :return:必要的 cookie 信息
    """
    specific_cookies = {
        'wr_vid': None,
        'wr_skey': None
    }
    cnt = 0
    page = await browser_instance.newPage()
    await page.goto('https://weread.qq.com/', {'waitUntil': 'load'})
    while not all(specific_cookies.values()) and cnt < max_retries:
        all_cookies = await page.cookies()
        for cookie in all_cookies:
            if cookie.get('name') == 'wr_vid':
                specific_cookies['wr_vid'] = cookie.get('value')
            elif cookie.get('name') == 'wr_skey':
                specific_cookies['wr_skey'] = cookie.get('value')

        if all(specific_cookies.values()):
            break
        await asyncio.sleep(0.5)
        await page.reload({'waitUntil': 'load'})
        cnt += 1
    await browser_instance.close()
    return specific_cookies

