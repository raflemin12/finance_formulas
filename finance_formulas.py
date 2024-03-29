

def accounting_equation(assets:float, liabilities:float, shareholder_equity:float) -> bool:
    """Assets = Libabilities + Shareholders Equity
    Returns true when accounting equation is balanced
    Returns the difference when accounting equation is not balanced
    """
    balanced = assets == liabilities + shareholder_equity

    if not balanced:
        return assets - liabilities - shareholder_equity
    return balanced

def current_ratio(current_assets: float, current_liabilities:float) -> float:
    """
    Calculates if company can pay its current bills.
    In general, above 1.5 is safe and below 1.5 is risky
    """
    return current_assets / current_liabilities

def debt_ratio(total_liabilities: float, total_assets: float) -> float:
    """
    Amount of assets that go into paying debts.
    Ex: debt ratio = 80%. For each $1 owned, company owes $0.80.
    Lower ratio is generally better.
    """
    return total_liabilities / total_assets

def equity_ratio(total_shareholder_equity: float, total_assets: float, intangible_assets = 0) -> float:
    """
    Amount of assets that go to shareholders.
    In general, want it to be higher than debt ratio
    """
    return total_shareholder_equity / (total_assets - intangible_assets)

def acid_test_ratio(cash: float, short_investments: float, net_acc_receive: float, current_liabilities: float) -> float:
    """
    Most liquid assets that go into paying debts.
    In general, looking for 0.9 - 1.o
    """
    return (cash + short_investments + net_acc_receive) / current_liabilities

def inventory_turnover(cogs: float, avg_inventory: float) -> float:
    """
    The number of times sold through your inventory.
    The higher the better.
    """
    return cogs / avg_inventory

def days_sales_inventory(inventory_turn: float) -> float:
    """
    Average number of days it takes to sell off inventory. Measures efficiency of sales.
    Lower is better.
    """
    return 365 / inventory_turn

def acc_receive_turnonver(net_credit_sales:float, avg_net_acc_receive: float) -> float:
    """
    Amount of times receivables converted to cash.
    Measures the efficiency in collecting receivables.
    Higher ratio is better.
    """
    return net_credit_sales / avg_net_acc_receive

def collection_period(acc_receive_turn: float) -> float:
    """
    Length of time a business needs to collect accounts receivables.
    Low average indicates that payments collected faster.
    """
    return 365 / acc_receive_turn

def time_interest_earned(ebit: float, interest_expense: float) -> float:
    """
    Ability to pay debts based on current income.
    Higher ratio is better.
    """
    return ebit / interest_expense

def gross_profit_percent(gross_profit: float, net_sales:float) -> float:
    """
    Percentage of revenue kept for each sale after all costs are deducted. 
    Indicates how successful in generating revenue, whilst keeping the expenses low
    """
    return gross_profit / net_sales

def return_on_sales(net_income: float, net_sales:float) -> float:
    """
    How efficiently sales are turned into proft.

    """
    return net_income / net_sales

def return_on_assets(net_income: float, interest_exp: float, avg_total_assets: float) -> float:
    """
    Determines if company uses its assets efficiently to generate a profit.
    """
    return (net_income + interest_exp) / avg_total_assets

def return_on_equity(net_income: float, preferred_div: float, avg_common_share_equity: float) -> float:
    """
    Efficiency in generating profits.
    Higher ROE is better
    """
    return (net_income - preferred_div) / avg_common_share_equity

def earnings_per_share(net_income: float, preferred_div: float, avg_common_shares_out: float) -> float:
    """
    How much money a company makes for each share of its stock.
    Estimates corporate value.
    Higher indicates greater value
    """
    return (net_income - preferred_div) / avg_common_shares_out

def price_earnings_ratio(share_price: float, earnings_share: float) -> float:
    """
    A high P/E ratio can mean that a stock's price is high relative to earnings and possibly overvalued. 
    A low P/E ratio might indicate that the current stock price is low relative to earnings.
    """
    return share_price / earnings_share

def dividend_yield(div_per_share: float, share_price: float) -> float:
    """
    Percentage of a company’s share price that it pays out in dividends each year.
    """
    return div_per_share / share_price
