# error-budget-SLO

Service Level Indicator (SLI) We are measuigng the percentage of HTTP requests that successfully connect without any issues.

Service Level Objective (SLO) - We are targeting 98 percent or better in successful requests. 

Error Budget: SLO - 100% = Error Budget { 100% - 98% = 2% }

### The Budget v. The Margin

The SLO being at 98% means that there is a 2% allowance for errors and failures. The nthe application error rate excedes the allowance of the SLO then it becomes debt. Now the SWE team must stop pushing features and focus on the bugs that are in the application throwing the errors. 

Changing the app.py to throw a smaller failure rate like <0.005  which is a 0.4% failure rate. This equals to a 99.5% rate. 