# các biến đc gửi lên server đc gói gọn trong request
from flask import render_template, request
import dao  #nhập file dao
from app import app


@app.route('/')
def index():
    #truyền tham số kw để tìm vé
    kw=request.args.get('kw')
    account = dao.load_acccount() #gọi hàm bên module dao
    # employee = dao.load_employee(kw=kw)
    admin = dao.load_admin()
    employee = dao.load_employee()
    customer = dao.load_customer()
    revenue = dao.load_
    return render_template('index.html', account=account, employee=employee) #tạo biến categories,products có thể sd bên index.html

#(ten doi tuong/mã của sản phẩm) truyền tham số id để show chi tiết vé
@app.route('/product/<id>')
def details(id):
    #trỏ tới template để add details vào file index
    return render_template("details.html")


if __name__== '__main__':
    app.run(debug=True)