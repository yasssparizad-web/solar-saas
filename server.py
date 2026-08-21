import os
from flask import Flask, request, jsonify, render_template_string
from solar_calculator import calculate_solar_system

app = Flask(__name__)

leads = []

@app.route('/')
def home():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return render_template_string(f.read())
    except Exception as e:
        return f"Error loading index.html: {str(e)}", 500

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json(silent=True) or {}
        
        raw_kwh = data.get('monthly_kwh', 0)
        phone = data.get('phone', '')

        try:
            monthly_kwh = float(raw_kwh)
        except (ValueError, TypeError):
            return jsonify({"error": "لطفاً میزان مصرف را به صورت عدد معتبر وارد کنید."}), 400

        if monthly_kwh <= 0:
            return jsonify({"error": "میزان مصرف باید بزرگتر از صفر باشد."}), 400

        result = calculate_solar_system(monthly_kwh)

        if phone:
            leads.append({
                "phone": phone, 
                "consumption": monthly_kwh, 
                "kw": result.get('recommended_capacity_kw', 0)
            })

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": f"خطای داخلی سرور: {str(e)}"}), 500

@app.route('/admin')
def admin():
    html = "<h2 style='font-family:tahoma;'>لیست درخواست‌های مشتریان (لیدها)</h2><ul style='font-family:tahoma;'>"
    if not leads:
        html += "<li>هنوز درخواستی ثبت نشده است.</li>"
    else:
        for lead in leads:
            html += f"<li>شماره: {lead['phone']} | مصرف: {lead['consumption']}kWh | ظرفیت: {lead['kw']}kW</li>"
    html += "</ul><br><a href='/' style='font-family:tahoma;'>بازگشت به سایت</a>"
    return html

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
