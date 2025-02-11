import time
import asyncio
from pyppeteer import launch
from pyppeteer.errors import TimeoutError  # Import TimeoutError for explicit handling


async def main():
    chrome_executable_path = '/Users/dongliwei/Downloads/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
    browser = await launch(executablePath=chrome_executable_path)  # 启动浏览器，指定路径
    page = await browser.newPage()

    try:  # Add try-except block for overall error handling
        # 1. 打开登录页面
        login_url = "https://taoqitu.me/index.html"
        await page.goto(login_url)

        # 2. 输入用户名
        username_field = await page.waitForSelector('#regusername', timeout=10000)
        await username_field.type("2074759416@qq.com")  # Replace with your actual username

        # 3. 输入密码
        password_field = await page.waitForSelector('#regpassword', timeout=10000)
        await password_field.type("TianCai.54")  # Replace with your actual password

        # 4. 点击登录按钮
        login_button = await page.waitForSelector('.loginbutton', timeout=10000)
        await login_button.click()

        # 5. 等待登录完成 (wait for navigation)
        try:
            await page.waitForNavigation(timeout=10000)  # Robust navigation wait
        except TimeoutError:
            print("Navigation Timeout after login button click. Proceeding...")

        # **处理登录后的弹窗**
        try:
            await asyncio.sleep(1)  # Add a small delay before looking for popup
            popup_confirm_button = await page.waitForXPath("/html/body/div[7]/div/button", timeout=5000)

            if popup_confirm_button:
                print("弹窗按钮已找到", popup_confirm_button)
                await popup_confirm_button.click()  # 点击弹窗上的 "我知道了" 按钮
                print("已点击弹窗确认按钮")
            else:
                print("未找到登录弹窗")
        except TimeoutError:
            print("未找到登录弹窗或弹窗超时，可能没有弹窗出现或者出现异常")
        except Exception as e:  # Catch potential errors during popup handling
            print(f"弹窗有误{e}")
            if 'Node is either not visible or not an HTMLElement' in str(e):
                print("尝试使用 JavaScript 点击弹窗按钮...")
                try:
                    await page.evaluate(
                        'document.querySelector("body > div:nth-child(7) > div > button").click()')  # More specific CSS selector
                    print("JavaScript 点击弹窗按钮成功")
                except Exception as js_click_err:
                    print(f"JavaScript 点击弹窗按钮失败: {js_click_err}")

        # 6. 查找签到按钮并点击
        qiandao_button = await page.waitForXPath("/html/body/div[1]/div/div[3]/a[1]", timeout=10000)

        await qiandao_button.click()  # 点击签到按钮
        print("签到按钮已点击，跳转到签到页面：https://taoqitu.me/qiandao.html")
        try:
            await page.waitForNavigation(timeout=10000)  # Wait for navigation to qiandao page
        except TimeoutError:
            print("Navigation to 签到页面 Timeout. Proceeding...")

        button1_xpath = "/html/body/div[3]/div/div[2]/div[1]/div/button[1]"  # Define xpath for re-use and clarity
        button1 = await page.waitForXPath(button1_xpath, timeout=10000)
        await button1.click()
        print("自动签到成功")
        # 7. 等待签到操作完成 (optional, but good to have some delay)
        await asyncio.sleep(2)
    except Exception as main_e:  # Catch any top-level exceptions
        print(f"An error occurred in main: {main_e}")
    finally:  # Ensure browser closes even if errors occur
        await browser.close()
        print("Browser closed")
        print("=================")


if __name__ == "__main__":
    # 获取当前时间
    current_time = time.localtime()

    # 格式化输出时间
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

    print("======={}========".format(formatted_time))
    asyncio.run(main())
