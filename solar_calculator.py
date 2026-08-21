# solar_calculator.py
# Solar SaaS Core - Tailored for German Regulations (EEG) and Euro (€)

def calculate_solar_system(monthly_kwh):
    """
    Input: Monthly electricity consumption in kWh
    Output: Technical parameters and Financial analysis based on German Standards
    """
    # --- 1. Technical Calculations (German Solar Conditions) ---
    # Average peak sun hours in Germany ~ 3.1 hours/day (approx. 1000 kWh/kWp/year)
    peak_sun_hours_per_day = 3.1
    system_efficiency = 0.82
    
    daily_kwh = monthly_kwh / 30.0
    required_system_kw = daily_kwh / (peak_sun_hours_per_day * system_efficiency)
    recommended_capacity_kw = round(required_system_kw, 2)
    
    # Modern standard solar modules in Europe (approx. 430W - 450W, e.g. 440W = 0.44kW)
    panel_power_kw = 0.44
    total_panels = int(round((recommended_capacity_kw / panel_power_kw) + 0.49))
    inverter_size_kw = round(recommended_capacity_kw * 1.05, 1)
    
    # --- 2. Financial Calculations in Euro (€) ---
    # Turnkey system cost in Germany (Panel, Inverter, Mounting, Installation & Grid Connection)
    # Average ~ 1,500 € per kWp (0% MwSt / VAT-free under German EEG regulations)
    cost_per_kw_euro = 1500
    estimated_total_cost_euro = int(round(recommended_capacity_kw * cost_per_kw_euro))
    
    # --- 3. Savings & Feed-in Tariff (Einspeisevergütung) ---
    # Annual Production in kWh (Approx 950 - 1000 kWh per 1 kWp installed in Germany)
    annual_production_kwh = recommended_capacity_kw * 950
    
    # German Electricity Retail Price ~ 0.37 €/kWh
    # Assuming ~ 35% Self-Consumption (Eigenverbrauch) and 65% Grid Feed-in (Einspeisung)
    self_consumption_rate = 0.35
    grid_feedin_rate = 0.65
    
    electricity_price_euro = 0.37
    feedin_tariff_euro = 0.081  # EEG Feed-in tariff (~8.1 Cent/kWh)
    
    annual_self_consumption_kwh = annual_production_kwh * self_consumption_rate
    annual_feedin_kwh = annual_production_kwh * grid_feedin_rate
    
    annual_savings_direct = annual_self_consumption_kwh * electricity_price_euro
    annual_feedin_income = annual_feedin_kwh * feedin_tariff_euro
    
    total_annual_savings_euro = int(round(annual_savings_direct + annual_feedin_income))
    monthly_savings_euro = int(round(total_annual_savings_euro / 12))
    
    # --- 4. Payback Period (Amortisationszeit) ---
    if total_annual_savings_euro > 0:
        payback_years = round(estimated_total_cost_euro / total_annual_savings_euro, 1)
    else:
        payback_years = 0

    return {
        "monthly_consumption_kwh": monthly_kwh,
        "recommended_capacity_kw": recommended_capacity_kw,
        "total_panels_440w": total_panels,
        "inverter_size_kw": inverter_size_kw,
        "estimated_total_cost_euro": estimated_total_cost_euro,
        "monthly_savings_euro": monthly_savings_euro,
        "annual_savings_euro": total_annual_savings_euro,
        "payback_years": payback_years
    }
