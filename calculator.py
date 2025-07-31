def calculate_roi(capex, annual_generation_kwh, electricity_tariff):
    annual_savings = annual_generation_kwh * electricity_tariff
    payback_years = capex / annual_savings if annual_savings > 0 else float('inf')
    roi = ((annual_savings * 25) - capex) / capex * 100
    return payback_years, roi
