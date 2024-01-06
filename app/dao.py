from app.models import Account, Employee, Customer,  Admin, Revenue, Receipt

def load_acccount():
    return Account.query.all() #dùng dòng này để cập nhật csdl WB thì web cũng đổi theo
    # return [{
    #     'id':1,
    #     'name':'Sân bay Phù Cát'
    # }, {
    #     'id':2,
    #     'name':'Sân bay Quy Nhơn'
    # }]
# cài kw mặc định là None giá trị sẽ thay đổi nếu tìm đc kw
def load_employee(kw=None):
    return Account.query.all() #dùng dòng này để cập nhật csdl WB thì web cũng đổi theo

def load_admin(kw=None):
    return Account.query.all()
def load_customer(kw=None):
    return Account.query.all()