import os
from flask import Flask, request, jsonify, render_template_string
from solar_calculator import calculate_solar_system

app = Flask(__name__)

# ذخیره درخواست‌های مشتریان در حافظه موقت سرور
leads = []

@app.route('/')
def home():
    # باز کردن و نمایش صفحه اصلی وب‌سایت
    with open('index.html', 'r', encoding='utf-8') as f:
        return render_template_string(f.read())

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json or {}
    monthly_kwh = float(data.get('monthly_kwh', 0))
    phone = data.get('phone', '')

    if monthly_kwh <= 0:
        return jsonify({"error": "لطفاً میزان مصرف را معتبر وارد کنید"}), 400

    # فراخوانی هسته محاسباتی پایتون که در گام قبل ساختید
    result = calculate_solar_system(monthly_kwh)

    # اگر کاربر شماره تماس وارد کرده بود، آن را ذخیره کن
    if phone:
        leads.append({"phone": phone, "consumption": monthly_kwh, "kw": result['recommended_capacity_kw']})

    return jsonify(result)

@app.route('/admin')
def admin():
    # صفحه ساده مدیریت برای مشاهده شماره تماس مشتریان
    html = "<h2>لیست درخواست‌های مشتریان (لیدها)</h2><ul>"
    for lead in leads:
        html += f"<li>شماره: {lead['phone']} | مصرف: {lead['consumption']}kWh | ظرفیت پیشنهادی: {lead['kw']}kW</li>"
    html += "</ul><br><a href='/'>بازگشت به سایت</a>"
    return html

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
