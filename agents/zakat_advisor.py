from litellm import completion  # type: ignore
from zakat_utils import calculate_zakat
from config import get_prompt

class ZakatAdvisor:
    def __init__(self, model="openrouter/mistralai/mistral-7b-instruct", ayah_model="openrouter/deepseek/deepseek-r1-0528:free"):
        self.model = model
        self.ayah_model = ayah_model

    def advise(self, data, lang="english"):
        try:
            zakat, net, eligible = calculate_zakat(data)

            zakat_prompt = get_prompt("zakat_prompt.txt").format(
                cash=data["cash"], gold=data["gold"], silver=data["silver"],
                liabilities=data["liabilities"], net=net, zakat=zakat, lang=lang
            )
            zakat_res = completion(model=self.model, messages=[{"role": "user", "content": zakat_prompt}])
            zakat_summary = zakat_res["choices"][0]["message"]["content"]
        except Exception as e:
            zakat_summary = f"⚠️ Could not generate zakat explanation: {e}"

        try:
            ayah_prompt = get_prompt("ayah_prompt.txt").format(topic="zakat", lang=lang)
            ayah_res = completion(model=self.ayah_model, messages=[{"role": "user", "content": ayah_prompt}])
            ayah_text = ayah_res["choices"][0]["message"]["content"]
        except Exception as e:
            ayah_text = f"⚠️ Could not fetch Quranic ayah: {e}"

        return f"""
# 🧮 Zakat Summary

{zakat_summary}

---

## 📖 Quranic Ayah

{ayah_text}
"""

