from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models.data import Payroll
from .conn import db
from models.decorator import admin_required

class PayrollResource(Resource):

    @jwt_required()
    @admin_required  # ✅ Admin-only access
    def get(self):
        payroll_list = Payroll.query.all()
        return [payroll.to_dict() for payroll in payroll_list], 200

    @jwt_required()
    @admin_required
    def post(self):
        data = request.get_json()

        new_payroll = Payroll(
            name=data.get("name"),
            id_number=data.get("id_number"),
            pay_per_hour=data.get("pay_per_hour"),
            basic_salary=data.get("basic_salary"),
            house_allowance=data.get("house_allowance"),
            normal_hrs=data.get("normal_hrs"),
            hours_worked=data.get("hours_worked"),
            overtime_worked=data.get("overtime_worked"),
            absent_hrs=data.get("absent_hrs"),
            absent_amount=data.get("absent_amount"),
            double_overtime=data.get("double_overtime"),
            doubletime_amount=data.get("doubletime_amount"),
            hrs_arrears=data.get("hrs_arrears"),
            leave_amount=data.get("leave_amount"),
            total_earnings=data.get("total_earnings"),
            paye=data.get("paye"),
            less_pension_nssf=data.get("less_pension_nssf"),
            tax_charge=data.get("tax_charge"),
            personal_relief=data.get("personal_relief"),
            deductions=data.get("deductions"),
            advance=data.get("advance"),
            nssf=data.get("nssf"),
            shif=data.get("shif"),
            loan=data.get("loan"),
            sacco=data.get("sacco"),
            total_deductions=data.get("total_deductions"),
            netpay=data.get("netpay")
        )

        db.session.add(new_payroll)
        db.session.commit()
        return new_payroll.to_dict(), 201

    @jwt_required()
    @admin_required
    def patch(self):
        data = request.get_json()
        payroll_id = data.get("id")

        payroll = Payroll.query.filter_by(id=payroll_id).first()
        if not payroll:
            return {"message": "Payroll record not found"}, 404

        updatable_fields = [
            "name", "id_number", "pay_per_hour", "basic_salary", "house_allowance",
            "normal_hrs", "hours_worked", "overtime_worked", "absent_hrs", "absent_amount",
            "double_overtime", "doubletime_amount", "hrs_arrears", "leave_amount", "total_earnings",
            "paye", "less_pension_nssf", "tax_charge", "personal_relief", "deductions",
            "advance", "nssf", "shif", "loan", "sacco", "total_deductions", "netpay"
        ]

        for field in updatable_fields:
            if field in data:
                setattr(payroll, field, data[field])

        db.session.commit()
        return payroll.to_dict(), 200
