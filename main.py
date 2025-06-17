
import chainlit as cl #type: ignore
from agents.zakat_advisor import ZakatAdvisor


start_welcome_message = """
🕌 **Welcome to the Zakat Advisor!**

💡 Please enter your financial info in this format:
 - Make sure  Gold and silver should be in grams like how many grams do you have



⬇️ must follow this sequence (otherwise wrong calculation count): 
cash, gold, silver, laibilites

📌 Example:
`100000, 30, 200, 20000`


🗣️ To receive your answer in **Urdu**, include the word `urdu` in your message.
"""

error_message = """
❗ **Invalid input format.**  
Please enter your cash, gold, silver, laibilites in 4 numbers separated by commas in given name sequence.

**Example:**
`50000, 20, 100, 5000`
"""
@cl.on_chat_start
async def start():
    await cl.Message(content=start_welcome_message).send()

@cl.on_message
async def main(message: cl.Message):
    try:
        parts = [float(p.strip()) for p in message.content.split(",")]
        if len(parts) != 4:
            raise ValueError

        data = {
            "cash": parts[0], 
            "gold": parts[1], 
            "silver": parts[2],
            "liabilities": parts[3]
            }
        # Detect language
        lang = "urdu" if "urdu" in message.content.lower() else "english"

        
        msg = cl.Message("Calculating your zakat...")
        await msg.send()

        agent = ZakatAdvisor()
        summary = agent.advise(data, lang=lang)
        await cl.Message(content=summary).send()

    except Exception as e:
        print("❌ Exception:", e)
        await cl.Message(content=error_message).send()

