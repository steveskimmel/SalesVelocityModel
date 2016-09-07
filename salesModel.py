import numpy as np

class salesModel():
    def calc_sales_per_year(self,deals, deal_size, win_rate, avg_sales_cycle):
        global global_deals
        global global_deal_size
        global global_win_rate
        global global_avg_sales_cycle
        global global_sales
        global_deals = deals + 0.0
        global_deal_size = deal_size + 0.0
        global_win_rate = win_rate + 0.0
        global_avg_sales_cycle = avg_sales_cycle + 0.0
        global_sales = (global_deals*global_deal_size*(global_win_rate/100))/(global_avg_sales_cycle/365)
        return str(int(round(global_sales))) + ";" +str(global_sales)

    def new_sales_percentage_increase(self,new_sales,current_sales):
        new_sales = float(new_sales)
        current_sales = float(current_sales)
        percentage_increase = ((new_sales-current_sales)/current_sales)*100
        return round(percentage_increase,2)

    def uniform_variable_percentage_increase(self,percentage_increase):
        percentage_increase /= 100
        a = 1
        b = 3
        c = 4 + percentage_increase
        d = 0 - percentage_increase

        coefs = [ 0, 0, 0, 0 ]

        coefs[ 0 ] = a
        coefs[ 1 ] = b
        coefs[ 2 ] = c
        coefs[ 3 ] = d

        r = np.roots(coefs)

        variable_percentage_increase = r[ np.isreal( r ) ]
        variable_percentage_increase *= 100
        variable_percentage_increase += 0.0

        return round(np.real(variable_percentage_increase)[0],2)

    def new_sales_value(self,percentage_increase_deals, percentage_increase_deal_size, percentage_increase_win_rate, percentage_increase_avg_sales_cycle,current_deals,current_deal_size,current_win_rate,current_avg_sales_cycle):
        percentage_increase_deals += 0.0
        percentage_increase_deal_size += 0.0
        percentage_increase_win_rate += 0.0
        percentage_increase_avg_sales_cycle += 0.0

        percentage_increase_deals /= 100
        percentage_increase_deal_size /= 100
        percentage_increase_win_rate /= 100
        percentage_increase_avg_sales_cycle /= 100

        sales_value = (((1+percentage_increase_deals)*current_deals)*((1+percentage_increase_deal_size)*current_deal_size)*((1+percentage_increase_win_rate)*(current_win_rate/100)))/((1-percentage_increase_avg_sales_cycle)*(current_avg_sales_cycle/365))
        return int(round(sales_value))

    def new_sales_value_test(self,a,b,c,d,e,f,g,h):
        return 10

#current = calc_sales_per_year(deals, deal_size, win_rate, avg_sales_cycle)
#perc = increase(new_sales)
#percInc = m.perc_Inc(perc)/100
#m.new_Value(percInc, percInc, percInc, percInc)
