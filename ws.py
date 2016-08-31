from salesModel import salesModel
from flask import Flask, request
from flask_restful import Resource, Api
import ast

app = Flask(__name__)
api = Api(app)

#calc_sales_per_year, new_sales_percentage_increase, uniform_variable_percentage_increase, new_sales_value

class webService(Resource):
    global SalesVelocityModel
    SalesVelocityModel = salesModel()
    def post(self):
        json_data = request.get_json(force=True)
        if 'calc_sales' in json_data:
            variables_dict = json_data['calc_sales']
            return SalesVelocityModel.calc_sales_per_year(variables_dict['deals'],variables_dict['deal_size'],variables_dict['win_rate'],variables_dict['avg_sales_cycle'])
        elif 'sales_perc_increase' in request.form:
            variables_dict = ast.literal_eval(request.form['sales_perc_increase'])
            return SalesVelocityModel.new_sales_percentage_increase(variables_dict['new_sales'])
        elif 'variables_perc_increase' in request.form:
            variables_dict = ast.literal_eval(request.form['variables_perc_increase'])
            return SalesVelocityModel.uniform_variable_percentage_increase(variables_dict['percentage_increase'])
        elif 'increased_sales_value' in request.form:
            variables_dict = ast.literal_eval(request.form['increased_sales_value'])
            return SalesVelocityModel.new_sales_value(variables_dict['percentage_increase_deals'],variables_dict['percentage_increase_deal_size'],variables_dict['percentage_increase_win_rate'],variables_dict['percentage_increase_avg_sales_cycle'])
api.add_resource(webService, '/')

if __name__ == '__main__':
    app.run(debug=True)
