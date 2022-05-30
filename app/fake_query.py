from app.models import Brand


brands_list = Brand.query.all()
print(brands_list)