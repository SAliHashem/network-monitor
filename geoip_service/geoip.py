import geoip2.database

def get_geoip(ip):
    try:
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')  # تحتاج تنزل قاعدة البيانات
        response = reader.city(ip)
        return {
            "country": response.country.name,
            "city": response.city.name
        }
    except Exception as e:
        return {"error": str(e)}