def calculate_zakat(data):
   #prices per gram in local currency (eg. PKR)
   gold_price = 18000
   silver_price =  48.31

   #total asset value
   total = data.get("cash",0) + (data.get("gold",0) * gold_price) + (data.get("silver",0) * silver_price)

   net = total - data.get("liabilities",0)

   #calculate nisab threshold
   gold_nisab = 87.48 * gold_price
   silver_nisab = 612.36 * silver_price

   nisab = min(gold_nisab, silver_nisab)
   if net >= nisab and net > 0:
      zakat = net * 0.025
      eligible = True
   else:
      zakat = 0
      eligible = False

   return round(zakat), round(net), eligible