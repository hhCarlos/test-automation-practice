export const loginData = {
  paths: {
    login: '/practice-test-login/',
    success: '/logged-in-successfully/',
  },

  validUser: {
    username: 'student',
    password: 'Password123',
  },

  invalidUsername: {
    username: 'incorrectUser',
    password: 'Password123',
    expectedError: 'Your username is invalid!',
  },

  invalidPassword: {
    username: 'student',
    password: 'incorrectPassword',
    expectedError: 'Your password is invalid!',
  },

  success: {
    title: 'Logged In Successfully',
    expectedText: 'Congratulations',
    logoutText: 'Log out',
  },
};
