class ROICalculator():

    def expenses(self, cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8):
        return cost1 + cost2 + cost3 + cost4 + cost5 + cost6 + cost7 + cost8

    def cashFlow(self, cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8):
        total_cost = ROICalculator.expenses(self, cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8)
        monthly_profit = gross_monthly_income - total_cost
        return monthly_profit

    def cashReturn(self, investment1, investment2, investment3, investment4):
        return investment1 + investment2 + investment3 + investment4

    def return_on_investment(self, cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8, investment1, investment2, investment3, investment4):
        yearly_profit = ROICalculator.cashFlow(self, cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8) * 12
        total_investment = ROICalculator.cashReturn(self, investment1, investment2, investment3, investment4)
        roi = (yearly_profit / total_investment) * 100
        print("Your calculated ROI: ", roi)

print(ROICalculator.cashReturn)
inquiry = print("How much does it cost to own your house?(enter whole numbers below)")
cost1 = int(input("Taxes: "))
cost2 = int(input("Insurance: "))
cost3 = int(input("Utilities: "))
cost4 = int(input("HOA: "))
cost5 = int(input("Vacancy: "))
cost6 = int(input("Repairs: "))
cost7 = int(input("Property Management: "))
cost8 = int(input("Mortgage: "))
gross_monthly_income = int(input("Total monthly income(enter a whole number): "))
inquiry = print("How much are you investing?(enter whole numbers below)")
investment1 = int(input("Down Payment: "))
investment2 = int(input("Closing costs: "))
investment3 = int(input("Repair/rehab budget: "))
investment4 = int(input("Misc: "))




property = ROICalculator()
property.expenses(cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8)
property.cashFlow(cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8)
property.cashReturn(investment1, investment2, investment3, investment4)
property.return_on_investment(cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8, investment1, investment2, investment3, investment4)