from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import func
from .conn import db

class Payroll(db.Model, SerializerMixin):
    __tablename__ = "payrolls"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    id_number = db.Column(db.Integer)
    pay_per_hour = db.Column(db.Integer)
    basic_salary = db.Column(db.Integer)
    house_allowance = db.Column(db.Integer)
    normal_hrs = db.Column(db.Integer)
    hours_worked = db.Column(db.Integer)
    overtime_worked = db.Column(db.Integer)  
    absent_hrs = db.Column(db.Integer)
    absent_amount = db.Column(db.Integer)
    double_overtime = db.Column(db.Integer)
    doubletime_amount = db.Column(db.Integer)
    hrs_arrears = db.Column(db.Integer)
    leave_amount = db.Column(db.Integer)
    total_earnings = db.Column(db.Integer)
    paye = db.Column(db.Integer)
    less_pension_nssf = db.Column(db.Integer)
    tax_charge = db.Column(db.Integer)
    personal_relief = db.Column(db.Integer)

    # deductions
    advance = db.Column(db.Integer)
    nssf = db.Column(db.Integer)
    shif = db.Column(db.Integer)  # Renamed from 'shif' if that's what you meant
    loan = db.Column(db.Integer)
    sacco = db.Column(db.Integer)
    total_deductions = db.Column(db.Integer)
    netpay = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=func.now())

    def __repr__(self):
        return f"<Payroll id={self.id} name={self.name} netpay={self.netpay}>"
