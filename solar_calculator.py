# solar_calculator.py
# Solar SaaS Core - Tailored for German Regulations (EEG) & KfW 270 Financing

def calculate_solar_system(monthly_kwh):
    # --- ۱. محاسبات فنی ---
    peak_sun_hours_per_day = 3.1
    system_efficiency = 0.82
    
    daily_kwh = monthly_kwh / 30.0
    required_system_kw = daily_kwh / (peak_sun_hours_per_day * system_efficiency)
    recommended_capacity_kw = round(required_system_kw, 2)
    
    panel_power_kw = 0.44
    total_panels = int(round((recommended_capacity_kw / panel_power_kw) + 0.49))
    inverter_size_kw = round(recommended_capacity_kw * 1.05, 1)
    
    # --- ۲. سرمایه‌گذاری کل (€) ---
    cost_per_kw_euro = 1500
    estimated_total_cost_euro = int(round(recommended_capacity_kw * cost_per_kw_euro))
    
    # --- ۳. تولید و درآمد/صرفه‌جویی سالانه ---
    annual_production_kwh = recommended_capacity_kw * 950
    
    self_consumption_rate = 0.35
    grid_feedin_rate = 0.65
    
    electricity_price_euro = 0.37
    feedin_tariff_euro = 0.081
    
    annual_self_consumption_kwh = annual_production_kwh * self_consumption_rate
    annual_feedin_kwh = annual_production_kwh * grid_feedin_rate
    
    annual_savings_direct = annual_self_consumption_kwh * electricity_price_euro
    annual_feedin_income = annual_feedin_kwh * feedin_tariff_euro
    
    total_annual_savings_euro = int(round(annual_savings_direct + annual_feedin_income))
    monthly_savings_euro = int(round(total_annual_savings_euro / 12))
    
    # --- ۴. بازگشت سرمایه خرید نقدی ---
    payback_years = round(estimated_total_cost_euro / total_annual_savings_euro, 1) if total_annual_savings_euro > 0 else 0

    # --- ۵. محاسبات وام KfW 270 (بازپرداخت ۱۰ ساله، نرخ ۴.۵٪) ---
    interest_rate_annual = 0.045
    years = 10
    months = years * 12
    monthly_interest_rate = interest_rate_annual / 12
    
    # فرمول آنوئیتی (محاسبه قسط ثابت ماهانه)
    if monthly_interest_rate > 0:
        kfw_monthly_payment = estimated_total_cost_euro * (monthly_interest_rate * (1 + monthly_interest_rate)**months) / (((1 + monthly_interest_rate)**months) - 1)
    else:
        kfw_monthly_payment = estimated_total_cost_euro / months
        
    kfw_monthly_payment = int(round(kfw_monthly_payment))
    kfw_net_monthly_benefit = monthly_savings_euro - kfw_monthly_payment

    return {
        "monthly_consumption_kwh": monthly_kwh,
        "recommended_capacity_kw": recommended_capacity_kw,
        "total_panels_440w": total_panels,
        "inverter_size_kw": inverter_size_kw,
        "estimated_total_cost_euro": estimated_total_cost_euro,
        "monthly_savings_euro": monthly_savings_euro,
        "annual_savings_euro": total_annual_savings_euro,
        "payback_years": payback_years,
        "kfw_monthly_payment": kfw_monthly_payment,
        "kfw_net_monthly_benefit": kfw_net_monthly_benefit
    }
