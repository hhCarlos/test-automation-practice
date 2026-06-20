export const practiceSelectors = {
  content: {
    container: '#main-container',
    article: '#main-container article',
    postContent: '#main-container .post-content',
  },

  links: {
    testLoginPage: 'a[href*="/practice-test-login/"]',
    testExceptionsPage: 'a[href*="/practice-test-exceptions/"]',
    testTablePage: 'a[href*="/practice-test-table/"]',
  },
};

export const practiceLinks = {
  testLoginPage: {
    path: '/practice-test-login/',
    text: 'Test Login Page',
  },
  testExceptionsPage: {
    path: '/practice-test-exceptions/',
    text: 'Test Exceptions',
  },
  testTablePage: {
    path: '/practice-test-table/',
    text: 'Test Table',
  },
};
