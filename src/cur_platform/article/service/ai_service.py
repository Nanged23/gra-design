# from openai import OpenAI
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
#
# async def get_summary(a):
#     try:
#         client = OpenAI(
#             api_key=os.getenv('MOONSHOT_API_KEY'),
#             base_url="https://api.moonshot.cn/v1",
#         )
#         str1 = f"请以专业的、客观的风格分析以下博客文章的内容，无论文章类型，尝试提取其核心主题和主要信息。如果文章是观点或结论类，请重点总结其核心观点和结论；如果文章是日记、散文等其他类型，请提炼文章所表达的情感、经历或事件。用简洁的语言概括文章的主题。总结的字数控制在 180 字以内。{a}"
#         completion = client.chat.completions.create(
#             model="moonshot-v1-8k",
#             messages=[
#                 {"role": "system",
#                  "content": "你是一位[擅长内容总结]的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。"},
#                 {"role": "user", "content": str1}
#             ],
#             temperature=0.3,
#         )
#         return completion.choices[0].message.content
#     except Exception as e:
#         raise e
#
#
# if __name__ == "__main__":
#
#     print(get_summary(a))
