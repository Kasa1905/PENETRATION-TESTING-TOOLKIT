class BruteForcer:
    def attempt_login(self, target, username, password_list):
        for password in password_list:
            if self.try_login(target, username, password):
                self.report_success(username, password)
                return True
        return False

    def try_login(self, target, username, password):
        # Simulate a login attempt (replace with actual implementation)
        return password == "correct_password"  # Placeholder for demonstration

    def report_success(self, username, password):
        print(f"Successful login for {username} with password: {password}")