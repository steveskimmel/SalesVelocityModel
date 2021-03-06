import numpy as np

class salesModel():
    def calc_sales_per_year(self,deals, deal_size, win_rate, avg_sales_cycle):
        deals = deals + 0.0
        deal_size = deal_size + 0.0
        win_rate = win_rate + 0.0
        avg_sales_cycle = avg_sales_cycle + 0.0
        sales = (deals*deal_size*(win_rate/100))/(avg_sales_cycle/365)
        return str(sales)

    def new_sales_percentage_increase(self,new_sales,current_sales):
        new_sales = float(new_sales)
        current_sales = float(current_sales)
        percentage_increase = ((new_sales-current_sales)/current_sales)*100
        return str(percentage_increase)

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

        return str(np.real(variable_percentage_increase)[0])

    def new_sales_value(self,percentage_increase_deals,percentage_increase_deal_size,percentage_increase_win_rate,percentage_increase_avg_sales_cycle,current_deals,current_deal_size,current_win_rate,current_avg_sales_cycle):
        percentage_increase_deals += 0.0
        percentage_increase_deal_size += 0.0
        percentage_increase_win_rate += 0.0
        percentage_increase_avg_sales_cycle += 0.0
        current_deals += 0.0
        current_deal_size += 0.0
        current_win_rate += 0.0
        current_avg_sales_cycle += 0.0

        percentage_increase_deals /= 100
        percentage_increase_deal_size /= 100
        percentage_increase_win_rate /= 100
        percentage_increase_avg_sales_cycle /= 100

        sales_value = (((1+percentage_increase_deals)*current_deals)*((1+percentage_increase_deal_size)*current_deal_size)*((1+percentage_increase_win_rate)*(current_win_rate/100)))/((1-percentage_increase_avg_sales_cycle)*(current_avg_sales_cycle/365))
        return str(sales_value)


#current = calc_sales_per_year(deals, deal_size, win_rate, avg_sales_cycle)
#perc = increase(new_sales)
#percInc = m.perc_Inc(perc)/100
#m.new_Value(percInc, percInc, percInc, percInc)
