# solar_calculator.py
# هسته محاسباتی و مالی نیروگاه خورشیدی (Solar SaaS Core)

def calculate_solar_system(monthly_kwh):
    """
    ورودی: میزان مصرف برق ماهانه به کیلووات‌ساعت (kWh)
    خروجی: دیکشنری شامل مشخصات فنی و تحلیل مالی کامل
    """
    # ۱. محاسبات فنی
    peak_sun_hours_per_day = 4.5
    system_efficiency = 0.80
    
    daily_kwh = monthly_kwh / 30.0
    required_system_kw = daily_kwh / (peak_sun_hours_per_day * system_efficiency)
    recommended_capacity_kw = round(required_system_kw, 2)
    
    panel_power_kw = 0.55
    total_panels = int(round((recommended_capacity_kw / panel_power_kw) + 0.49))
    inverter_size_kw = round(recommended_capacity_kw * 1.1, 1)
    
    # ۲. محاسبات مالی (تومان)
    cost_per_kw_toman = 45_000_000
    estimated_total_cost_toman = int(round(recommended_capacity_kw * cost_per_kw_toman))
    
    # ۳. محاسبه تولید سالانه و صرفه‌جویی
    annual_production_kwh = recommended_capacity_kw * peak_sun_hours_per_day * 365 * system_efficiency
    electricity_rate_toman = 3_000
    annual_savings_toman = int(round(annual_production_kwh * electricity_rate_toman))
    monthly_savings_toman = int(round(annual_savings_toman / 12))
    
    # ۴. محاسبه بازگشت سرمایه
    if annual_savings_toman > 0:
        payback_years = round(estimated_total_cost_toman / annual_savings_toman, 1)
    else:
        payback_years = 0

    return {
        "monthly_consumption_kwh": monthly_kwh,
        "recommended_capacity_kw": recommended_capacity_kw,
        "total_panels_550w": total_panels,
        "inverter_size_kw": inverter_size_kw,
        "estimated_total_cost_toman": estimated_total_cost_toman,
        "monthly_savings_toman": monthly_savings_toman,
        "annual_savings_toman": annual_savings_toman,
        "payback_years": payback_years
    }
