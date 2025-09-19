from CheckingsAccount import CheckingAccount
from SavingsAccount import SavingsAccount

josiasChecking = CheckingAccount("Josias")
josiasSavings = SavingsAccount("Josias", 25)
AlondraChecking = CheckingAccount("Alondra", 2003)
AlondraSavings = SavingsAccount("Alondra", 25, 12.5)

josiasChecking.deposit(50000)
josiasChecking.transfer(25000, josiasSavings)
josiasChecking.transfer(499, josiasSavings)
josiasChecking.printCustomerInformation()

josiasSavings.printCustomerInformation()
josiasSavings.apply_interest()
josiasSavings.apply_interest()
josiasSavings.printCustomerInformation()

AlondraChecking.printCustomerInformation()
AlondraChecking.transfer(400, AlondraSavings)
AlondraChecking.printCustomerInformation()
AlondraSavings.apply_interest()
AlondraSavings.apply_interest()

