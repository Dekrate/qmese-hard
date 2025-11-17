from datetime import datetime


class UM:
    """
    Class for user management in system.
    Implements basic CRUD operations.
    """

    def __init__(self):
        self.u = []  # user list

    def au(self, n, e, bd):
        """
        Add new user to system.

        Parameters:
        n - user name
        e - email address
        bd - birth date in YYYY-MM-DD format

        Returns:
        Nothing returned
        """
        x = {
            'n': n,
            'e': e,
            'bd': bd,
            'rd': datetime.now().strftime("%Y-%m-%d"),
            'ia': True
        }
        self.u.append(x)
        print(f"added: {n}")

    def fue(self, e):
        """
        Find user in database.

        Parameters:
        e - email to find

        Returns:
        User object or None
        """
        for x in self.u:
            if x['e'] == e:
                return x
        return None

    def du(self, e):
        """
        Change user status.

        Parameters:
        e - user email

        Returns:
        Operation status
        """
        x = self.fue(e)
        if x:
            x['ia'] = False
            return True
        return False

    # TODO: Implement functions below according to requirements

    def ca(self, bd):
        """
        Function calculating age in years based on date.

        Returns:
        Calculation result
        """
        pass

    def gabd(self, e):
        """
        Calculate discount.
        - 0-17 years: 20% discount
        - 18-64 years: 0% discount
        - 65+ years: 15% discount.

        Parameters:
        e - user identifier

        Returns:
        Numeric value
        """
        pass

    def gus(self):
        """
        Generate user data summary.

        Returns:
        Dictionary of user groups quantity
        """
        pass