class ClassImporter:
    """ClassImporter allows a developer to define a list of 
    classes that should be imported under an assigned variable name.
    
    Eample usage:
        from app.helpers import ClassImporter

        importer = ClassImporter(__import__('app.helpers.database'))
        
        connection_classes = importer[[
            'AbstractBalanceConnection',
            'AbstractTransactionConnection',
            'BalanceFundConnection',
            'BalanceJarConnection',
            'ExpenseTransactionConnection',
            'IncomeTransactionConnection',
            'SavingStrategyConnection',
            'TransactionScheduleConnection',
            'AbstractDashboardConnection',
            'AllocationFacadeConnection',
            'AnalyticsDashboardConnection',
            'BalanceDashboardConnection',
            'DashboardFacadeConnection',
            'UserAccountConnection'
            ]]
    """
    def __init__(self, module):
        self.module = module
        
    def __getitem__(self, class_names):
        """Takes a list of class names as an argument and returns 
        a list of their attribute names.

        Args:
            class_names (List): A list of class names

        Returns:
            List: A List of class attributes of their respective class
        """
        imported_classes = []
        for name in class_names:
            imported_classes.append(getattr(self.module, name))
        return imported_classes
    