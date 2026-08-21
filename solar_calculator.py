# solar_calculator.py
# هسته محاسباتی نیروگاه خورشیدی (Solar SaaS Core)

def calculate_solar_system(monthly_kwh):
    """
    ورودی: میزان مصرف برق ماهانه به کیلووات‌ساعت (kWh)
    خروجی: دیکشنری شامل مشخصات کامل سیستم خورشیدی
    """
    # ۱. متوسط ساعات تابش مفید خورشید در روز (بر اساس میانگین)
    peak_sun_hours_per_day = 4.5
    
    # ۲. ضریب تلفات سیستم (تلفات دما، کابل، کثیفی پنل و اینورتر - حدود ۲۰ درصد)
    system_efficiency = 0.80
    
    # ۳. محاسبه مصرف روزانه (کیلووات‌ساعت)
    daily_kwh = monthly_kwh / 30.0
    
    # ۴. محاسبه ظرفیت نیروگاه مورد نیاز (کیلووات - kW)
    required_system_kw = daily_kwh / (peak_sun_hours_per_day * system_efficiency)
    
    # ۵. گرد کردن ظرفیت به سمت بالا برای اطمینان مهندسی
    recommended_capacity_kw = round(required_system_kw, 2)
    
    # ۶. محاسبه تعداد پنل‌ها (فرض: پنل‌های استاندارد ۵۵۰ وات = ۰.۵۵ کیلووات)
    panel_power_kw = 0.55
    total_panels = round((recommended_capacity_kw / panel_power_kw) + 0.49) # گرد کردن به بالا
    
    # ۷. تعیین توان اینورتر مورد نیاز (۱۰٪ بالاتر از توان سیستم)
    inverter_size_kw = round(recommended_capacity_kw * 1.1, 1)
    
    # ۸. خروجی نهایی به صورت یک ساختار منظم
    return {
        "monthly_consumption_kwh": monthly_kwh,
        "recommended_capacity_kw": recommended_capacity_kw,
        "total_panels_550w": total_panels,
        "inverter_size_kw": inverter_size_kw,
    }

# --- تست کد ---
if __name__ == "__main__":
    # فرض کنید مصرف ماهانه یک خانه یا واحد تجاری ۶۰۰ کیلووات ساعت است
    user_consumption = 600
    result = calculate_solar_system(user_consumption)
    
    print("=== نتیجه برآورد مهندسی نیروگاه خورشیدی ===")
    print(f"مصرف ماهانه: {result['monthly_consumption_kwh']} کیلووات‌ساعت")
    print(f"ظرفیت پیشنهادی نیروگاه: {result['recommended_capacity_kw']} کیلووات")
    print(f"تعداد پنل ۵۵۰ وات مورد نیاز: {result['total_panels_550w']} عدد")
    print(f"توان اینورتر مورد نیاز: {result['inverter_size_kw']} کیلووات")
